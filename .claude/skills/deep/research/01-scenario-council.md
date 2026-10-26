# Research: a "Scenario Council" — agents that enumerate what could go wrong, argue, pick, and build

Date: 2026-10-26
Status: research only, no implementation yet

---

## 1. The problem, stated precisely

The two real misses you described:

1. **White play button on a white thumbnail.** Nobody asked "what if the content behind this control has the same colour as the control?"
2. **Batch of 5 runs, 2 fail.** The table was designed for "all succeed" and "all fail", not "some succeed".

Both are the same failure: a chat model answers **the question that was asked** and samples **one plausible path** through the design space. It is not being asked to enumerate the space. The knowledge is in the model (it knows about contrast ratios and partial failures), but a single conversational turn never applies that knowledge unless something forces it to.

So the system you want is not "a smarter model". It is a **forcing function**: a pipeline that makes the model walk the state space on purpose, from several different angles, then argue about what matters, then commit.

---

## 2. What the research actually says (and what it does not)

I read Anthropic's engineering post on their multi-agent research system directly. arxiv.org is blocked from this container, so the paper findings below come from search excerpts, not full text. Treat the exact numbers as approximate.

### 2.1 Diversity comes from independent parallel sampling, not from refinement

- Wharton's "Prompting Diverse Ideas" (arXiv 2402.01727): a single LLM produces **less diverse** ideas than a group of humans, but prompting strategy "dramatically increases idea diversity".
- Multi-persona studies (Cambridge Design Science; arXiv 2607.27553, 2609.30492): giving **multiple parallel prompts, each with a different professional persona**, produces more distinct concepts. Assigning the persona to the *proposer* gives the most diversity; a specialised *critic* mainly improves quality, not variety.
- Important counter-result (arXiv 2607.27553): **iterative refinement collapses diversity**. A "bold ideas" refinement agent greatly reduced variety, and independent sessions that each produce **one** idea were also worse.

**Design consequence:** generate scenarios with **N independent agents in parallel, each with a different lens, each producing a long list**. Do not let them see each other during generation. Do not "refine" the list repeatedly; merge once, then critique once.

### 2.2 Debate is overrated for finding the right answer; voting does most of the work

- "Debate or Vote" (arXiv 2508.17536): **majority voting accounts for most of the gains attributed to multi-agent debate**; in most cases voting without any debate performs on par with debate.
- "Talk Isn't Always Cheap" (arXiv 2509.05396): debate can make agents **switch from a correct answer to an incorrect one** under social pressure; gains are "far from guaranteed" even with stronger models in the group.
- Heterogeneous-role debate (Springer A-HMAD) reports 4 to 6 point gains over *standard* debate, but was not compared against plain voting.

**Design consequence:** use debate for what it is good at, which is **falsification** ("here is why this scenario is unreachable / already handled / not worth it"), with a **fixed number of rounds** and a **separate judge**. Do not use free-form "discuss until you agree" debate to pick the winner. Pick winners with **independent scoring plus aggregation**.

### 2.3 LLM judges are noisy and biased; aggregate them

- "Rating Roulette" (EMNLP 2025 Findings): the same judge gives different scores on re-runs; **aggregating several runs improves agreement with humans**; forcing deterministic output *lowers* quality.
- "Judging with Many Minds" (arXiv 2505.19477): a judge "consistently favors the side with the same LLM backbone". Multi-agent judging can **amplify** bias as well as reduce it.
- Survey (arXiv 2411.16594) lists **Peer Rank** and pairwise tournament ranking as the closest match to "rank many candidates".

**Design consequence:** score each scenario with a **rubric**, run the judge **3 times at non-zero temperature and take the median**, and use **pairwise comparison only for the top few** when the ranking actually matters.

### 2.4 Orchestration lessons from Anthropic's research system (primary source)

From https://www.anthropic.com/engineering/multi-agent-research-system:

- Each subagent brief needs "an objective, an output format", tool guidance and "clear task boundaries". Vague briefs caused duplicated work.
- Embed **effort scaling rules** in the prompt: simple query = 1 agent, 3 to 10 tool calls; comparison = 2 to 4 agents; complex = 10+ agents with divided responsibilities.
- Separate context windows per subagent "reduce path dependency", which is exactly the "one plausible path" problem above.
- Cost: agents use about 4x the tokens of chat, multi-agent about **15x**. Only worth it when the outcome justifies it. For your use (a design decision that otherwise costs a production bug) it usually does.
- "Start wide, then narrow down." "Prefer heuristics over rigid rules." "Think like your agents": run them with their real prompts and watch where they fail.
- Evaluation: start with about **20 representative cases** and an LLM judge with a rubric, not a big eval suite.

### 2.5 Edge-case generation specifically

- EdgeGen (arXiv 2609.24115): derive **rules** from the spec, build **violation scenarios by combining rules**, and **ground each scenario in real state** before accepting it. Sparse specs give incomplete rules.
- ForesightSafety-SAGE (arXiv 2606.08531): define **failure categories**, write a "scenario family" per category, seed with a few human examples, let the LLM expand each family to many candidates.
- 900-trace failure study (arXiv 2512.07497): recurring archetypes are "premature action without grounding", "over-helpfulness under uncertainty", "context pollution", "fragile execution under load". Useful as a checklist.
- Test-generation study (arXiv 2503.17998): LLMs **omit obvious cases** (an invalid-file-type case, a field needing context) when not prompted by a checklist.

**Design consequence:** the lens agents must carry **explicit checklists** (state taxonomies), not just a persona. Persona gives diversity; checklist gives recall. You need both.

### 2.6 Prioritisation: borrow FMEA and premortem

- Premortem: "assume it already failed, explain why". Generate failures **without filtering for likelihood first**, then prioritise.
- FMEA: score each failure **Severity x Occurrence x Detection** (RPN). "Detection" is the one people forget: a white-on-white play button has low severity but **very low detectability** (no error, no log, user just does not click). That is why it slipped.

---

## 3. The design: Scenario Council

A fixed pipeline. Each stage has its own agent(s), its own output schema, and its own stopping rule. "Debate" lives in exactly one stage.

```
Stage 0  Spec capture        (1 agent, reads code + asks you)        -> feature spec
Stage 1  Lens generation     (8 to 10 agents, PARALLEL, isolated)   -> raw scenario lists
Stage 2  Merge + dedupe      (1 cheap agent)                          -> candidate set
Stage 3  Grounding           (1 to 3 agents, read the actual code)   -> reachable / unreachable / already handled
Stage 4  Adversarial pass    (proposer vs skeptic, 2 rounds, judged) -> survivors with arguments attached
Stage 5  Scoring             (judge x3, median, FMEA rubric)          -> ranked list
Stage 6  Decision            (1 agent + you)                          -> per scenario: build / defer / accept / reject
Stage 7  Build + verify      (implementer per group, verifier writes a test per scenario)
Stage 8  Learn               (append misses to lens checklists)
```

### Stage 0: Spec capture

One agent reads the relevant code and produces a short structured spec. Without this, the lens agents hallucinate a generic app. Fields:

- Surfaces (pages, modals, table, cards, buttons)
- Actions (submit, fetch, retry, cancel, bulk operations)
- Entities and their statuses (run: queued / running / done / failed / partial / cancelled)
- Cardinalities (1 item vs N items vs 10,000 items)
- External dependencies (APIs, queues, storage, media)
- Actors (anonymous, user, admin, automated job)

### Stage 1: Lens agents (the heart of it)

Each lens is a separate subagent with a **persona + a checklist + a required output schema**. They run in parallel and never see each other. Each must produce at least 15 scenarios and is told explicitly to include unlikely ones.

| Lens | Persona | Checklist it must walk | Would have caught |
|---|---|---|---|
| **State machine** | QA lead | For every surface x {empty, loading, partial, error, success, stale, offline, permission denied, disabled, read-only, overflow / too many} | Table partial-failure state |
| **Batch and partial failure** | Distributed-systems engineer | N items: 0 fail, 1 fails, all fail, some fail; retry one; retry all; idempotency; ordering; progress reporting; cancel mid-way | 5 runs, 2 fail |
| **Data shape** | Data engineer | null, zero, negative, huge, unicode, emoji, very long string, duplicate keys, missing field, wrong type, future dates, timezones | |
| **Visual and perceptual** | Accessibility-minded designer | Control on same-colour background, dark mode, high contrast, RTL, 200% zoom, truncated text, broken image, image of unexpected aspect ratio, image that is all one colour | White play button |
| **Human behaviour** | Support engineer who reads tickets | Double submit, back button mid-flow, refresh during upload, two tabs, slow network, mobile keyboard covering button, paste instead of type, leaves and returns after an hour | |
| **Timing and concurrency** | Backend engineer | Two users edit same row; status changes while page open; webhook arrives before DB write; job finishes after user cancelled | |
| **Security and abuse** | Pentester | IDOR on ids, mass submission, upload of wrong file type, script in a text field, rate limits | |
| **Operations** | On-call SRE | Can we tell from logs which of the 5 runs failed? Alerting on partial? Rollback? Feature flag off state? | |
| **First-time and long-time user** | Product manager | Zero-data onboarding; power user with 3 years of data; user whose plan expired | |
| **Wildcard** | "Someone who has seen this exact app break" | No checklist; told to produce the 10 strangest plausible scenarios | |

Output schema per scenario (strict, so Stage 2 can merge mechanically):

```yaml
- id: visual-07
  title: Play icon invisible on white or near-white thumbnail
  trigger: thumbnail luminance close to icon colour
  surface: video card
  consequence: user sees no affordance, does not click; no error anywhere
  likelihood: medium       # 1-5
  severity: medium         # 1-5
  detectability: very low  # 1-5, 1 = nobody would notice
  proposed_handling: icon with contrasting backdrop / outline / scrim
```

Why personas AND checklists: the research says personas raise diversity, and checklists raise recall of the "obvious" cases LLMs omit. The wildcard lens exists because checklists only find what is already on the checklist.

### Stage 2: Merge and dedupe

A cheap model (Haiku-class) clusters near-duplicates, keeps the best-worded version, and records which lenses proposed it. A scenario raised independently by 3 lenses is a weak prior that it matters. Output: candidate set, typically 60 to 150 items.

### Stage 3: Grounding against the real code

This is the EdgeGen lesson and the one most people skip. For each candidate, a read-only agent with code access answers:

- **Reachable?** Can this state actually occur given the code and data model? (A "partial" status on a single-item page is not reachable.)
- **Already handled?** Point to the file and line if so.
- **Evidence:** file paths.

Unreachable and already-handled items are archived with their reason, not deleted. They are useful later when the code changes.

### Stage 4: Adversarial pass (the only debate)

Structured, bounded, judged. For each surviving candidate above a cheap threshold:

- **Proposer** (fresh context, has the scenario + grounding evidence) writes the strongest one-paragraph case that this must be handled.
- **Skeptic** (fresh context) writes the strongest case that it should be ignored, deferred or accepted as-is.
- One rebuttal each. **Two rounds, then stop.**
- **Judge** (third context, does not see which side was which model) outputs: keep / drop, confidence, and a one-line reason.

Rules that come straight from the debate literature:

- Fixed rounds. No "until consensus". Consensus is where correct answers get talked out of existence.
- Proposer and skeptic never see the judge's verdict on other items (no conformity drift).
- The judge never sees the raw lens output, only the arguments, so it is judging the case, not the author.

### Stage 5: Scoring

A judge agent scores each survivor on the FMEA rubric: Severity (1 to 5), Occurrence (1 to 5), Detection (1 to 5, where 5 = would never be noticed), plus Cost-to-handle (1 to 5). Run the judge **three times**, take the **median** per field. Rank by Severity x Occurrence x Detection, with cost as a tie-breaker. Do pairwise comparisons only among the top 10 if the exact order matters.

### Stage 6: Decision

For each ranked scenario, one of four outcomes, each with a one-line justification:

- **Build now** (goes into the spec as an acceptance criterion)
- **Defer** (ticket with the scenario text attached)
- **Accept** (we knowingly do not handle; write down why)
- **Reject** (judge says not real)

This is the point where a human looks. The deliverable is a **scenario table**, not prose. In your workflow this table should be attached to the feature before any implementation starts, because it is literally the list of states the UI and the table must support.

### Stage 7: Build and verify

One implementer per group of related scenarios (for example, all the "partial" table states together). Then a **separate verifier** agent that has only the scenario table and writes one test (or a manual check script) per "build now" scenario. The implementer never writes its own verification; that is the same path-dependency problem again.

### Stage 8: Learn

Every miss found in production goes into a `misses.md` file with: what happened, which lens should have caught it, what checklist line would have caught it. That line is added to the lens. This is the only "learning" mechanism that is cheap and works without training anything. The two misses you described become the first two entries.

---

## 4. How to build it in Claude Code

Three pieces, all plain files in the repo.

### 4.1 Lens subagents: `.claude/agents/lens-*.md`

One file per lens. Frontmatter supports `name`, `description`, `tools`, `model`, `maxTurns`, `skills`, `isolation`. The body is the system prompt. Example:

```markdown
---
name: lens-batch
description: Enumerates batch and partial-failure scenarios for a feature. Use when asked to run the scenario council.
tools: Read, Grep, Glob
model: sonnet
maxTurns: 15
---
You are a distributed-systems engineer reviewing a feature spec for what happens
when operations are performed on more than one item.

Walk this checklist for EVERY action in the spec that can touch N items:
- N = 0, N = 1, N = many, N = the maximum allowed, N = over the maximum
- 0 fail, exactly 1 fails, all fail, some fail (state the mixed state precisely)
- retry one, retry all, retry while others still running
- cancel mid-way; what do already-finished items do
- same item submitted twice (idempotency)
- progress and ordering shown to the user
- what the table / list / card shows for each of the above

Produce at least 15 scenarios. Include unlikely ones. Do not filter for
likelihood; that is a later stage's job. Output ONLY the YAML list in the
schema below. ...
```

Subagents run in isolated context windows, results come back as a summary, and by default up to 20 can run concurrently. That matches Stage 1 exactly.

### 4.2 Orchestration: a Workflow script or a skill

Two options.

**Option A: a skill (`.claude/skills/scenarios/SKILL.md`)** that tells the main agent to spawn the lens agents in parallel via the Agent tool, then run the later stages. Simpler, good enough to start, and the main agent keeps full context.

**Option B: the Workflow tool.** Deterministic script: `parallel()` over the lenses, then `pipeline()` into grounding, adversarial pass and scoring, with JSON schemas enforced at each stage. Better once the pipeline is stable, because the stages cannot drift and each agent gets exactly the inputs the script hands it. The `review-changes` pattern in the Workflow docs (review dimensions in parallel, verify each finding) is almost this shape already.

Recommendation: **start with A, move to B** once the lens prompts have settled.

### 4.3 Effort scaling (from the Anthropic post)

Put this in the skill so it does not over-run on small asks:

- A single button or field: 3 lenses (state, visual, human behaviour), no adversarial stage, go straight to scoring.
- A page or a table: all lenses, adversarial pass on the top 30 only.
- A whole feature with batch operations and external services: all lenses, full pipeline, grounding against code mandatory.

---

## 5. Walking the two real misses through the pipeline

**White play button**

- Stage 1: the Visual lens checklist line "control on same-colour background" and "image that is all one colour" both produce it. The Data-shape lens may also produce "thumbnail is a solid colour / blank frame".
- Stage 3: reachable, since thumbnails come from user video and the first frame can be anything.
- Stage 4: skeptic argues "rare". Proposer argues "zero detectability, cheap fix". Judge keeps it.
- Stage 5: Severity 2, Occurrence 2, Detection 5, Cost 1. RPN 20, but the Detection score is what gets it built.
- Stage 6: build now; acceptance criterion "play affordance remains visible on any thumbnail luminance".

**5 runs, 2 fail**

- Stage 1: the Batch lens line "some fail (state the mixed state precisely)" produces it, along with the follow-ups that were also missing: retry only the failed two, what the aggregate row shows, whether the batch is "done" or "partial".
- Stage 3: reachable.
- Stage 5: Severity 4, Occurrence 4, Detection 2. Top of the list.
- Stage 6: build now, and the scenario table forces the table design to carry a `partial` status plus per-row status, which is the thing that was missed.

---

## 6. Where this system itself will fail, and the mitigations

| Failure | Mitigation |
|---|---|
| Lens agents produce generic scenarios for a generic app | Stage 0 spec capture is mandatory input; lens prompts say "only scenarios that reference a surface or action from the spec" |
| Lens output converges because all lenses share a backbone | Use different models for some lenses (Sonnet vs Opus vs Haiku). The judge-bias paper suggests judge and candidates should not share a backbone where possible |
| Scenario explosion, 150 items nobody reads | Dedupe, grounding and the adversarial threshold are filters; the human only sees the ranked table after Stage 5 |
| Debate talks a true scenario out of existence | Fixed rounds, separate judge, Detection score weighted explicitly |
| Judge scores drift between runs | 3 runs, median |
| Cost (about 15x chat) | Effort scaling rules; cheap model for merge; only run the full pipeline before implementation, not on every message |
| Checklists stale | Stage 8 misses log is the feed |

---

## 7. How to evaluate it before trusting it

Following the Anthropic advice, build about **20 seed cases**: features you already shipped where you know what was missed (start with the two above, plus whatever your bug tracker says). Run the pipeline on the spec as it existed before implementation. Metric: **recall of known misses in the "build now" list**, and **how far down the ranking** each known miss landed. Tune lens checklists until recall on the seed set is high, then watch the misses log on real features.

---

## 8. Recommended next step

Build Option A: a `/scenarios` skill plus 6 lens agents (state, batch, data shape, visual, human behaviour, wildcard), a grounding agent, a scoring judge, and the misses log. Run it against one real feature you are about to build and compare its "build now" table with what you would have written by hand. Add the adversarial stage and the Workflow version only if the ranked list is too long or too noisy to act on.

---

## Sources

Primary, read in full:
- Anthropic, How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Claude Code subagents documentation: https://code.claude.com/docs/en/sub-agents

From search excerpts (arxiv.org unreachable from this container):
- Debate or Vote: https://arxiv.org/html/2508.17536v1
- Talk Isn't Always Cheap: Failure Modes in Multi-Agent Debate: https://arxiv.org/html/2509.05396v1
- Adaptive heterogeneous multi-agent debate (A-HMAD): https://link.springer.com/article/10.1007/s44443-025-00353-3
- The Confident Liar: Diagnosing Multi-Agent Debate: https://arxiv.org/pdf/2606.10296
- Prompting Diverse Ideas (Wharton): https://arxiv.org/pdf/2402.01727
- AI and Its Impact on Creativity and Diversity: https://arxiv.org/abs/2607.27553
- Multi-persona prompting for design concept diversity: https://www.cambridge.org/core/journals/design-science/article/enhancing-design-concept-diversity-multipersona-prompting-strategies-for-large-language-models/3B346E253508337A4EE899499BE49D9B
- Breaking Homogeneity: Diversifying Persona Sets: https://arxiv.org/html/2609.30492v1
- Multi-Agent LLM Dialogues for Research Ideation: https://arxiv.org/html/2507.08350v1
- Rating Roulette: Self-Inconsistency in LLM-as-a-Judge: https://aclanthology.org/2025.findings-emnlp.1361.pdf
- Judging with Many Minds (judge bias): https://arxiv.org/pdf/2505.19477
- From Generation to Judgment (LLM-as-judge survey): https://arxiv.org/pdf/2411.16594
- EdgeGen: Synthetic Edge Case Generation: https://arxiv.org/html/2609.24115
- ForesightSafety-SAGE scenario generation: https://arxiv.org/pdf/2606.08531
- How Do LLMs Fail in Agentic Scenarios: https://arxiv.org/pdf/2512.07497
- Automatic High-Level Test Case Generation using LLMs: https://arxiv.org/html/2503.17998v1
- UI state checklists: https://pluma.customer.io/patterns/states and https://openskillindex.com/skills/openclaw-skills-ux-baseline-check
- Premortem + FMEA agent skill (community): https://skills.cat/skills/neurofoo/agent-skills/premortem

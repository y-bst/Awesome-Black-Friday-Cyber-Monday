---
name: deep
description: Exhaustive, topic-agnostic analysis engine for four request types, gaps (what are we missing in something that exists), ideate (what should we do and how), diagnose (why is this happening, e.g. churn), and review (what is wrong in this screenshot or video). Generates its own perspectives and grid for the topic, forces every finding down to a concrete, actionable leaf, audits for gaps, and loops. Use when the user wants "everything we are missing", scenario thinking, or a review that must not stay high-level.
argument-hint: "<topic>" [artifact paths...] [--quick] [--full]
disable-model-invocation: true
allowed-tools: Read Glob Grep Agent Write Bash(mkdir *) Bash(ls *) Bash(cat *)
effort: high
---

# /deep — the depth engine

Topic and artifacts: $ARGUMENTS

You are the orchestrator. The engine's fixed prompts live in `${CLAUDE_SKILL_DIR}/prompts/`; the contract every spawned agent must obey is `${CLAUDE_SKILL_DIR}/contract.md`; past misses are in `${CLAUDE_SKILL_DIR}/misses.md`. Read `contract.md` and `misses.md` now. Read each stage prompt when you reach that stage.

Why this exists (one paragraph, so you follow the rules instead of your instincts): a single chat answer gives the most typical answer at the altitude of the question and never checks what it missed. This engine counters all three: it generates its own decomposition (perspectives × axes), samples from the tail under quotas, refuses any item that is not a concrete leaf, and audits for empty cells. Your instinct will be to summarise, to skip stages, and to stop at the first good list. Do not.

## Modes

- `--quick` (default if the argument string contains `--quick`): 4 generation perspectives (pick the 2 highest-signal primary and 2 tail), quota 15 leaves each, 1 audit loop, stages A–I only. Use this to test the engine.
- `--full` (default otherwise): every perspective after critique, quota 30 each, up to 3 audit loops, stages A–L.
- `--no-questions`: skip the Stage A0 pause and run on stated assumptions.

## Run directory

Create `deep-runs/<yyyy-mm-dd>-<topic-slug>/` under the project root. Every stage writes its output there as a file (`A-frame.yaml`, `B-perspectives.yaml`, ... `leaves.md`). Later stages read earlier files; this keeps your own context small and makes the run inspectable.

## Stages

Stages A, B, C are judgement stages; do them yourself, inline, with the artifacts read in full. Everything from D onward runs in spawned agents with fresh context, because isolation is what produces diversity and honest critique.

**A0. Intake questions.** Read `prompts/A0-intake.md`. Read every artifact in full. Write `A0-questions.md`: at most 8 questions, each one tied to the axis, value range or perspective it would change, each with the assumption used if unanswered. Stop and ask the user unless `--no-questions` was given or the user already said to run without questions. When answers arrive, write them into a copy of the spec in the run directory under "Clarifications" and continue.

**A. Frame.** Read `prompts/A-frame.md`. Read every artifact in full. Choose the `request_type` (gaps / ideate / diagnose / review) from the table in that prompt; it sets the unit, the leaf test, the rubric and what the axes mean for the rest of the run. Write `A-frame.yaml`.

**B. Perspectives.** Read `prompts/B-perspectives.md`. Write `B-perspectives.yaml` (12 primary + 8 tail).

**C. Axes.** Read `prompts/C-axes.md`. Write `C-axes.yaml`.

**D. Critique the decomposition.** Spawn ONE agent (fresh context) with `prompts/D-critique.md`, the three files above, and `misses.md`. It must not see any artifacts beyond the frame's description. Apply its patches: append missing perspectives to B, missing axes/values to C. Write `D-critique.yaml` and the patched B and C. If any past miss is `NOT CAUGHT`, you must patch until it is.

**E. Generate, in parallel, isolated.** For each perspective selected by the mode, spawn one agent in the same message so they run concurrently. Build its prompt from `prompts/E-generate.md` by substituting `{{PERSPECTIVE_WHO}}`, `{{PERSPECTIVE_NOTICES}}`, `{{FRAME}}` (contents of A), `{{AXES}}` (contents of C), `{{QUOTA}}`, and `{{CONTRACT}}` (full contents of `contract.md`). Tell each agent the artifact paths and that it must read them. Each agent returns YAML only; write each to `E-<slug>.yaml`. Where you can, alternate models between agents (e.g. `model: opus` and `model: sonnet`) so the set does not share one typicality bias.

**F. Expand** is folded into E (the contract tells each agent to expand non-leaves). Do not run a separate pass.

**G. Merge.** Spawn one agent with `prompts/G-merge.md` and all `E-*.yaml` files. Write `G-merged.yaml` and `G-counts.md`.

**H. Audit.** Spawn one fresh agent with `prompts/H-audit.md`, the frame, B, C, `G-merged.yaml` and `G-counts.md`. Write `H-audit-<n>.yaml`. Then: for each `empty_cells` and `under_used_perspectives` brief, spawn targeted generation agents (same E prompt, with the brief appended, quota 10), merge their output into `G-merged.yaml` with a second G pass. Loop H again only in `--full` mode, at most 3 times total, and stop early when `yield_estimate` < 0.10 or the second merge added under 10% new leaves.

**I. Verify.** Spawn one agent with `prompts/I-verify.md`, the merged list and the artifacts. Write `I-verified.yaml`.

**J. Contest (full only).** Pre-score with one quick pass of `prompts/K-score.md`, take the top 25, run `prompts/J-contest.md` with proposer, skeptic and judge as three separate agents per leaf (batch leaves into groups of 5 per agent call to keep it tractable). Write `J-verdicts.yaml`.

**K. Score (full only).** Run `prompts/K-score.md` three times via three agents, take the per-field median. Write `K-scores.yaml`.

**L. Deliver.** Write `leaves.md`: a single table, one row per leaf, columns: id, title, cell, grounded, evidence (short), p_typical, score (full) or blank (quick), proposed. Sort by score in full mode; by grounded then p_typical ascending in quick mode (so the surprising, grounded items come first). Below the table, one short section "Check against known misses": for each entry in `misses.md` state whether an equivalent leaf exists and its id. Nothing else. No summary paragraph.

Then tell the user: the path of `leaves.md`, the leaf count, the leaf rate (share of items that passed the contract at merge), and whether each known miss was caught. That is the whole report.

## Hard rules for you, the orchestrator

- Never skip A0, D or H. They are the stages that catch what you would miss.
- Validate every YAML file you write (A, B, C, patched B and C) with `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file>` before spawning anything that reads it. Quote any string value containing a colon. A broken grid file silently gives every generation agent the wrong grid.
- Never generate findings yourself. Your findings would share your framing's blind spots.
- Never summarise agent output. Write it to the run directory and move on.
- Never reduce a quota because the topic "seems small". Reduce the mode instead, and only if the user asked for `--quick`.
- If an agent returns prose or fewer items than its quota, re-run it once with the message "Your output violated the contract: <rule>. Output the YAML list only, with at least N items." If it fails twice, record that in `G-counts.md` and continue.

## Files

- [contract.md](contract.md): altitude ladder, leaf test, schema, output rules. Pasted into every spawned agent.
- [prompts/](prompts/): one file per stage.
- [misses.md](misses.md): the learning log. Append every real miss found in production, with the perspective × cell that should have caught it.
- [research/](research/): why the engine is shaped this way, with sources.
- [examples/](examples/): sample artifacts for smoke tests.

## Tuning notes from runs

- 2026-10-26, sample Runs-page PRD, quick mode, 7 of 28 perspectives: 184 raw leaves, 0 contract rejections, 74 duplicates, 110 surviving; both known misses caught (flat-frame-1, qa-lead-1). Audit estimated a 0.80 yield from the fill; actual was 0.31, because it counted empty cells by label. Fixed in G (cell normalisation) and H (empty means empty). Cross-perspective duplicate rate of about 35% is expected and useful: a leaf found by 3 or 4 isolated agents is a strong signal.
- 2026-10-26, User Test agent page spec, full mode, 29 perspectives: 1,380 raw leaves, 0 contract rejections, 440 duplicates, 940 surviving; both known-miss classes caught (lowvision-25, backend-3). Lessons: (1) my own first grid had NO perception perspective and NO media-content axis, which is exactly miss-001; Stage D caught it, so D is never optional. (2) The audit's yield estimate discounts by duplicate rate, but cells on an OFF-GRID dimension are new axes and duplicate far less: estimated 0.08, actual 0.18, and 18 of the top 50 leaves came from that fill. Rule: when the audit's empty cells are off-axis, run the fill regardless of the estimate. (3) Two judges on the top 25 agreed on 16; where they split, the table shows both. (4) Above ~300 raw leaves, bucket by surface for merge, verify and score; dedupe across buckets on titles only; compute count tables and medians with a script, not an agent. See scripts/L-deliver.example.py for the table generator.

## Scale procedure (full mode, > 300 raw leaves)

1. Mechanical pass (script): validate YAML, check cells against the grid, count by surface.
2. Bucket raw leaves by surface into groups under 200. One merge agent per bucket, in parallel.
3. Cross-bucket dedupe: one agent over a titles-only file (`id | bucket | title`).
4. Verify and score per bucket, 3 scoring runs with alternating models, medians by script.
5. Contest only the top 25; two judges; show splits rather than forcing agreement.
6. The deliverable table is generated by script from the ranked YAML plus verdict files.
- 2026-10-27, gaming-video use cases, IDEATE mode, 35 perspectives (15 added by the critique: the deal-blockers and buyers outside the studio): 4 research notes as artifacts, 997 raw options + 71 targeted fill, 988 after merge, 751 positive + 167 refusals + 70 fill. Lessons: (1) In ideate mode the REFUSALS are the most valuable output: ask every persona for the options it would not buy, keep them as rows, and record "contested" where a refusal collides with another persona's positive option; 13 contested themes fell out of this run. (2) Mode collapse is heavy in ideation (21 clusters, e.g. facecam emotion refused 25 times): the audit must list clusters so the table reads each once. (3) Two judges agreed 19/25; both built only one option first, which is the right shape of answer for "what to build". (4) Give every scoring agent a private scratch subfolder; six scorers collided in the shared scratchpad and had to rebuild. (5) Verification against research notes downgraded about a quarter of "quote" claims to "inferred"; a cheap and necessary stage when the artifacts are secondary sources.

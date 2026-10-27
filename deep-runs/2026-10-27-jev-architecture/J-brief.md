# Stage J brief (contest, ideate, top 25)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-27-jev-architecture

Read: .claude/skills/deep/prompts/J-contest.md, A-frame.yaml, spec.md, memo.md, then J-top25.yaml (25 options with scores). Your batch is options at positions given in your prompt (1-based, in file order).

Role PROPOSER: for each option in your batch, write the strongest one-paragraph case (5-8 sentences) that JEV should build this in the next quarter, as part of making unknown studio questions answerable correctly and fast. Cite the option's evidence, spec.md or memo.md. Be concrete about which studio questions it makes answerable, how fast, and what breaks without it.
Role SKEPTIC: for each option in your batch, write the strongest one-paragraph case that it should be deferred, folded into another option, or rejected: it duplicates the memo, costs more than it returns, depends on something not yet built, only helps tutorial questions, or will not work with today's models. Be honest; if you cannot make a real case, say so in one line.
Role JUDGE (later, separate agent): sees both cases, not the authors.

Write deep-runs/2026-10-27-jev-architecture/J-<role>-batch<B>.yaml as:
```yaml
- id: <option id>
  case: <paragraph>
```
Final reply: the path and the count. Nothing else.

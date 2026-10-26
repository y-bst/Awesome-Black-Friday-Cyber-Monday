# Stage J brief (contest, top 25)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-user-test-agent-page

Read: .claude/skills/deep/prompts/J-contest.md, A-frame.yaml, spec.md, then J-top25.yaml (25 leaves with scores). Your batch is leaves at positions given in your prompt (1-based, in file order).

Role PROPOSER: for each leaf in your batch, write the strongest one-paragraph case (5-8 sentences) that the PM must specify this NOW, before build. Cite the leaf's evidence and the spec. Be concrete about what goes wrong and for whom if it ships unspecified.
Role SKEPTIC: for each leaf in your batch, write the strongest one-paragraph case that it should be deferred, accepted as-is, or rejected as unreal: it is improbable, covered by a reasonable default, cheap to fix later, or not this feature's job. Be honest; if you cannot make a real case, say so in one line.
Role JUDGE (later, separate agent): sees both cases, not the authors.

Write deep-runs/2026-10-26-user-test-agent-page/J-<role>-batch<B>.yaml as:
```yaml
- id: <leaf id>
  case: <paragraph>
```
Final reply: the path and the count. Nothing else.

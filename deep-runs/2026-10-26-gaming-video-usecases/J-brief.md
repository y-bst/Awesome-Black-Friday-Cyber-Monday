# Stage J brief (contest, top 25, IDEATE run)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-gaming-video-usecases

Read: .claude/skills/deep/prompts/J-contest.md, A-frame.yaml, the four research notes in research/, then J-top25.yaml (25 options with scores). Your batch is the options at the positions given in your prompt (1-based, file order).

Role PROPOSER: for each option in your batch, write the strongest one-paragraph case (5-8 sentences) that the founder should build and sell this FIRST. Name the buyer, the price anchor from the notes, what it replaces, and why incumbents cannot copy it quickly.
Role SKEPTIC: for each option, write the strongest one-paragraph case that it should be explored later, dropped, or is already served: the buyer has no budget line, an incumbent is one feature flag away, the capture or consent burden kills it, the accuracy is not there, or the research notes do not actually support the demand. Be honest; if you cannot make a real case, say so in one line.

Write J-<role>-batch<B>.yaml as `- id: ... / case: ...`. Final reply: the path and count. Nothing else.

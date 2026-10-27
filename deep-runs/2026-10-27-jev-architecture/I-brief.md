# Stage I brief (verify against the artifact)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-27-jev-architecture

Read first: .claude/skills/deep/prompts/I-verify.md, then every artifact listed in A-frame.yaml in full, then your input G-merged-<N>.yaml.
For EVERY item set `grounded` (quote: the artifact directly supports the situation or demand, exact quote in `evidence`; inferred: implied, closest quote plus one clause; speculative: nothing in the artifacts, `evidence: none`) and `already_specified: true|false` (gaps) or `already_offered: true|false` (ideate, true only when the memo or spec already contains this exact option). Do not delete or reword. Write I-verified-<N>.yaml with a trailing comment of counts. Final reply: path and counts. Use a private scratch subfolder.

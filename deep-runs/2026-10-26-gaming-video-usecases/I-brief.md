# Stage I brief (verify options against the research notes, IDEATE run)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-gaming-video-usecases

Read first: .claude/skills/deep/prompts/I-verify.md, then the four research notes in research/ (market.md, methods-churn-funnel.md, competitor-and-ua.md, adjacent-usecases.md), then your input file G-merged-<N>.yaml.

For EVERY option, re-check `grounded`, `evidence`, `why_existing_tools_cannot` and `willingness_to_pay` against the notes:
- `grounded: quote` — a note states a buyer, price, vendor gap or complaint that directly supports this option's demand or feasibility; `evidence` must quote it with the file name.
- `grounded: inferred` — the notes imply it (an adjacent price, a named gap in the gap map) but nothing states it; `evidence` = closest quote plus one clause on the inference.
- `grounded: speculative` — nothing in the notes supports it; `evidence: none`.
Also add `already_offered: true|false` — true when a note shows a vendor ALREADY sells this exact option (name the vendor in `already_offered_by`), which is the ideate equivalent of "already specified". Be strict: PlaytestCloud's AI reading transcripts is not the same as vision on gameplay frames.
Do NOT delete any option. Do not reword titles. Preserve every other field.

Write I-verified-<N>.yaml (full list, updated fields) with a trailing YAML comment of counts: quote / inferred / speculative, already_offered count with ids. Final reply: the path and the counts.

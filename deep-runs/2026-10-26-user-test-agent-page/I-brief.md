# Stage I brief (verify against the artifact)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-user-test-agent-page

Read first: .claude/skills/deep/prompts/I-verify.md, then the artifact deep-runs/2026-10-26-user-test-agent-page/spec.md in full, then your input file G-merged-<N>.yaml.

For EVERY leaf, re-check `grounded` and `evidence` against spec.md and correct them:
- `grounded: quote` — spec.md contains a sentence, field, mode, control or rule that directly makes this situation possible. `evidence` must be an exact quote from spec.md.
- `grounded: inferred` — spec.md implies it (the feature exists so the situation can arise) but no sentence directly supports it. `evidence` = closest quote plus one clause on the inference.
- `grounded: speculative` — nothing in spec.md supports it; it comes from general knowledge. `evidence: none`.
Also add `already_specified: true|false`. True only when spec.md already answers the situation; quote where in `already_specified_by`. Be strict: "Follow-up questions are supported" does NOT specify where the follow-up box is, limits, or failure handling. The "Still unspecified" list in spec.md confirms those items are gaps, not answers.

Do NOT delete any leaf. Do not reword titles. Preserve every other field (including also_from and bucket).

Write deep-runs/2026-10-26-user-test-agent-page/I-verified-<N>.yaml (full list, updated fields) and append a trailing YAML comment with counts: quote / inferred / speculative, and already_specified true count with ids.
Final reply: the path and those counts. Nothing else.

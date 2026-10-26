# Stage K brief (score)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-user-test-agent-page

Read first: .claude/skills/deep/prompts/K-score.md, then A-frame.yaml (rubric: fmea), then spec.md, then your input file I-verified-<N>.yaml.

Score EVERY leaf independently on the FMEA rubric. Do not compare leaves to each other. Do not skip any.
- severity 1-5: how bad for the user or business if this situation happens unspecified (5 = data loss, wrong decisions made from a report, legal exposure, or a user who cannot proceed).
- occurrence 1-5: how often the situation will arise in normal use of a user-testing product (5 = most sessions).
- detectability 1-5: 5 = nobody on the team would notice without this list (silent wrong output, invisible UI state); 1 = obvious the first time anyone tries it.
- cost_to_address 1-5: 1 = a spec sentence or copy change; 5 = new subsystem.
Use the `grounded` field as context but do not score it.

Write deep-runs/2026-10-26-user-test-agent-page/K-scores-<N>-run<R>.yaml as a YAML list of {id, severity, occurrence, detectability, cost_to_address} only, one entry per leaf, same order as the input. Final reply: the path and the count. Nothing else.

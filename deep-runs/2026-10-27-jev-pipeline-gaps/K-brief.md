# Stage K brief (score, gaps run; rubric fmea)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-27-jev-pipeline-gaps

Read: .claude/skills/deep/prompts/K-score.md, A-frame.yaml, spec.md, then I-verified-<N>.yaml. Score EVERY leaf independently: severity 1-5 (5 = a studio makes a wrong decision from a wrong answer, or data is unrecoverably lost), occurrence 1-5 (5 = most sessions), detectability 1-5 (5 = nobody would notice without this list), cost_to_address 1-5 (1 = a rule or prompt line; 5 = new subsystem). Write K-scores-<N>-run<R>.yaml as {id, severity, occurrence, detectability, cost_to_address} in input order. Private scratch subfolder. Do not open other K-scores files. Final reply: path and count.

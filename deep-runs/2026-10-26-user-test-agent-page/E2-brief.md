# Targeted fill brief (after audit 1)

Same as E-brief.md, with these changes:
- Read E-brief.md first and follow it, EXCEPT: your job is ONE cell named in your prompt, not the whole grid.
- The cell may name an off-axis dimension (one not in C-axes.yaml). Put the off-axis key and value in `cell` anyway, alongside at least 2 values that ARE in C-axes.yaml.
- Before writing, grep deep-runs/2026-10-26-user-test-agent-page/G-titles-all.txt for your cell's key terms so you do not repeat an existing leaf; the audit listed the few existing hits in your brief.
- Quota: at least 12 leaves. At least two thirds with p_typical below 0.10.
- Output path and id prefix are given in your prompt.

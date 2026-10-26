# Stage E brief (shared by every generation agent of this run)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-user-test-agent-page

Read these files in full, in this order, before writing anything:
1. .claude/skills/deep/contract.md  — the contract: altitude ladder, leaf test, schema, output rules. Obey it exactly.
2. deep-runs/2026-10-26-user-test-agent-page/A-frame.yaml  — topic, unit, leaf test, assumptions.
3. deep-runs/2026-10-26-user-test-agent-page/C-axes.yaml  — the grid you must walk (18 axes). Use its exact value strings in `cell`.
4. deep-runs/2026-10-26-user-test-agent-page/spec.md  — the artifact under review. Quote it in `evidence`.

Procedure:
1. For each axis, for each value, ask: what would I, specifically, notice in this situation that the spec does not specify? Write it down even if minor or improbable.
2. For at least 12 full cells (combinations across several axes), do the same.
3. Classify each item on the altitude ladder. Anything above L3: expand into at least 3 children, apply the leaf test, keep only leaves.
4. Re-read your list and ask: "what would I say is missing if a colleague showed me this?" Add those.
5. Quota: at least 30 leaves. At least two thirds with p_typical below 0.10.
6. Every leaf's `cell` must name at least 3 axis values from C-axes.yaml, using the exact strings.

Write the YAML list only to the output path given in your prompt. Final reply: the path and the leaf count. Nothing else.

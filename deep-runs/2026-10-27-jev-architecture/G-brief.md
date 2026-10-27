# Stage G brief (bucket merge)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-27-jev-architecture

Read first: .claude/skills/deep/contract.md, .claude/skills/deep/prompts/G-merge.md (including cell normalisation), A-frame.yaml, C-axes.yaml, then your bucket file G-bucket-<N>.yaml.

1. Reject contract violations (not a leaf, no concrete object, banned vocabulary without an instance, prose). List rejected ids with the rule.
2. Cluster duplicates: the SAME situation on the same object (gaps run) or the SAME mechanism for the same part and input (ideate run). Survivor keeps id; add `also_from`. Same mechanism with a different part or scope is a VARIANT: add `variants_of`, keep both.
3. Ideate run only: refusal rows (willingness 1 or titled refused) stay as rows with `refusal: true`; if a refusal collides with a positive option, keep both and add `contested_by` on the positive.
4. Cell normalisation: add any C-axes.yaml value the item plainly satisfies. Drop `_from_file`; add `perspective` (id prefix).
5. Do not rank. Do not drop improbable items.
Write G-merged-<N>.yaml (survivors, full schema) and G-counts-<N>.md (in / rejected / clusters / variants / contested / surviving; counts per value for every axis, zero values listed). Final reply: paths and surviving count. Use a private subfolder of the scratchpad for working files.

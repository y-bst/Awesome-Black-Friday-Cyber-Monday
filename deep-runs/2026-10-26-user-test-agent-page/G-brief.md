# Stage G brief (bucket merge)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-user-test-agent-page

Read first: .claude/skills/deep/contract.md and .claude/skills/deep/prompts/G-merge.md (including the cell-normalisation section), then deep-runs/2026-10-26-user-test-agent-page/C-axes.yaml, then your bucket file.

Do exactly this on your bucket:
1. Reject items that violate the contract: not L3/L4, no concrete object from the spec, banned vocabulary without a specific instance on the same line, prose instead of schema. List every rejected id with the rule broken. (A mechanical pass already confirmed every item is L3/L4 and uses valid axis values, so expect few rejections.)
2. Cluster near-duplicates: same situation on the same object, even if worded differently or from different perspectives. Keep the most specific wording as the survivor, keep its id, add `also_from: [<other ids>]`. Different gaps on a similar situation are NOT duplicates ("no partial state" vs "no retry for the failed ones" are two leaves).
3. Cell normalisation: add to each survivor's `cell` any axis value from C-axes.yaml that its `situation` plainly satisfies but the agent did not name. Keep exact value strings.
4. Keep every surviving leaf's full schema. Drop the `_from_file` key.
5. Do not rank. Do not drop improbable items.

Write:
- deep-runs/2026-10-26-user-test-agent-page/G-merged-<N>.yaml : surviving leaves (YAML list, full schema, also_from where clustered)
- deep-runs/2026-10-26-user-test-agent-page/G-counts-<N>.md : leaves in, rejected (ids + rule), duplicate clusters (survivor <- merged ids), surviving count, and a table of surviving counts per axis VALUE for every axis in C-axes.yaml (list values with zero leaves explicitly; a leaf counts under every value its cell names).

Final reply: the two paths and the surviving count. Nothing else.

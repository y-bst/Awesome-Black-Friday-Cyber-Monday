# Stage G: Merge

Input: the YAML leaf lists from every perspective agent.

1. Reject items that violate the contract (not a leaf, no concrete object, banned vocabulary without an instance, prose). List rejected ids with the rule broken.
2. Cluster near-duplicates. Keep the most specific wording. Record `also_from: [<perspective slugs>]` so convergence is visible.
3. Tag every surviving leaf with its cell. Items with `uncategorised: true` are kept and listed separately for the audit.
4. Output: the merged YAML list, then a short table of counts: leaves per perspective, leaves per axis value, rejected count, duplicate count.

Do not rank. Do not drop improbable items.

## Cell normalisation (added after smoke test 2026-10-26)

Agents label cells inconsistently: one writes `batch-size: exactly-5-files`, another `batch-size: 2-5-files-one-submit`, for the same situation. Before counting, add to each leaf's `cell` every axis value from C-axes.yaml that its `situation` plainly satisfies, even if the agent did not name it. Then build the count table from the normalised cells. Record how many leaves had values added.

# Stage G: Merge

Input: the YAML leaf lists from every perspective agent.

1. Reject items that violate the contract (not a leaf, no concrete object, banned vocabulary without an instance, prose). List rejected ids with the rule broken.
2. Cluster near-duplicates. Keep the most specific wording. Record `also_from: [<perspective slugs>]` so convergence is visible.
3. Tag every surviving leaf with its cell. Items with `uncategorised: true` are kept and listed separately for the audit.
4. Output: the merged YAML list, then a short table of counts: leaves per perspective, leaves per axis value, rejected count, duplicate count.

Do not rank. Do not drop improbable items.

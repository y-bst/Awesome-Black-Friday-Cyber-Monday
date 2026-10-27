# Stage G brief (bucket merge, IDEATE run)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-gaming-video-usecases

Read first: .claude/skills/deep/contract.md (note the ideate fields), .claude/skills/deep/prompts/G-merge.md, A-frame.yaml, C-axes.yaml, then your bucket file G-bucket-<N>.yaml.

These are OPTIONS (things to build and sell), bucketed by buyer-role. Do exactly this:
1. Reject items that violate the contract: a category rather than a concrete option, no buyer or no mechanism or no concrete example, banned vocabulary without a specific instance. List rejected ids with the rule.
2. Cluster duplicates: the SAME option (same mechanism for the same buyer on the same input), even if worded differently or proposed by different perspectives. Keep the most specific wording as survivor, keep its id, add `also_from: [ids]`. Two options with the same mechanism but a different buyer or a different delivery form are NOT duplicates; record the relationship in `variants_of: <id>` instead and keep both.
3. Refusal leaves (willingness_to_pay 1, persona would not buy) are kept, tagged `refusal: true`, and if a refusal duplicates a positive option from another perspective, do NOT merge them: add `contested_by: [<refusal ids>]` on the positive option and keep the refusal as its own row. That disagreement is the most useful signal in the run.
4. Cell normalisation: add any C-axes.yaml value the option plainly satisfies. Drop `_from_file`.
5. Do not rank. Do not drop improbable options.

Write G-merged-<N>.yaml (survivors, full schema) and G-counts-<N>.md (in / rejected / duplicate clusters / variants / contested count / surviving; counts per value for buyer-role, video-source, analysis-type, delivery-form, pricing-model, value-lever-b2b, buyer-org-type). Final reply: the paths and surviving count.

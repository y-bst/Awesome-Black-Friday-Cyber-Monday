# Stage E brief (ideate run: gaming video use cases)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-gaming-video-usecases

Read in full, in this order:
1. .claude/skills/deep/contract.md  (contract; note the IDEATE type-specific fields: mechanism, example, cost, depends_on)
2. deep-runs/2026-10-26-gaming-video-usecases/A-frame.yaml  (request_type ideate; leaf test; extra_leaf_fields: buyer, input, why_existing_tools_cannot, willingness_to_pay)
3. deep-runs/2026-10-26-gaming-video-usecases/B-perspectives.yaml  (find YOUR slug; that is who you are)
4. deep-runs/2026-10-26-gaming-video-usecases/C-axes.yaml  (the SOLUTION-space grid; use exact value strings)
5. The four research notes in deep-runs/2026-10-26-gaming-video-usecases/research/ (market.md, methods-churn-funnel.md, competitor-and-ua.md, adjacent-usecases.md). Cite them by file and section in `evidence` and in `why_existing_tools_cannot`.

You are generating OPTIONS (things to build and sell), not gaps. Each leaf = one concrete capability or service.

Procedure:
1. For each axis, for each value, ask: what would I, this person, buy or build here? Write it down even if it seems niche.
2. For at least 10 full cells (combinations across 5+ axes), do the same; each cell should yield several distinct options.
3. Apply the leaf test from A-frame.yaml: buyer role, input, mechanism, one concrete example, why existing tools cannot. Expand categories into leaves.
4. Include the options your persona would REFUSE to buy, as leaves with low willingness_to_pay and the reason in `consequence`; those are as useful as the ones they would buy.
5. Quota: at least 20 leaves; at least two thirds with p_typical below 0.10 (the obvious "video-based funnel analytics" is the mode; the job is the tail).
6. `cell` must name at least 4 axis values with exact strings. Required fields beyond the base schema: mechanism, example, cost (S/M/L), depends_on, buyer, input, why_existing_tools_cannot, willingness_to_pay (1-5 plus the price or buyer signal from the notes).

Write the YAML list only to the output path in your prompt. Final reply: path and leaf count. Nothing else.

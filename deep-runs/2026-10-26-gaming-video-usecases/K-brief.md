# Stage K brief (score, IDEATE run; rubric: impact)

Working directory: /home/user/Awesome-Black-Friday-Cyber-Monday
Run directory: deep-runs/2026-10-26-gaming-video-usecases

Read first: .claude/skills/deep/prompts/K-score.md, A-frame.yaml, the four research notes in research/, then your input file I-verified-<N>.yaml.

Score EVERY option independently. Do not compare options to each other. Do not skip any.
- impact 1-5: value to the buyer if it works (5 = changes a go/kill, retention or revenue decision worth a team's quarter; 1 = nice to have).
- confidence 1-5: that it can be built and will work as described with today's models on consented device video (5 = proven components, a note cites it working; 1 = research problem).
- willingness 1-5: that the named buyer pays for it as a line item, from the notes' price and buyer signals (5 = a vendor already charges for an adjacent thing at a stated price; 1 = the buyer persona refuses or no budget line exists).
- cost 1-5: 1 = weeks with the existing User Test pipeline; 5 = new subsystem (SDK, on-device models, platform deals).
- moat 1-5: how hard it is for an incumbent (session-replay SDK, analytics vendor, playtest platform) to copy (5 = needs a data asset or platform position they lack; 1 = a feature flag for them).
Use `grounded` and `refusal` as context but do not score them.

Write K-scores-<N>-run<R>.yaml as a YAML list of {id, impact, confidence, willingness, cost, moat}, one entry per option, same order as the input. Final reply: the path and count.

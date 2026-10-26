# Feature: User Test agent page (draft spec, as described verbally)

## Agent page
Opening the agent page shows two modes: **Report** and **Ask question**.

### Report mode
- Run name (optional)
- Select videos the agent will run on
- Prompt / instructions (optional)
- Submit

### Ask question mode
- Select videos
- Type a question about the videos
- Suggested questions are shown and can be picked
- Submit

## After submit
There is no loading page, to save the user's time. On submit the user is redirected to the **History page**, where a new entry appears with whatever was submitted.

## History page
Lists past and current submissions (both modes).

## Unspecified (to be confirmed)
- What the third "thing" in the UI is (two modes were named: Report, Ask question)
- Where videos are selected from (existing library, upload now, both), and min/max count
- What a Report produces and whether one run covers all selected videos or one per video
- Statuses an entry can have on the History page, and what opening an entry shows
- Whether Ask question is one-shot or supports follow-ups, and whether suggested questions are static or derived from the selected videos
- Whether History is per user or per workspace

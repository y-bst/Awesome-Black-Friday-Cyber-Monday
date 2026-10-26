# Feature: User Test — agent page, history tab (spec as described verbally, with clarifications)

## Pages involved
- **Videos page**: users upload videos; uploaded videos get ingested.
- **Agent page**: two modes, **Report** and **Ask question**, plus a **History** tab.

## Agent page, Report mode
- Run name (optional)
- Add video: clicking "Add video" opens a pop-up where the user selects videos from their ingested videos. The pop-up supports filtering by the tags the user has applied to videos, and searching by name.
- Prompt / instructions (optional)
- Submit

## Agent page, Ask question mode
- Add video (same pop-up as Report mode)
- A question about the selected videos, typed by the user
- Suggested questions are shown and can be picked
- Submit
- Follow-up questions are supported after the first answer.

## After submit
There is no loading page, to save the user's time. On submit the user is redirected to the **History** tab, where a new entry appears with whatever was submitted.

## History tab
Lists past and current submissions from both modes. History is per user.

## Clarifications (from the product owner, 2026-10-26)
- The "third thing" in the UI is the History tab.
- Videos are selected from already-uploaded, ingested videos via the Add video pop-up, filterable by tags or search.
- A Report produces one output covering all selected videos, not one per video.
- Ask question supports follow-ups.
- History is per user, currently.

## Still unspecified (left for the engine to surface)
- Minimum and maximum number of videos per run; video length and size limits.
- Statuses an entry can have on the History tab, and what opening an entry shows while running, when done, and when failed.
- Whether suggested questions are static or derived from the selected videos.
- Whether a video that is still ingesting, or failed ingestion, can be selected.

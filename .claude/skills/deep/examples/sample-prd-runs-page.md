# PRD: Runs page (v0.3)

## Summary
The Runs page lets a user submit one or more video processing runs, watch their progress, and open a finished run to view the output video and its suggestions.

## Users
- Creator: submits runs, reviews outputs.
- Team admin: sees all runs for the workspace.

## Screens

### Runs table
Columns: thumbnail, title, status, submitted at, duration, actions.
Statuses: Queued, Processing, Done, Failed.
Actions: Open, Delete.
The thumbnail shows the first frame of the uploaded video with a white play icon centred on it. Clicking the thumbnail opens the run.
Rows are sorted by submitted-at descending. Page size is 25.

### Submit dialog
The user picks 1 to 5 video files (mp4, mov; max 2 GB each) and clicks Submit. One run is created per file. The dialog closes and the new rows appear at the top of the table with status Queued.

### Run detail page
Shows the output video player, a list of suggestions (text, each with Accept / Dismiss), and the run's metadata. Status badge in the header mirrors the table.

## Status transitions
Queued -> Processing -> Done
Queued -> Processing -> Failed
A Failed run shows an error message from the processing service in the detail page.

## Notifications
When a run reaches Done, the user receives an in-app notification.

## Non-goals
- Editing the output video.
- Sharing runs outside the workspace.

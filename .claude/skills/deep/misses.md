# Misses log

Every real-world miss goes here. Stage D reads this file and checks that the current grid would catch each one. This is the engine's only learning mechanism.

```yaml
- id: miss-001
  what: Video play button was white; thumbnails that are white or near-white made it invisible. No error, no log, users just did not click.
  should_have_been_caught_by: a perception perspective (colour-blind / low-contrast reviewer) x a content axis value "media is a single flat colour / very bright / very dark"
  detectability: 5

- id: miss-002
  what: Runs table was designed for all-succeed and all-fail. Submitting 5 runs where 2 fail had no defined aggregate row, no per-row retry, no "partial" batch status.
  should_have_been_caught_by: a QA / distributed-systems perspective x cardinality "2-20 items" x per-item-status "some failed" x action "retry"
  detectability: 2
```

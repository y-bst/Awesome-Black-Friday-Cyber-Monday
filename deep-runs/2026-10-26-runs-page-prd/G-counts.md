# Stage G merge counts: runs-page-prd

Inputs: 4 files, 130 leaves. Output: `G-merged.yaml` (84 surviving leaves; 83 on-grid, 1 in the uncategorised / off-grid section).

## Leaves in, per perspective

| perspective | leaves in | surviving | merged away as duplicates |
|---|---|---|---|
| qa-lead | 32 | 23 | 9 |
| support-agent | 34 | 16 | 18 |
| flat-frame-uploader | 30 | 21 | 9 |
| partial-run-failure | 34 | 24 | 10 |
| total | 130 | 84 | 46 |

## Rejected: 0

No leaf broke a contract rule. Checks run on all 130: level is L3 or L4 (130/130); every leaf names a concrete PRD object (quoted sentence, column, screen, status or action); every leaf is full schema, no prose; the banned-vocabulary scan found one hit ("such as" in flat-frame-10 line 115) and it is followed by a specific instance on the same line ('moov atom not found'), so it stands. No other banned word or "etc." appears anywhere.

## Duplicates clustered: 46 leaves merged into 28 survivors

Format: survivor, then the ids merged into it (recorded as `also_from` on the survivor).

| survivor | merged in | count |
|---|---|---|
| qa-lead-2 | support-agent-7, flat-frame-25, partial-failure-20 | 3 |
| qa-lead-1 | partial-failure-21 | 1 |
| qa-lead-5 | support-agent-11, flat-frame-19 | 2 |
| partial-failure-16 | qa-lead-9, support-agent-8 | 2 |
| support-agent-6 | qa-lead-10 | 1 |
| qa-lead-12 | flat-frame-9 | 1 |
| qa-lead-14 | support-agent-34, partial-failure-7 | 2 |
| partial-failure-22 | support-agent-21, flat-frame-10 | 2 |
| support-agent-1 | partial-failure-14 | 1 |
| qa-lead-23 | support-agent-3, support-agent-4 | 2 |
| qa-lead-26 | support-agent-10, partial-failure-2 | 2 |
| partial-failure-32 | qa-lead-19, support-agent-12, flat-frame-22 | 3 |
| partial-failure-11 | qa-lead-18, support-agent-23 | 2 |
| qa-lead-4 | flat-frame-12, support-agent-22 | 2 |
| flat-frame-20 | support-agent-20 | 1 |
| flat-frame-1 | support-agent-14 | 1 |
| support-agent-32 | qa-lead-31 | 1 |
| qa-lead-27 | support-agent-24, partial-failure-18 | 2 |
| partial-failure-23 | support-agent-9, flat-frame-16 | 2 |
| qa-lead-8 | support-agent-17 | 1 |
| support-agent-28 | qa-lead-32 | 1 |
| partial-failure-34 | qa-lead-28 | 1 |
| qa-lead-16 | support-agent-18, partial-failure-15 | 2 |
| support-agent-15 | qa-lead-29, flat-frame-13, partial-failure-25 | 3 |
| qa-lead-13 | flat-frame-23, partial-failure-24 | 2 |
| flat-frame-21 | support-agent-13 | 1 |
| support-agent-25 | partial-failure-31 | 1 |
| support-agent-29 | qa-lead-3 | 1 |

Judgement calls on the boundary (kept separate because the gap differs even where the situation is similar, per the "partial failure" rule in the brief): qa-lead-15 vs support-agent-2 (no Queued -> Failed timeout vs no cancel/Delete rule on Queued); flat-frame-17 vs qa-lead-26 (silent no-audio clip is a distinct cause of 0 suggestions); flat-frame-11 vs qa-lead-14 (non-retryable bad-codec Failed run vs transient failure); qa-lead-22 vs support-agent-28 (live update on Failed with error message vs on Done with notification); qa-lead-17 vs qa-lead-16 (row count after a partial upload vs missing Uploading state); partial-failure-4 and partial-failure-5 vs qa-lead-23 (internal-id leak and 50 KB length cap vs user-readable content); qa-lead-24 vs support-agent-33 (bulk delete vs recovery/retention); qa-lead-25 vs support-agent-5 (admin permission matrix vs deleted-by-teammate notice).

## Surviving leaf count

84 (83 on-grid + 1 uncategorised / off-grid: support-agent-26, whose cell uses `notification-state: mark-notification-read`, a value not in C-axes.yaml; no leaf uses `{uncategorised: true}`).

## Leaf rate

(surviving + duplicates) / input = (84 + 46) / 130 = 130 / 130 = 1.00 (rejected: 0).

## Surviving leaf counts per axis value

A leaf is counted under every value its cell names. Counts are survivors only; merged duplicates are not added. Where a zero-count value is named by a merged duplicate, that is noted. Off-grid values are listed at the end of their axis.

### surface

| value | surviving leaves |
|---|---|
| runs-table | 31 |
| submit-dialog | 6 |
| run-detail | 20 |
| in-app-notification | 5 |
| empty-state | 1 |
| delete-confirm-dialog | 3 |
| error-toast-or-banner | 2 |
| pagination-control | 2 |
| browser-tab-title | 1 |
| expired-or-deleted-run-url | 1 |

### batch-size

| value | surviving leaves |
|---|---|
| 0-files | 1 |
| 1-file | 0 |
| 2-5-files-one-submit | 0 (named only by 3 merged duplicate leaf/leaves) |
| exactly-5-files | 11 |
| 5-files-with-1-invalid | 1 |
| same-file-twice-in-one-submit | 1 |
| 6+-files-attempted | 2 |
| exactly-25-rows | 0 |
| 26-rows-then-delete-one-on-page-1 | 1 |
| table-26-plus-rows-multiple-pages | 2 |
| table-1000-plus-rows | 0 |
| 5-files-same-submitted-at-second | 1 |

### status-mix

| value | surviving leaves |
|---|---|
| uploading-pre-queued | 2 |
| upload-cancelled | 0 |
| all-queued | 2 |
| stuck-queued-over-1h | 3 |
| all-processing | 3 |
| stuck-processing-over-1h | 1 |
| all-done | 6 |
| all-failed | 3 |
| some-done-some-failed | 9 |
| some-processing-some-failed | 2 |
| deleted-while-processing | 2 |
| done-with-zero-suggestions | 3 |
| done-but-output-missing | 1 |
| failed-after-retry | 4 |
| failures-only-on-page-2 | 1 |
| unknown-status-string-from-backend | 1 |

### failure-point

| value | surviving leaves |
|---|---|
| client-validation | 4 |
| upload-transfer | 2 |
| queue-timeout-never-picked-up | 3 |
| processing-crash | 9 |
| output-encoding | 4 |
| suggestion-generation-only | 5 |
| output-stored-but-unplayable | 1 |
| delete-failed | 1 |

### media-content

| value | surviving leaves |
|---|---|
| ordinary-footage-first-frame | 0 |
| first-frame-flat-white-or-near-white | 2 |
| first-frame-flat-black | 1 |
| logo-on-plain-background | 4 |
| first-frame-already-contains-a-play-icon-or-text | 1 |
| portrait-or-square-aspect | 3 |
| 3-second-clip | 0 |
| 3-hour-video | 3 |
| no-video-track-or-0-seconds | 2 |
| video-with-no-audio-track | 1 |
| multiple-audio-tracks | 1 |
| unsupported-codec-in-valid-container | 1 |
| 4k-hdr-10bit | 1 |
| variable-frame-rate | 1 |
| corrupt-but-valid-extension | 0 (named only by 2 merged duplicate leaf/leaves) |
| exactly-2gb-or-over | 2 |
| filename-255-chars-or-emoji-or-no-extension | 1 |
| file-identical-to-existing-run | 1 |

### suggestion-state

| value | surviving leaves |
|---|---|
| 0-suggestions | 2 |
| 1 | 0 |
| 50 | 0 |
| 400-plus | 1 |
| none-acted-on | 0 |
| all-accepted | 0 |
| all-dismissed | 0 |
| mixed | 1 |
| accept-then-dismiss-same-item | 1 |
| acted-on-by-teammate | 0 |

### notification-state

| value | surviving leaves |
|---|---|
| single | 0 (named only by 1 merged duplicate leaf/leaves) |
| burst-of-5-in-one-minute | 4 |
| unread-for-days | 0 |
| clicked-after-run-deleted | 1 |
| arrives-while-viewing-that-run | 3 |
| app-closed-when-fired | 1 |
| mark-notification-read (off-grid, not in C-axes.yaml) | 1 |

### owner-lifecycle

| value | surviving leaves |
|---|---|
| owner-active | 2 |
| owner-removed-from-workspace | 1 |
| owner-account-deleted | 0 |
| workspace-plan-downgraded-or-over-quota | 1 |
| workspace-deleted | 0 |

### action

| value | surviving leaves |
|---|---|
| submit | 3 |
| double-click-submit | 1 |
| cancel-upload | 0 |
| cancel-queued-run | 1 |
| open | 8 |
| delete | 5 |
| confirm-delete-dialog | 1 |
| undo-delete | 1 |
| bulk-select-delete | 1 |
| accept-suggestion | 1 |
| dismiss-suggestion | 0 |
| download-output | 0 |
| rename-title | 0 (named only by 1 merged duplicate leaf/leaves) |
| change-sort-or-filter | 1 |
| paginate | 1 |
| refresh-or-back | 3 |
| retry-not-in-prd | 5 |
| notification-click | 1 |
| mark-notification-read | 1 |
| copy-run-link | 1 |

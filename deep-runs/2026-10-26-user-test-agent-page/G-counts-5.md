# Stage G counts, bucket 5 (G-bucket-5.yaml)

Surfaces in bucket: history-tab, redirect-transition, notification-email-or-in-app, empty-state.

## Summary

| Measure | Count |
|---|---|
| Leaves in | 182 |
| Rejected | 0 |
| Duplicate clusters | 30 |
| Leaves merged into survivors | 62 |
| Surviving leaves | 120 |
| Survivors with cell values added by normalisation | 83 (139 values added) |
| Uncategorised (`uncategorised: true`) | 0 |

## Rejected

None. Every item has the full schema, is L3/L4 and names a concrete spec object. The banned-vocabulary scan found one hit: "considered" in the `consequence` of realtime-3 ("the cache is considered fresh"). It describes cache behaviour and is not filler, so the item stays.

## Duplicate clusters (survivor <- merged ids)

- realtime-1 <- backend-30, mobile-8, redirect-2, support-1, qa-lead-8  (Spec does not say whether the History entry is written before Submit returns; if the job worker creates it, th)
- dup-12 <- firsttime-14, realtime-35, redirect-3  (Redirect lands before the entry exists on a first-ever use, History shows its empty state and the user resubmi)
- realtime-28 <- redirect-12, cost-14, history-25, qa-lead-27, mobile-11  (Submit succeeds but the client-side redirect fails, leaving the user on the form with no confirmation)
- draft-11 <- mobile-25, support-19  (Browser Back from the History tab returns a filled form, enabling a second submit of the same run)
- prompt-14 <- thread-2, draft-12  (Browser Back from History after submit returns a form that is either still filled (invites re-submit) or empty)
- dup-10 <- backend-45, redirect-11  (Refresh on the History tab after redirect - spec does not say that it cannot re-post the submission)
- realtime-27 <- qa-lead-24  (Refresh right after redirect: if History is in-memory tab state, reload lands on Report mode and any optimisti)
- a11y-8 <- redirect-37  (Redirect to History after Submit gives no announcement that the submit worked or what page the user is now on)
- dup-11 <- qa-lead-11, realtime-6, realtime-7  (Redirect lands on a History page where the new entry is not visible, so the user resubmits)
- history-26 <- redirect-33, redirect-5  (Redirect lands on page 1 of a paginated or sorted list where the new entry is not visible)
- dup-4 <- backend-32, qa-lead-62  (Ordering of two History entries created in the same second is unspecified)
- notify-26 <- history-22, qa-lead-59, realtime-17, redirect-26  (Second browser tab left on History for hours shows a stale list: new entry absent and finished entries still ')
- mobile-35 <- tags-37  (Same phone user with two browser tabs open submits from both, producing near-identical entries with no cross-t)
- support-20 <- history-21, backend-31  (History tab left open for hours - a Running entry never turns Done without a manual refresh)
- history-7 <- mobile-40  (Pagination or infinite scroll for 500+ entries is unspecified (page size, total count, load failure))
- notify-1 <- draft-24, firsttime-18, redirect-23, qa-lead-63  (Run turns Done while the submitter is on the Videos page: the spec names no channel (toast, badge, email) that)
- realtime-24 <- support-21, cost-41  (Long runs (21-100 videos) finish after the user has closed the browser and nothing reaches them)
- realtime-10 <- sre-16  (Job enqueued but history row insert fails, so a run executes with no entry to attach its output to)
- sec-4 <- privacy-9, admin-7  ('History is per user, currently' leaves admin and workspace-owner visibility into other users' History undefin)
- support-32 <- history-40, sre-18  (Support and admin cannot see a user's History - "my report never came" cannot be checked without the user shar)
- support-33 <- history-32  (Colleague asks "where is my teammate's report" - History is per user and there is no share or export)
- privacy-8 <- admin-10, sec-20, consumer-15  (History is per user, so a deactivated member's reports, threads and prompts have no stated owner or fate)
- sharing-16 <- privacy-10, admin-26  (Existing private entries become visible to the team on launch without any notice or opt-out)
- history-18 <- qa-lead-64, support-40  (Retention after a year: are entries kept, archived or purged?)
- history-3 <- prompt-44  (History tab has no stated search or filter, so finding one run among 500 means scrolling)
- popup-31 <- qa-lead-34, mobile-29  (Empty library: the pop-up opens with nothing to select and no pointer to the Videos page)
- firsttime-13 <- qa-lead-58  (History tab empty state before the first submission has no specified copy)
- popup-14 <- tags-16  (Zero results in the pop-up: search or tag combination matching nothing has no specified message or recovery)
- notify-16 <- participant-18  (Email body content undefined: including report text or question answers puts test-participant quotes in person)
- ingest-27 <- draft-35  (First-use empty pop-up while 20 uploads are still ingesting says 'no videos' instead of '20 ingesting')

## Notes on normalisation

- admin-25 had a non-axis key `surface-secondary: empty-state`. It was folded into `surface` as `[history-tab, empty-state]` and the key was removed.
- Values that agents mislabelled are kept as written. Where the situation plainly satisfies another value, that value was added next to the original. Example: history-4 keeps `action: filter-by-tag` and gains `filter-history-by-mode-or-status`. history-7 keeps `action: open-add-video-popup`, and nothing was added because no action value matches opening the History list.
- Survivors keep their own cell plus the values added by normalisation. Cells of merged ids were not combined into the survivor.

## Leaves per perspective (in -> surviving)

| Perspective file | In | Surviving |
|---|---|---|
| E-notification-consumer.yaml | 25 | 25 |
| E-realtime-consistency.yaml | 20 | 16 |
| E-history-power-user.yaml | 14 | 9 |
| E-redirect-skeptic.yaml | 12 | 3 |
| E-qa-lead.yaml | 11 | 1 |
| E-support-agent.yaml | 9 | 5 |
| E-future-sharing-pm.yaml | 8 | 8 |
| E-mobile-user.yaml | 8 | 3 |
| E-accessibility-reviewer.yaml | 7 | 7 |
| E-interrupted-composer.yaml | 7 | 4 |
| E-cost-analyst.yaml | 6 | 4 |
| E-double-submitter.yaml | 6 | 6 |
| E-retention-and-deletion.yaml | 6 | 4 |
| E-workspace-admin.yaml | 6 | 3 |
| E-agent-backend-engineer.yaml | 4 | 0 |
| E-first-time-user.yaml | 4 | 2 |
| E-question-asker.yaml | 4 | 3 |
| E-sre-on-call.yaml | 4 | 2 |
| E-low-vision-perception.yaml | 3 | 3 |
| E-security-reviewer.yaml | 3 | 2 |
| E-test-participant-data-subject.yaml | 3 | 2 |
| E-localisation-vendor.yaml | 2 | 2 |
| E-other-video-uploader.yaml | 2 | 2 |
| E-popup-interaction-designer.yaml | 2 | 2 |
| E-prompt-writer.yaml | 2 | 1 |
| E-tag-librarian.yaml | 2 | 0 |
| E-ingestion-engineer.yaml | 1 | 1 |
| E-report-consumer.yaml | 1 | 0 |

## Surviving leaves per axis value

A leaf counts under every value its normalised cell names. Values with 0 leaves are listed.

### surface (leaves naming this axis: 120)

| Value | Leaves |
|---|---|
| videos-page | 0 |
| agent-page-mode-switch | 0 |
| report-form | 1 |
| ask-question-form | 0 |
| add-video-popup | 6 |
| tag-filter | 0 |
| search-box | 1 |
| selected-videos-list | 0 |
| suggested-questions | 0 |
| run-name-field | 0 |
| prompt-field | 0 |
| question-field | 0 |
| submit-button | 0 |
| redirect-transition | 29 |
| history-tab | 70 |
| history-entry-row | 0 |
| history-entry-detail | 1 |
| follow-up-thread | 3 |
| empty-state | 13 |
| error-toast-or-banner | 0 |
| notification-email-or-in-app | 26 |
| global-running-indicator-or-badge | 1 |
| history-entry-status-badge | 0 |
| popup-footer-confirm-cancel | 0 |
| popup-selection-count | 0 |
| popup-zero-results | 1 |
| video-thumbnail-overlay | 0 |
| cited-video-timestamp-player | 0 |
| export-or-copy-output | 0 |
| history-filter-or-sort-controls | 2 |
| mode-tab-on-history-entry | 0 |
| quota-or-limit-message | 1 |
| onboarding-or-help-for-suggested-questions | 0 |

### actor (leaves naming this axis: 47)

| Value | Leaves |
|---|---|
| creator-owner | 12 |
| same-user-second-tab | 3 |
| other-user-same-workspace | 7 |
| admin | 3 |
| background-agent-job | 4 |
| ingestion-job | 0 |
| video-uploader-other-than-runner | 2 |
| workspace-owner | 6 |
| viewer-role-member | 3 |
| removed-or-deactivated-user | 3 |
| support-staff-impersonating | 1 |
| test-participant-data-subject | 5 |
| report-recipient-without-access | 1 |

### videos-selected (leaves naming this axis: 10)

| Value | Leaves |
|---|---|
| 0 | 0 |
| 1 | 0 |
| 2-5 | 4 |
| 6-20 | 3 |
| 21-100 | 3 |
| all-videos-in-library | 0 |
| more-than-popup-shows-at-once | 0 |
| exceeds-limit-once-defined | 0 |
| selection-with-duplicate-uploads-of-same-session | 0 |
| selection-where-all-become-unusable-before-run | 0 |

### video-state (leaves naming this axis: 8)

| Value | Leaves |
|---|---|
| ingested | 0 |
| still-ingesting | 1 |
| ingestion-failed | 0 |
| deleted-after-selection-before-run | 0 |
| deleted-after-run | 3 |
| re-uploaded-same-name | 0 |
| silent-or-no-transcript | 2 |
| 3-hour-long | 1 |
| 3-second-clip | 0 |
| untagged | 0 |
| non-english-audio | 0 |
| ingestion-queued-not-started | 0 |
| re-ingesting-after-edit | 0 |
| ingested-with-partial-transcript | 0 |
| multi-language-audio | 0 |
| duplicate-name-different-content | 0 |
| very-large-file | 0 |
| owned-by-another-user | 1 |
| access-revoked | 0 |
| moved-to-hidden-folder | 0 |
| ingested-but-thumbnail-missing | 0 |

### library-state (leaves naming this axis: 9)

| Value | Leaves |
|---|---|
| empty-library | 6 |
| 1-video | 0 |
| 50-videos | 1 |
| 2000-videos | 0 |
| all-untagged | 0 |
| 200-tags | 1 |
| tag-renamed-or-deleted-after-filtering | 0 |
| all-videos-still-ingesting | 2 |
| mixed-ownership-library | 1 |
| library-changing-while-popup-open | 0 |
| videos-in-folders-or-projects | 0 |
| library-at-plan-max | 0 |

### mode (leaves naming this axis: 27)

| Value | Leaves |
|---|---|
| report | 21 |
| ask-question | 7 |
| switching-mode-after-selecting-videos | 0 |

### text-input-state (leaves naming this axis: 9)

| Value | Leaves |
|---|---|
| run-name-empty | 1 |
| run-name-duplicate-of-existing | 1 |
| run-name-200-chars | 0 |
| prompt-empty | 0 |
| prompt-5000-chars | 4 |
| prompt-contradicts-report-mode | 0 |
| question-empty | 0 |
| question-picked-from-suggested | 0 |
| question-unrelated-to-videos | 0 |
| non-english-text | 2 |
| text-contains-instructions-to-ignore-rules | 0 |
| text-contains-html-or-markdown | 0 |
| whitespace-only | 0 |
| emoji-or-rtl | 0 |
| newline-pasted-into-run-name | 0 |
| suggested-question-edited-after-pick | 0 |
| question-exceeds-limit | 0 |
| text-contains-participant-personal-data | 1 |

### run-status (leaves naming this axis: 69)

| Value | Leaves |
|---|---|
| submitted-not-yet-visible-in-history | 17 |
| queued | 6 |
| running | 12 |
| done | 22 |
| failed | 6 |
| partial-some-videos-unusable | 1 |
| cancelled-not-in-spec | 0 |
| stuck-over-1h | 1 |
| done-with-empty-output | 1 |
| submit-accepted-but-entry-never-created | 4 |
| failed-before-start-validation | 1 |
| retrying | 1 |
| timed-out | 1 |
| rate-limited-waiting | 1 |
| done-but-unread | 1 |
| done-then-source-video-changed-stale | 0 |
| deleted-entry | 2 |
| superseded-by-re-run | 0 |

### thread-state (leaves naming this axis: 4)

| Value | Leaves |
|---|---|
| first-question | 0 |
| follow-up-1 | 2 |
| follow-up-10 | 1 |
| follow-up-while-first-still-running | 1 |
| follow-up-after-video-deleted | 0 |
| follow-up-with-changed-video-set | 0 |
| thread-opened-from-history | 0 |
| thread-where-an-answer-failed | 0 |
| follow-up-limit-reached | 0 |
| follow-up-after-agent-version-change | 0 |
| follow-up-from-second-tab-simultaneously | 0 |
| wanting-to-ask-about-a-report-entry | 0 |

### history-state (leaves naming this axis: 56)

| Value | Leaves |
|---|---|
| empty | 8 |
| 1-entry | 5 |
| 100-entries | 14 |
| 1000-entries | 14 |
| report-and-question-entries-interleaved | 4 |
| entry-referencing-deleted-video | 2 |
| two-entries-same-second | 3 |
| entries-with-blank-run-name | 2 |
| mix-of-done-and-failed-across-recent-runs | 1 |
| filtered-so-new-entry-hidden | 1 |
| scrolled-to-page-3-at-redirect | 1 |
| sorted-not-by-newest | 1 |
| several-running-at-once | 7 |
| entries-from-older-agent-version | 0 |
| filtered-to-zero | 0 |

### time-and-connection (leaves naming this axis: 62)

| Value | Leaves |
|---|---|
| first-ever-use | 11 |
| steady-state | 10 |
| offline-at-submit | 2 |
| submit-succeeds-redirect-fails | 4 |
| redirect-lands-before-entry-exists | 11 |
| session-expired-at-submit | 3 |
| page-open-for-hours | 10 |
| during-agent-outage | 5 |
| after-a-year | 6 |
| deploy-during-run | 2 |
| two-devices-same-user | 4 |
| timezone-of-entry-timestamp | 0 |
| session-expired-while-composing-long-prompt | 0 |
| rate-limit-at-submit | 1 |
| agent-model-version-changed-since-entry | 0 |

### action (leaves naming this axis: 77)

| Value | Leaves |
|---|---|
| open-agent-page | 6 |
| switch-mode | 0 |
| open-add-video-popup | 6 |
| filter-by-tag | 1 |
| search | 4 |
| select-video | 0 |
| deselect-video | 0 |
| close-popup-without-confirm | 0 |
| type-run-name | 0 |
| type-prompt | 0 |
| pick-suggested-question | 0 |
| type-question | 0 |
| submit | 29 |
| double-submit | 5 |
| back-button-after-redirect | 3 |
| refresh-after-redirect | 4 |
| open-history-entry | 10 |
| re-run-not-in-spec | 1 |
| delete-entry-not-in-spec | 2 |
| rename-entry-not-in-spec | 0 |
| ask-follow-up | 5 |
| cancel-run-not-in-spec | 0 |
| share-or-export-not-in-spec | 3 |
| retry-failed-videos-only | 0 |
| retry-whole-run | 1 |
| clear-all-selection | 0 |
| select-all-filtered | 0 |
| navigate-away-mid-compose | 1 |
| return-to-draft | 0 |
| edit-and-resubmit-from-entry | 0 |
| filter-history-by-mode-or-status | 1 |
| search-history | 2 |
| copy-output | 0 |
| open-cited-timestamp | 0 |
| mark-read | 2 |
| logout-while-running | 2 |
| follow-up-from-two-tabs | 0 |

### media-appearance (leaves naming this axis: 0)

| Value | Leaves |
|---|---|
| thumbnail-near-white | 0 |
| thumbnail-near-black | 0 |
| thumbnail-busy-or-high-detail | 0 |
| no-thumbnail-yet | 0 |
| generic-placeholder-thumbnail | 0 |
| identical-thumbnails-across-videos | 0 |
| thumbnail-with-burned-in-text | 0 |
| portrait-or-odd-aspect-ratio | 0 |

### per-video-outcome-within-run (leaves naming this axis: 3)

| Value | Leaves |
|---|---|
| all-videos-used | 0 |
| one-video-unusable | 0 |
| some-videos-unusable | 1 |
| all-videos-unusable | 2 |
| video-truncated-to-fit-context | 0 |
| video-skipped-because-deleted | 0 |
| video-replaced-mid-run | 0 |

### entry-point-and-lifecycle-phase (leaves naming this axis: 14)

| Value | Leaves |
|---|---|
| before-first-ingestion-completes | 1 |
| arriving-from-nav | 1 |
| arriving-from-videos-page-with-preselection | 0 |
| deep-link-to-mode | 0 |
| returning-mid-compose | 0 |
| post-submit-same-screen | 2 |
| post-submit-elsewhere-in-app | 2 |
| app-closed-while-running | 4 |
| after-done-consuming-output | 2 |
| long-after-retention-window | 2 |

### observer-location-at-status-change (leaves naming this axis: 22)

| Value | Leaves |
|---|---|
| on-history-tab-top | 4 |
| on-history-tab-scrolled-or-filtered | 2 |
| inside-entry-detail | 0 |
| on-agent-form-composing-next-run | 2 |
| other-page-in-app | 4 |
| other-tab | 1 |
| other-device | 3 |
| logged-out | 6 |

### permission-and-plan (leaves naming this axis: 14)

| Value | Leaves |
|---|---|
| full-access | 5 |
| viewer-role | 3 |
| trial-or-plan-without-agent | 1 |
| quota-remaining | 2 |
| quota-exhausted-at-submit | 1 |
| access-revoked-mid-run | 2 |
| member-removed-from-workspace | 2 |
| video-owned-by-other-user | 0 |
| video-in-folder-user-cannot-see | 0 |

### popup-session-state (leaves naming this axis: 4)

| Value | Leaves |
|---|---|
| first-open | 3 |
| reopen-with-prior-selection | 0 |
| closed-without-confirm | 0 |
| selection-hidden-by-filter | 0 |
| filter-yields-zero | 1 |
| library-changed-while-open | 0 |
| at-max-selection | 0 |
| select-all-filtered | 0 |

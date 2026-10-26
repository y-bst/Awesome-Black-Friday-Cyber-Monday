# Stage G counts, bucket 1

Bucket: G-bucket-1.yaml (surfaces history-entry-detail, cited-video-timestamp-player, export-or-copy-output)

- Leaves in: 198
- Rejected: 0
- Duplicate clusters: 29 (leaves merged into survivors: 49)
- Surviving leaves: 149
- Leaves with cell values added by normalisation: 108 (204 values added)
- Uncategorised leaves: 0

## Rejected

None. All 198 items are L3/L4, name a concrete spec object, contain no banned vocabulary (scan of title, object, situation, consequence, evidence, proposed for improve / ensure / consider / robust / handle / proper / appropriate / various / etc. / such as / and so on / best practices / edge case(s) / user-friendly / seamless returned 0 hits), and follow the leaf schema. Notes, not rejections: `redirect-30` has no `proposed` (optional field); `admin-22` carried a non-axis cell key `actor-secondary: workspace-owner` (leaf merged into `participant-4`, so the key does not appear in the output).

## Duplicate clusters (survivor <- merged ids)

- thread-8 <- history-15, qa-lead-46, support-28, redirect-30
- qa-lead-15 <- firsttime-38, support-7
- ingest-40 <- uploader-28
- backend-4 <- ingest-16, output-26, support-8, qa-lead-17, qa-lead-18
- consumer-12 <- output-15
- output-1 <- support-22, qa-lead-16
- history-12 <- ingest-6, qa-lead-60, support-13
- participant-1 <- privacy-1
- participant-4 <- uploader-30, sec-14, admin-22
- sharing-37 <- admin-12
- backend-26 <- history-28, ingest-10, output-21, privacy-35
- uploader-12 <- consumer-14
- support-6 <- draft-15, thread-31
- history-33 <- prompt-43
- history-37 <- qa-lead-21
- consumer-2 <- thread-23
- privacy-29 <- admin-24, consumer-37, participant-25
- consumer-39 <- sre-14
- prompt-15 <- firsttime-26, consumer-18
- notify-43 <- realtime-20
- a11y-38 <- prompt-26
- privacy-11 <- participant-17
- privacy-14 <- output-19
- notify-14 <- consumer-10
- sec-13 <- privacy-13
- sec-27 <- output-16
- thread-20 <- backend-35
- draft-40 <- notify-18
- l10n-3 <- consumer-30

## Surviving leaves per perspective (in -> out)

| perspective | in | out |
|---|---|---|
| a11y | 8 | 8 |
| admin | 4 | 1 |
| backend | 8 | 7 |
| consumer | 22 | 17 |
| cost | 7 | 7 |
| draft | 3 | 2 |
| dup | 1 | 1 |
| firsttime | 5 | 3 |
| history | 8 | 6 |
| ingest | 8 | 5 |
| l10n | 7 | 7 |
| lowvision | 3 | 3 |
| mobile | 2 | 2 |
| notify | 4 | 3 |
| output | 20 | 15 |
| participant | 12 | 10 |
| privacy | 7 | 4 |
| prompt | 6 | 4 |
| qa-lead | 12 | 6 |
| realtime | 5 | 4 |
| redirect | 2 | 1 |
| sec | 11 | 10 |
| sharing | 8 | 8 |
| sre | 4 | 3 |
| support | 7 | 2 |
| tags | 1 | 1 |
| thread | 5 | 3 |
| uploader | 8 | 6 |

## Surviving leaves per axis value (normalised cells; a leaf counts under every value its cell names)

### surface

| value | leaves |
|---|---|
| videos-page | 0 |
| agent-page-mode-switch | 0 |
| report-form | 0 |
| ask-question-form | 0 |
| add-video-popup | 0 |
| tag-filter | 0 |
| search-box | 0 |
| selected-videos-list | 0 |
| suggested-questions | 1 |
| run-name-field | 0 |
| prompt-field | 0 |
| question-field | 0 |
| submit-button | 0 |
| redirect-transition | 1 |
| history-tab | 1 |
| history-entry-row | 3 |
| history-entry-detail | 121 |
| follow-up-thread | 2 |
| empty-state | 0 |
| error-toast-or-banner | 0 |
| notification-email-or-in-app | 1 |
| global-running-indicator-or-badge | 0 |
| history-entry-status-badge | 0 |
| popup-footer-confirm-cancel | 0 |
| popup-selection-count | 0 |
| popup-zero-results | 0 |
| video-thumbnail-overlay | 0 |
| cited-video-timestamp-player | 11 |
| export-or-copy-output | 17 |
| history-filter-or-sort-controls | 0 |
| mode-tab-on-history-entry | 0 |
| quota-or-limit-message | 0 |
| onboarding-or-help-for-suggested-questions | 0 |

Zero-leaf values (24): videos-page, agent-page-mode-switch, report-form, ask-question-form, add-video-popup, tag-filter, search-box, selected-videos-list, run-name-field, prompt-field, question-field, submit-button, empty-state, error-toast-or-banner, global-running-indicator-or-badge, history-entry-status-badge, popup-footer-confirm-cancel, popup-selection-count, popup-zero-results, video-thumbnail-overlay, history-filter-or-sort-controls, mode-tab-on-history-entry, quota-or-limit-message, onboarding-or-help-for-suggested-questions

### actor

| value | leaves |
|---|---|
| creator-owner | 1 |
| same-user-second-tab | 2 |
| other-user-same-workspace | 12 |
| admin | 3 |
| background-agent-job | 4 |
| ingestion-job | 0 |
| video-uploader-other-than-runner | 11 |
| workspace-owner | 1 |
| viewer-role-member | 1 |
| removed-or-deactivated-user | 1 |
| support-staff-impersonating | 3 |
| test-participant-data-subject | 13 |
| report-recipient-without-access | 10 |

Zero-leaf values (1): ingestion-job

### videos-selected

| value | leaves |
|---|---|
| 0 | 0 |
| 1 | 4 |
| 2-5 | 15 |
| 6-20 | 37 |
| 21-100 | 5 |
| all-videos-in-library | 1 |
| more-than-popup-shows-at-once | 0 |
| exceeds-limit-once-defined | 0 |
| selection-with-duplicate-uploads-of-same-session | 0 |
| selection-where-all-become-unusable-before-run | 1 |

Zero-leaf values (4): 0, more-than-popup-shows-at-once, exceeds-limit-once-defined, selection-with-duplicate-uploads-of-same-session

### video-state

| value | leaves |
|---|---|
| ingested | 6 |
| still-ingesting | 1 |
| ingestion-failed | 2 |
| deleted-after-selection-before-run | 1 |
| deleted-after-run | 16 |
| re-uploaded-same-name | 3 |
| silent-or-no-transcript | 10 |
| 3-hour-long | 4 |
| 3-second-clip | 3 |
| untagged | 0 |
| non-english-audio | 6 |
| ingestion-queued-not-started | 0 |
| re-ingesting-after-edit | 4 |
| ingested-with-partial-transcript | 1 |
| multi-language-audio | 2 |
| duplicate-name-different-content | 1 |
| very-large-file | 0 |
| owned-by-another-user | 4 |
| access-revoked | 2 |
| moved-to-hidden-folder | 1 |
| ingested-but-thumbnail-missing | 0 |

Zero-leaf values (4): untagged, ingestion-queued-not-started, very-large-file, ingested-but-thumbnail-missing

### library-state

| value | leaves |
|---|---|
| empty-library | 0 |
| 1-video | 0 |
| 50-videos | 2 |
| 2000-videos | 1 |
| all-untagged | 0 |
| 200-tags | 0 |
| tag-renamed-or-deleted-after-filtering | 1 |
| all-videos-still-ingesting | 0 |
| mixed-ownership-library | 3 |
| library-changing-while-popup-open | 0 |
| videos-in-folders-or-projects | 0 |
| library-at-plan-max | 0 |

Zero-leaf values (8): empty-library, 1-video, all-untagged, 200-tags, all-videos-still-ingesting, library-changing-while-popup-open, videos-in-folders-or-projects, library-at-plan-max

### mode

| value | leaves |
|---|---|
| report | 100 |
| ask-question | 14 |
| switching-mode-after-selecting-videos | 0 |

Zero-leaf values (1): switching-mode-after-selecting-videos

### text-input-state

| value | leaves |
|---|---|
| run-name-empty | 1 |
| run-name-duplicate-of-existing | 1 |
| run-name-200-chars | 0 |
| prompt-empty | 2 |
| prompt-5000-chars | 2 |
| prompt-contradicts-report-mode | 1 |
| question-empty | 0 |
| question-picked-from-suggested | 1 |
| question-unrelated-to-videos | 1 |
| non-english-text | 4 |
| text-contains-instructions-to-ignore-rules | 0 |
| text-contains-html-or-markdown | 3 |
| whitespace-only | 0 |
| emoji-or-rtl | 0 |
| newline-pasted-into-run-name | 0 |
| suggested-question-edited-after-pick | 1 |
| question-exceeds-limit | 0 |
| text-contains-participant-personal-data | 5 |

Zero-leaf values (7): run-name-200-chars, question-empty, text-contains-instructions-to-ignore-rules, whitespace-only, emoji-or-rtl, newline-pasted-into-run-name, question-exceeds-limit

### run-status

| value | leaves |
|---|---|
| submitted-not-yet-visible-in-history | 0 |
| queued | 3 |
| running | 8 |
| done | 33 |
| failed | 13 |
| partial-some-videos-unusable | 10 |
| cancelled-not-in-spec | 1 |
| stuck-over-1h | 1 |
| done-with-empty-output | 7 |
| submit-accepted-but-entry-never-created | 0 |
| failed-before-start-validation | 0 |
| retrying | 1 |
| timed-out | 0 |
| rate-limited-waiting | 0 |
| done-but-unread | 0 |
| done-then-source-video-changed-stale | 7 |
| deleted-entry | 2 |
| superseded-by-re-run | 3 |

Zero-leaf values (6): submitted-not-yet-visible-in-history, submit-accepted-but-entry-never-created, failed-before-start-validation, timed-out, rate-limited-waiting, done-but-unread

### thread-state

| value | leaves |
|---|---|
| first-question | 3 |
| follow-up-1 | 0 |
| follow-up-10 | 0 |
| follow-up-while-first-still-running | 1 |
| follow-up-after-video-deleted | 0 |
| follow-up-with-changed-video-set | 0 |
| thread-opened-from-history | 6 |
| thread-where-an-answer-failed | 1 |
| follow-up-limit-reached | 0 |
| follow-up-after-agent-version-change | 0 |
| follow-up-from-second-tab-simultaneously | 0 |
| wanting-to-ask-about-a-report-entry | 5 |

Zero-leaf values (7): follow-up-1, follow-up-10, follow-up-after-video-deleted, follow-up-with-changed-video-set, follow-up-limit-reached, follow-up-after-agent-version-change, follow-up-from-second-tab-simultaneously

### history-state

| value | leaves |
|---|---|
| empty | 0 |
| 1-entry | 4 |
| 100-entries | 3 |
| 1000-entries | 6 |
| report-and-question-entries-interleaved | 1 |
| entry-referencing-deleted-video | 9 |
| two-entries-same-second | 0 |
| entries-with-blank-run-name | 1 |
| mix-of-done-and-failed-across-recent-runs | 1 |
| filtered-so-new-entry-hidden | 0 |
| scrolled-to-page-3-at-redirect | 0 |
| sorted-not-by-newest | 0 |
| several-running-at-once | 0 |
| entries-from-older-agent-version | 3 |
| filtered-to-zero | 0 |

Zero-leaf values (7): empty, two-entries-same-second, filtered-so-new-entry-hidden, scrolled-to-page-3-at-redirect, sorted-not-by-newest, several-running-at-once, filtered-to-zero

### time-and-connection

| value | leaves |
|---|---|
| first-ever-use | 1 |
| steady-state | 0 |
| offline-at-submit | 0 |
| submit-succeeds-redirect-fails | 0 |
| redirect-lands-before-entry-exists | 0 |
| session-expired-at-submit | 0 |
| page-open-for-hours | 1 |
| during-agent-outage | 2 |
| after-a-year | 5 |
| deploy-during-run | 1 |
| two-devices-same-user | 1 |
| timezone-of-entry-timestamp | 1 |
| session-expired-while-composing-long-prompt | 0 |
| rate-limit-at-submit | 0 |
| agent-model-version-changed-since-entry | 3 |

Zero-leaf values (7): steady-state, offline-at-submit, submit-succeeds-redirect-fails, redirect-lands-before-entry-exists, session-expired-at-submit, session-expired-while-composing-long-prompt, rate-limit-at-submit

### action

| value | leaves |
|---|---|
| open-agent-page | 0 |
| switch-mode | 0 |
| open-add-video-popup | 0 |
| filter-by-tag | 0 |
| search | 0 |
| select-video | 0 |
| deselect-video | 0 |
| close-popup-without-confirm | 0 |
| type-run-name | 0 |
| type-prompt | 0 |
| pick-suggested-question | 1 |
| type-question | 4 |
| submit | 7 |
| double-submit | 0 |
| back-button-after-redirect | 1 |
| refresh-after-redirect | 1 |
| open-history-entry | 44 |
| re-run-not-in-spec | 9 |
| delete-entry-not-in-spec | 2 |
| rename-entry-not-in-spec | 0 |
| ask-follow-up | 5 |
| cancel-run-not-in-spec | 2 |
| share-or-export-not-in-spec | 12 |
| retry-failed-videos-only | 2 |
| retry-whole-run | 3 |
| clear-all-selection | 0 |
| select-all-filtered | 0 |
| navigate-away-mid-compose | 0 |
| return-to-draft | 0 |
| edit-and-resubmit-from-entry | 1 |
| filter-history-by-mode-or-status | 0 |
| search-history | 0 |
| copy-output | 12 |
| open-cited-timestamp | 9 |
| mark-read | 0 |
| logout-while-running | 0 |
| follow-up-from-two-tabs | 0 |

Zero-leaf values (21): open-agent-page, switch-mode, open-add-video-popup, filter-by-tag, search, select-video, deselect-video, close-popup-without-confirm, type-run-name, type-prompt, double-submit, rename-entry-not-in-spec, clear-all-selection, select-all-filtered, navigate-away-mid-compose, return-to-draft, filter-history-by-mode-or-status, search-history, mark-read, logout-while-running, follow-up-from-two-tabs

### media-appearance

| value | leaves |
|---|---|
| thumbnail-near-white | 0 |
| thumbnail-near-black | 0 |
| thumbnail-busy-or-high-detail | 0 |
| no-thumbnail-yet | 0 |
| generic-placeholder-thumbnail | 1 |
| identical-thumbnails-across-videos | 0 |
| thumbnail-with-burned-in-text | 0 |
| portrait-or-odd-aspect-ratio | 0 |

Zero-leaf values (7): thumbnail-near-white, thumbnail-near-black, thumbnail-busy-or-high-detail, no-thumbnail-yet, identical-thumbnails-across-videos, thumbnail-with-burned-in-text, portrait-or-odd-aspect-ratio

### per-video-outcome-within-run

| value | leaves |
|---|---|
| all-videos-used | 2 |
| one-video-unusable | 2 |
| some-videos-unusable | 10 |
| all-videos-unusable | 3 |
| video-truncated-to-fit-context | 2 |
| video-skipped-because-deleted | 0 |
| video-replaced-mid-run | 1 |

Zero-leaf values (1): video-skipped-because-deleted

### entry-point-and-lifecycle-phase

| value | leaves |
|---|---|
| before-first-ingestion-completes | 0 |
| arriving-from-nav | 0 |
| arriving-from-videos-page-with-preselection | 0 |
| deep-link-to-mode | 1 |
| returning-mid-compose | 0 |
| post-submit-same-screen | 0 |
| post-submit-elsewhere-in-app | 0 |
| app-closed-while-running | 0 |
| after-done-consuming-output | 2 |
| long-after-retention-window | 2 |

Zero-leaf values (7): before-first-ingestion-completes, arriving-from-nav, arriving-from-videos-page-with-preselection, returning-mid-compose, post-submit-same-screen, post-submit-elsewhere-in-app, app-closed-while-running

### observer-location-at-status-change

| value | leaves |
|---|---|
| on-history-tab-top | 0 |
| on-history-tab-scrolled-or-filtered | 0 |
| inside-entry-detail | 4 |
| on-agent-form-composing-next-run | 0 |
| other-page-in-app | 0 |
| other-tab | 3 |
| other-device | 1 |
| logged-out | 0 |

Zero-leaf values (5): on-history-tab-top, on-history-tab-scrolled-or-filtered, on-agent-form-composing-next-run, other-page-in-app, logged-out

### permission-and-plan

| value | leaves |
|---|---|
| full-access | 2 |
| viewer-role | 4 |
| trial-or-plan-without-agent | 0 |
| quota-remaining | 1 |
| quota-exhausted-at-submit | 0 |
| access-revoked-mid-run | 1 |
| member-removed-from-workspace | 1 |
| video-owned-by-other-user | 2 |
| video-in-folder-user-cannot-see | 3 |

Zero-leaf values (2): trial-or-plan-without-agent, quota-exhausted-at-submit

### popup-session-state

| value | leaves |
|---|---|
| first-open | 0 |
| reopen-with-prior-selection | 0 |
| closed-without-confirm | 0 |
| selection-hidden-by-filter | 0 |
| filter-yields-zero | 0 |
| library-changed-while-open | 0 |
| at-max-selection | 0 |
| select-all-filtered | 0 |

Zero-leaf values (8): first-open, reopen-with-prior-selection, closed-without-confirm, selection-hidden-by-filter, filter-yields-zero, library-changed-while-open, at-max-selection, select-all-filtered


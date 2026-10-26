# Stage G counts, bucket 4

Surfaces: follow-up-thread, question-field, suggested-questions, ask-question-form

- Leaves in: 156
- Rejected: 0. No item broke a rule. All 156 are L3/L4, each names a spec object (a quoted spec sentence or a named element), there is no banned vocabulary (regex scan of all string fields: 0 hits), and every item uses the leaf schema.
- Duplicate clusters: 22 clusters, 46 leaves merged into survivors
- Surviving leaves: 110
- Leaves with cell values added by normalisation: 92. `mode: ask-question` was added wherever it was missing, because follow-ups and suggested questions exist only in Ask question mode. Other values were added only where the situation states them: video counts mapped to `videos-selected` buckets, follow-up sends to `ask-follow-up`, and similar.
- Uncategorised leaves: 0

## Duplicate clusters (survivor <- merged ids)

| survivor | merged | situation |
|---|---|---|
| prompt-34 | firsttime-9, qa-lead-40 | picking a suggested question: fills the field or submits at once |
| a11y-17 | prompt-35 | picking a suggestion when the field already holds typed text |
| prompt-37 | qa-lead-41, draft-22 | derived suggestion is picked, then the video selection changes and the question goes stale |
| backend-38 | cost-25 | a derived suggestion triggers a model call on every selection change |
| qa-lead-2 | firsttime-7 | suggested-questions area with 0 videos selected |
| output-24 | consumer-23 | suggestion edited after pick; the entry shows the original text |
| prompt-38 | output-6 | question unrelated to the selected videos |
| output-34 | prompt-33 | whitespace-only or emoji-only question is accepted |
| support-45 | ingest-23 | question language differs from the audio language |
| l10n-20 | prompt-31, thread-19 | follow-up in a different language from the first question |
| backend-17 | qa-lead-42, thread-3, support-24, mobile-18, redirect-28, cost-23 | follow-up sent while the first answer is still Running |
| ingest-8 | backend-18, cost-38, privacy-2, qa-lead-45, sec-15, support-25, thread-11, output-12 | follow-up after one of the thread's videos was deleted |
| thread-12 | draft-37 | video re-uploaded under the same name; which file a follow-up reads |
| sre-13 | backend-14, output-29, consumer-28, cost-39 | model/agent version changes between the first answer and a follow-up |
| dup-14 | thread-9, realtime-32, cost-22 | same user sends follow-ups from 2 tabs at once |
| backend-13 | support-27 | follow-up 10 on a large video set goes over the context limit |
| sec-17 | cost-5, thread-6 | no cap on follow-ups per thread |
| backend-16 | cost-4 | what a follow-up reads: the transcripts again, or only the prior answer |
| output-13 | thread-7, sre-34 | a follow-up answer fails: how the failed turn shows and whether it stays in context |
| qa-lead-43 | redirect-27 | submitting a follow-up: redirect to History or stay in the thread |
| thread-1 | firsttime-25 | where the follow-up input lives (entry detail or the Agent page) |
| thread-4 | support-26, firsttime-27, tags-30 | changing the video set in the middle of a thread |

Kept separate on purpose: these are different gaps on a similar situation.

- a11y-16: element semantics and focus of the suggestion chips.
- dup-17: double-pick creates duplicate entries.
- mobile-22 and l10n-38: chip layout at 360px.
- a11y-21, lowvision-33, dup-15, thread-13 and thread-28: variants of the follow-up-while-running situation.
- uploader-4: a different actor deleted the video.
- participant-15: answer given after the participant's erasure.
- admin-37: access revoked.
- thread-43: video deleted while the run was queued.
- sec-40: missing ownership check on the thread id.
- sharing-4: two different users.
- sharing-31: another user, version change.
- backend-15: prompt drift, not model drift.
- output-25 and support-46: silent video vs 3-second clips.
- notify-19 and realtime-31: signal elsewhere in the app vs unread marker on the History row.

## Surviving leaves per axis value (normalised cells; a leaf counts under every value its cell names)

### surface

| value | leaves |
|---|---|
| videos-page | 0 |
| agent-page-mode-switch | 1 |
| report-form | 1 |
| ask-question-form | 3 |
| add-video-popup | 2 |
| tag-filter | 0 |
| search-box | 0 |
| selected-videos-list | 0 |
| suggested-questions | 26 |
| run-name-field | 0 |
| prompt-field | 0 |
| question-field | 23 |
| submit-button | 3 |
| redirect-transition | 2 |
| history-tab | 0 |
| history-entry-row | 1 |
| history-entry-detail | 4 |
| follow-up-thread | 69 |
| empty-state | 0 |
| error-toast-or-banner | 0 |
| notification-email-or-in-app | 0 |
| global-running-indicator-or-badge | 0 |
| history-entry-status-badge | 0 |
| popup-footer-confirm-cancel | 0 |
| popup-selection-count | 0 |
| popup-zero-results | 0 |
| video-thumbnail-overlay | 0 |
| cited-video-timestamp-player | 0 |
| export-or-copy-output | 1 |
| history-filter-or-sort-controls | 0 |
| mode-tab-on-history-entry | 0 |
| quota-or-limit-message | 0 |
| onboarding-or-help-for-suggested-questions | 0 |

### actor

| value | leaves |
|---|---|
| creator-owner | 4 |
| same-user-second-tab | 3 |
| other-user-same-workspace | 6 |
| admin | 1 |
| background-agent-job | 3 |
| ingestion-job | 1 |
| video-uploader-other-than-runner | 2 |
| workspace-owner | 0 |
| viewer-role-member | 0 |
| removed-or-deactivated-user | 0 |
| support-staff-impersonating | 0 |
| test-participant-data-subject | 2 |
| report-recipient-without-access | 0 |

### videos-selected

| value | leaves |
|---|---|
| 0 | 1 |
| 1 | 7 |
| 2-5 | 17 |
| 6-20 | 5 |
| 21-100 | 1 |
| all-videos-in-library | 1 |
| more-than-popup-shows-at-once | 0 |
| exceeds-limit-once-defined | 0 |
| selection-with-duplicate-uploads-of-same-session | 0 |
| selection-where-all-become-unusable-before-run | 0 |

### video-state

| value | leaves |
|---|---|
| ingested | 2 |
| still-ingesting | 0 |
| ingestion-failed | 1 |
| deleted-after-selection-before-run | 2 |
| deleted-after-run | 4 |
| re-uploaded-same-name | 1 |
| silent-or-no-transcript | 4 |
| 3-hour-long | 4 |
| 3-second-clip | 1 |
| untagged | 0 |
| non-english-audio | 3 |
| ingestion-queued-not-started | 0 |
| re-ingesting-after-edit | 1 |
| ingested-with-partial-transcript | 0 |
| multi-language-audio | 1 |
| duplicate-name-different-content | 0 |
| very-large-file | 0 |
| owned-by-another-user | 0 |
| access-revoked | 1 |
| moved-to-hidden-folder | 0 |
| ingested-but-thumbnail-missing | 0 |

### library-state

| value | leaves |
|---|---|
| empty-library | 0 |
| 1-video | 0 |
| 50-videos | 0 |
| 2000-videos | 1 |
| all-untagged | 0 |
| 200-tags | 0 |
| tag-renamed-or-deleted-after-filtering | 0 |
| all-videos-still-ingesting | 0 |
| mixed-ownership-library | 0 |
| library-changing-while-popup-open | 0 |
| videos-in-folders-or-projects | 0 |
| library-at-plan-max | 0 |

### mode

| value | leaves |
|---|---|
| report | 3 |
| ask-question | 110 |
| switching-mode-after-selecting-videos | 1 |

### text-input-state

| value | leaves |
|---|---|
| run-name-empty | 0 |
| run-name-duplicate-of-existing | 0 |
| run-name-200-chars | 0 |
| prompt-empty | 0 |
| prompt-5000-chars | 0 |
| prompt-contradicts-report-mode | 1 |
| question-empty | 2 |
| question-picked-from-suggested | 15 |
| question-unrelated-to-videos | 4 |
| non-english-text | 4 |
| text-contains-instructions-to-ignore-rules | 5 |
| text-contains-html-or-markdown | 1 |
| whitespace-only | 1 |
| emoji-or-rtl | 2 |
| newline-pasted-into-run-name | 0 |
| suggested-question-edited-after-pick | 3 |
| question-exceeds-limit | 2 |
| text-contains-participant-personal-data | 3 |

### run-status

| value | leaves |
|---|---|
| submitted-not-yet-visible-in-history | 2 |
| queued | 1 |
| running | 10 |
| done | 7 |
| failed | 5 |
| partial-some-videos-unusable | 1 |
| cancelled-not-in-spec | 1 |
| stuck-over-1h | 1 |
| done-with-empty-output | 2 |
| submit-accepted-but-entry-never-created | 0 |
| failed-before-start-validation | 1 |
| retrying | 0 |
| timed-out | 1 |
| rate-limited-waiting | 0 |
| done-but-unread | 0 |
| done-then-source-video-changed-stale | 1 |
| deleted-entry | 0 |
| superseded-by-re-run | 0 |

### thread-state

| value | leaves |
|---|---|
| first-question | 3 |
| follow-up-1 | 30 |
| follow-up-10 | 14 |
| follow-up-while-first-still-running | 6 |
| follow-up-after-video-deleted | 5 |
| follow-up-with-changed-video-set | 1 |
| thread-opened-from-history | 6 |
| thread-where-an-answer-failed | 4 |
| follow-up-limit-reached | 3 |
| follow-up-after-agent-version-change | 3 |
| follow-up-from-second-tab-simultaneously | 4 |
| wanting-to-ask-about-a-report-entry | 1 |

### history-state

| value | leaves |
|---|---|
| empty | 0 |
| 1-entry | 1 |
| 100-entries | 0 |
| 1000-entries | 1 |
| report-and-question-entries-interleaved | 3 |
| entry-referencing-deleted-video | 2 |
| two-entries-same-second | 0 |
| entries-with-blank-run-name | 0 |
| mix-of-done-and-failed-across-recent-runs | 0 |
| filtered-so-new-entry-hidden | 0 |
| scrolled-to-page-3-at-redirect | 0 |
| sorted-not-by-newest | 0 |
| several-running-at-once | 0 |
| entries-from-older-agent-version | 1 |
| filtered-to-zero | 0 |

### time-and-connection

| value | leaves |
|---|---|
| first-ever-use | 0 |
| steady-state | 2 |
| offline-at-submit | 1 |
| submit-succeeds-redirect-fails | 0 |
| redirect-lands-before-entry-exists | 0 |
| session-expired-at-submit | 1 |
| page-open-for-hours | 2 |
| during-agent-outage | 0 |
| after-a-year | 1 |
| deploy-during-run | 1 |
| two-devices-same-user | 0 |
| timezone-of-entry-timestamp | 0 |
| session-expired-while-composing-long-prompt | 0 |
| rate-limit-at-submit | 0 |
| agent-model-version-changed-since-entry | 2 |

### action

| value | leaves |
|---|---|
| open-agent-page | 1 |
| switch-mode | 2 |
| open-add-video-popup | 0 |
| filter-by-tag | 0 |
| search | 0 |
| select-video | 5 |
| deselect-video | 3 |
| close-popup-without-confirm | 1 |
| type-run-name | 0 |
| type-prompt | 0 |
| pick-suggested-question | 12 |
| type-question | 14 |
| submit | 13 |
| double-submit | 4 |
| back-button-after-redirect | 2 |
| refresh-after-redirect | 0 |
| open-history-entry | 5 |
| re-run-not-in-spec | 0 |
| delete-entry-not-in-spec | 2 |
| rename-entry-not-in-spec | 0 |
| ask-follow-up | 61 |
| cancel-run-not-in-spec | 1 |
| share-or-export-not-in-spec | 2 |
| retry-failed-videos-only | 0 |
| retry-whole-run | 0 |
| clear-all-selection | 0 |
| select-all-filtered | 0 |
| navigate-away-mid-compose | 3 |
| return-to-draft | 2 |
| edit-and-resubmit-from-entry | 0 |
| filter-history-by-mode-or-status | 0 |
| search-history | 0 |
| copy-output | 1 |
| open-cited-timestamp | 0 |
| mark-read | 0 |
| logout-while-running | 0 |
| follow-up-from-two-tabs | 3 |

### media-appearance

| value | leaves |
|---|---|
| thumbnail-near-white | 0 |
| thumbnail-near-black | 0 |
| thumbnail-busy-or-high-detail | 0 |
| no-thumbnail-yet | 0 |
| generic-placeholder-thumbnail | 0 |
| identical-thumbnails-across-videos | 0 |
| thumbnail-with-burned-in-text | 0 |
| portrait-or-odd-aspect-ratio | 0 |

### per-video-outcome-within-run

| value | leaves |
|---|---|
| all-videos-used | 0 |
| one-video-unusable | 1 |
| some-videos-unusable | 1 |
| all-videos-unusable | 1 |
| video-truncated-to-fit-context | 0 |
| video-skipped-because-deleted | 0 |
| video-replaced-mid-run | 0 |

### entry-point-and-lifecycle-phase

| value | leaves |
|---|---|
| before-first-ingestion-completes | 0 |
| arriving-from-nav | 0 |
| arriving-from-videos-page-with-preselection | 0 |
| deep-link-to-mode | 0 |
| returning-mid-compose | 2 |
| post-submit-same-screen | 1 |
| post-submit-elsewhere-in-app | 2 |
| app-closed-while-running | 0 |
| after-done-consuming-output | 0 |
| long-after-retention-window | 0 |

### observer-location-at-status-change

| value | leaves |
|---|---|
| on-history-tab-top | 0 |
| on-history-tab-scrolled-or-filtered | 0 |
| inside-entry-detail | 2 |
| on-agent-form-composing-next-run | 0 |
| other-page-in-app | 2 |
| other-tab | 0 |
| other-device | 0 |
| logged-out | 0 |

### permission-and-plan

| value | leaves |
|---|---|
| full-access | 0 |
| viewer-role | 0 |
| trial-or-plan-without-agent | 0 |
| quota-remaining | 1 |
| quota-exhausted-at-submit | 0 |
| access-revoked-mid-run | 1 |
| member-removed-from-workspace | 0 |
| video-owned-by-other-user | 0 |
| video-in-folder-user-cannot-see | 0 |

### popup-session-state

| value | leaves |
|---|---|
| first-open | 0 |
| reopen-with-prior-selection | 1 |
| closed-without-confirm | 1 |
| selection-hidden-by-filter | 0 |
| filter-yields-zero | 0 |
| library-changed-while-open | 0 |
| at-max-selection | 0 |
| select-all-filtered | 0 |

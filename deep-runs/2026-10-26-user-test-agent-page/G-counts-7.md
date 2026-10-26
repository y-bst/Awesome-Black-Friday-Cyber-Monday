# Stage G counts, bucket 7

Bucket: G-bucket-7.yaml (surfaces selected-videos-list, error-toast-or-banner, quota-or-limit-message, videos-page, and leaves with no surface named)

| Measure | Count |
|---|---|
| Leaves in | 164 |
| Rejected | 0 |
| Duplicate clusters | 25 |
| Leaves merged into a survivor | 38 |
| Surviving leaves | 126 |
| Survivors with axis values added by cell normalisation | 103 |
| Survivors whose cell also took values from merged duplicates | 23 |
| Leaves with no surface in the input, given one during normalisation | 59 (all now carry a surface, directly or via their cluster survivor) |

## Rejected

None. Every item is L3/L4, names a concrete spec object, has the full schema, and no banned word appears in any field. Two items (admin-3, admin-17) used a non-axis key `surface-secondary`; this is not a contract violation, so the value was moved under `surface` during normalisation (admin-3 is merged into draft-32).

## Duplicate clusters (survivor <- merged ids)

- a11y-34 <- lowvision-34  (Offline or failed submit shows an error that disappears or is not announced, and the form content may be lost)
- backend-5 <- support-14, participant-19  (Video deleted on the Videos page between Submit and the job starting: job does not know whether to fail, skip, or use a snapshot)
- backend-6 <- redirect-24  (If still-ingesting videos are selectable, the job needs a wait-for-ingestion rule with a timeout (e.g. 60 min) and a status shown while waiting)
- backend-25 <- qa-lead-55  (Output language undefined when videos are in German, the prompt in English and the UI in English)
- backend-28 <- sre-28  (Job runs under whose credentials: session expiring during a 30-minute run may revoke the worker's access to the video store)
- backend-40 <- qa-lead-56, ingest-36  (A 3-second clip gives a one-line transcript; with no minimum-content threshold the model writes a confident report from nothing)
- sharing-12 <- admin-4  (Run counts and quotas have no scope (per user or per team))
- ingest-11 <- popup-38  (Selected-video chip shows only the name, so a same-name re-upload in another tab makes the selection ambiguous)
- ingest-31 <- uploader-15, sre-30  (Re-ingestion overwrites transcript rows while a run is reading them, producing mixed old/new content)
- draft-3 <- firsttime-34  (Arriving on the Agent page from the Videos page with videos preselected is not specified (mode, selection, count))
- draft-32 <- cost-9, admin-3  (Quota exhausted at Submit after a long compose redirects to History and discards the draft)
- uploader-1 <- ingest-7  (Videos page delete confirmation shows no count of runs, reports or threads that reference the video)
- uploader-21 <- admin-21  (Videos of an uploader who leaves the workspace have no defined fate for teammates' runs and entries)
- uploader-37 <- admin-33  (Admin bulk delete to get under the plan limit breaks many users' entries at once with no impact preview)
- popup-16 <- mobile-19  (Selected-videos list on the form after the pop-up closes: layout, order, count and per-item remove are unspecified)
- prompt-13 <- qa-lead-25, redirect-13  (Offline at Submit: whether the redirect happens anyway and whether the typed prompt/question stays in the form is undefined)
- qa-lead-6 <- ingest-4, draft-26, popup-33, redirect-25, support-48, mobile-37, uploader-5  (Video deleted on Videos page in a second tab after being added to the selected-videos list, then Submit: reject, drop silently, or submit and fail is unspecified)
- qa-lead-38 <- firsttime-12  (Switching Report -> Ask question with 3 videos selected: selection carried over or reset is unspecified)
- privacy-3 <- uploader-2  (Video deleted while a run that selected it is Running; spec does not say whether the running job keeps and uses its transcript copy)
- sec-19 <- privacy-26, sre-29  (Member removed from workspace while their run is Running: whether the job finishes, under whose identity, and where its output goes is unspecified)
- sec-33 <- cost-2, qa-lead-33  (100 selected three-hour videos in one run: no per-run size or duration budget bounds compute)
- sre-3 <- qa-lead-49  (Whether submissions made during an outage are accepted into a queue or rejected at submit is unspecified, as is the queue's maximum depth)
- sre-25 <- support-39  (No incident banner on the History tab is specified to tell users their Queued or Running entries are affected by an outage)
- participant-26 <- privacy-22  (Failed run's error banner or logs echo prompt and transcript snippets containing participant personal data)
- participant-31 <- consumer-20  (Agent uses the participant's real first name from their spoken self-introduction although the study promised pseudonyms)

## Normalisation notes

- Leaves with no surface got the surface their situation or object points to (for backend-only items, the screen where the gap becomes visible: usually history-entry-status-badge or history-entry-detail).
- Where a leaf satisfies more than one value of an axis, the cell value is a list.
- A survivor's cell is the union of its own cell, the cells of the leaves merged into it, and the normalisation additions.
- videos-selected values written as the strings "0" / "1" were normalised to the integers 0 / 1 used in C-axes.yaml.

## Surviving leaves per perspective (id prefix)

| Perspective | Survivors |
|---|---|
| a11y | 3 |
| admin | 4 |
| backend | 15 |
| consumer | 6 |
| cost | 3 |
| draft | 8 |
| dup | 5 |
| firsttime | 3 |
| ingest | 8 |
| l10n | 6 |
| lowvision | 2 |
| mobile | 1 |
| participant | 8 |
| popup | 4 |
| privacy | 3 |
| prompt | 1 |
| qa-lead | 2 |
| realtime | 1 |
| sec | 9 |
| sharing | 1 |
| sre | 13 |
| support | 2 |
| tags | 4 |
| thread | 1 |
| uploader | 13 |

## Surviving counts per axis value

A leaf counts under every value its cell names. Zero-count values are listed explicitly.

### surface

| Value | Leaves |
|---|---|
| videos-page | 28 |
| agent-page-mode-switch | 1 |
| report-form | 5 |
| ask-question-form | 0 |
| add-video-popup | 16 |
| tag-filter | 2 |
| search-box | 1 |
| selected-videos-list | 32 |
| suggested-questions | 1 |
| run-name-field | 2 |
| prompt-field | 6 |
| question-field | 3 |
| submit-button | 23 |
| redirect-transition | 7 |
| history-tab | 4 |
| history-entry-row | 6 |
| history-entry-detail | 25 |
| follow-up-thread | 1 |
| empty-state | 1 |
| error-toast-or-banner | 19 |
| notification-email-or-in-app | 0 |
| global-running-indicator-or-badge | 0 |
| history-entry-status-badge | 10 |
| popup-footer-confirm-cancel | 0 |
| popup-selection-count | 2 |
| popup-zero-results | 1 |
| video-thumbnail-overlay | 0 |
| cited-video-timestamp-player | 0 |
| export-or-copy-output | 3 |
| history-filter-or-sort-controls | 0 |
| mode-tab-on-history-entry | 0 |
| quota-or-limit-message | 11 |
| onboarding-or-help-for-suggested-questions | 0 |

Zero leaves: ask-question-form, notification-email-or-in-app, global-running-indicator-or-badge, popup-footer-confirm-cancel, video-thumbnail-overlay, cited-video-timestamp-player, history-filter-or-sort-controls, mode-tab-on-history-entry, onboarding-or-help-for-suggested-questions

### actor

| Value | Leaves |
|---|---|
| creator-owner | 4 |
| same-user-second-tab | 4 |
| other-user-same-workspace | 9 |
| admin | 2 |
| background-agent-job | 16 |
| ingestion-job | 13 |
| video-uploader-other-than-runner | 14 |
| workspace-owner | 3 |
| viewer-role-member | 1 |
| removed-or-deactivated-user | 3 |
| support-staff-impersonating | 1 |
| test-participant-data-subject | 6 |
| report-recipient-without-access | 0 |

Zero leaves: report-recipient-without-access

### videos-selected

| Value | Leaves |
|---|---|
| 0 | 2 |
| 1 | 7 |
| 2-5 | 15 |
| 6-20 | 21 |
| 21-100 | 10 |
| all-videos-in-library | 1 |
| more-than-popup-shows-at-once | 0 |
| exceeds-limit-once-defined | 2 |
| selection-with-duplicate-uploads-of-same-session | 1 |
| selection-where-all-become-unusable-before-run | 0 |

Zero leaves: more-than-popup-shows-at-once, selection-where-all-become-unusable-before-run

### video-state

| Value | Leaves |
|---|---|
| ingested | 8 |
| still-ingesting | 6 |
| ingestion-failed | 3 |
| deleted-after-selection-before-run | 7 |
| deleted-after-run | 9 |
| re-uploaded-same-name | 7 |
| silent-or-no-transcript | 1 |
| 3-hour-long | 7 |
| 3-second-clip | 2 |
| untagged | 0 |
| non-english-audio | 4 |
| ingestion-queued-not-started | 0 |
| re-ingesting-after-edit | 5 |
| ingested-with-partial-transcript | 1 |
| multi-language-audio | 1 |
| duplicate-name-different-content | 2 |
| very-large-file | 0 |
| owned-by-another-user | 4 |
| access-revoked | 2 |
| moved-to-hidden-folder | 0 |
| ingested-but-thumbnail-missing | 1 |

Zero leaves: untagged, ingestion-queued-not-started, very-large-file, moved-to-hidden-folder

### library-state

| Value | Leaves |
|---|---|
| empty-library | 0 |
| 1-video | 4 |
| 50-videos | 4 |
| 2000-videos | 4 |
| all-untagged | 0 |
| 200-tags | 1 |
| tag-renamed-or-deleted-after-filtering | 0 |
| all-videos-still-ingesting | 0 |
| mixed-ownership-library | 7 |
| library-changing-while-popup-open | 1 |
| videos-in-folders-or-projects | 1 |
| library-at-plan-max | 2 |

Zero leaves: empty-library, all-untagged, tag-renamed-or-deleted-after-filtering, all-videos-still-ingesting

### mode

| Value | Leaves |
|---|---|
| report | 36 |
| ask-question | 8 |
| switching-mode-after-selecting-videos | 1 |

Zero leaves: none

### text-input-state

| Value | Leaves |
|---|---|
| run-name-empty | 0 |
| run-name-duplicate-of-existing | 1 |
| run-name-200-chars | 0 |
| prompt-empty | 1 |
| prompt-5000-chars | 5 |
| prompt-contradicts-report-mode | 0 |
| question-empty | 0 |
| question-picked-from-suggested | 1 |
| question-unrelated-to-videos | 1 |
| non-english-text | 2 |
| text-contains-instructions-to-ignore-rules | 1 |
| text-contains-html-or-markdown | 0 |
| whitespace-only | 0 |
| emoji-or-rtl | 1 |
| newline-pasted-into-run-name | 0 |
| suggested-question-edited-after-pick | 0 |
| question-exceeds-limit | 1 |
| text-contains-participant-personal-data | 1 |

Zero leaves: run-name-empty, run-name-200-chars, prompt-contradicts-report-mode, question-empty, text-contains-html-or-markdown, whitespace-only, newline-pasted-into-run-name, suggested-question-edited-after-pick

### run-status

| Value | Leaves |
|---|---|
| submitted-not-yet-visible-in-history | 2 |
| queued | 9 |
| running | 11 |
| done | 6 |
| failed | 7 |
| partial-some-videos-unusable | 4 |
| cancelled-not-in-spec | 0 |
| stuck-over-1h | 0 |
| done-with-empty-output | 1 |
| submit-accepted-but-entry-never-created | 1 |
| failed-before-start-validation | 5 |
| retrying | 4 |
| timed-out | 2 |
| rate-limited-waiting | 3 |
| done-but-unread | 0 |
| done-then-source-video-changed-stale | 0 |
| deleted-entry | 2 |
| superseded-by-re-run | 1 |

Zero leaves: cancelled-not-in-spec, stuck-over-1h, done-but-unread, done-then-source-video-changed-stale

### thread-state

| Value | Leaves |
|---|---|
| first-question | 0 |
| follow-up-1 | 2 |
| follow-up-10 | 0 |
| follow-up-while-first-still-running | 0 |
| follow-up-after-video-deleted | 0 |
| follow-up-with-changed-video-set | 0 |
| thread-opened-from-history | 0 |
| thread-where-an-answer-failed | 0 |
| follow-up-limit-reached | 0 |
| follow-up-after-agent-version-change | 0 |
| follow-up-from-second-tab-simultaneously | 0 |
| wanting-to-ask-about-a-report-entry | 0 |

Zero leaves: first-question, follow-up-10, follow-up-while-first-still-running, follow-up-after-video-deleted, follow-up-with-changed-video-set, thread-opened-from-history, thread-where-an-answer-failed, follow-up-limit-reached, follow-up-after-agent-version-change, follow-up-from-second-tab-simultaneously, wanting-to-ask-about-a-report-entry

### history-state

| Value | Leaves |
|---|---|
| empty | 0 |
| 1-entry | 3 |
| 100-entries | 5 |
| 1000-entries | 0 |
| report-and-question-entries-interleaved | 0 |
| entry-referencing-deleted-video | 8 |
| two-entries-same-second | 3 |
| entries-with-blank-run-name | 0 |
| mix-of-done-and-failed-across-recent-runs | 0 |
| filtered-so-new-entry-hidden | 0 |
| scrolled-to-page-3-at-redirect | 0 |
| sorted-not-by-newest | 0 |
| several-running-at-once | 4 |
| entries-from-older-agent-version | 0 |
| filtered-to-zero | 0 |

Zero leaves: empty, 1000-entries, report-and-question-entries-interleaved, entries-with-blank-run-name, mix-of-done-and-failed-across-recent-runs, filtered-so-new-entry-hidden, scrolled-to-page-3-at-redirect, sorted-not-by-newest, entries-from-older-agent-version, filtered-to-zero

### time-and-connection

| Value | Leaves |
|---|---|
| first-ever-use | 2 |
| steady-state | 3 |
| offline-at-submit | 3 |
| submit-succeeds-redirect-fails | 1 |
| redirect-lands-before-entry-exists | 0 |
| session-expired-at-submit | 3 |
| page-open-for-hours | 3 |
| during-agent-outage | 10 |
| after-a-year | 2 |
| deploy-during-run | 2 |
| two-devices-same-user | 0 |
| timezone-of-entry-timestamp | 0 |
| session-expired-while-composing-long-prompt | 1 |
| rate-limit-at-submit | 2 |
| agent-model-version-changed-since-entry | 0 |

Zero leaves: redirect-lands-before-entry-exists, two-devices-same-user, timezone-of-entry-timestamp, agent-model-version-changed-since-entry

### action

| Value | Leaves |
|---|---|
| open-agent-page | 1 |
| switch-mode | 1 |
| open-add-video-popup | 4 |
| filter-by-tag | 2 |
| search | 1 |
| select-video | 7 |
| deselect-video | 2 |
| close-popup-without-confirm | 0 |
| type-run-name | 0 |
| type-prompt | 0 |
| pick-suggested-question | 1 |
| type-question | 0 |
| submit | 30 |
| double-submit | 5 |
| back-button-after-redirect | 1 |
| refresh-after-redirect | 0 |
| open-history-entry | 1 |
| re-run-not-in-spec | 5 |
| delete-entry-not-in-spec | 2 |
| rename-entry-not-in-spec | 0 |
| ask-follow-up | 1 |
| cancel-run-not-in-spec | 1 |
| share-or-export-not-in-spec | 2 |
| retry-failed-videos-only | 1 |
| retry-whole-run | 2 |
| clear-all-selection | 0 |
| select-all-filtered | 1 |
| navigate-away-mid-compose | 2 |
| return-to-draft | 3 |
| edit-and-resubmit-from-entry | 0 |
| filter-history-by-mode-or-status | 0 |
| search-history | 0 |
| copy-output | 1 |
| open-cited-timestamp | 0 |
| mark-read | 0 |
| logout-while-running | 2 |
| follow-up-from-two-tabs | 0 |

Zero leaves: close-popup-without-confirm, type-run-name, type-prompt, type-question, refresh-after-redirect, rename-entry-not-in-spec, clear-all-selection, edit-and-resubmit-from-entry, filter-history-by-mode-or-status, search-history, open-cited-timestamp, mark-read, follow-up-from-two-tabs

### media-appearance

| Value | Leaves |
|---|---|
| thumbnail-near-white | 0 |
| thumbnail-near-black | 0 |
| thumbnail-busy-or-high-detail | 0 |
| no-thumbnail-yet | 1 |
| generic-placeholder-thumbnail | 0 |
| identical-thumbnails-across-videos | 0 |
| thumbnail-with-burned-in-text | 1 |
| portrait-or-odd-aspect-ratio | 0 |

Zero leaves: thumbnail-near-white, thumbnail-near-black, thumbnail-busy-or-high-detail, generic-placeholder-thumbnail, identical-thumbnails-across-videos, portrait-or-odd-aspect-ratio

### per-video-outcome-within-run

| Value | Leaves |
|---|---|
| all-videos-used | 2 |
| one-video-unusable | 5 |
| some-videos-unusable | 1 |
| all-videos-unusable | 0 |
| video-truncated-to-fit-context | 2 |
| video-skipped-because-deleted | 4 |
| video-replaced-mid-run | 2 |

Zero leaves: all-videos-unusable

### entry-point-and-lifecycle-phase

| Value | Leaves |
|---|---|
| before-first-ingestion-completes | 1 |
| arriving-from-nav | 0 |
| arriving-from-videos-page-with-preselection | 3 |
| deep-link-to-mode | 1 |
| returning-mid-compose | 5 |
| post-submit-same-screen | 0 |
| post-submit-elsewhere-in-app | 0 |
| app-closed-while-running | 0 |
| after-done-consuming-output | 0 |
| long-after-retention-window | 3 |

Zero leaves: arriving-from-nav, post-submit-same-screen, post-submit-elsewhere-in-app, app-closed-while-running, after-done-consuming-output

### observer-location-at-status-change

| Value | Leaves |
|---|---|
| on-history-tab-top | 1 |
| on-history-tab-scrolled-or-filtered | 0 |
| inside-entry-detail | 0 |
| on-agent-form-composing-next-run | 0 |
| other-page-in-app | 0 |
| other-tab | 0 |
| other-device | 1 |
| logged-out | 1 |

Zero leaves: on-history-tab-scrolled-or-filtered, inside-entry-detail, on-agent-form-composing-next-run, other-page-in-app, other-tab

### permission-and-plan

| Value | Leaves |
|---|---|
| full-access | 1 |
| viewer-role | 0 |
| trial-or-plan-without-agent | 1 |
| quota-remaining | 7 |
| quota-exhausted-at-submit | 5 |
| access-revoked-mid-run | 2 |
| member-removed-from-workspace | 3 |
| video-owned-by-other-user | 2 |
| video-in-folder-user-cannot-see | 1 |

Zero leaves: viewer-role

### popup-session-state

| Value | Leaves |
|---|---|
| first-open | 1 |
| reopen-with-prior-selection | 2 |
| closed-without-confirm | 0 |
| selection-hidden-by-filter | 1 |
| filter-yields-zero | 0 |
| library-changed-while-open | 1 |
| at-max-selection | 1 |
| select-all-filtered | 1 |

Zero leaves: closed-without-confirm, filter-yields-zero


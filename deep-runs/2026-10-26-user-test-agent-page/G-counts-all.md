# Combined counts after bucket merge

surviving leaves: 844 (from 1225 raw)

## per perspective (surviving)
- notify: 43
- a11y: 41
- l10n: 39
- lowvision: 37
- sec: 37
- dup: 36
- sharing: 35
- uploader: 34
- participant: 34
- backend: 33
- prompt: 32
- realtime: 32
- sre: 32
- thread: 31
- consumer: 30
- draft: 29
- popup: 29
- ingest: 28
- cost: 27
- admin: 25
- privacy: 24
- qa-lead: 23
- mobile: 22
- output: 22
- history: 21
- firsttime: 18
- tags: 18
- redirect: 16
- support: 16

## per axis value (a leaf counts under every value its cell names)

### surface
- videos-page: 28
- agent-page-mode-switch: 22
- report-form: 19
- ask-question-form: 3
- add-video-popup: 101
- tag-filter: 35
- search-box: 23
- selected-videos-list: 32
- suggested-questions: 28
- run-name-field: 17
- prompt-field: 31
- question-field: 26
- submit-button: 60
- redirect-transition: 41
- history-tab: 75
- history-entry-row: 96
- history-entry-detail: 151
- follow-up-thread: 75
- empty-state: 14
- error-toast-or-banner: 19
- notification-email-or-in-app: 28
- global-running-indicator-or-badge: 6
- history-entry-status-badge: 37
- popup-footer-confirm-cancel: 4
- popup-selection-count: 6
- popup-zero-results: 8
- video-thumbnail-overlay: 9
- cited-video-timestamp-player: 11
- export-or-copy-output: 21
- history-filter-or-sort-controls: 7
- mode-tab-on-history-entry: 0
- quota-or-limit-message: 12
- onboarding-or-help-for-suggested-questions: 0

### actor
- creator-owner: 38
- same-user-second-tab: 24
- other-user-same-workspace: 53
- admin: 13
- background-agent-job: 45
- ingestion-job: 21
- video-uploader-other-than-runner: 34
- workspace-owner: 15
- viewer-role-member: 11
- removed-or-deactivated-user: 11
- support-staff-impersonating: 7
- test-participant-data-subject: 33
- report-recipient-without-access: 12

### videos-selected
- 0: 5
- 1: 18
- 2-5: 93
- 6-20: 97
- 21-100: 42
- all-videos-in-library: 9
- more-than-popup-shows-at-once: 4
- exceeds-limit-once-defined: 3
- selection-with-duplicate-uploads-of-same-session: 4
- selection-where-all-become-unusable-before-run: 2

### video-state
- ingested: 26
- still-ingesting: 27
- ingestion-failed: 14
- deleted-after-selection-before-run: 15
- deleted-after-run: 40
- re-uploaded-same-name: 15
- silent-or-no-transcript: 20
- 3-hour-long: 24
- 3-second-clip: 10
- untagged: 5
- non-english-audio: 16
- ingestion-queued-not-started: 1
- re-ingesting-after-edit: 13
- ingested-with-partial-transcript: 2
- multi-language-audio: 6
- duplicate-name-different-content: 6
- very-large-file: 0
- owned-by-another-user: 14
- access-revoked: 5
- moved-to-hidden-folder: 1
- ingested-but-thumbnail-missing: 3

### library-state
- empty-library: 6
- 1-video: 13
- 50-videos: 42
- 2000-videos: 23
- all-untagged: 3
- 200-tags: 15
- tag-renamed-or-deleted-after-filtering: 8
- all-videos-still-ingesting: 5
- mixed-ownership-library: 19
- library-changing-while-popup-open: 5
- videos-in-folders-or-projects: 1
- library-at-plan-max: 2

### mode
- report: 247
- ask-question: 171
- switching-mode-after-selecting-videos: 12

### text-input-state
- run-name-empty: 13
- run-name-duplicate-of-existing: 9
- run-name-200-chars: 6
- prompt-empty: 8
- prompt-5000-chars: 29
- prompt-contradicts-report-mode: 6
- question-empty: 5
- question-picked-from-suggested: 19
- question-unrelated-to-videos: 7
- non-english-text: 24
- text-contains-instructions-to-ignore-rules: 11
- text-contains-html-or-markdown: 10
- whitespace-only: 4
- emoji-or-rtl: 6
- newline-pasted-into-run-name: 1
- suggested-question-edited-after-pick: 4
- question-exceeds-limit: 3
- text-contains-participant-personal-data: 20

### run-status
- submitted-not-yet-visible-in-history: 26
- queued: 34
- running: 65
- done: 87
- failed: 41
- partial-some-videos-unusable: 19
- cancelled-not-in-spec: 4
- stuck-over-1h: 9
- done-with-empty-output: 12
- submit-accepted-but-entry-never-created: 8
- failed-before-start-validation: 11
- retrying: 10
- timed-out: 4
- rate-limited-waiting: 10
- done-but-unread: 7
- done-then-source-video-changed-stale: 9
- deleted-entry: 9
- superseded-by-re-run: 6

### thread-state
- first-question: 6
- follow-up-1: 39
- follow-up-10: 20
- follow-up-while-first-still-running: 9
- follow-up-after-video-deleted: 5
- follow-up-with-changed-video-set: 3
- thread-opened-from-history: 14
- thread-where-an-answer-failed: 6
- follow-up-limit-reached: 3
- follow-up-after-agent-version-change: 3
- follow-up-from-second-tab-simultaneously: 4
- wanting-to-ask-about-a-report-entry: 6

### history-state
- empty: 10
- 1-entry: 21
- 100-entries: 46
- 1000-entries: 30
- report-and-question-entries-interleaved: 17
- entry-referencing-deleted-video: 25
- two-entries-same-second: 16
- entries-with-blank-run-name: 12
- mix-of-done-and-failed-across-recent-runs: 3
- filtered-so-new-entry-hidden: 2
- scrolled-to-page-3-at-redirect: 1
- sorted-not-by-newest: 2
- several-running-at-once: 23
- entries-from-older-agent-version: 4
- filtered-to-zero: 0

### time-and-connection
- first-ever-use: 27
- steady-state: 33
- offline-at-submit: 9
- submit-succeeds-redirect-fails: 5
- redirect-lands-before-entry-exists: 11
- session-expired-at-submit: 9
- page-open-for-hours: 23
- during-agent-outage: 25
- after-a-year: 18
- deploy-during-run: 8
- two-devices-same-user: 7
- timezone-of-entry-timestamp: 7
- session-expired-while-composing-long-prompt: 2
- rate-limit-at-submit: 7
- agent-model-version-changed-since-entry: 6

### action
- open-agent-page: 19
- switch-mode: 14
- open-add-video-popup: 33
- filter-by-tag: 27
- search: 27
- select-video: 50
- deselect-video: 7
- close-popup-without-confirm: 5
- type-run-name: 12
- type-prompt: 7
- pick-suggested-question: 15
- type-question: 18
- submit: 135
- double-submit: 26
- back-button-after-redirect: 9
- refresh-after-redirect: 5
- open-history-entry: 70
- re-run-not-in-spec: 16
- delete-entry-not-in-spec: 15
- rename-entry-not-in-spec: 3
- ask-follow-up: 76
- cancel-run-not-in-spec: 8
- share-or-export-not-in-spec: 22
- retry-failed-videos-only: 3
- retry-whole-run: 7
- clear-all-selection: 1
- select-all-filtered: 7
- navigate-away-mid-compose: 9
- return-to-draft: 13
- edit-and-resubmit-from-entry: 3
- filter-history-by-mode-or-status: 3
- search-history: 5
- copy-output: 14
- open-cited-timestamp: 9
- mark-read: 5
- logout-while-running: 4
- follow-up-from-two-tabs: 3

### media-appearance
- thumbnail-near-white: 2
- thumbnail-near-black: 4
- thumbnail-busy-or-high-detail: 2
- no-thumbnail-yet: 2
- generic-placeholder-thumbnail: 2
- identical-thumbnails-across-videos: 2
- thumbnail-with-burned-in-text: 2
- portrait-or-odd-aspect-ratio: 0

### per-video-outcome-within-run
- all-videos-used: 4
- one-video-unusable: 8
- some-videos-unusable: 14
- all-videos-unusable: 6
- video-truncated-to-fit-context: 5
- video-skipped-because-deleted: 5
- video-replaced-mid-run: 3

### entry-point-and-lifecycle-phase
- before-first-ingestion-completes: 4
- arriving-from-nav: 6
- arriving-from-videos-page-with-preselection: 4
- deep-link-to-mode: 5
- returning-mid-compose: 15
- post-submit-same-screen: 4
- post-submit-elsewhere-in-app: 6
- app-closed-while-running: 5
- after-done-consuming-output: 4
- long-after-retention-window: 8

### observer-location-at-status-change
- on-history-tab-top: 11
- on-history-tab-scrolled-or-filtered: 4
- inside-entry-detail: 6
- on-agent-form-composing-next-run: 3
- other-page-in-app: 11
- other-tab: 8
- other-device: 6
- logged-out: 7

### permission-and-plan
- full-access: 10
- viewer-role: 12
- trial-or-plan-without-agent: 5
- quota-remaining: 14
- quota-exhausted-at-submit: 7
- access-revoked-mid-run: 7
- member-removed-from-workspace: 9
- video-owned-by-other-user: 8
- video-in-folder-user-cannot-see: 7

### popup-session-state
- first-open: 10
- reopen-with-prior-selection: 7
- closed-without-confirm: 3
- selection-hidden-by-filter: 4
- filter-yields-zero: 5
- library-changed-while-open: 6
- at-max-selection: 2
- select-all-filtered: 7

## zero-leaf values (5)
- surface: mode-tab-on-history-entry
- surface: onboarding-or-help-for-suggested-questions
- video-state: very-large-file
- history-state: filtered-to-zero
- media-appearance: portrait-or-odd-aspect-ratio

## one-leaf values (6)
- video-state: ingestion-queued-not-started
- video-state: moved-to-hidden-folder
- library-state: videos-in-folders-or-projects
- text-input-state: newline-pasted-into-run-name
- history-state: scrolled-to-page-3-at-redirect
- action: clear-all-selection

# G-counts-2 (bucket 2, gaps run)

| metric | count |
|---|---|
| in | 167 |
| rejected | 0 |
| clusters (survivor + duplicates) | 30 |
| duplicates merged into survivors | 51 |
| variant links (pairs) | 94 |
| leaves carrying variants_of | 106 |
| contested (ideate only) | 0 (n/a, gaps run) |
| surviving | 116 |
| uncategorised | 0 |
| leaves with cell values added by normalisation | 83 |
| cell values added in total | 130 |

## Rejected ids

None. All 167 items are L3/L4, name a pipeline stage, data element or spec sentence, and are actionable. Banned-word hits (improve x4, improvement x1) are inside spec quotes or followed by a specific instance (sec-18 situation names the mined object: past conversations used as a global improvement set).

## Clusters (survivor <- merged ids)

- chat-4 <- skeptic-16, onboard-27
- chat-8 <- onboard-16, exec-5
- chat-27 <- design-27, analyst-14, onboard-33
- chat-3 <- analyst-1, skeptic-1, exec-24, qauthor-11
- cost-7 <- chat-10
- chat-6 <- ds-21, exec-25, cost-6, analyst-8, skeptic-7
- auditor-2 <- exec-2, chat-13, analyst-7, stitch-36
- chat-37 <- exec-17, ds-9, analyst-39
- onboard-5 <- design-30
- ops-24 <- analyst-17
- analyst-4 <- exec-4
- chat-24 <- ops-14, exec-29
- auditor-1 <- analyst-28
- chat-9 <- player-30, analyst-20
- chat-35 <- skeptic-33
- cost-5 <- eval-34, exec-34, chat-25, analyst-32
- chat-38 <- exec-11
- chat-1 <- stitch-11
- chat-32 <- exec-26
- sec-7 <- analyst-23
- chat-18 <- auditor-37
- ops-37 <- chat-23
- auditor-30 <- chat-19
- player-17 <- privacy-17
- l10n-5 <- l10n-10
- l10n-25 <- chat-36
- l10n-19 <- speech-28
- chat-15 <- analyst-19
- chat-30 <- design-26
- analyst-26 <- exec-6

## Leaves per perspective (in -> surviving)

| perspective | in | surviving |
|---|---|---|
| analyst | 29 | 18 |
| auditor | 10 | 9 |
| chat | 32 | 26 |
| cost | 9 | 8 |
| design | 3 | 0 |
| ds | 7 | 5 |
| eval | 6 | 5 |
| exec | 12 | 1 |
| l10n | 6 | 5 |
| moderator | 1 | 1 |
| onboard | 4 | 1 |
| ops | 3 | 2 |
| percep | 3 | 3 |
| player | 4 | 3 |
| privacy | 3 | 2 |
| qauthor | 1 | 0 |
| sec | 12 | 12 |
| skeptic | 13 | 9 |
| speech | 1 | 0 |
| stitch | 3 | 1 |
| uxr | 5 | 5 |

## Counts per axis value (normalised cells, survivors; a leaf with a list value counts once per value)

### stage

| value | count |
|---|---|
| video-capture | 0 |
| 15-minute-split | 0 |
| session-stitching | 1 |
| transcription | 1 |
| fixed-question-set | 0 |
| answer-options | 3 |
| per-video-answers | 9 |
| session-level-aggregation | 1 |
| answers-table | 1 |
| chatbot-query-planning | 48 |
| chatbot-answer | 50 |
| evidence-display | 0 |
| studio-ui | 0 |
| recruitment-and-consent | 0 |
| build-and-metadata-tagging | 0 |
| upload-and-ingest | 0 |
| audio-extraction | 0 |
| language-detection | 0 |
| question-set-registry | 0 |
| extraction-prompt | 0 |
| job-orchestration-and-status | 0 |
| rerun-and-backfill | 0 |
| aggregate-cache | 1 |
| access-control | 0 |
| retention-and-deletion | 2 |
| export-and-share | 1 |
| studio-feedback-loop | 0 |

zero values (16): video-capture, 15-minute-split, fixed-question-set, evidence-display, studio-ui, recruitment-and-consent, build-and-metadata-tagging, upload-and-ingest, audio-extraction, language-detection, question-set-registry, extraction-prompt, job-orchestration-and-status, rerun-and-backfill, access-control, studio-feedback-loop

### data-element

| value | count |
|---|---|
| session | 2 |
| video | 3 |
| transcript | 8 |
| utterance | 2 |
| timestamp | 3 |
| question | 1 |
| option | 3 |
| answer | 4 |
| player | 9 |
| cohort | 2 |
| game-version | 4 |
| game-target | 6 |
| tutorial-step | 2 |
| screen-state | 0 |
| build-id | 0 |
| device-platform | 2 |
| moderator | 2 |
| consent-record | 1 |
| question-set-version | 4 |
| prompt-version | 3 |
| extraction-model-version | 0 |
| transcription-model-version | 0 |
| extraction-run-id | 3 |
| answer-confidence | 3 |
| evidence-span | 3 |
| null-vs-no | 3 |
| studio-tenant | 1 |
| chatbot-conversation-log | 11 |
| cached-aggregate | 3 |

zero values (4): screen-state, build-id, extraction-model-version, transcription-model-version

### session-shape

| value | count |
|---|---|
| one-video | 0 |
| 2-4-videos | 0 |
| 5-20-videos | 4 |
| missing-middle-video | 1 |
| videos-out-of-order | 1 |
| overlapping-videos | 0 |
| session-ends-mid-sentence | 0 |
| zero-videos-session-failed | 0 |
| last-video-under-1-minute | 0 |
| duplicate-upload | 0 |
| video-with-no-audio-track | 0 |
| session-split-by-crash-into-two | 1 |
| same-player-multiple-sessions | 3 |
| tutorial-started-before-recording | 1 |
| 10-plus-hour-session | 3 |

zero values (8): one-video, 2-4-videos, overlapping-videos, session-ends-mid-sentence, zero-videos-session-failed, last-video-under-1-minute, duplicate-upload, video-with-no-audio-track

### speech-shape

| value | count |
|---|---|
| silent-player | 4 |
| continuous-think-aloud | 1 |
| game-audio-dominates | 0 |
| two-speakers | 0 |
| non-english | 5 |
| mixed-language | 0 |
| profanity-or-slang | 0 |
| inaudible-segments | 0 |
| moderator-speaking-or-leading | 1 |
| player-reading-chat-or-overlay-aloud | 1 |
| background-tv-or-other-people | 0 |
| whispering | 0 |
| mic-muted-for-a-period | 1 |
| emotional-nonverbal-only (sighs, laughs, swearing-masked) | 0 |

zero values (8): game-audio-dominates, two-speakers, mixed-language, profanity-or-slang, inaudible-segments, background-tv-or-other-people, whispering, emotional-nonverbal-only (sighs, laughs, swearing-masked)

### question-shape

| value | count |
|---|---|
| fits-an-option | 1 |
| fits-no-option | 0 |
| fits-two-options | 0 |
| answer-spans-videos | 0 |
| answer-is-a-count | 0 |
| answer-is-a-time | 4 |
| answer-is-a-why | 3 |
| answer-needs-visuals | 0 |
| question-not-in-set | 10 |
| event-did-not-happen-in-this-video | 3 |
| answer-changes-within-video | 0 |
| answer-depends-on-prior-video | 1 |
| negation-player-never-did-x | 3 |
| unknowable-from-audio | 0 |
| two-options-both-partly-true | 1 |
| perceptual-cause-not-verbalised | 1 |

zero values (7): fits-no-option, fits-two-options, answer-spans-videos, answer-is-a-count, answer-needs-visuals, answer-changes-within-video, unknowable-from-audio

### studio-question-type

| value | count |
|---|---|
| one-player-what-happened | 2 |
| cohort-count | 27 |
| cohort-why | 9 |
| compare-two-versions | 8 |
| compare-two-steps | 2 |
| find-players-who | 10 |
| timeline-of-one-player | 3 |
| quote-me-evidence | 4 |
| follow-up-question | 5 |
| question-outside-game-target | 2 |
| trend-over-time | 1 |
| distribution-not-count | 5 |
| segment-by-metadata (device, country, build) | 3 |
| what-can-you-answer | 4 |
| recommendation-what-should-we-change | 2 |
| cross-game-or-cross-studio-benchmark | 4 |
| show-me-raw-transcript-or-clip | 1 |
| correction-that-is-wrong | 2 |
| question-about-a-step-the-set-never-asked | 10 |

zero values (0): none

### scale

| value | count |
|---|---|
| 1-player | 3 |
| 50-players | 3 |
| 500-players | 24 |
| 5000-players | 2 |
| 10-games-at-once | 0 |
| 0-players-new-game | 1 |
| 1-player-10-hour-session | 3 |
| 50000-videos | 2 |
| many-concurrent-studio-users | 2 |
| question-set-of-50-questions | 2 |
| 500-players-x-3-question-set-versions | 2 |

zero values (1): 10-games-at-once

### correctness-failure

| value | count |
|---|---|
| hallucinated-answer | 3 |
| forced-choice-bias | 1 |
| inconsistent-across-videos | 1 |
| stale-after-prompt-change | 2 |
| wrong-denominator | 13 |
| right-answer-wrong-player | 0 |
| confident-no-evidence | 8 |
| instruction-injected-via-transcript | 4 |
| answer-attached-to-wrong-video-index | 2 |
| duplicate-counted | 3 |
| null-treated-as-no | 6 |
| other-option-overused | 0 |
| mixed-version-aggregation | 6 |
| perceptual-cause-attributed-to-verbal-option | 1 |
| moderator-words-attributed-to-player | 1 |
| transcription-hallucination-propagated | 1 |

zero values (2): right-answer-wrong-player, other-option-overused

### time-and-change

| value | count |
|---|---|
| first-game-onboarded | 6 |
| game-update-changes-tutorial | 2 |
| question-set-revised | 4 |
| model-upgraded | 2 |
| a-year-of-data | 2 |
| studio-asks-at-3am | 2 |
| player-deletion-request | 3 |
| transcription-model-upgraded | 0 |
| rerun-in-progress-while-queried | 4 |
| studio-offboarded | 0 |
| retention-expiry | 0 |
| game-target-changes-beyond-tutorial | 0 |
| extraction-vendor-deprecates-model | 0 |

zero values (5): transcription-model-upgraded, studio-offboarded, retention-expiry, game-target-changes-beyond-tutorial, extraction-vendor-deprecates-model

### latency

| value | count |
|---|---|
| under-2s | 4 |
| under-30s | 6 |
| minutes | 3 |
| batch-overnight | 1 |
| first-token-vs-complete-answer | 2 |
| p99-tail-under-concurrency | 2 |
| ingest-to-queryable (hours or days after session) | 1 |
| fast-but-stale | 3 |

zero values (0): none

### processing-status

| value | count |
|---|---|
| not-yet-uploaded | 1 |
| uploaded-partial | 0 |
| queued | 1 |
| transcribing | 1 |
| transcribed | 1 |
| transcription-failed | 2 |
| transcript-empty | 1 |
| extracting | 0 |
| extraction-partial-some-questions | 0 |
| extraction-failed | 0 |
| complete | 0 |
| superseded-by-rerun | 2 |
| rerun-in-progress | 3 |
| deleted-by-request | 3 |

zero values (5): uploaded-partial, extracting, extraction-partial-some-questions, extraction-failed, complete

### batch-failure-mix

| value | count |
|---|---|
| all-succeed | 0 |
| one-video-of-session-failed | 1 |
| some-questions-failed-in-one-video | 0 |
| some-sessions-failed-in-cohort | 1 |
| all-failed | 0 |
| retry-produced-duplicate | 1 |
| late-arriving-video-after-aggregation | 0 |

zero values (4): all-succeed, some-questions-failed-in-one-video, all-failed, late-arriving-video-after-aggregation

### recovery-action

| value | count |
|---|---|
| retry-one-video | 0 |
| retry-one-question | 0 |
| rerun-whole-session | 1 |
| backfill-after-question-set-change | 2 |
| backfill-after-model-upgrade | 3 |
| skip-and-mark-unknown | 0 |
| manual-override-answer | 1 |
| delete-and-propagate | 1 |

zero values (3): retry-one-video, retry-one-question, skip-and-mark-unknown

### question-set-version-state

| value | count |
|---|---|
| single-version | 0 |
| mixed-versions-in-table | 4 |
| option-added | 1 |
| option-renamed-same-id | 2 |
| question-reworded-same-id | 1 |
| question-retired | 1 |
| per-game-fork | 2 |
| per-game-version-fork | 1 |
| rollback-to-old-version | 0 |

zero values (2): single-version, rollback-to-old-version

### transcription-subsystem

| value | count |
|---|---|
| hallucinated-text-on-silence-or-music | 1 |
| wrong-language-detected | 0 |
| language-flips-between-videos | 0 |
| truncated-at-length-limit | 0 |
| timestamps-reset-per-video | 3 |
| sentence-cut-at-15min-boundary | 0 |
| transcription-model-version-differs-across-videos | 0 |
| profanity-masked-by-vendor | 0 |
| game-lyrics-or-npc-voice-transcribed-as-player | 0 |
| low-confidence-segments-dropped-silently | 0 |
| empty-transcript-for-non-empty-video | 0 |

zero values (9): wrong-language-detected, language-flips-between-videos, truncated-at-length-limit, sentence-cut-at-15min-boundary, transcription-model-version-differs-across-videos, profanity-masked-by-vendor, game-lyrics-or-npc-voice-transcribed-as-player, low-confidence-segments-dropped-silently, empty-transcript-for-non-empty-video

### chatbot-response-behaviour

| value | count |
|---|---|
| answers-correctly | 6 |
| says-no-data-correctly | 1 |
| substitutes-nearest-fixed-question | 7 |
| answers-from-general-game-knowledge | 11 |
| invents-number | 8 |
| silently-truncates-rows | 4 |
| differs-on-re-ask | 12 |
| answers-in-wrong-tenant-scope | 6 |
| times-out | 3 |
| refuses-answerable-question | 1 |
| mixes-null-with-no | 1 |

zero values (0): none

### fast-path-dependency

| value | count |
|---|---|
| precomputed-aggregate-exists | 3 |
| table-fits-in-llm-context | 6 |
| text-to-sql-generated-correctly | 11 |
| index-on-game-target-and-version | 1 |
| cache-hit | 1 |
| cache-stale-after-rerun | 2 |
| question-requires-raw-transcript-fallback | 12 |
| concurrent-studio-load | 2 |
| table-growth-over-a-year | 0 |
| cold-start | 2 |

zero values (1): table-growth-over-a-year

### capture-integrity

| value | count |
|---|---|
| audio-and-video-ok | 0 |
| video-black-or-frozen | 0 |
| wrong-window-captured | 0 |
| no-audio-track | 0 |
| mic-muted-for-a-period | 1 |
| stereo-channel-only-game-audio | 0 |
| codec-unreadable | 0 |
| clock-drift-between-videos | 0 |
| upload-truncated | 0 |

zero values (8): audio-and-video-ok, video-black-or-frozen, wrong-window-captured, no-audio-track, stereo-channel-only-game-audio, codec-unreadable, clock-drift-between-videos, upload-truncated

### answer-afterlife

| value | count |
|---|---|
| read-once-in-chat | 3 |
| copied-into-deck | 12 |
| exported-csv | 2 |
| shared-link | 0 |
| re-asked-after-rerun | 2 |
| acted-on-tutorial-changed | 4 |
| disputed-by-studio | 2 |
| cited-after-player-deletion | 2 |

zero values (1): shared-link

### tenancy

| value | count |
|---|---|
| one-studio-one-game | 0 |
| one-studio-many-games | 1 |
| many-studios-shared-infra | 10 |
| cross-studio-benchmark-request | 3 |
| studio-offboarded | 0 |

zero values (2): one-studio-one-game, studio-offboarded


# Stage G counts, bucket 1

Bucket: G-bucket-1.yaml (stages transcription, per-video-answers). Run type: gaps.

- Leaves in: 142
- Rejected: 0
- Duplicate clusters: 24 (leaves merged into survivors: 42)
- Variants: 61 leaves carry `variants_of` (69 links); all variants kept
- Contested: 0 (gaps run; no refusal rows)
- Surviving leaves: 100
- Leaves with cell values added by normalisation: 95 (210 values added); values removed as plainly wrong: 1 (privacy-14 `transcription-subsystem: transcription-model-version-differs-across-videos`)
- Uncategorised leaves: 0
- Cell values not in C-axes.yaml after normalisation: 0

## Rejected

None. All 142 items are L3/L4, name a concrete object (a spec step or sentence, a named stage, a named data element, or a question/option), and could be acted on from the line alone. Banned-vocabulary scan over the whole bucket returned 2 hits of 'such as', both followed by a specific instance on the same line (speech-2 situation: 'such as ''Thanks for watching'''; pipe-23 title: 'such as ''confused at 03:00, understood at 10:00'''), which the contract allows. Notes, not rejections: player-19 is about the extraction vendor although filed under stage transcription (stage list extended, see normalisation); privacy-14 carried a transcription-subsystem value its situation does not satisfy (removed).

## Duplicate clusters (survivor <- merged ids; same situation on the same object)

- speech-2 <- cost-12, ds-35, pipe-20, player-31
- speech-1 <- pipe-19, ops-8, design-5
- extract-44 <- cost-15, pipe-16
- l10n-3 <- design-20, extract-30, speech-8
- moderator-5 <- pipe-36, design-16, uxr-6
- speech-14 <- skeptic-26
- speech-13 <- design-17, moderator-16, uxr-31
- speech-9 <- extract-37, uxr-10
- speech-34 <- uxr-9
- speech-3 <- onboard-13
- l10n-6 <- speech-24
- l10n-17 <- design-18, uxr-22
- privacy-28 <- player-27
- privacy-3 <- player-6
- extract-26 <- qauthor-15, speech-33
- pipe-23 <- design-13, skeptic-34, uxr-18
- design-1 <- analyst-10
- onboard-21 <- uxr-16
- skeptic-4 <- onboard-24
- extract-22 <- eval-15
- ds-28 <- eval-31
- percep-1 <- design-6, ds-34
- pipe-12 <- stitch-16
- extract-15 <- qauthor-28

## Variants (leaf -> variants_of; same mechanism, different part or scope; both kept)

- cost-30 -> moderator-5
- auditor-21 -> extract-44
- design-22 -> uxr-2
- l10n-13 -> extract-44, auditor-21
- l10n-14 -> speech-9
- l10n-18 -> l10n-3
- l10n-20 -> speech-34
- l10n-29 -> moderator-5
- l10n-31 -> speech-9, l10n-14
- onboard-14 -> speech-1
- onboard-26 -> speech-13
- onboard-32 -> speech-9
- percep-16 -> speech-3
- percep-18 -> speech-9
- ops-30 -> pipe-12
- privacy-11 -> extract-44
- privacy-13 -> moderator-5
- privacy-28 -> privacy-3
- eval-2 -> percep-1
- eval-4 -> extract-44
- eval-17 -> speech-2
- player-13 -> speech-13, sec-34
- player-14 -> moderator-5
- sec-34 -> speech-13, player-13
- stitch-21 -> speech-1
- stitch-24 -> moderator-5
- skeptic-6 -> percep-1
- speech-7 -> l10n-6
- speech-14 -> moderator-5
- speech-16 -> speech-13, player-13
- speech-19 -> speech-1
- uxr-2 -> design-22
- ds-3 -> extract-26
- ds-5 -> speech-1
- ds-6 -> speech-1
- auditor-19 -> extract-22
- design-1 -> onboard-21
- design-7 -> uxr-3
- extract-6 -> skeptic-4
- onboard-21 -> design-1
- percep-2 -> uxr-1
- percep-17 -> percep-20
- percep-20 -> percep-17
- percep-32 -> percep-1
- percep-34 -> moderator-5
- pipe-12 -> skeptic-4
- ops-39 -> ds-28
- eval-6 -> skeptic-4
- eval-19 -> speech-14, moderator-5
- qauthor-2 -> skeptic-4
- player-11 -> speech-9, l10n-31
- player-22 -> speech-34
- moderator-13 -> moderator-5
- stitch-38 -> extract-6
- speech-21 -> speech-1, uxr-3
- exec-18 -> speech-1
- uxr-1 -> percep-2
- uxr-3 -> speech-21
- uxr-11 -> percep-1
- uxr-23 -> percep-1
- uxr-30 -> extract-6

## Surviving leaves per perspective (in -> out)

| perspective | in | out |
|---|---|---|
| analyst | 1 | 0 |
| auditor | 2 | 2 |
| cost | 3 | 1 |
| design | 10 | 3 |
| ds | 8 | 6 |
| eval | 8 | 6 |
| exec | 1 | 1 |
| extract | 8 | 6 |
| l10n | 12 | 12 |
| moderator | 4 | 3 |
| onboard | 6 | 4 |
| ops | 5 | 4 |
| percep | 8 | 8 |
| pipe | 8 | 4 |
| player | 9 | 6 |
| privacy | 5 | 5 |
| qauthor | 3 | 1 |
| sec | 2 | 2 |
| skeptic | 4 | 2 |
| speech | 14 | 11 |
| stitch | 5 | 4 |
| uxr | 16 | 9 |

## Surviving leaves per axis value (normalised cells; a leaf counts under every value its cell names, zero values listed)

### stage

| value | leaves |
|---|---|
| video-capture | 0 |
| 15-minute-split | 1 |
| session-stitching | 1 |
| transcription | 49 |
| fixed-question-set | 0 |
| answer-options | 1 |
| per-video-answers | 53 |
| session-level-aggregation | 6 |
| answers-table | 0 |
| chatbot-query-planning | 0 |
| chatbot-answer | 0 |
| evidence-display | 2 |
| studio-ui | 0 |
| recruitment-and-consent | 2 |
| build-and-metadata-tagging | 0 |
| upload-and-ingest | 1 |
| audio-extraction | 0 |
| language-detection | 4 |
| question-set-registry | 0 |
| extraction-prompt | 2 |
| job-orchestration-and-status | 3 |
| rerun-and-backfill | 3 |
| aggregate-cache | 0 |
| access-control | 0 |
| retention-and-deletion | 2 |
| export-and-share | 0 |
| studio-feedback-loop | 0 |

### data-element

| value | leaves |
|---|---|
| session | 0 |
| video | 4 |
| transcript | 12 |
| utterance | 19 |
| timestamp | 6 |
| question | 1 |
| option | 2 |
| answer | 14 |
| player | 2 |
| cohort | 1 |
| game-version | 1 |
| game-target | 0 |
| tutorial-step | 7 |
| screen-state | 7 |
| build-id | 0 |
| device-platform | 2 |
| moderator | 11 |
| consent-record | 3 |
| question-set-version | 0 |
| prompt-version | 0 |
| extraction-model-version | 1 |
| transcription-model-version | 6 |
| extraction-run-id | 2 |
| answer-confidence | 4 |
| evidence-span | 6 |
| null-vs-no | 10 |
| studio-tenant | 0 |
| chatbot-conversation-log | 0 |
| cached-aggregate | 0 |

### session-shape

| value | leaves |
|---|---|
| one-video | 0 |
| 2-4-videos | 5 |
| 5-20-videos | 16 |
| missing-middle-video | 1 |
| videos-out-of-order | 0 |
| overlapping-videos | 0 |
| session-ends-mid-sentence | 1 |
| zero-videos-session-failed | 0 |
| last-video-under-1-minute | 3 |
| duplicate-upload | 0 |
| video-with-no-audio-track | 1 |
| session-split-by-crash-into-two | 0 |
| same-player-multiple-sessions | 0 |
| tutorial-started-before-recording | 0 |
| 10-plus-hour-session | 1 |

### speech-shape

| value | leaves |
|---|---|
| silent-player | 18 |
| continuous-think-aloud | 9 |
| game-audio-dominates | 5 |
| two-speakers | 6 |
| non-english | 10 |
| mixed-language | 1 |
| profanity-or-slang | 5 |
| inaudible-segments | 5 |
| moderator-speaking-or-leading | 12 |
| player-reading-chat-or-overlay-aloud | 3 |
| background-tv-or-other-people | 3 |
| whispering | 1 |
| mic-muted-for-a-period | 2 |
| emotional-nonverbal-only (sighs, laughs, swearing-masked) | 2 |

### question-shape

| value | leaves |
|---|---|
| fits-an-option | 8 |
| fits-no-option | 4 |
| fits-two-options | 3 |
| answer-spans-videos | 1 |
| answer-is-a-count | 1 |
| answer-is-a-time | 6 |
| answer-is-a-why | 10 |
| answer-needs-visuals | 9 |
| question-not-in-set | 0 |
| event-did-not-happen-in-this-video | 5 |
| answer-changes-within-video | 2 |
| answer-depends-on-prior-video | 3 |
| negation-player-never-did-x | 1 |
| unknowable-from-audio | 9 |
| two-options-both-partly-true | 2 |
| perceptual-cause-not-verbalised | 5 |

### studio-question-type

| value | leaves |
|---|---|
| one-player-what-happened | 2 |
| cohort-count | 15 |
| cohort-why | 7 |
| compare-two-versions | 1 |
| compare-two-steps | 6 |
| find-players-who | 2 |
| timeline-of-one-player | 3 |
| quote-me-evidence | 3 |
| follow-up-question | 0 |
| question-outside-game-target | 0 |
| trend-over-time | 2 |
| distribution-not-count | 1 |
| segment-by-metadata (device, country, build) | 6 |
| what-can-you-answer | 0 |
| recommendation-what-should-we-change | 1 |
| cross-game-or-cross-studio-benchmark | 0 |
| show-me-raw-transcript-or-clip | 0 |
| correction-that-is-wrong | 0 |
| question-about-a-step-the-set-never-asked | 0 |

### scale

| value | leaves |
|---|---|
| 1-player | 1 |
| 50-players | 3 |
| 500-players | 16 |
| 5000-players | 1 |
| 10-games-at-once | 0 |
| 0-players-new-game | 0 |
| 1-player-10-hour-session | 1 |
| 50000-videos | 1 |
| many-concurrent-studio-users | 0 |
| question-set-of-50-questions | 1 |
| 500-players-x-3-question-set-versions | 0 |

### correctness-failure

| value | leaves |
|---|---|
| hallucinated-answer | 8 |
| forced-choice-bias | 13 |
| inconsistent-across-videos | 8 |
| stale-after-prompt-change | 0 |
| wrong-denominator | 9 |
| right-answer-wrong-player | 6 |
| confident-no-evidence | 7 |
| instruction-injected-via-transcript | 2 |
| answer-attached-to-wrong-video-index | 4 |
| duplicate-counted | 1 |
| null-treated-as-no | 19 |
| other-option-overused | 7 |
| mixed-version-aggregation | 4 |
| perceptual-cause-attributed-to-verbal-option | 8 |
| moderator-words-attributed-to-player | 9 |
| transcription-hallucination-propagated | 6 |

### time-and-change

| value | leaves |
|---|---|
| first-game-onboarded | 2 |
| game-update-changes-tutorial | 0 |
| question-set-revised | 0 |
| model-upgraded | 1 |
| a-year-of-data | 1 |
| studio-asks-at-3am | 0 |
| player-deletion-request | 0 |
| transcription-model-upgraded | 5 |
| rerun-in-progress-while-queried | 0 |
| studio-offboarded | 0 |
| retention-expiry | 0 |
| game-target-changes-beyond-tutorial | 0 |
| extraction-vendor-deprecates-model | 1 |

### latency

| value | leaves |
|---|---|
| under-2s | 1 |
| under-30s | 0 |
| minutes | 0 |
| batch-overnight | 1 |
| first-token-vs-complete-answer | 0 |
| p99-tail-under-concurrency | 0 |
| ingest-to-queryable (hours or days after session) | 1 |
| fast-but-stale | 0 |

### processing-status

| value | leaves |
|---|---|
| not-yet-uploaded | 0 |
| uploaded-partial | 0 |
| queued | 0 |
| transcribing | 0 |
| transcribed | 4 |
| transcription-failed | 3 |
| transcript-empty | 7 |
| extracting | 1 |
| extraction-partial-some-questions | 1 |
| extraction-failed | 1 |
| complete | 1 |
| superseded-by-rerun | 0 |
| rerun-in-progress | 0 |
| deleted-by-request | 0 |

### batch-failure-mix

| value | leaves |
|---|---|
| all-succeed | 0 |
| one-video-of-session-failed | 1 |
| some-questions-failed-in-one-video | 3 |
| some-sessions-failed-in-cohort | 1 |
| all-failed | 1 |
| retry-produced-duplicate | 1 |
| late-arriving-video-after-aggregation | 0 |

### recovery-action

| value | leaves |
|---|---|
| retry-one-video | 2 |
| retry-one-question | 1 |
| rerun-whole-session | 1 |
| backfill-after-question-set-change | 0 |
| backfill-after-model-upgrade | 4 |
| skip-and-mark-unknown | 2 |
| manual-override-answer | 0 |
| delete-and-propagate | 0 |

### question-set-version-state

| value | leaves |
|---|---|
| single-version | 1 |
| mixed-versions-in-table | 0 |
| option-added | 0 |
| option-renamed-same-id | 0 |
| question-reworded-same-id | 0 |
| question-retired | 0 |
| per-game-fork | 0 |
| per-game-version-fork | 0 |
| rollback-to-old-version | 0 |

### transcription-subsystem

| value | leaves |
|---|---|
| hallucinated-text-on-silence-or-music | 3 |
| wrong-language-detected | 2 |
| language-flips-between-videos | 0 |
| truncated-at-length-limit | 1 |
| timestamps-reset-per-video | 2 |
| sentence-cut-at-15min-boundary | 0 |
| transcription-model-version-differs-across-videos | 2 |
| profanity-masked-by-vendor | 3 |
| game-lyrics-or-npc-voice-transcribed-as-player | 3 |
| low-confidence-segments-dropped-silently | 7 |
| empty-transcript-for-non-empty-video | 4 |

### chatbot-response-behaviour

| value | leaves |
|---|---|
| answers-correctly | 0 |
| says-no-data-correctly | 0 |
| substitutes-nearest-fixed-question | 0 |
| answers-from-general-game-knowledge | 0 |
| invents-number | 1 |
| silently-truncates-rows | 0 |
| differs-on-re-ask | 2 |
| answers-in-wrong-tenant-scope | 0 |
| times-out | 0 |
| refuses-answerable-question | 0 |
| mixes-null-with-no | 0 |

### fast-path-dependency

| value | leaves |
|---|---|
| precomputed-aggregate-exists | 0 |
| table-fits-in-llm-context | 0 |
| text-to-sql-generated-correctly | 0 |
| index-on-game-target-and-version | 0 |
| cache-hit | 0 |
| cache-stale-after-rerun | 0 |
| question-requires-raw-transcript-fallback | 0 |
| concurrent-studio-load | 0 |
| table-growth-over-a-year | 0 |
| cold-start | 0 |

### capture-integrity

| value | leaves |
|---|---|
| audio-and-video-ok | 6 |
| video-black-or-frozen | 0 |
| wrong-window-captured | 0 |
| no-audio-track | 2 |
| mic-muted-for-a-period | 2 |
| stereo-channel-only-game-audio | 1 |
| codec-unreadable | 0 |
| clock-drift-between-videos | 1 |
| upload-truncated | 1 |

### answer-afterlife

| value | leaves |
|---|---|
| read-once-in-chat | 0 |
| copied-into-deck | 2 |
| exported-csv | 0 |
| shared-link | 0 |
| re-asked-after-rerun | 1 |
| acted-on-tutorial-changed | 0 |
| disputed-by-studio | 0 |
| cited-after-player-deletion | 0 |

### tenancy

| value | leaves |
|---|---|
| one-studio-one-game | 0 |
| one-studio-many-games | 0 |
| many-studios-shared-infra | 3 |
| cross-studio-benchmark-request | 0 |
| studio-offboarded | 0 |


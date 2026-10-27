# G-counts-4 (bucket 4, gaps run)

| metric | count |
|---|---|
| in | 174 |
| rejected | 0 |
| clusters (duplicate groups) | 35 |
| absorbed into a survivor (listed in `absorbed`, perspectives in `also_from`) | 53 |
| variants (survivors carrying `variants_of`) | 61 |
| contested | 0 (gaps run; refusal rows do not apply) |
| surviving | 121 |
| uncategorised | 0 |
| leaves with cell values added by normalisation | 96 of 121 (272 values added) |

Normalisation method: a survivor's `cell` is the agent's own labels, plus the labels of the duplicates it absorbed (same situation), plus any C-axes value its title/object/situation/consequence text plainly states (word-bounded patterns on numbers and status words, e.g. "of 500" -> `500-players`, "queued" -> `queued`, "crash" -> `session-split-by-crash-into-two`; `proposed` text is never used). `stage` and `data-element` are NOT inferred from text, because every noun a situation mentions is not a value it plainly satisfies; those two axes carry agent labels only. Each automatic addition was reviewed by hand and 41 false positives removed before counting. Where an axis has several values on one leaf, the leaf is counted once under each value.

## Rejected

None. Every item is labelled L3/L4, names a concrete spec object or pipeline element (quoted spec sentence, answers-table row/column, question/option id, session/video id, chatbot reply), has a precise situation and consequence, and contains no prose outside the schema. Banned-vocabulary scan over title/object/situation/consequence/proposed/evidence: one hit, `eval-21` evidence field quoting the spec verbatim ("The owner wants to improve ... (b)"), which is artifact text, not the item's own wording; every "e.g." is followed by a specific instance on the same line. Nothing rejected.

## Clusters (survivor <- absorbed)

- ops-2 <- chat-2, auditor-20, pipe-8
- ds-1 <- cost-21
- qauthor-8 <- pipe-26
- ops-5 <- chat-33, pipe-4, eval-30
- pipe-6 <- ops-26, ds-24, auditor-13, extract-19, qauthor-6
- ds-7 <- qauthor-7
- auditor-14 <- extract-41
- ops-25 <- ds-38, qauthor-33
- sec-17 <- onboard-6
- qauthor-9 <- onboard-23
- onboard-7 <- sec-19
- qauthor-10 <- onboard-19, pipe-37
- auditor-4 <- design-9, analyst-9
- moderator-1 <- ds-27
- chat-12 <- auditor-27
- moderator-3 <- onboard-34, exec-32
- privacy-22 <- player-24
- onboard-22 <- stitch-29
- privacy-2 <- chat-34, player-2
- privacy-1 <- pipe-40
- auditor-11 <- ds-32
- privacy-32 <- player-32
- privacy-8 <- onboard-31, player-20, cost-34
- privacy-7 <- player-18
- ops-34 <- skeptic-14
- stitch-14 <- design-23, pipe-14, moderator-8
- ds-15 <- pipe-41
- pipe-9 <- stitch-18
- design-2 <- stitch-30
- stitch-6 <- pipe-11
- ops-22 <- skeptic-13
- qauthor-1 <- skeptic-32
- onboard-4 <- skeptic-15, exec-30
- uxr-34 <- qauthor-27
- ds-26 <- qauthor-23

## Variants (kept, `variants_of`)

- ds-1 -> ops-2
- ds-8 -> pipe-25
- design-2 -> pipe-9
- ops-41 -> pipe-30
- eval-14 -> ops-2
- qauthor-8 -> ops-2
- stitch-22 -> ops-2
- cost-26 -> onboard-1
- l10n-8 -> sec-17
- pipe-25 -> ds-7, pipe-6
- eval-21 -> ds-7
- eval-23 -> eval-1
- qauthor-25 -> eval-1
- auditor-16 -> qauthor-10
- design-8 -> pipe-6, qauthor-10
- design-12 -> ds-13
- design-25 -> onboard-4
- percep-15 -> uxr-25
- eval-9 -> eval-1
- qauthor-9 -> sec-17
- qauthor-13 -> uxr-25
- qauthor-19 -> percep-22
- qauthor-35 -> eval-33
- uxr-14 -> ds-13
- uxr-28 -> onboard-4
- onboard-12 -> moderator-1
- onboard-22 -> privacy-22
- percep-3 -> chat-12
- percep-21 -> percep-3
- pipe-13 -> uxr-25
- privacy-23 -> onboard-22
- eval-37 -> ds-13
- moderator-17 -> chat-12
- moderator-18 -> ds-26
- exec-15 -> auditor-4
- uxr-13 -> ds-13
- auditor-12 -> privacy-2
- auditor-23 -> privacy-8
- auditor-24 -> ops-34
- l10n-24 -> privacy-2
- ops-16 -> privacy-1
- privacy-2 -> privacy-1
- eval-38 -> privacy-1
- player-1 -> privacy-1
- player-5 -> stitch-37
- player-23 -> privacy-1, cost-8
- sec-30 -> privacy-8
- stitch-37 -> privacy-1
- skeptic-31 -> privacy-1
- speech-30 -> privacy-1
- ds-15 -> stitch-14
- auditor-26 -> pipe-9
- extract-43 -> stitch-14
- ops-28 -> stitch-14
- privacy-32 -> privacy-1
- eval-28 -> sec-11
- eval-29 -> stitch-20
- sec-11 -> stitch-1
- stitch-19 -> pipe-9
- speech-12 -> moderator-29, stitch-6
- exec-23 -> stitch-14

## Leaves per perspective

| perspective | in | absorbed | surviving |
|---|---|---|---|
| analyst | 1 | 1 | 0 |
| auditor | 13 | 3 | 10 |
| chat | 4 | 3 | 1 |
| cost | 4 | 2 | 2 |
| design | 7 | 2 | 5 |
| ds | 10 | 4 | 6 |
| eval | 12 | 1 | 11 |
| exec | 4 | 2 | 2 |
| extract | 4 | 2 | 2 |
| l10n | 3 | 0 | 3 |
| moderator | 8 | 1 | 7 |
| onboard | 10 | 5 | 5 |
| ops | 9 | 1 | 8 |
| percep | 5 | 0 | 5 |
| pipe | 13 | 8 | 5 |
| player | 9 | 5 | 4 |
| privacy | 8 | 0 | 8 |
| qauthor | 17 | 5 | 12 |
| sec | 5 | 1 | 4 |
| skeptic | 8 | 4 | 4 |
| speech | 4 | 0 | 4 |
| stitch | 10 | 3 | 7 |
| uxr | 6 | 0 | 6 |

## Counts per axis value (normalised cells; a leaf may carry several values per axis)

### stage (leaves with no value on this axis: 0)

| value | leaves |
|---|---|
| video-capture | 0 |
| 15-minute-split | 0 |
| session-stitching | 18 |
| transcription | 0 |
| fixed-question-set | 26 |
| answer-options | 0 |
| per-video-answers | 0 |
| session-level-aggregation | 0 |
| answers-table | 22 |
| chatbot-query-planning | 0 |
| chatbot-answer | 0 |
| evidence-display | 0 |
| studio-ui | 0 |
| recruitment-and-consent | 0 |
| build-and-metadata-tagging | 20 |
| upload-and-ingest | 0 |
| audio-extraction | 0 |
| language-detection | 0 |
| question-set-registry | 23 |
| extraction-prompt | 0 |
| job-orchestration-and-status | 0 |
| rerun-and-backfill | 0 |
| aggregate-cache | 0 |
| access-control | 0 |
| retention-and-deletion | 19 |
| export-and-share | 0 |
| studio-feedback-loop | 0 |

### data-element (leaves with no value on this axis: 18)

| value | leaves |
|---|---|
| session | 8 |
| video | 2 |
| transcript | 4 |
| utterance | 4 |
| timestamp | 9 |
| question | 7 |
| option | 4 |
| answer | 1 |
| player | 7 |
| cohort | 2 |
| game-version | 5 |
| game-target | 10 |
| tutorial-step | 7 |
| screen-state | 0 |
| build-id | 3 |
| device-platform | 5 |
| moderator | 2 |
| consent-record | 2 |
| question-set-version | 7 |
| prompt-version | 1 |
| extraction-model-version | 1 |
| transcription-model-version | 0 |
| extraction-run-id | 1 |
| answer-confidence | 2 |
| evidence-span | 4 |
| null-vs-no | 5 |
| studio-tenant | 3 |
| chatbot-conversation-log | 3 |
| cached-aggregate | 4 |

### session-shape (leaves with no value on this axis: 88)

| value | leaves |
|---|---|
| one-video | 1 |
| 2-4-videos | 3 |
| 5-20-videos | 8 |
| missing-middle-video | 0 |
| videos-out-of-order | 3 |
| overlapping-videos | 2 |
| session-ends-mid-sentence | 2 |
| zero-videos-session-failed | 1 |
| last-video-under-1-minute | 0 |
| duplicate-upload | 2 |
| video-with-no-audio-track | 0 |
| session-split-by-crash-into-two | 7 |
| same-player-multiple-sessions | 7 |
| tutorial-started-before-recording | 1 |
| 10-plus-hour-session | 2 |

### speech-shape (leaves with no value on this axis: 108)

| value | leaves |
|---|---|
| silent-player | 4 |
| continuous-think-aloud | 3 |
| game-audio-dominates | 0 |
| two-speakers | 2 |
| non-english | 3 |
| mixed-language | 0 |
| profanity-or-slang | 1 |
| inaudible-segments | 0 |
| moderator-speaking-or-leading | 2 |
| player-reading-chat-or-overlay-aloud | 0 |
| background-tv-or-other-people | 1 |
| whispering | 0 |
| mic-muted-for-a-period | 0 |
| emotional-nonverbal-only (sighs, laughs, swearing-masked) | 0 |

### question-shape (leaves with no value on this axis: 79)

| value | leaves |
|---|---|
| fits-an-option | 1 |
| fits-no-option | 1 |
| fits-two-options | 3 |
| answer-spans-videos | 1 |
| answer-is-a-count | 1 |
| answer-is-a-time | 5 |
| answer-is-a-why | 7 |
| answer-needs-visuals | 5 |
| question-not-in-set | 11 |
| event-did-not-happen-in-this-video | 10 |
| answer-changes-within-video | 0 |
| answer-depends-on-prior-video | 2 |
| negation-player-never-did-x | 4 |
| unknowable-from-audio | 5 |
| two-options-both-partly-true | 1 |
| perceptual-cause-not-verbalised | 0 |

### studio-question-type (leaves with no value on this axis: 49)

| value | leaves |
|---|---|
| one-player-what-happened | 1 |
| cohort-count | 19 |
| cohort-why | 7 |
| compare-two-versions | 11 |
| compare-two-steps | 4 |
| find-players-who | 3 |
| timeline-of-one-player | 5 |
| quote-me-evidence | 3 |
| follow-up-question | 0 |
| question-outside-game-target | 3 |
| trend-over-time | 5 |
| distribution-not-count | 2 |
| segment-by-metadata (device, country, build) | 6 |
| what-can-you-answer | 2 |
| recommendation-what-should-we-change | 1 |
| cross-game-or-cross-studio-benchmark | 2 |
| show-me-raw-transcript-or-clip | 3 |
| correction-that-is-wrong | 0 |
| question-about-a-step-the-set-never-asked | 7 |

### scale (leaves with no value on this axis: 61)

| value | leaves |
|---|---|
| 1-player | 1 |
| 50-players | 6 |
| 500-players | 43 |
| 5000-players | 2 |
| 10-games-at-once | 3 |
| 0-players-new-game | 5 |
| 1-player-10-hour-session | 3 |
| 50000-videos | 2 |
| many-concurrent-studio-users | 1 |
| question-set-of-50-questions | 0 |
| 500-players-x-3-question-set-versions | 3 |

### correctness-failure (leaves with no value on this axis: 52)

| value | leaves |
|---|---|
| hallucinated-answer | 10 |
| forced-choice-bias | 5 |
| inconsistent-across-videos | 3 |
| stale-after-prompt-change | 3 |
| wrong-denominator | 11 |
| right-answer-wrong-player | 10 |
| confident-no-evidence | 9 |
| instruction-injected-via-transcript | 1 |
| answer-attached-to-wrong-video-index | 3 |
| duplicate-counted | 6 |
| null-treated-as-no | 4 |
| other-option-overused | 3 |
| mixed-version-aggregation | 11 |
| perceptual-cause-attributed-to-verbal-option | 2 |
| moderator-words-attributed-to-player | 2 |
| transcription-hallucination-propagated | 0 |

### time-and-change (leaves with no value on this axis: 61)

| value | leaves |
|---|---|
| first-game-onboarded | 8 |
| game-update-changes-tutorial | 9 |
| question-set-revised | 11 |
| model-upgraded | 1 |
| a-year-of-data | 9 |
| studio-asks-at-3am | 0 |
| player-deletion-request | 15 |
| transcription-model-upgraded | 0 |
| rerun-in-progress-while-queried | 3 |
| studio-offboarded | 3 |
| retention-expiry | 4 |
| game-target-changes-beyond-tutorial | 7 |
| extraction-vendor-deprecates-model | 0 |

### latency (leaves with no value on this axis: 111)

| value | leaves |
|---|---|
| under-2s | 3 |
| under-30s | 2 |
| minutes | 2 |
| batch-overnight | 2 |
| first-token-vs-complete-answer | 0 |
| p99-tail-under-concurrency | 1 |
| ingest-to-queryable (hours or days after session) | 3 |
| fast-but-stale | 1 |

### processing-status (leaves with no value on this axis: 96)

| value | leaves |
|---|---|
| not-yet-uploaded | 1 |
| uploaded-partial | 0 |
| queued | 1 |
| transcribing | 0 |
| transcribed | 0 |
| transcription-failed | 1 |
| transcript-empty | 0 |
| extracting | 2 |
| extraction-partial-some-questions | 1 |
| extraction-failed | 1 |
| complete | 3 |
| superseded-by-rerun | 1 |
| rerun-in-progress | 3 |
| deleted-by-request | 13 |

### batch-failure-mix (leaves with no value on this axis: 113)

| value | leaves |
|---|---|
| all-succeed | 1 |
| one-video-of-session-failed | 1 |
| some-questions-failed-in-one-video | 1 |
| some-sessions-failed-in-cohort | 2 |
| all-failed | 0 |
| retry-produced-duplicate | 2 |
| late-arriving-video-after-aggregation | 1 |

### recovery-action (leaves with no value on this axis: 94)

| value | leaves |
|---|---|
| retry-one-video | 1 |
| retry-one-question | 0 |
| rerun-whole-session | 1 |
| backfill-after-question-set-change | 10 |
| backfill-after-model-upgrade | 2 |
| skip-and-mark-unknown | 0 |
| manual-override-answer | 0 |
| delete-and-propagate | 13 |

### question-set-version-state (leaves with no value on this axis: 97)

| value | leaves |
|---|---|
| single-version | 2 |
| mixed-versions-in-table | 5 |
| option-added | 4 |
| option-renamed-same-id | 2 |
| question-reworded-same-id | 4 |
| question-retired | 3 |
| per-game-fork | 7 |
| per-game-version-fork | 2 |
| rollback-to-old-version | 1 |

### transcription-subsystem (leaves with no value on this axis: 117)

| value | leaves |
|---|---|
| hallucinated-text-on-silence-or-music | 0 |
| wrong-language-detected | 0 |
| language-flips-between-videos | 0 |
| truncated-at-length-limit | 1 |
| timestamps-reset-per-video | 2 |
| sentence-cut-at-15min-boundary | 0 |
| transcription-model-version-differs-across-videos | 0 |
| profanity-masked-by-vendor | 0 |
| game-lyrics-or-npc-voice-transcribed-as-player | 0 |
| low-confidence-segments-dropped-silently | 1 |
| empty-transcript-for-non-empty-video | 0 |

### chatbot-response-behaviour (leaves with no value on this axis: 100)

| value | leaves |
|---|---|
| answers-correctly | 0 |
| says-no-data-correctly | 1 |
| substitutes-nearest-fixed-question | 4 |
| answers-from-general-game-knowledge | 3 |
| invents-number | 4 |
| silently-truncates-rows | 0 |
| differs-on-re-ask | 2 |
| answers-in-wrong-tenant-scope | 4 |
| times-out | 1 |
| refuses-answerable-question | 6 |
| mixes-null-with-no | 4 |

### fast-path-dependency (leaves with no value on this axis: 99)

| value | leaves |
|---|---|
| precomputed-aggregate-exists | 5 |
| table-fits-in-llm-context | 1 |
| text-to-sql-generated-correctly | 4 |
| index-on-game-target-and-version | 3 |
| cache-hit | 0 |
| cache-stale-after-rerun | 3 |
| question-requires-raw-transcript-fallback | 6 |
| concurrent-studio-load | 1 |
| table-growth-over-a-year | 2 |
| cold-start | 0 |

### capture-integrity (leaves with no value on this axis: 116)

| value | leaves |
|---|---|
| audio-and-video-ok | 0 |
| video-black-or-frozen | 0 |
| wrong-window-captured | 1 |
| no-audio-track | 0 |
| mic-muted-for-a-period | 0 |
| stereo-channel-only-game-audio | 0 |
| codec-unreadable | 0 |
| clock-drift-between-videos | 4 |
| upload-truncated | 0 |

### answer-afterlife (leaves with no value on this axis: 95)

| value | leaves |
|---|---|
| read-once-in-chat | 0 |
| copied-into-deck | 11 |
| exported-csv | 2 |
| shared-link | 1 |
| re-asked-after-rerun | 3 |
| acted-on-tutorial-changed | 8 |
| disputed-by-studio | 2 |
| cited-after-player-deletion | 6 |

### tenancy (leaves with no value on this axis: 108)

| value | leaves |
|---|---|
| one-studio-one-game | 0 |
| one-studio-many-games | 5 |
| many-studios-shared-infra | 7 |
| cross-studio-benchmark-request | 2 |
| studio-offboarded | 3 |


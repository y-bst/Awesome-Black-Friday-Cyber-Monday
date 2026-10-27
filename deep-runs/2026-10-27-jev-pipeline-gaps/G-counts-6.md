# G-counts-6: bucket 6 merge counts

| metric | count |
|---|---|
| in (bucket leaves) | 28 |
| rejected | 0 |
| duplicate clusters | 3 (absorbed 3 leaves) |
| variants (leaves tagged variants_of) | 8 |
| contested (refusal collisions; ideate only) | 0 (n/a, gaps run) |
| surviving | 25 |
| uncategorised | 0 |
| leaves with cell values added by normalisation | 16 (22 values) |

## Rejected

None. Checked: every leaf is L3 or L4, names a concrete object (spec sentence, stage or data element), and the banned-vocabulary scan (improve, ensure, consider, robust, handle, proper, appropriate, various, etc., such as, and so on, best practices, edge cases, user-friendly, seamless) found 0 hits.

## Duplicate clusters

| survivor | absorbed | also_from | same situation on the same object |
|---|---|---|---|
| pipe-1 | speech-4 | speech | churn-reason sentence straddles the 15:00 cut ('I quit because the second | tutorial popup...' / 'I'm going to quit because | the controls are awful'); each half answered alone, reason never recovered |
| stitch-7 | extract-27 | extract | conditional quit-intent clause straddles the 15:00 cut ('I'm going to quit- | the tutorial if this doesn't load'); video 3 marked Yes on half the sentence |
| design-4 | skeptic-36 | skeptic | player quits 40 s into a last video under 1 minute; the quit-reason question sees 6-100 words with no lead-up |

## Variants (kept, cross-linked)

| leaf | variants_of | same mechanism, different part or scope |
|---|---|---|
| stitch-7 | pipe-1 | utterance straddles cut: quit-intent yes/no question instead of why-reason question |
| percep-24 | pipe-1 | event straddles cut: visual cue before / reaction after, answer attached to wrong video index |
| ds-29 | pipe-1 | event straddles cut: count question, event counted twice or zero |
| exec-9 | privacy-18 | shared link without expiry or revocation: conversation link after studio offboarding instead of clip link after player deletion |
| exec-8 | auditor-10 | CSV export missing columns: confidence and null-vs-No instead of version/run columns |
| sec-14 | privacy-16 | raw player_id in CSV: cross-tenant join instead of small-cell re-identification |
| player-15 | privacy-16 | identifying metadata on studio-facing output: evidence quote pasted into a deck instead of CSV rows |
| percep-37 | percep-12 | insufficient contrast: dark-mode evidence highlight instead of confidence caveat |

## Cell normalisation (values added)

| leaf | added |
|---|---|
| ds-29 | scale: 1-player-10-hour-session |
| design-4 | question-shape: answer-is-a-why, processing-status: transcript-empty |
| percep-24 | studio-question-type: timeline-of-one-player, data-element: video |
| pipe-1 | correctness-failure: other-option-overused |
| stitch-7 | data-element: utterance |
| uxr-17 | studio-question-type: cohort-count |
| auditor-9 | processing-status: superseded-by-rerun, chatbot-response-behaviour: differs-on-re-ask |
| auditor-10 | question-set-version-state: option-added, scale: 500-players |
| privacy-18 | time-and-change: player-deletion-request, studio-question-type: show-me-raw-transcript-or-clip |
| player-3 | scale: 500-players, recovery-action: delete-and-propagate |
| exec-8 | scale: 500-players |
| exec-9 | studio-question-type: quote-me-evidence |
| percep-12 | scale: 500-players |
| percep-13 | answer-afterlife: read-once-in-chat |
| privacy-34 | scale: 1-player |
| analyst-21 | data-element: player |

## Leaves per perspective (id prefix -> E file)

| perspective | E file | in | surviving |
|---|---|---|---|
| analyst | E-studio-analyst.yaml | 2 | 2 |
| auditor | E-decision-consumer-auditor.yaml | 2 | 2 |
| design | E-game-designer.yaml | 2 | 2 |
| ds | E-data-scientist.yaml | 1 | 1 |
| exec | E-studio-exec.yaml | 2 | 2 |
| extract | E-llm-extraction-engineer.yaml | 1 | 0 |
| l10n | E-localisation-owner.yaml | 2 | 2 |
| percep | E-perception-and-accessibility-reviewer.yaml | 5 | 5 |
| pipe | E-pipeline-engineer.yaml | 1 | 1 |
| player | E-recorded-player.yaml | 2 | 2 |
| privacy | E-privacy-counsel.yaml | 3 | 3 |
| sec | E-security-and-tenancy-engineer.yaml | 1 | 1 |
| skeptic | E-skeptic-of-structure.yaml | 1 | 0 |
| speech | E-speech-and-audio-engineer.yaml | 1 | 0 |
| stitch | E-session-stitching-engineer.yaml | 1 | 1 |
| uxr | E-ux-researcher.yaml | 1 | 1 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### stage (25 leaves carry a value)

| value | count |
|---|---|
| video-capture | 0 |
| 15-minute-split | 7 |
| session-stitching | 0 |
| transcription | 0 |
| fixed-question-set | 0 |
| answer-options | 0 |
| per-video-answers | 0 |
| session-level-aggregation | 0 |
| answers-table | 0 |
| chatbot-query-planning | 0 |
| chatbot-answer | 0 |
| evidence-display | 0 |
| studio-ui | 9 |
| recruitment-and-consent | 0 |
| build-and-metadata-tagging | 0 |
| upload-and-ingest | 0 |
| audio-extraction | 0 |
| language-detection | 0 |
| question-set-registry | 0 |
| extraction-prompt | 0 |
| job-orchestration-and-status | 0 |
| rerun-and-backfill | 0 |
| aggregate-cache | 0 |
| access-control | 0 |
| retention-and-deletion | 0 |
| export-and-share | 9 |
| studio-feedback-loop | 0 |

### data-element (25 leaves carry a value)

| value | count |
|---|---|
| session | 0 |
| video | 4 |
| transcript | 0 |
| utterance | 2 |
| timestamp | 1 |
| question | 0 |
| option | 0 |
| answer | 1 |
| player | 4 |
| cohort | 2 |
| game-version | 0 |
| game-target | 1 |
| tutorial-step | 0 |
| screen-state | 0 |
| build-id | 0 |
| device-platform | 0 |
| moderator | 0 |
| consent-record | 0 |
| question-set-version | 1 |
| prompt-version | 1 |
| extraction-model-version | 0 |
| transcription-model-version | 0 |
| extraction-run-id | 0 |
| answer-confidence | 2 |
| evidence-span | 4 |
| null-vs-no | 0 |
| studio-tenant | 0 |
| chatbot-conversation-log | 2 |
| cached-aggregate | 0 |

### session-shape (8 leaves carry a value)

| value | count |
|---|---|
| one-video | 0 |
| 2-4-videos | 2 |
| 5-20-videos | 2 |
| missing-middle-video | 0 |
| videos-out-of-order | 0 |
| overlapping-videos | 0 |
| session-ends-mid-sentence | 1 |
| zero-videos-session-failed | 0 |
| last-video-under-1-minute | 1 |
| duplicate-upload | 0 |
| video-with-no-audio-track | 0 |
| session-split-by-crash-into-two | 0 |
| same-player-multiple-sessions | 1 |
| tutorial-started-before-recording | 0 |
| 10-plus-hour-session | 1 |

### speech-shape (3 leaves carry a value)

| value | count |
|---|---|
| silent-player | 0 |
| continuous-think-aloud | 0 |
| game-audio-dominates | 0 |
| two-speakers | 0 |
| non-english | 2 |
| mixed-language | 0 |
| profanity-or-slang | 1 |
| inaudible-segments | 0 |
| moderator-speaking-or-leading | 0 |
| player-reading-chat-or-overlay-aloud | 0 |
| background-tv-or-other-people | 0 |
| whispering | 0 |
| mic-muted-for-a-period | 0 |
| emotional-nonverbal-only (sighs, laughs, swearing-masked) | 0 |

### question-shape (7 leaves carry a value)

| value | count |
|---|---|
| fits-an-option | 0 |
| fits-no-option | 0 |
| fits-two-options | 0 |
| answer-spans-videos | 1 |
| answer-is-a-count | 2 |
| answer-is-a-time | 0 |
| answer-is-a-why | 2 |
| answer-needs-visuals | 0 |
| question-not-in-set | 0 |
| event-did-not-happen-in-this-video | 0 |
| answer-changes-within-video | 0 |
| answer-depends-on-prior-video | 2 |
| negation-player-never-did-x | 0 |
| unknowable-from-audio | 0 |
| two-options-both-partly-true | 0 |
| perceptual-cause-not-verbalised | 0 |

### studio-question-type (14 leaves carry a value)

| value | count |
|---|---|
| one-player-what-happened | 0 |
| cohort-count | 2 |
| cohort-why | 0 |
| compare-two-versions | 0 |
| compare-two-steps | 0 |
| find-players-who | 2 |
| timeline-of-one-player | 1 |
| quote-me-evidence | 4 |
| follow-up-question | 0 |
| question-outside-game-target | 0 |
| trend-over-time | 0 |
| distribution-not-count | 1 |
| segment-by-metadata (device, country, build) | 0 |
| what-can-you-answer | 2 |
| recommendation-what-should-we-change | 0 |
| cross-game-or-cross-studio-benchmark | 0 |
| show-me-raw-transcript-or-clip | 2 |
| correction-that-is-wrong | 0 |
| question-about-a-step-the-set-never-asked | 0 |

### scale (9 leaves carry a value)

| value | count |
|---|---|
| 1-player | 1 |
| 50-players | 0 |
| 500-players | 6 |
| 5000-players | 0 |
| 10-games-at-once | 0 |
| 0-players-new-game | 0 |
| 1-player-10-hour-session | 1 |
| 50000-videos | 0 |
| many-concurrent-studio-users | 1 |
| question-set-of-50-questions | 0 |
| 500-players-x-3-question-set-versions | 0 |

### correctness-failure (8 leaves carry a value)

| value | count |
|---|---|
| hallucinated-answer | 2 |
| forced-choice-bias | 0 |
| inconsistent-across-videos | 1 |
| stale-after-prompt-change | 0 |
| wrong-denominator | 0 |
| right-answer-wrong-player | 0 |
| confident-no-evidence | 0 |
| instruction-injected-via-transcript | 0 |
| answer-attached-to-wrong-video-index | 1 |
| duplicate-counted | 1 |
| null-treated-as-no | 1 |
| other-option-overused | 1 |
| mixed-version-aggregation | 1 |
| perceptual-cause-attributed-to-verbal-option | 0 |
| moderator-words-attributed-to-player | 0 |
| transcription-hallucination-propagated | 0 |

### time-and-change (5 leaves carry a value)

| value | count |
|---|---|
| first-game-onboarded | 0 |
| game-update-changes-tutorial | 0 |
| question-set-revised | 1 |
| model-upgraded | 0 |
| a-year-of-data | 0 |
| studio-asks-at-3am | 0 |
| player-deletion-request | 2 |
| transcription-model-upgraded | 0 |
| rerun-in-progress-while-queried | 0 |
| studio-offboarded | 1 |
| retention-expiry | 0 |
| game-target-changes-beyond-tutorial | 1 |
| extraction-vendor-deprecates-model | 0 |

### latency (2 leaves carry a value)

| value | count |
|---|---|
| under-2s | 1 |
| under-30s | 0 |
| minutes | 0 |
| batch-overnight | 0 |
| first-token-vs-complete-answer | 0 |
| p99-tail-under-concurrency | 0 |
| ingest-to-queryable (hours or days after session) | 0 |
| fast-but-stale | 1 |

### processing-status (2 leaves carry a value)

| value | count |
|---|---|
| not-yet-uploaded | 0 |
| uploaded-partial | 0 |
| queued | 0 |
| transcribing | 0 |
| transcribed | 0 |
| transcription-failed | 0 |
| transcript-empty | 1 |
| extracting | 0 |
| extraction-partial-some-questions | 0 |
| extraction-failed | 0 |
| complete | 0 |
| superseded-by-rerun | 1 |
| rerun-in-progress | 0 |
| deleted-by-request | 0 |

### batch-failure-mix (0 leaves carry a value)

| value | count |
|---|---|
| all-succeed | 0 |
| one-video-of-session-failed | 0 |
| some-questions-failed-in-one-video | 0 |
| some-sessions-failed-in-cohort | 0 |
| all-failed | 0 |
| retry-produced-duplicate | 0 |
| late-arriving-video-after-aggregation | 0 |

### recovery-action (1 leaves carry a value)

| value | count |
|---|---|
| retry-one-video | 0 |
| retry-one-question | 0 |
| rerun-whole-session | 0 |
| backfill-after-question-set-change | 0 |
| backfill-after-model-upgrade | 0 |
| skip-and-mark-unknown | 0 |
| manual-override-answer | 0 |
| delete-and-propagate | 1 |

### question-set-version-state (1 leaves carry a value)

| value | count |
|---|---|
| single-version | 0 |
| mixed-versions-in-table | 0 |
| option-added | 1 |
| option-renamed-same-id | 0 |
| question-reworded-same-id | 0 |
| question-retired | 0 |
| per-game-fork | 0 |
| per-game-version-fork | 0 |
| rollback-to-old-version | 0 |

### transcription-subsystem (5 leaves carry a value)

| value | count |
|---|---|
| hallucinated-text-on-silence-or-music | 0 |
| wrong-language-detected | 0 |
| language-flips-between-videos | 0 |
| truncated-at-length-limit | 0 |
| timestamps-reset-per-video | 0 |
| sentence-cut-at-15min-boundary | 4 |
| transcription-model-version-differs-across-videos | 0 |
| profanity-masked-by-vendor | 0 |
| game-lyrics-or-npc-voice-transcribed-as-player | 0 |
| low-confidence-segments-dropped-silently | 0 |
| empty-transcript-for-non-empty-video | 1 |

### chatbot-response-behaviour (7 leaves carry a value)

| value | count |
|---|---|
| answers-correctly | 2 |
| says-no-data-correctly | 1 |
| substitutes-nearest-fixed-question | 0 |
| answers-from-general-game-knowledge | 0 |
| invents-number | 0 |
| silently-truncates-rows | 2 |
| differs-on-re-ask | 1 |
| answers-in-wrong-tenant-scope | 0 |
| times-out | 0 |
| refuses-answerable-question | 1 |
| mixes-null-with-no | 0 |

### fast-path-dependency (1 leaves carry a value)

| value | count |
|---|---|
| precomputed-aggregate-exists | 0 |
| table-fits-in-llm-context | 0 |
| text-to-sql-generated-correctly | 0 |
| index-on-game-target-and-version | 0 |
| cache-hit | 0 |
| cache-stale-after-rerun | 1 |
| question-requires-raw-transcript-fallback | 0 |
| concurrent-studio-load | 0 |
| table-growth-over-a-year | 0 |
| cold-start | 0 |

### capture-integrity (0 leaves carry a value)

| value | count |
|---|---|
| audio-and-video-ok | 0 |
| video-black-or-frozen | 0 |
| wrong-window-captured | 0 |
| no-audio-track | 0 |
| mic-muted-for-a-period | 0 |
| stereo-channel-only-game-audio | 0 |
| codec-unreadable | 0 |
| clock-drift-between-videos | 0 |
| upload-truncated | 0 |

### answer-afterlife (15 leaves carry a value)

| value | count |
|---|---|
| read-once-in-chat | 3 |
| copied-into-deck | 2 |
| exported-csv | 6 |
| shared-link | 4 |
| re-asked-after-rerun | 0 |
| acted-on-tutorial-changed | 0 |
| disputed-by-studio | 0 |
| cited-after-player-deletion | 0 |

### tenancy (5 leaves carry a value)

| value | count |
|---|---|
| one-studio-one-game | 2 |
| one-studio-many-games | 1 |
| many-studios-shared-infra | 1 |
| cross-studio-benchmark-request | 0 |
| studio-offboarded | 1 |

uncategorised leaves: none

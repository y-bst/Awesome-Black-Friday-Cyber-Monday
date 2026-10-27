# G-counts-5: bucket 5 merge counts

| metric | count |
|---|---|
| in (bucket leaves) | 174 |
| rejected | 0 |
| duplicate clusters | 33 (absorbed 50 leaves) |
| variants (leaves tagged variants_of) | 41 |
| contested (refusal collisions; ideate only) | 0 (n/a, gaps run) |
| surviving | 124 |
| uncategorised | 0 |
| leaves with cell values added by normalisation | 78 (114 values) |

## Rejected

None. Checked all 174 leaves: every leaf is L3 or L4, names a concrete object (a spec sentence, a pipeline stage, a data element or a named row/video/clip), and states a situation an engineer or PM could act on. Banned-vocabulary scan (improve, ensure, consider, robust, handle, proper, appropriate, various, etc., such as, and so on, best practices, edge cases, user-friendly, seamless): 4 hits, all allowed - three "such as" each followed by a specific instance on the same line (pipe-10, speech-5, exec-13) and one "improve" inside a quoted spec sentence in auditor-3's evidence field. No prose, no headings. Four leaves reference a sibling leaf by id (percep-25 -> percep-5, percep-26 -> percep-14, sec-26 -> sec-1, cost-19 -> cost-7); each still names its own object and situation, so they are kept.

## Duplicate clusters

| survivor | absorbed | also_from | same situation on the same object |
|---|---|---|---|
| ops-18 | ds-31, extract-42, pipe-15, stitch-17 | ds, extract, pipe, stitch | client upload retry after a network timeout stores the same 15-minute video twice; both copies transcribed and extracted; player's counts double |
| stitch-2 | pipe-10, ops-29 | ops, pipe | video_index assigned by upload/completion order instead of recorder sequence; a late or fast video takes the wrong index and prior-video / 'first video where X' answers shift |
| chat-41 | pipe-29, exec-20 | exec, pipe | studio asks a cohort question while sessions are still mid-processing; answer is computed over the completed subset with no processed/pending count |
| ops-7 | stitch-27 | stitch | a video arrives or is repaired days after session and cohort aggregates were built; neither rollup is recomputed |
| percep-5 | pipe-22 | pipe | black or non-game capture with a normal audio track passes transcription and extraction as complete; no stage stores whether the video had usable frames |
| privacy-27 | player-25 | player | wrong window captured (desktop/browser) records personal on-screen data; game audio is normal so status is complete and nobody looks at frames |
| moderator-4 | design-3, speech-26, uxr-15 | design, speech, uxr | recording starts after tutorial steps 1-2; step-1 questions are answered No / not mentioned and counted as No, with no 'not observed' value |
| ds-30 | stitch-13 | stitch | left-truncated sessions bias step-level cohort rates low; no session field marks recording_started_at_step |
| moderator-12 | uxr-35 | uxr | moderator's consent and briefing speech at the start of video 1 is extracted as player tutorial speech and stored in the transcript |
| privacy-6 | player-9, moderator-32 | moderator, player | player consented to 30 minutes; capture runs hours; no stage compares recorded duration with consented duration, so later videos are extracted and quotable |
| player-8 | privacy-5 | privacy | consent covers research only; chatbot returns verbatim quotes/clips to the studio with no per-row consent-scope flag |
| privacy-4 | player-7 | player | no age or guardian-consent field on the player; a minor's session is processed and shown like an adult's |
| privacy-26 | player-28 | player | English-only consent form signed by a player whose session is in another language; mismatch never flagged |
| auditor-39 | moderator-2 | moderator | moderator assigns one player id to two different people; their sessions merge into one player row / list entry |
| cost-13 | ds-16, extract-33 | ds, extract | one question fails on a video; retry re-runs or re-inserts all questions and duplicate rows are written (no (video, question, version) key) |
| pipe-3 | speech-18 | speech | one video of a session fails transcription/decoding; the session has no expected_videos/coverage marker and is served as complete |
| ops-6 | pipe-38 | pipe | a game's daily ingest drops to zero after a build/SDK update; no volume alert, nothing in a failed-job queue because no jobs were created |
| chat-14 | cost-10, ds-18, auditor-29, ops-32 | auditor, cost, ds, ops | cached cohort aggregate keyed on (game, question) is not invalidated by a rerun/backfill/model upgrade; chatbot serves the pre-rerun number |
| ops-17 | pipe-31 | pipe | cached cohort aggregate still includes a player deleted by request; no cache-to-player dependency |
| analyst-2 | auditor-25, design-28, uxr-19 | auditor, design, uxr | answer row stores video id + option only; 'show me the clip / find players who' has no timestamp or utterance to seek to |
| qauthor-31 | design-29 | design | no stored utterance on the row, so a requested quote is regenerated from the transcript or option label and may never have been spoken |
| privacy-30 | exec-13 | exec | ASR hallucinates a sentence over silence; quote-me-evidence attributes it to a named player |
| sec-13 | player-16 | player | evidence link is a non-expiring direct URL to the full raw video; anyone with the link (or an incremented id) can play it |
| chat-17 | privacy-9, exec-7 | exec, privacy | studio asks a cross-studio benchmark question; the chatbot's only tenant filter is in the prompt/generated SQL and other studios' rows are in scope |
| privacy-19 | sec-31 | sec | no per-user access log of who viewed which player's clip or transcript (shared or role-less accounts) |
| chat-28 | analyst-16 | analyst | analyst asserts a wrong correction in chat; bot complies and restates a number no table query reproduces, with no write-back or dispute rule |
| auditor-3 | onboard-29, exec-16 | exec, onboard | studio finds a wrong row and there is no dispute/override path; an ad-hoc override is erased by the next rerun |
| ds-36 | qauthor-16 | qauthor | studio questions the chatbot could not answer are not logged, so coverage of the fixed set and the top unmet questions are unmeasured |
| pipe-17 | stitch-23, speech-6 | speech, stitch | language auto-detected per 15-minute video flips for one video with little player speech (silence, cutscene, loading screen); that video's transcript is garbage inside an otherwise consistent session |
| uxr-26 | design-19 | design | voiced tutorial/NPC lines in the mixed game-audio track are transcribed as the player and answered as player sentiment/frustration |
| privacy-29 | player-26 | player | other humans on in-game voice chat are captured through game audio and transcribed as the player, without consent |
| speech-10 | pipe-39 | pipe | mic muted for ~6 minutes mid-video is read as the player being silent/disengaged/'No' instead of no audio coverage |
| ds-4 | moderator-31 | moderator | recruitment source and sampling frame of the 500 players are not stored; cohort rates are quoted as population rates |

## Variants (kept, cross-linked)

| leaf | variants_of | same mechanism, different part or scope |
|---|---|---|
| auditor-33 | ops-18 | duplicate upload: the later dedup job silently moves a number already in a deck, instead of the double-count itself |
| moderator-27 | ops-18 | duplicate video from a second capture source (lab recorder + player device, different hashes) instead of a client retry |
| moderator-19 | chat-41 | partial cohort because sessions are recorded but not yet uploaded (moderator batch upload), which the pipeline cannot count on its own |
| design-31 | chat-41 | partial cohort on the new build only, used in a compare-two-versions answer; needs a completeness threshold per version |
| ops-23 | cost-25 | shared FIFO with no per-tenant priority: a 50,000-video backfill instead of a 10-game launch delays fresh sessions |
| speech-31 | ops-7 | late-arriving videos of a still-open 10-hour session instead of a failed retry; aggregate built at video 30 is served as final |
| onboard-11 | percep-5 | black capture at first-game onboarding (DRM/anti-cheat), found after 100 sessions; smoke test rather than per-video check |
| exec-31 | percep-5 | frozen (not black) picture for 6 minutes; capture bug reported to the exec as a UX finding via a why-answer |
| percep-6 | percep-5 | frozen frame (encoder stall) indistinguishable from a paused game; needs frame-difference not luminance |
| percep-25 | percep-5 | the black detector itself: game fades/loading screens vs capture failure; threshold and allowed-black duration unspecified |
| percep-7 | privacy-27 | wrong window captured: consequence is a wrong evidence clip disputed by the studio, not personal data in storage |
| ds-30 | moderator-4 | left-truncated recording at cohort scope: step-level rates biased low rather than per-player null-treated-as-no |
| eval-36 | moderator-4 | left-truncated recording at eval scope: gold set has no unknown/not-observed label |
| onboard-25 | moderator-4 | launcher/EULA/account flow before recording: time-to-first-action measured from record start, disagrees with studio telemetry |
| exec-33 | player-8 | consent scope exceeded by a quote with player id in an investor deck (duration and purpose both exceeded) |
| moderator-25 | privacy-4 | minor's age is on the moderator's paper form and never reaches the session record; quote and CSV export unblocked |
| onboard-30 | privacy-4 | studio-sourced Discord testers include minors and the studio consent names no third-party chatbot; onboarding checklist scope |
| exec-12 | onboard-10 | moderator's leading line credited to the player in the quote-me-evidence path instead of in the extraction answer |
| pipe-24 | cost-13 | partial question failure committed as complete: missing rows read as No; retry granularity is whole video or nothing (status, not duplicates) |
| exec-10 | ops-17 | deleted player survives in stored chat conversations and deck exports as well as the cache |
| cost-24 | ops-17 | deletion invalidates 42 cached aggregates; no rebuild-vs-subtract rule (cost of propagation) |
| privacy-33 | ops-17 | deletion changes a number already in a deck; answers carry no table version or tombstone count to explain it |
| qauthor-31 | analyst-2 | missing evidence span produces a fabricated quote (regenerated from transcript/option label) instead of a missing clip |
| speech-29 | privacy-30 | quoted line is a mis-transcription of inaudible speech rather than a hallucination over silence |
| player-12 | privacy-30 | quoted line is invented by wrong-language decoding of mixed-language speech |
| onboard-17 | chat-17 | cross-tenant exposure on a sales demo with another studio's sample data loaded into the same bot |
| sec-6 | chat-17 | tenant filter bypassed by direct prompt injection ("ignore the studio filter") instead of a benchmark question |
| skeptic-30 | chat-17 | tenant leak through a shared transcript index used by the raw-text fallback instead of the answers table |
| eval-25 | auditor-3 | dispute handling at eval scope: confirmed corrections never reach the gold set, unconfirmed ones poison the table |
| speech-27 | pipe-17 | detection picks the game voice-over's language for the whole session (70% game audio) rather than flipping on one video |
| l10n-2 | pipe-17 | player genuinely switches language between videos; per-video detection yields two option-language contexts in one session |
| moderator-11 | pipe-17 | first video detected as the moderator's language because of setup talk; remaining videos as the player's |
| moderator-23 | pipe-17 | bilingual moderator translating every instruction flips detection every ~40 s within one video |
| l10n-7 | pipe-17 | last video under 1 minute has too few words to detect; wrong language stored as complete on the quit moment |
| onboard-9 | l10n-26 | no language check at first-game onboarding (Japanese studio, English-only question set); acceptance-test scope |
| ds-33 | l10n-26 | lower non-English accuracy makes segment-by-country answers measure extractor accuracy; no language column to stratify |
| eval-18 | l10n-26 | no gold labels per language, so non-English accuracy is assumed equal to English |
| exec-19 | l10n-26 | exec's cohort headline silently covers English-speaking sessions only; answer should state language mix |
| privacy-29 | uxr-26 | voice-chat humans (not NPC lines) transcribed as the player through the mixed game-audio track; consent consequence |
| ops-20 | pipe-21 | unreadable codec labelled transcript-empty (not transcription-failed), so no retry and it reads as a silent player |
| ops-38 | pipe-21 | whole-day no-audio-track (mic unplugged): needs a per-game empty-transcript rate alert, not a per-video status |

## Cell normalisation (values added)

Rule applied: one value per axis (the leaf schema is a map); values were added only for axes the leaf had not set and only when the situation (or, for a survivor, the situations it absorbed) plainly satisfies the value. Existing values were not changed.

| leaf | added |
|---|---|
| cost-25 | processing-status: queued |
| auditor-33 | data-element: video, studio-question-type: cohort-count, chatbot-response-behaviour: differs-on-re-ask |
| onboard-2 | session-shape: 5-20-videos, data-element: session |
| percep-6 | studio-question-type: show-me-raw-transcript-or-clip, question-shape: answer-needs-visuals |
| ops-6 | data-element: build-id, batch-failure-mix: all-failed, studio-question-type: compare-two-versions |
| ops-18 | data-element: video, recovery-action: retry-one-video, processing-status: complete |
| ops-19 | data-element: video |
| privacy-31 | capture-integrity: codec-unreadable, time-and-change: retention-expiry |
| moderator-7 | session-shape: 5-20-videos |
| moderator-19 | studio-question-type: cohort-count, correctness-failure: wrong-denominator, processing-status: not-yet-uploaded |
| moderator-30 | session-shape: 5-20-videos |
| stitch-2 | recovery-action: retry-one-video, studio-question-type: timeline-of-one-player |
| stitch-35 | transcription-subsystem: empty-transcript-for-non-empty-video |
| cost-23 | chatbot-response-behaviour: times-out |
| percep-9 | question-shape: answer-needs-visuals |
| percep-33 | session-shape: 5-20-videos |
| percep-38 | session-shape: 5-20-videos, studio-question-type: show-me-raw-transcript-or-clip |
| privacy-30 | data-element: utterance |
| speech-29 | data-element: utterance |
| analyst-2 | answer-afterlife: disputed-by-studio |
| ds-30 | scale: 500-players |
| onboard-11 | batch-failure-mix: all-succeed |
| percep-5 | data-element: screen-state, session-shape: 5-20-videos |
| percep-7 | question-shape: answer-needs-visuals |
| percep-8 | question-shape: answer-needs-visuals, scale: 500-players |
| percep-23 | question-shape: answer-needs-visuals |
| percep-31 | data-element: screen-state |
| privacy-12 | studio-question-type: quote-me-evidence |
| privacy-27 | processing-status: complete |
| moderator-4 | studio-question-type: compare-two-steps |
| exec-31 | data-element: screen-state |
| ds-4 | correctness-failure: wrong-denominator |
| auditor-39 | answer-afterlife: copied-into-deck |
| onboard-25 | time-and-change: first-game-onboarded |
| moderator-6 | time-and-change: game-update-changes-tutorial |
| moderator-26 | time-and-change: game-update-changes-tutorial, scale: 500-players |
| exec-33 | session-shape: 5-20-videos |
| chat-41 | chatbot-response-behaviour: differs-on-re-ask, data-element: session |
| cost-13 | processing-status: extraction-partial-some-questions |
| cost-31 | processing-status: transcription-failed |
| cost-32 | question-shape: answer-is-a-why |
| auditor-28 | chatbot-response-behaviour: differs-on-re-ask |
| percep-36 | data-element: screen-state |
| pipe-3 | session-shape: 5-20-videos, studio-question-type: cohort-count, scale: 500-players |
| pipe-24 | correctness-failure: null-treated-as-no |
| ops-9 | scale: 500-players, correctness-failure: wrong-denominator |
| ops-23 | processing-status: queued |
| ops-35 | data-element: studio-tenant |
| ops-42 | session-shape: 5-20-videos |
| moderator-20 | session-shape: one-video, studio-question-type: cohort-count |
| stitch-5 | scale: 500-players, data-element: session |
| speech-31 | scale: 1-player-10-hour-session, data-element: session |
| l10n-2 | data-element: transcript |
| l10n-7 | question-shape: answer-is-a-why |
| l10n-26 | correctness-failure: other-option-overused, data-element: transcript |
| onboard-9 | time-and-change: first-game-onboarded, session-shape: 5-20-videos |
| pipe-17 | correctness-failure: inconsistent-across-videos |
| player-12 | data-element: utterance |
| moderator-11 | session-shape: 5-20-videos |
| chat-14 | chatbot-response-behaviour: differs-on-re-ask, batch-failure-mix: some-sessions-failed-in-cohort, scale: 500-players, time-and-change: rerun-in-progress-while-queried |
| cost-24 | fast-path-dependency: precomputed-aggregate-exists, answer-afterlife: cited-after-player-deletion |
| cost-27 | question-set-version-state: mixed-versions-in-table |
| ops-7 | recovery-action: retry-one-video, data-element: cached-aggregate, chatbot-response-behaviour: differs-on-re-ask |
| ops-17 | time-and-change: player-deletion-request, recovery-action: delete-and-propagate, scale: 500-players |
| privacy-33 | chatbot-response-behaviour: differs-on-re-ask |
| sec-10 | chatbot-response-behaviour: answers-in-wrong-tenant-scope |
| skeptic-21 | studio-question-type: question-about-a-step-the-set-never-asked, chatbot-response-behaviour: differs-on-re-ask |
| exec-10 | processing-status: deleted-by-request |
| pipe-21 | scale: 500-players, data-element: device-platform |
| privacy-29 | time-and-change: player-deletion-request |
| speech-10 | data-element: tutorial-step |
| uxr-26 | scale: 500-players |
| cost-19 | latency: p99-tail-under-concurrency |
| onboard-17 | time-and-change: first-game-onboarded |
| skeptic-30 | data-element: transcript |
| chat-28 | recovery-action: manual-override-answer |
| design-31 | scale: 50-players, latency: ingest-to-queryable (hours or days after session) |
| player-34 | scale: 500-players |

## Leaves per perspective (id prefix -> E file)

| perspective | E file | in | surviving |
|---|---|---|---|
| analyst | E-studio-analyst.yaml | 2 | 1 |
| auditor | E-decision-consumer-auditor.yaml | 6 | 4 |
| chat | E-chatbot-engineer.yaml | 4 | 4 |
| cost | E-cost-and-latency-engineer.yaml | 9 | 8 |
| design | E-game-designer.yaml | 6 | 2 |
| ds | E-data-scientist.yaml | 7 | 4 |
| eval | E-qa-eval-lead.yaml | 3 | 3 |
| exec | E-studio-exec.yaml | 9 | 5 |
| extract | E-llm-extraction-engineer.yaml | 2 | 0 |
| l10n | E-localisation-owner.yaml | 4 | 4 |
| moderator | E-session-moderator.yaml | 17 | 14 |
| onboard | E-new-studio-onboarder.yaml | 9 | 8 |
| ops | E-pipeline-on-call-ops.yaml | 13 | 11 |
| percep | E-perception-and-accessibility-reviewer.yaml | 14 | 14 |
| pipe | E-pipeline-engineer.yaml | 11 | 4 |
| player | E-recorded-player.yaml | 9 | 3 |
| privacy | E-privacy-counsel.yaml | 12 | 10 |
| qauthor | E-question-author.yaml | 2 | 1 |
| sec | E-security-and-tenancy-engineer.yaml | 9 | 8 |
| skeptic | E-skeptic-of-structure.yaml | 3 | 3 |
| speech | E-speech-and-audio-engineer.yaml | 10 | 7 |
| stitch | E-session-stitching-engineer.yaml | 9 | 5 |
| uxr | E-ux-researcher.yaml | 4 | 1 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### stage (124 leaves carry a value)

| value | count |
|---|---|
| video-capture | 15 |
| 15-minute-split | 0 |
| session-stitching | 0 |
| transcription | 0 |
| fixed-question-set | 0 |
| answer-options | 0 |
| per-video-answers | 0 |
| session-level-aggregation | 0 |
| answers-table | 0 |
| chatbot-query-planning | 0 |
| chatbot-answer | 0 |
| evidence-display | 16 |
| studio-ui | 0 |
| recruitment-and-consent | 13 |
| build-and-metadata-tagging | 0 |
| upload-and-ingest | 16 |
| audio-extraction | 9 |
| language-detection | 15 |
| question-set-registry | 0 |
| extraction-prompt | 0 |
| job-orchestration-and-status | 15 |
| rerun-and-backfill | 0 |
| aggregate-cache | 10 |
| access-control | 8 |
| retention-and-deletion | 0 |
| export-and-share | 0 |
| studio-feedback-loop | 7 |

### data-element (112 leaves carry a value)

| value | count |
|---|---|
| session | 10 |
| video | 11 |
| transcript | 6 |
| utterance | 11 |
| timestamp | 3 |
| question | 3 |
| option | 2 |
| answer | 3 |
| player | 2 |
| cohort | 2 |
| game-version | 0 |
| game-target | 1 |
| tutorial-step | 5 |
| screen-state | 7 |
| build-id | 2 |
| device-platform | 4 |
| moderator | 2 |
| consent-record | 8 |
| question-set-version | 0 |
| prompt-version | 0 |
| extraction-model-version | 0 |
| transcription-model-version | 0 |
| extraction-run-id | 1 |
| answer-confidence | 0 |
| evidence-span | 11 |
| null-vs-no | 0 |
| studio-tenant | 7 |
| chatbot-conversation-log | 1 |
| cached-aggregate | 10 |

### session-shape (43 leaves carry a value)

| value | count |
|---|---|
| one-video | 2 |
| 2-4-videos | 0 |
| 5-20-videos | 18 |
| missing-middle-video | 2 |
| videos-out-of-order | 1 |
| overlapping-videos | 0 |
| session-ends-mid-sentence | 1 |
| zero-videos-session-failed | 0 |
| last-video-under-1-minute | 2 |
| duplicate-upload | 5 |
| video-with-no-audio-track | 2 |
| session-split-by-crash-into-two | 0 |
| same-player-multiple-sessions | 2 |
| tutorial-started-before-recording | 5 |
| 10-plus-hour-session | 3 |

### speech-shape (32 leaves carry a value)

| value | count |
|---|---|
| silent-player | 2 |
| continuous-think-aloud | 3 |
| game-audio-dominates | 3 |
| two-speakers | 1 |
| non-english | 9 |
| mixed-language | 6 |
| profanity-or-slang | 0 |
| inaudible-segments | 1 |
| moderator-speaking-or-leading | 3 |
| player-reading-chat-or-overlay-aloud | 1 |
| background-tv-or-other-people | 1 |
| whispering | 1 |
| mic-muted-for-a-period | 1 |
| emotional-nonverbal-only (sighs, laughs, swearing-masked) | 0 |

### question-shape (24 leaves carry a value)

| value | count |
|---|---|
| fits-an-option | 1 |
| fits-no-option | 0 |
| fits-two-options | 0 |
| answer-spans-videos | 1 |
| answer-is-a-count | 1 |
| answer-is-a-time | 3 |
| answer-is-a-why | 2 |
| answer-needs-visuals | 10 |
| question-not-in-set | 2 |
| event-did-not-happen-in-this-video | 2 |
| answer-changes-within-video | 0 |
| answer-depends-on-prior-video | 0 |
| negation-player-never-did-x | 0 |
| unknowable-from-audio | 1 |
| two-options-both-partly-true | 0 |
| perceptual-cause-not-verbalised | 1 |

### studio-question-type (62 leaves carry a value)

| value | count |
|---|---|
| one-player-what-happened | 2 |
| cohort-count | 10 |
| cohort-why | 3 |
| compare-two-versions | 4 |
| compare-two-steps | 2 |
| find-players-who | 2 |
| timeline-of-one-player | 2 |
| quote-me-evidence | 18 |
| follow-up-question | 0 |
| question-outside-game-target | 0 |
| trend-over-time | 0 |
| distribution-not-count | 2 |
| segment-by-metadata (device, country, build) | 1 |
| what-can-you-answer | 0 |
| recommendation-what-should-we-change | 0 |
| cross-game-or-cross-studio-benchmark | 2 |
| show-me-raw-transcript-or-clip | 9 |
| correction-that-is-wrong | 3 |
| question-about-a-step-the-set-never-asked | 2 |

### scale (33 leaves carry a value)

| value | count |
|---|---|
| 1-player | 0 |
| 50-players | 3 |
| 500-players | 16 |
| 5000-players | 2 |
| 10-games-at-once | 6 |
| 0-players-new-game | 1 |
| 1-player-10-hour-session | 2 |
| 50000-videos | 1 |
| many-concurrent-studio-users | 2 |
| question-set-of-50-questions | 0 |
| 500-players-x-3-question-set-versions | 0 |

### correctness-failure (43 leaves carry a value)

| value | count |
|---|---|
| hallucinated-answer | 2 |
| forced-choice-bias | 3 |
| inconsistent-across-videos | 3 |
| stale-after-prompt-change | 0 |
| wrong-denominator | 6 |
| right-answer-wrong-player | 1 |
| confident-no-evidence | 3 |
| instruction-injected-via-transcript | 1 |
| answer-attached-to-wrong-video-index | 1 |
| duplicate-counted | 7 |
| null-treated-as-no | 4 |
| other-option-overused | 2 |
| mixed-version-aggregation | 0 |
| perceptual-cause-attributed-to-verbal-option | 2 |
| moderator-words-attributed-to-player | 4 |
| transcription-hallucination-propagated | 4 |

### time-and-change (24 leaves carry a value)

| value | count |
|---|---|
| first-game-onboarded | 9 |
| game-update-changes-tutorial | 3 |
| question-set-revised | 0 |
| model-upgraded | 0 |
| a-year-of-data | 1 |
| studio-asks-at-3am | 1 |
| player-deletion-request | 6 |
| transcription-model-upgraded | 0 |
| rerun-in-progress-while-queried | 2 |
| studio-offboarded | 1 |
| retention-expiry | 1 |
| game-target-changes-beyond-tutorial | 0 |
| extraction-vendor-deprecates-model | 0 |

### latency (17 leaves carry a value)

| value | count |
|---|---|
| under-2s | 2 |
| under-30s | 0 |
| minutes | 2 |
| batch-overnight | 1 |
| first-token-vs-complete-answer | 0 |
| p99-tail-under-concurrency | 1 |
| ingest-to-queryable (hours or days after session) | 9 |
| fast-but-stale | 2 |

### processing-status (39 leaves carry a value)

| value | count |
|---|---|
| not-yet-uploaded | 2 |
| uploaded-partial | 6 |
| queued | 4 |
| transcribing | 1 |
| transcribed | 2 |
| transcription-failed | 4 |
| transcript-empty | 2 |
| extracting | 1 |
| extraction-partial-some-questions | 3 |
| extraction-failed | 0 |
| complete | 8 |
| superseded-by-rerun | 1 |
| rerun-in-progress | 2 |
| deleted-by-request | 3 |

### batch-failure-mix (24 leaves carry a value)

| value | count |
|---|---|
| all-succeed | 6 |
| one-video-of-session-failed | 4 |
| some-questions-failed-in-one-video | 1 |
| some-sessions-failed-in-cohort | 4 |
| all-failed | 1 |
| retry-produced-duplicate | 4 |
| late-arriving-video-after-aggregation | 4 |

### recovery-action (17 leaves carry a value)

| value | count |
|---|---|
| retry-one-video | 4 |
| retry-one-question | 2 |
| rerun-whole-session | 1 |
| backfill-after-question-set-change | 1 |
| backfill-after-model-upgrade | 0 |
| skip-and-mark-unknown | 2 |
| manual-override-answer | 3 |
| delete-and-propagate | 4 |

### question-set-version-state (2 leaves carry a value)

| value | count |
|---|---|
| single-version | 0 |
| mixed-versions-in-table | 1 |
| option-added | 0 |
| option-renamed-same-id | 0 |
| question-reworded-same-id | 0 |
| question-retired | 0 |
| per-game-fork | 1 |
| per-game-version-fork | 0 |
| rollback-to-old-version | 0 |

### transcription-subsystem (24 leaves carry a value)

| value | count |
|---|---|
| hallucinated-text-on-silence-or-music | 1 |
| wrong-language-detected | 9 |
| language-flips-between-videos | 5 |
| truncated-at-length-limit | 1 |
| timestamps-reset-per-video | 2 |
| sentence-cut-at-15min-boundary | 0 |
| transcription-model-version-differs-across-videos | 0 |
| profanity-masked-by-vendor | 0 |
| game-lyrics-or-npc-voice-transcribed-as-player | 2 |
| low-confidence-segments-dropped-silently | 1 |
| empty-transcript-for-non-empty-video | 3 |

### chatbot-response-behaviour (20 leaves carry a value)

| value | count |
|---|---|
| answers-correctly | 3 |
| says-no-data-correctly | 1 |
| substitutes-nearest-fixed-question | 0 |
| answers-from-general-game-knowledge | 0 |
| invents-number | 1 |
| silently-truncates-rows | 0 |
| differs-on-re-ask | 8 |
| answers-in-wrong-tenant-scope | 6 |
| times-out | 1 |
| refuses-answerable-question | 0 |
| mixes-null-with-no | 0 |

### fast-path-dependency (9 leaves carry a value)

| value | count |
|---|---|
| precomputed-aggregate-exists | 3 |
| table-fits-in-llm-context | 0 |
| text-to-sql-generated-correctly | 0 |
| index-on-game-target-and-version | 0 |
| cache-hit | 2 |
| cache-stale-after-rerun | 2 |
| question-requires-raw-transcript-fallback | 2 |
| concurrent-studio-load | 0 |
| table-growth-over-a-year | 0 |
| cold-start | 0 |

### capture-integrity (29 leaves carry a value)

| value | count |
|---|---|
| audio-and-video-ok | 5 |
| video-black-or-frozen | 7 |
| wrong-window-captured | 3 |
| no-audio-track | 2 |
| mic-muted-for-a-period | 2 |
| stereo-channel-only-game-audio | 5 |
| codec-unreadable | 2 |
| clock-drift-between-videos | 1 |
| upload-truncated | 2 |

### answer-afterlife (28 leaves carry a value)

| value | count |
|---|---|
| read-once-in-chat | 1 |
| copied-into-deck | 8 |
| exported-csv | 1 |
| shared-link | 2 |
| re-asked-after-rerun | 1 |
| acted-on-tutorial-changed | 2 |
| disputed-by-studio | 9 |
| cited-after-player-deletion | 4 |

### tenancy (26 leaves carry a value)

| value | count |
|---|---|
| one-studio-one-game | 4 |
| one-studio-many-games | 6 |
| many-studios-shared-infra | 12 |
| cross-studio-benchmark-request | 3 |
| studio-offboarded | 1 |

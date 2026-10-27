# G-counts-2 (bucket 2, part: ingestion-extraction)

| metric | count |
|---|---|
| in | 122 |
| rejected | 0 |
| duplicate clusters | 18 |
| ids merged into a survivor | 21 |
| leaves carrying variants_of | 44 |
| refusal rows kept | 7 |
| positives contested by a refusal | 5 |
| surviving | 101 |
| leaves with cell values added by normalisation | 99 (values added: 309) |
| uncategorised | 0 |

## Rejected

none (every item is L3/L4, points at a spec.md or memo.md object, and each banned-word hit is followed by a concrete instance on the same line: `such as resource-zero`, `such as "no idea what this bench"`, `such as "ignore your instructions"`, `improves ... by 12 pts`; `proper`/`handle` hits are substrings of `property`/`handles`).

## Duplicate clusters (survivor <- merged)

- extract-5 <- askdata-31
- clinical-8 <- eval-24
- convo-1 <- latency-26, obs-20
- owner-2 <- extract-19
- extract-8 <- platform-21
- cv-11 <- uxrepo-11
- gur-2 <- extract-38
- datateam-31 <- analyst-16
- ops-7 <- telem-5
- obs-19 <- kg-25
- sec-3 <- extract-9, platform-30
- sec-1 <- privacy-14
- extract-27 <- platform-33
- extract-32 (refusal) <- stitch-12
- gur-10 (refusal) <- cv-16
- vidsearch-26 (refusal) <- cv-31
- privacy-28 (refusal) <- latency-30, sec-30
- vidsearch-6 <- longctx-5

## Variants (leaf -> variants_of)

- eval-5 -> extract-5
- cv-21 -> latency-11
- extract-1 -> clinical-8
- owner-2 -> convo-1
- stitch-18 -> convo-1
- convo-25 -> convo-1
- store-32 -> extract-7
- designer-2 -> cv-11
- obs-30 -> cv-11
- convo-14 -> cv-11
- gur-19 -> cv-11
- retr-26 -> cv-11
- telem-13 -> cv-11
- longctx-22 -> convo-14
- ops-22 -> telem-13
- cv-6 -> ops-22
- extract-12 -> publisher-21
- clinical-33 -> extract-12
- analyst-33 -> extract-12
- gur-6 -> gur-29
- kg-8 -> gur-29
- extract-20 -> datateam-31
- kg-2 -> cv-5
- extract-2 -> ops-7
- retr-2 -> extract-2
- ops-7 -> obs-19
- qgen-34 -> sec-3
- sec-18 -> sec-3
- privacy-26 -> extract-26
- ops-26 -> extract-27
- cv-30 -> extract-27
- extract-14 -> convo-6
- designer-25 -> convo-6
- vidsearch-33 -> cv-9
- tar-13 -> cv-9
- cv-32 -> cv-3
- cv-25 -> cv-3
- cv-10 -> vidsearch-4
- cv-33 -> vidsearch-4
- clinical-9 -> kg-7
- qgen-20 -> designer-7
- longctx-16 -> latency-10
- stitch-27 -> latency-10
- cv-20 -> cv-2

## Refusals kept and the positives they contest

- extract-15: contests uxrepo-3
- extract-32: contests longctx-16
- gur-10: contests clinical-33
- vidsearch-20: contests owner-2, longctx-22
- vidsearch-26: contests none in this bucket
- privacy-28: contests none in this bucket
- stitch-11: contests owner-2

## Leaves per perspective (surviving)

| perspective | surviving | merged away |
|---|---|---|
| analyst | 1 | 1 |
| askdata | 0 | 1 |
| clinical | 4 | 0 |
| convo | 4 | 0 |
| cv | 15 | 2 |
| datateam | 2 | 0 |
| designer | 3 | 0 |
| eval | 4 | 1 |
| extract | 12 | 3 |
| gur | 5 | 0 |
| kg | 4 | 1 |
| latency | 5 | 2 |
| longctx | 2 | 1 |
| obs | 2 | 1 |
| ops | 4 | 0 |
| owner | 2 | 0 |
| platform | 1 | 3 |
| privacy | 4 | 1 |
| publisher | 1 | 0 |
| qgen | 3 | 0 |
| retr | 2 | 0 |
| sec | 3 | 1 |
| stitch | 6 | 1 |
| store | 2 | 0 |
| tar | 1 | 0 |
| telem | 2 | 1 |
| uxrepo | 1 | 1 |
| vidsearch | 6 | 0 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### part (unset: 0)

| value | count |
|---|---|
| ingestion-extraction | 101 |
| store | 0 |
| query-path | 0 |
| question-generation | 0 |
| evaluation | 0 |
| chatbot-ui | 0 |
| session-stitching | 0 |
| frame-pipeline | 0 |
| collection-protocol | 0 |
| tenancy-access-control | 0 |
| export-integration | 0 |
| feedback-loop-from-query-log | 0 |
| cost-governance | 0 |
| schema-evolution | 0 |

### representation (unset: 20)

| value | count |
|---|---|
| fixed-mcq-answers | 3 |
| timestamped-observation-log | 26 |
| entity-relation-graph | 5 |
| per-step-summary | 1 |
| per-session-summary | 1 |
| transcript-chunks-with-embeddings | 1 |
| learned-schema-from-data | 1 |
| raw-transcript-only | 3 |
| hybrid | 1 |
| wide-event-schema-on-read | 1 |
| inverted-full-text-index | 0 |
| olap-cube-materialized-views | 0 |
| step-funnel-state-machine-per-player | 6 |
| hierarchical-temporal-summary-tree | 6 |
| clip-or-frame-embeddings | 0 |
| time-series-signals-affect-pace-silence | 15 |
| customer-defined-trackers-over-universal-primitives | 3 |
| common-data-model-with-per-game-vocab-map | 5 |
| behaviour-archetype-clusters | 1 |
| issue-list-with-severity-frequency | 1 |
| question-answer-bank-precomputed | 1 |

### granularity (unset: 12)

| value | count |
|---|---|
| frame | 4 |
| utterance | 19 |
| tutorial-step | 17 |
| video | 7 |
| session | 16 |
| player | 1 |
| cohort | 0 |
| game | 2 |
| variable-length-moment-or-episode | 22 |
| level-quest-match-mission | 0 |
| game-system | 0 |
| build-version | 0 |
| player-segment-cluster | 1 |
| studio-portfolio | 0 |

### query-path (unset: 77)

| value | count |
|---|---|
| precomputed-aggregate | 2 |
| sql-over-closed-fields | 8 |
| retrieval-then-llm | 4 |
| lazy-backfill-extraction | 3 |
| map-reduce-over-raw | 2 |
| cached-prior-answer | 0 |
| clip-lookup | 1 |
| full-text-keyword-search | 2 |
| semantic-cache-similar-question | 0 |
| query-by-example-clip | 0 |
| automatic-contrast-cohort-diff | 1 |
| sampled-map-reduce-with-ci | 0 |
| progressive-answer-then-refine | 0 |
| agentic-multi-tool-plan | 0 |
| text-to-semantic-layer-metrics | 0 |
| human-analyst-escalation | 0 |
| push-alert-no-query | 1 |

### question-type (unset: 27)

| value | count |
|---|---|
| what-happened | 4 |
| when | 3 |
| how-long | 4 |
| how-many | 21 |
| why | 11 |
| how-felt | 7 |
| what-said | 4 |
| compare-versions | 2 |
| compare-steps | 4 |
| find-players-who | 3 |
| timeline | 0 |
| outside-game-target | 0 |
| what-surprised-unknown-unknowns | 2 |
| what-to-fix-first-prioritised | 1 |
| who-are-the-churners-segment-discovery | 2 |
| technical-issue-bug-perf | 1 |
| counterfactual-why-not | 3 |
| prevalence-of-quoted-sentiment | 2 |
| did-the-fix-work-pre-post | 0 |

### extraction-trigger (unset: 1)

| value | count |
|---|---|
| at-ingestion | 82 |
| on-first-question | 0 |
| scheduled-batch | 2 |
| on-game-update | 0 |
| on-model-upgrade | 1 |
| on-new-game-onboarding | 7 |
| on-new-field-added | 1 |
| on-low-confidence-or-disagreement | 4 |
| on-cohort-size-threshold | 1 |
| continuous-during-live-session | 1 |
| on-studio-tracker-defined | 1 |

### modality (unset: 31)

| value | count |
|---|---|
| speech-transcript | 18 |
| on-screen-text-ocr | 10 |
| screen-state-classifier | 18 |
| input-events | 3 |
| game-telemetry | 4 |
| audio-non-speech | 3 |
| webcam-face-and-posture | 1 |
| survey-or-in-game-prompt-response | 0 |
| player-profile-metadata | 1 |
| build-version-metadata | 0 |
| frame-embeddings | 3 |
| silence-or-absence-of-speech | 9 |
| controller-or-touch-heatmap | 0 |

### scope (unset: 92)

| value | count |
|---|---|
| one-player | 0 |
| cohort | 3 |
| all-players | 2 |
| cross-game | 2 |
| cross-studio-benchmark | 1 |
| query-time-defined-cohort | 0 |
| build-version-pair | 1 |

### latency-tier (unset: 86)

| value | count |
|---|---|
| under-2s | 5 |
| under-30s | 1 |
| minutes | 2 |
| overnight | 6 |
| progressive-streaming | 0 |
| push-no-query | 1 |
| sub-200ms-cached | 0 |

### question-origin (unset: 86)

| value | count |
|---|---|
| hand-written-per-game | 1 |
| ontology-generated | 1 |
| induced-from-data | 5 |
| learned-from-studio-usage | 0 |
| studio-written-at-runtime | 0 |
| genre-template-library | 0 |
| design-doc-patch-notes-store-page-derived | 3 |
| kpi-backward-from-studio-metrics | 0 |
| discriminative-contrast-churn-vs-retain | 0 |
| emergent-topic-clustering-of-player-speech | 0 |
| established-gur-frameworks-heuristics-pxi-mda | 3 |
| failed-query-log | 0 |
| few-shot-tracker-from-examples | 1 |
| onboarding-interview-with-studio | 1 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 0 |

### evidence-form (unset: 31)

| value | count |
|---|---|
| none | 1 |
| quote-with-timestamp | 9 |
| clip | 5 |
| count-with-denominator | 22 |
| confidence-score | 4 |
| per-player-list | 2 |
| clip-montage-n-examples | 6 |
| contrast-vs-baseline | 9 |
| coverage-statement-n-of-m-players | 5 |
| extraction-provenance-model-and-schema-version | 4 |
| recall-estimate | 1 |
| chart | 1 |
| severity-frequency-matrix | 1 |

### effort (unset: 0)

| value | count |
|---|---|
| S-weeks | 48 |
| M-one-quarter | 33 |
| L-multi-quarter | 4 |
| XS-days | 16 |
| buy-or-integrate | 0 |

### mechanism-type (unset: 11)

| value | count |
|---|---|
| precompute-more | 58 |
| defer-to-query-time | 0 |
| reuse-or-cache-prior-work | 3 |
| approximate-then-refine | 4 |
| narrow-or-clarify-the-question | 1 |
| push-instead-of-pull | 1 |
| transfer-across-games | 4 |
| change-data-at-source | 10 |
| human-in-the-loop | 4 |
| auto-discover-without-question | 5 |

### user-segment (unset: 87)

| value | count |
|---|---|
| studio-analyst | 2 |
| game-designer | 6 |
| ux-researcher | 0 |
| producer-exec | 0 |
| studio-data-engineer | 4 |
| live-ops-community | 0 |
| publisher-portfolio | 1 |
| platform-devrel | 0 |
| indie-solo-dev | 0 |
| jev-internal-ops | 1 |

### moment-in-journey (unset: 94)

| value | count |
|---|---|
| game-onboarding-day-0 | 6 |
| first-cohort-ingested | 0 |
| first-studio-question | 0 |
| steady-state-weekly | 1 |
| new-build-version | 0 |
| pre-launch-greenlight | 0 |
| live-ops-update | 0 |
| renewal-review | 0 |

### delivery-surface (unset: 98)

| value | count |
|---|---|
| chatbot | 0 |
| dashboard-standard-report | 0 |
| warehouse-share-or-export | 0 |
| api-sdk | 0 |
| notebook | 0 |
| slack-jira-integration | 0 |
| scheduled-digest | 1 |
| clip-reel | 1 |
| alert | 1 |

### subject-domain (unset: 16)

| value | count |
|---|---|
| onboarding-tutorial | 64 |
| core-loop | 1 |
| progression-difficulty | 1 |
| economy-monetization | 1 |
| social-multiplayer | 2 |
| narrative | 1 |
| ui-navigation | 4 |
| technical-bugs-performance | 2 |
| accessibility | 1 |
| player-affect | 8 |

### tenancy-and-deployment (unset: 97)

| value | count |
|---|---|
| shared-multi-tenant | 0 |
| logically-isolated-per-studio | 3 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 1 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 0 |

### reuse-scope-of-extraction (unset: 80)

| value | count |
|---|---|
| game-specific | 6 |
| genre-shared | 1 |
| universal-primitives | 12 |
| customer-defined-on-top-of-universal | 2 |

### schema-evolution (unset: 95)

| value | count |
|---|---|
| frozen-schema | 0 |
| append-only-versioned-fields | 1 |
| schema-on-read | 1 |
| eager-backfill-all-history | 2 |
| lazy-backfill-on-demand | 0 |
| deprecate-and-migrate | 0 |
| model-upgrade-reextract | 2 |

### uncertainty-policy (unset: 88)

| value | count |
|---|---|
| always-answer | 0 |
| answer-with-ci-and-n | 4 |
| abstain-below-coverage | 6 |
| ask-clarifying-question | 0 |
| give-range-then-refine | 2 |
| escalate-to-human-analyst | 1 |

### build-or-buy (unset: 85)

| value | count |
|---|---|
| build-in-house | 4 |
| open-source-component | 4 |
| managed-cloud-service | 6 |
| third-party-video-understanding-api | 0 |
| studio-owned-stack | 2 |


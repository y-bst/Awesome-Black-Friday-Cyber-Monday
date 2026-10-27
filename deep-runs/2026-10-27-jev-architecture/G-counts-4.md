# G-counts-4 (bucket 4, part = question-generation, ideate run)

| measure | count |
|---|---|
| in (rows in G-bucket-4.yaml) | 106 |
| rejected (contract violations) | 0 |
| duplicate clusters | 14 |
| absorbed into a survivor (ids in `absorbed`, perspective slugs in `also_from`) | 15 |
| variants (survivors carrying `variants_of`) | 63 |
| refusal rows kept (`refusal: true`) | 10 |
| contested positives (carrying `contested_by`) | 28 |
| surviving | 91 |
| leaves with cell values added by normalisation | 90 (340 values) |

## Rejected

None. Every row is L3/L4, names a spec.md, memo.md or A-frame object, and carries mechanism, example, cost, depends_on. The one banned phrase in the bucket (`such as`, sec-29 example) is followed by a specific instance on the same line. Notes: kg-19 cites B-perspectives.yaml as object but its situation grounds in spec.md step 3; publisher-4 had top-level `part: query` against `cell.part: question-generation` and was normalised to question-generation.

## Duplicate clusters (survivor <- absorbed)

- extract-21 <- qgen-30
- extract-11 <- qgen-21
- eval-13 <- analyst-1
- designer-6 <- gur-8
- qgen-18 <- owner-3
- gur-4 <- qgen-19
- qgen-4 <- telem-11
- convo-34 <- analyst-20
- telem-25 <- uxrepo-18
- qgen-2 <- owner-6
- owner-14 <- ops-19
- qgen-1 <- store-4
- clinical-12 <- tar-9
- convo-19 <- owner-7, qgen-15

## Variants (kept, `variants_of`)

- askdata-26 -> eval-13
- clinical-5 -> clinical-7
- clinical-7 -> qgen-18
- convo-3 -> extract-21
- convo-4 -> qgen-18
- convo-17 -> convo-2
- tar-3 -> extract-21
- tar-28 -> qgen-4
- tar-32 -> eval-12
- eval-27 -> eval-12
- extract-33 -> qgen-4
- designer-18 -> designer-6
- designer-27 -> convo-34
- gur-9 -> eval-13
- gur-22 -> gur-4
- gur-23 -> convo-34
- kg-6 -> qgen-18
- kg-17 -> kg-32
- kg-19 -> qgen-2
- longctx-8 -> convo-21
- longctx-21 -> convo-19
- obs-17 -> convo-34
- obs-18 -> convo-34
- platform-1 -> owner-1
- platform-4 -> qgen-18
- platform-8 -> convo-4
- platform-11 -> convo-19
- platform-26 -> owner-25
- platform-27 -> gur-4
- platform-29 -> convo-19
- platform-32 -> extract-21
- ops-15 -> gur-4
- ops-20 -> eval-13
- privacy-32 -> privacy-12
- privacy-34 -> owner-25
- owner-1 -> qgen-18
- owner-4 -> designer-6
- owner-26 -> owner-1
- owner-32 -> eval-13
- publisher-5 -> owner-23
- publisher-20 -> qgen-27
- planner-12 -> extract-11
- qgen-3 -> owner-14
- qgen-7 -> qgen-1
- qgen-12 -> convo-34
- qgen-14 -> eval-13
- qgen-16 -> longctx-8
- qgen-27 -> qgen-4
- qgen-28 -> convo-34
- stitch-7 -> qgen-1
- stat-11 -> eval-12
- stat-21 -> extract-21
- analyst-22 -> convo-2
- datateam-22 -> convo-2
- datateam-27 -> qgen-1
- sec-6 -> qgen-18
- telem-12 -> qgen-27
- telem-29 -> qgen-2
- uxrepo-5 -> convo-34
- vidsearch-12 -> convo-34
- vidsearch-13 -> qgen-4
- vidsearch-23 -> telem-25
- vidsearch-27 -> qgen-2

## Refusals and the positives they contest

- convo-19: contests owner-23
- convo-21: contests latency-12, kg-32, tar-32, stat-11, qgen-10
- longctx-8: contests latency-12, tar-32, kg-32
- longctx-21: contests owner-23
- platform-11: contests eval-13, askdata-26, ops-20, qgen-14, gur-9, designer-6, owner-1, owner-32, owner-23
- platform-29: contests owner-23
- owner-7: absorbed into convo-19 (same refusal)
- publisher-4: contests analyst-22, extract-11, planner-12, convo-2, datateam-22
- qgen-15: absorbed into convo-19 (same refusal)
- qgen-16: contests latency-12
- privacy-13: contests convo-34, gur-23, obs-17, qgen-28, qgen-12, uxrepo-5
- sec-29: contests owner-25, platform-26, privacy-34

## Leaves per perspective

| perspective | in | absorbed | surviving |
|---|---|---|---|
| analyst | 3 | 2 | 1 |
| askdata | 1 | 0 | 1 |
| clinical | 3 | 0 | 3 |
| convo | 7 | 0 | 7 |
| datateam | 2 | 0 | 2 |
| designer | 3 | 0 | 3 |
| eval | 3 | 0 | 3 |
| extract | 3 | 0 | 3 |
| gur | 6 | 1 | 5 |
| kg | 4 | 0 | 4 |
| latency | 1 | 0 | 1 |
| longctx | 2 | 0 | 2 |
| obs | 2 | 0 | 2 |
| ops | 3 | 1 | 2 |
| owner | 10 | 3 | 7 |
| planner | 1 | 0 | 1 |
| platform | 9 | 0 | 9 |
| privacy | 4 | 0 | 4 |
| publisher | 3 | 0 | 3 |
| qgen | 16 | 4 | 12 |
| sec | 2 | 0 | 2 |
| stat | 2 | 0 | 2 |
| stitch | 1 | 0 | 1 |
| store | 1 | 1 | 0 |
| tar | 4 | 1 | 3 |
| telem | 4 | 1 | 3 |
| uxrepo | 2 | 1 | 1 |
| vidsearch | 4 | 0 | 4 |

## Counts per axis value (normalised cells, surviving leaves; zero values listed)

### part (set on 91 of 91)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 0 |
| query-path | 0 |
| question-generation | 91 |
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

### representation (set on 40 of 91)

| value | count |
|---|---|
| fixed-mcq-answers | 8 |
| timestamped-observation-log | 0 |
| entity-relation-graph | 1 |
| per-step-summary | 0 |
| per-session-summary | 0 |
| transcript-chunks-with-embeddings | 2 |
| learned-schema-from-data | 2 |
| raw-transcript-only | 0 |
| hybrid | 0 |
| wide-event-schema-on-read | 1 |
| inverted-full-text-index | 0 |
| olap-cube-materialized-views | 0 |
| step-funnel-state-machine-per-player | 3 |
| hierarchical-temporal-summary-tree | 0 |
| clip-or-frame-embeddings | 4 |
| time-series-signals-affect-pace-silence | 0 |
| customer-defined-trackers-over-universal-primitives | 9 |
| common-data-model-with-per-game-vocab-map | 4 |
| behaviour-archetype-clusters | 2 |
| issue-list-with-severity-frequency | 0 |
| question-answer-bank-precomputed | 4 |

### granularity (set on 36 of 91)

| value | count |
|---|---|
| frame | 0 |
| utterance | 0 |
| tutorial-step | 20 |
| video | 3 |
| session | 3 |
| player | 1 |
| cohort | 0 |
| game | 4 |
| variable-length-moment-or-episode | 1 |
| level-quest-match-mission | 0 |
| game-system | 2 |
| build-version | 0 |
| player-segment-cluster | 2 |
| studio-portfolio | 0 |

### query-path (set on 16 of 91)

| value | count |
|---|---|
| precomputed-aggregate | 1 |
| sql-over-closed-fields | 2 |
| retrieval-then-llm | 0 |
| lazy-backfill-extraction | 2 |
| map-reduce-over-raw | 1 |
| cached-prior-answer | 1 |
| clip-lookup | 0 |
| full-text-keyword-search | 0 |
| semantic-cache-similar-question | 0 |
| query-by-example-clip | 3 |
| automatic-contrast-cohort-diff | 5 |
| sampled-map-reduce-with-ci | 0 |
| progressive-answer-then-refine | 0 |
| agentic-multi-tool-plan | 0 |
| text-to-semantic-layer-metrics | 1 |
| human-analyst-escalation | 0 |
| push-alert-no-query | 0 |

### question-type (set on 37 of 91)

| value | count |
|---|---|
| what-happened | 2 |
| when | 0 |
| how-long | 2 |
| how-many | 6 |
| why | 4 |
| how-felt | 1 |
| what-said | 0 |
| compare-versions | 0 |
| compare-steps | 0 |
| find-players-who | 1 |
| timeline | 1 |
| outside-game-target | 0 |
| what-surprised-unknown-unknowns | 8 |
| what-to-fix-first-prioritised | 1 |
| who-are-the-churners-segment-discovery | 5 |
| technical-issue-bug-perf | 1 |
| counterfactual-why-not | 0 |
| prevalence-of-quoted-sentiment | 5 |
| did-the-fix-work-pre-post | 0 |

### extraction-trigger (set on 49 of 91)

| value | count |
|---|---|
| at-ingestion | 6 |
| on-first-question | 2 |
| scheduled-batch | 11 |
| on-game-update | 1 |
| on-model-upgrade | 0 |
| on-new-game-onboarding | 15 |
| on-new-field-added | 2 |
| on-low-confidence-or-disagreement | 0 |
| on-cohort-size-threshold | 3 |
| continuous-during-live-session | 0 |
| on-studio-tracker-defined | 9 |

### modality (set on 26 of 91)

| value | count |
|---|---|
| speech-transcript | 11 |
| on-screen-text-ocr | 3 |
| screen-state-classifier | 1 |
| input-events | 0 |
| game-telemetry | 5 |
| audio-non-speech | 0 |
| webcam-face-and-posture | 0 |
| survey-or-in-game-prompt-response | 1 |
| player-profile-metadata | 0 |
| build-version-metadata | 1 |
| frame-embeddings | 4 |
| silence-or-absence-of-speech | 0 |
| controller-or-touch-heatmap | 0 |

### scope (set on 46 of 91)

| value | count |
|---|---|
| one-player | 0 |
| cohort | 5 |
| all-players | 29 |
| cross-game | 9 |
| cross-studio-benchmark | 1 |
| query-time-defined-cohort | 1 |
| build-version-pair | 1 |

### latency-tier (set on 12 of 91)

| value | count |
|---|---|
| under-2s | 1 |
| under-30s | 1 |
| minutes | 3 |
| overnight | 5 |
| progressive-streaming | 0 |
| push-no-query | 1 |
| sub-200ms-cached | 1 |

### question-origin (set on 88 of 91)

| value | count |
|---|---|
| hand-written-per-game | 4 |
| ontology-generated | 18 |
| induced-from-data | 10 |
| learned-from-studio-usage | 1 |
| studio-written-at-runtime | 4 |
| genre-template-library | 8 |
| design-doc-patch-notes-store-page-derived | 5 |
| kpi-backward-from-studio-metrics | 3 |
| discriminative-contrast-churn-vs-retain | 4 |
| emergent-topic-clustering-of-player-speech | 6 |
| established-gur-frameworks-heuristics-pxi-mda | 4 |
| failed-query-log | 1 |
| few-shot-tracker-from-examples | 8 |
| onboarding-interview-with-studio | 7 |
| public-reviews-and-community-mining | 4 |
| pilot-sessions-then-freeze | 1 |

### evidence-form (set on 66 of 91)

| value | count |
|---|---|
| none | 0 |
| quote-with-timestamp | 4 |
| clip | 1 |
| count-with-denominator | 26 |
| confidence-score | 8 |
| per-player-list | 0 |
| clip-montage-n-examples | 7 |
| contrast-vs-baseline | 11 |
| coverage-statement-n-of-m-players | 4 |
| extraction-provenance-model-and-schema-version | 2 |
| recall-estimate | 2 |
| chart | 1 |
| severity-frequency-matrix | 0 |

### effort (set on 91 of 91)

| value | count |
|---|---|
| S-weeks | 34 |
| M-one-quarter | 39 |
| L-multi-quarter | 1 |
| XS-days | 17 |
| buy-or-integrate | 0 |

### mechanism-type (set on 75 of 91)

| value | count |
|---|---|
| precompute-more | 7 |
| defer-to-query-time | 2 |
| reuse-or-cache-prior-work | 1 |
| approximate-then-refine | 0 |
| narrow-or-clarify-the-question | 15 |
| push-instead-of-pull | 0 |
| transfer-across-games | 17 |
| change-data-at-source | 0 |
| human-in-the-loop | 10 |
| auto-discover-without-question | 23 |

### user-segment (set on 48 of 91)

| value | count |
|---|---|
| studio-analyst | 3 |
| game-designer | 9 |
| ux-researcher | 6 |
| producer-exec | 2 |
| studio-data-engineer | 3 |
| live-ops-community | 1 |
| publisher-portfolio | 3 |
| platform-devrel | 6 |
| indie-solo-dev | 4 |
| jev-internal-ops | 11 |

### moment-in-journey (set on 58 of 91)

| value | count |
|---|---|
| game-onboarding-day-0 | 35 |
| first-cohort-ingested | 13 |
| first-studio-question | 2 |
| steady-state-weekly | 4 |
| new-build-version | 1 |
| pre-launch-greenlight | 2 |
| live-ops-update | 1 |
| renewal-review | 0 |

### delivery-surface (set on 24 of 91)

| value | count |
|---|---|
| chatbot | 7 |
| dashboard-standard-report | 9 |
| warehouse-share-or-export | 2 |
| api-sdk | 0 |
| notebook | 0 |
| slack-jira-integration | 0 |
| scheduled-digest | 6 |
| clip-reel | 0 |
| alert | 0 |

### subject-domain (set on 68 of 91)

| value | count |
|---|---|
| onboarding-tutorial | 62 |
| core-loop | 0 |
| progression-difficulty | 0 |
| economy-monetization | 1 |
| social-multiplayer | 0 |
| narrative | 0 |
| ui-navigation | 1 |
| technical-bugs-performance | 1 |
| accessibility | 2 |
| player-affect | 1 |

### tenancy-and-deployment (set on 9 of 91)

| value | count |
|---|---|
| shared-multi-tenant | 6 |
| logically-isolated-per-studio | 3 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 0 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 0 |

### reuse-scope-of-extraction (set on 38 of 91)

| value | count |
|---|---|
| game-specific | 10 |
| genre-shared | 15 |
| universal-primitives | 4 |
| customer-defined-on-top-of-universal | 9 |

### schema-evolution (set on 17 of 91)

| value | count |
|---|---|
| frozen-schema | 2 |
| append-only-versioned-fields | 9 |
| schema-on-read | 0 |
| eager-backfill-all-history | 2 |
| lazy-backfill-on-demand | 4 |
| deprecate-and-migrate | 0 |
| model-upgrade-reextract | 0 |

### uncertainty-policy (set on 12 of 91)

| value | count |
|---|---|
| always-answer | 1 |
| answer-with-ci-and-n | 3 |
| abstain-below-coverage | 7 |
| ask-clarifying-question | 0 |
| give-range-then-refine | 0 |
| escalate-to-human-analyst | 1 |

### build-or-buy (set on 3 of 91)

| value | count |
|---|---|
| build-in-house | 1 |
| open-source-component | 1 |
| managed-cloud-service | 0 |
| third-party-video-understanding-api | 0 |
| studio-owned-stack | 1 |

## Uncategorised

none

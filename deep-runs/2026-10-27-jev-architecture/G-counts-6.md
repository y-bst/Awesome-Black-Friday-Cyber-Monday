# G-counts-6 (bucket 6, parts = schema-evolution, export-integration, feedback-loop-from-query-log, session-stitching; ideate run)

| measure | count |
|---|---|
| in (rows in G-bucket-6.yaml) | 173 |
| rejected (contract violations) | 0 |
| duplicate clusters | 14 |
| absorbed into a survivor (ids in `absorbed`, perspective slugs in `also_from`) | 16 |
| variants (survivors carrying `variants_of`) | 78 |
| refusal rows kept (`refusal: true`) | 8 |
| contested positives (carrying `contested_by`) | 13 |
| surviving | 157 |
| leaves with cell values added by normalisation | 147 (548 values; includes effort mapped from cost and axis values carried over from absorbed rows) |
| uncategorised | 0 |

Check: kept 157 + absorbed 16 + rejected 0 = 173 = in 173; every bucket id accounted for exactly once.

## Rejected

None. Every row is L3/L4 with `shallow: false`, names a spec.md, memo.md or A-frame object, and carries mechanism, example, cost, depends_on, part, ingest_cost, query_cost and better_than_fixed_table. Banned-word hits are all followed by a specific instance on the same line: `improved` (extract-37, stitch-20 situations: a named prompt/ordering change), `improve` (designer-26 example, store-17 situation: quoted studio question), `improves` (privacy-31, convo-32: named measured effect), `considering backfill` (obs-7: names the derived column check), `Handles the 'long multi-video sessions' problem` (longctx-17: names the spec problem).

## Duplicate clusters (survivor <- absorbed)

- obs-25 <- owner-21
- store-15 <- owner-9
- clinical-24 <- designer-30
- eval-2 <- owner-22
- store-3 <- datateam-18
- datateam-2 <- owner-28, obs-27
- uxrepo-26 <- gur-24
- obs-32 <- planner-19, store-34
- qgen-5 <- owner-12
- stitch-1 <- store-9
- stitch-6 <- cv-14
- extract-3 <- designer-21
- extract-17 <- store-36
- telem-1 <- datateam-5

## Variants (kept, `variants_of`)

- askdata-13 -> store-3
- convo-27 -> qgen-24
- cv-22 -> obs-25
- cv-26 -> store-15
- tar-25 -> eval-2
- extract-10 -> obs-25
- extract-37 -> extract-10
- kg-15 -> extract-10
- kg-16 -> obs-24
- longctx-12 -> retr-22
- longctx-20 -> latency-21
- platform-17 -> store-15
- platform-25 -> latency-21
- privacy-31 -> latency-21
- publisher-1 -> store-15
- publisher-3 -> publisher-28
- publisher-28 -> qgen-24
- retr-25 -> latency-21
- stat-10 -> obs-25
- store-17 -> clinical-24
- datateam-11 -> datateam-3
- uxrepo-21 -> clinical-24
- vidsearch-28 -> retr-25
- convo-24 -> datateam-2
- cv-27 -> datateam-2
- tar-20 -> datateam-2
- gur-28 -> store-15
- kg-28 -> datateam-2
- latency-33 -> datateam-2
- platform-18 -> datateam-2
- privacy-24 -> datateam-2
- publisher-8 -> uxrepo-26
- publisher-15 -> datateam-1
- publisher-18 -> cv-28
- retr-33 -> datateam-2
- stitch-19 -> cv-19
- stitch-31 -> datateam-2
- store-28 -> datateam-2, datateam-3
- datateam-2 -> datateam-1
- datateam-17 -> stitch-19
- sec-13 -> datateam-2
- sec-27 -> analyst-4
- telem-7 -> datateam-2
- vidsearch-9 -> uxrepo-26
- clinical-34 -> obs-25
- convo-11 -> obs-32
- convo-32 -> clinical-11
- cv-28 -> convo-15
- tar-19 -> clinical-11
- tar-27 -> obs-32
- designer-9 -> convo-15
- kg-29 -> convo-15
- latency-18 -> obs-32
- longctx-32 -> owner-15
- platform-15 -> qgen-5
- privacy-19 -> qgen-5, sec-8
- planner-30 -> analyst-8
- stitch-24 -> convo-15
- stat-27 -> convo-15
- analyst-23 -> obs-32
- telem-17 -> convo-15
- uxrepo-4 -> qgen-33
- tar-12 -> planner-23
- tar-31 -> stitch-1
- kg-14 -> stitch-1
- longctx-4 -> stitch-1
- longctx-17 -> convo-7
- obs-29 -> stitch-1
- ops-28 -> stitch-5
- publisher-24 -> planner-23
- retr-16 -> retr-1
- stitch-17 -> store-33
- stitch-25 -> extract-17
- stat-7 -> planner-23
- datateam-29 -> stitch-31, planner-23
- telem-22 -> clinical-14
- uxrepo-12 -> obs-8
- uxrepo-28 -> extract-17

## Refusals and the positives they contest

- designer-26: no positive in this bucket proposes the refused option (kept, uncontested)
- datateam-19: no positive in this bucket proposes the refused option (kept, uncontested)
- datateam-8: contests longctx-26
- datateam-23: contests privacy-33, telem-1, telem-22, telem-17
- analyst-12: contests convo-15, cv-28, designer-9, kg-29, stat-27, telem-17, publisher-18, owner-15
- datateam-33: contests convo-15, cv-28, designer-9, kg-29, stat-27, telem-17, owner-15
- uxrepo-19: contests longctx-32
- privacy-5: no positive in this bucket proposes the refused option (kept, uncontested)

## Surviving leaves per part

| part | in | surviving |
|---|---|---|
| schema-evolution | 47 | 42 |
| export-integration | 43 | 40 |
| feedback-loop-from-query-log | 42 | 39 |
| session-stitching | 41 | 36 |

## Leaves per perspective

| perspective | in | absorbed | surviving |
|---|---|---|---|
| analyst | 5 | 0 | 5 |
| askdata | 2 | 0 | 2 |
| clinical | 4 | 0 | 4 |
| convo | 7 | 0 | 7 |
| cv | 8 | 1 | 7 |
| datateam | 15 | 2 | 13 |
| designer | 4 | 2 | 2 |
| eval | 3 | 0 | 3 |
| extract | 8 | 0 | 8 |
| gur | 2 | 1 | 1 |
| kg | 6 | 0 | 6 |
| latency | 3 | 0 | 3 |
| longctx | 6 | 0 | 6 |
| obs | 7 | 1 | 6 |
| ops | 3 | 0 | 3 |
| owner | 6 | 5 | 1 |
| planner | 3 | 1 | 2 |
| platform | 5 | 0 | 5 |
| privacy | 6 | 0 | 6 |
| publisher | 9 | 0 | 9 |
| qgen | 3 | 0 | 3 |
| retr | 5 | 0 | 5 |
| sec | 5 | 0 | 5 |
| stat | 5 | 0 | 5 |
| stitch | 9 | 0 | 9 |
| store | 8 | 3 | 5 |
| tar | 7 | 0 | 7 |
| telem | 4 | 0 | 4 |
| uxrepo | 10 | 0 | 10 |
| vidsearch | 5 | 0 | 5 |

## Counts per axis value (normalised cells, surviving leaves; zero values listed)

### part (set on 157 of 157)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 0 |
| query-path | 0 |
| question-generation | 0 |
| evaluation | 0 |
| chatbot-ui | 0 |
| session-stitching | 36 |
| frame-pipeline | 0 |
| collection-protocol | 0 |
| tenancy-access-control | 0 |
| export-integration | 40 |
| feedback-loop-from-query-log | 39 |
| cost-governance | 0 |
| schema-evolution | 42 |

### representation (set on 88 of 157)

| value | count |
|---|---|
| fixed-mcq-answers | 1 |
| timestamped-observation-log | 23 |
| entity-relation-graph | 5 |
| per-step-summary | 1 |
| per-session-summary | 3 |
| transcript-chunks-with-embeddings | 4 |
| learned-schema-from-data | 2 |
| raw-transcript-only | 4 |
| hybrid | 3 |
| wide-event-schema-on-read | 4 |
| inverted-full-text-index | 0 |
| olap-cube-materialized-views | 8 |
| step-funnel-state-machine-per-player | 6 |
| hierarchical-temporal-summary-tree | 2 |
| clip-or-frame-embeddings | 2 |
| time-series-signals-affect-pace-silence | 1 |
| customer-defined-trackers-over-universal-primitives | 8 |
| common-data-model-with-per-game-vocab-map | 7 |
| behaviour-archetype-clusters | 1 |
| issue-list-with-severity-frequency | 1 |
| question-answer-bank-precomputed | 2 |

### granularity (set on 123 of 157)

| value | count |
|---|---|
| frame | 2 |
| utterance | 7 |
| tutorial-step | 30 |
| video | 15 |
| session | 46 |
| player | 2 |
| cohort | 0 |
| game | 3 |
| variable-length-moment-or-episode | 7 |
| level-quest-match-mission | 0 |
| game-system | 0 |
| build-version | 10 |
| player-segment-cluster | 0 |
| studio-portfolio | 1 |

### query-path (set on 57 of 157)

| value | count |
|---|---|
| precomputed-aggregate | 2 |
| sql-over-closed-fields | 5 |
| retrieval-then-llm | 2 |
| lazy-backfill-extraction | 16 |
| map-reduce-over-raw | 4 |
| cached-prior-answer | 3 |
| clip-lookup | 2 |
| full-text-keyword-search | 0 |
| semantic-cache-similar-question | 0 |
| query-by-example-clip | 0 |
| automatic-contrast-cohort-diff | 1 |
| sampled-map-reduce-with-ci | 0 |
| progressive-answer-then-refine | 1 |
| agentic-multi-tool-plan | 0 |
| text-to-semantic-layer-metrics | 1 |
| human-analyst-escalation | 1 |
| push-alert-no-query | 19 |

### question-type (set on 71 of 157)

| value | count |
|---|---|
| what-happened | 1 |
| when | 1 |
| how-long | 9 |
| how-many | 12 |
| why | 0 |
| how-felt | 0 |
| what-said | 1 |
| compare-versions | 5 |
| compare-steps | 2 |
| find-players-who | 5 |
| timeline | 8 |
| outside-game-target | 1 |
| what-surprised-unknown-unknowns | 7 |
| what-to-fix-first-prioritised | 3 |
| who-are-the-churners-segment-discovery | 1 |
| technical-issue-bug-perf | 3 |
| counterfactual-why-not | 0 |
| prevalence-of-quoted-sentiment | 0 |
| did-the-fix-work-pre-post | 12 |

### extraction-trigger (set on 104 of 157)

| value | count |
|---|---|
| at-ingestion | 18 |
| on-first-question | 3 |
| scheduled-batch | 27 |
| on-game-update | 13 |
| on-model-upgrade | 17 |
| on-new-game-onboarding | 3 |
| on-new-field-added | 14 |
| on-low-confidence-or-disagreement | 3 |
| on-cohort-size-threshold | 3 |
| continuous-during-live-session | 2 |
| on-studio-tracker-defined | 1 |

### modality (set on 56 of 157)

| value | count |
|---|---|
| speech-transcript | 17 |
| on-screen-text-ocr | 4 |
| screen-state-classifier | 6 |
| input-events | 2 |
| game-telemetry | 8 |
| audio-non-speech | 1 |
| webcam-face-and-posture | 0 |
| survey-or-in-game-prompt-response | 1 |
| player-profile-metadata | 3 |
| build-version-metadata | 11 |
| frame-embeddings | 1 |
| silence-or-absence-of-speech | 2 |
| controller-or-touch-heatmap | 0 |

### scope (set on 45 of 157)

| value | count |
|---|---|
| one-player | 2 |
| cohort | 0 |
| all-players | 17 |
| cross-game | 9 |
| cross-studio-benchmark | 6 |
| query-time-defined-cohort | 1 |
| build-version-pair | 10 |

### latency-tier (set on 49 of 157)

| value | count |
|---|---|
| under-2s | 3 |
| under-30s | 3 |
| minutes | 2 |
| overnight | 18 |
| progressive-streaming | 2 |
| push-no-query | 19 |
| sub-200ms-cached | 2 |

### question-origin (set on 35 of 157)

| value | count |
|---|---|
| hand-written-per-game | 1 |
| ontology-generated | 2 |
| induced-from-data | 4 |
| learned-from-studio-usage | 6 |
| studio-written-at-runtime | 3 |
| genre-template-library | 4 |
| design-doc-patch-notes-store-page-derived | 1 |
| kpi-backward-from-studio-metrics | 1 |
| discriminative-contrast-churn-vs-retain | 0 |
| emergent-topic-clustering-of-player-speech | 0 |
| established-gur-frameworks-heuristics-pxi-mda | 0 |
| failed-query-log | 11 |
| few-shot-tracker-from-examples | 2 |
| onboarding-interview-with-studio | 0 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 0 |

### evidence-form (set on 89 of 157)

| value | count |
|---|---|
| none | 1 |
| quote-with-timestamp | 4 |
| clip | 5 |
| count-with-denominator | 10 |
| confidence-score | 6 |
| per-player-list | 2 |
| clip-montage-n-examples | 8 |
| contrast-vs-baseline | 11 |
| coverage-statement-n-of-m-players | 9 |
| extraction-provenance-model-and-schema-version | 30 |
| recall-estimate | 1 |
| chart | 1 |
| severity-frequency-matrix | 1 |

### effort (set on 155 of 157)

| value | count |
|---|---|
| S-weeks | 94 |
| M-one-quarter | 40 |
| L-multi-quarter | 0 |
| XS-days | 20 |
| buy-or-integrate | 1 |

### mechanism-type (set on 92 of 157)

| value | count |
|---|---|
| precompute-more | 10 |
| defer-to-query-time | 4 |
| reuse-or-cache-prior-work | 14 |
| approximate-then-refine | 1 |
| narrow-or-clarify-the-question | 3 |
| push-instead-of-pull | 22 |
| transfer-across-games | 9 |
| change-data-at-source | 11 |
| human-in-the-loop | 13 |
| auto-discover-without-question | 5 |

### user-segment (set on 92 of 157)

| value | count |
|---|---|
| studio-analyst | 10 |
| game-designer | 7 |
| ux-researcher | 5 |
| producer-exec | 4 |
| studio-data-engineer | 37 |
| live-ops-community | 2 |
| publisher-portfolio | 11 |
| platform-devrel | 0 |
| indie-solo-dev | 0 |
| jev-internal-ops | 16 |

### moment-in-journey (set on 66 of 157)

| value | count |
|---|---|
| game-onboarding-day-0 | 5 |
| first-cohort-ingested | 5 |
| first-studio-question | 2 |
| steady-state-weekly | 33 |
| new-build-version | 15 |
| pre-launch-greenlight | 1 |
| live-ops-update | 3 |
| renewal-review | 2 |

### delivery-surface (set on 78 of 157)

| value | count |
|---|---|
| chatbot | 2 |
| dashboard-standard-report | 11 |
| warehouse-share-or-export | 29 |
| api-sdk | 5 |
| notebook | 3 |
| slack-jira-integration | 2 |
| scheduled-digest | 11 |
| clip-reel | 4 |
| alert | 11 |

### subject-domain (set on 68 of 157)

| value | count |
|---|---|
| onboarding-tutorial | 43 |
| core-loop | 1 |
| progression-difficulty | 0 |
| economy-monetization | 0 |
| social-multiplayer | 0 |
| narrative | 0 |
| ui-navigation | 7 |
| technical-bugs-performance | 4 |
| accessibility | 0 |
| player-affect | 13 |

### tenancy-and-deployment (set on 38 of 157)

| value | count |
|---|---|
| shared-multi-tenant | 6 |
| logically-isolated-per-studio | 13 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 0 |
| export-only-no-hosting | 10 |
| federated-query-into-studio-warehouse | 9 |

### reuse-scope-of-extraction (set on 26 of 157)

| value | count |
|---|---|
| game-specific | 0 |
| genre-shared | 4 |
| universal-primitives | 10 |
| customer-defined-on-top-of-universal | 12 |

### schema-evolution (set on 64 of 157)

| value | count |
|---|---|
| frozen-schema | 3 |
| append-only-versioned-fields | 29 |
| schema-on-read | 3 |
| eager-backfill-all-history | 3 |
| lazy-backfill-on-demand | 5 |
| deprecate-and-migrate | 8 |
| model-upgrade-reextract | 13 |

### uncertainty-policy (set on 26 of 157)

| value | count |
|---|---|
| always-answer | 1 |
| answer-with-ci-and-n | 13 |
| abstain-below-coverage | 8 |
| ask-clarifying-question | 0 |
| give-range-then-refine | 1 |
| escalate-to-human-analyst | 3 |

### build-or-buy (set on 27 of 157)

| value | count |
|---|---|
| build-in-house | 2 |
| open-source-component | 8 |
| managed-cloud-service | 4 |
| third-party-video-understanding-api | 0 |
| studio-owned-stack | 13 |


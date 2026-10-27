# G-counts-3 (bucket 3, part = store, ideate run)

| measure | count |
|---|---|
| in (rows in G-bucket-3.yaml) | 107 |
| rejected (contract violations) | 0 |
| duplicate clusters | 14 |
| absorbed into a survivor (ids in `absorbed`, perspective slugs in `also_from`) | 20 |
| variants (survivors carrying `variants_of`) | 34 |
| refusal rows in bucket | 18 |
| refusal rows kept (`refusal: true`) | 12 |
| contested positives (carrying `contested_by`) | 13 |
| surviving | 87 |
| leaves with cell values added by normalisation | 87 (501 values, of which 28 inherited from absorbed duplicates' cells) |
| uncategorised | 0 |

## Rejected

None. Every row is L3/L4, names a spec.md, memo.md or A-frame object, and carries mechanism, example, cost, depends_on and the frame's extra fields (part, ingest_cost, query_cost, better_than_fixed_table). Banned-vocabulary hits checked: `such as` in vidsearch-2 (title, followed by `InternVideo2 or Marengo`) and vidsearch-7 (situation, followed by a quoted question); `improved` in obs-6 (example, followed by `from 6% to 14%`); `proper` in extract-30 (mechanism, `queue a proper field compile` after a stated 60% coverage threshold, read as naming the compile step). All cell values were already valid C-axes values. qgen-17's mechanism is `none (refused)`, accepted because it is a refusal row whose proposed/consequence carry the content.

## Duplicate clusters (survivor <- absorbed)

- latency-15 <- designer-1, store-5, analyst-2
- latency-1 <- store-6
- obs-1 <- store-2
- latency-16 <- store-22
- stitch-2 <- store-1
- clinical-13 <- qgen-32
- telem-15 <- store-20, datateam-32
- uxrepo-14 <- convo-13
- stitch-8 <- store-11
- analyst-18 <- uxrepo-24
- stitch-10 <- designer-10
- store-25 (refusal) <- obs-14, owner-8, longctx-7, telem-23
- obs-15 (refusal) <- designer-12
- extract-16 (refusal) <- qgen-17

## Variants (kept, `variants_of`)

- datateam-15 -> latency-15
- owner-31 -> latency-15
- obs-6 -> latency-15
- publisher-6 -> latency-15
- stat-13 -> latency-15
- cv-18 -> latency-15
- stitch-10 -> latency-15
- analyst-6 -> latency-1
- kg-4 -> latency-1
- publisher-2 -> latency-1
- publisher-19 -> publisher-2
- platform-3 -> publisher-19
- extract-30 -> obs-1
- eval-3 -> tar-15
- eval-19 -> clinical-13
- vidsearch-15 -> telem-15
- designer-20 -> telem-15
- uxrepo-14 -> telem-15
- privacy-27 -> uxrepo-14
- kg-30 -> stitch-8
- vidsearch-7 -> stitch-8
- vidsearch-2 -> cv-8
- vidsearch-19 -> vidsearch-2
- retr-4 -> store-30
- retr-9 -> store-30
- datateam-21 -> store-30
- sec-24 -> store-30
- clinical-16 -> store-23
- ops-17 -> analyst-18
- gur-14 -> gur-1
- telem-14 -> clinical-15
- uxrepo-1 -> convo-5
- analyst-31 -> store-25
- extract-16 -> obs-15

## Refusals kept and the positives they contest

- clinical-28: contests obs-1, extract-30
- extract-16 (absorbed qgen-17): contests none in this bucket
- kg-23: contests none in this bucket
- kg-24: contests none in this bucket
- longctx-31: contests cv-8, vidsearch-2, vidsearch-19, vidsearch-7
- obs-15 (absorbed designer-12): contests stitch-8, kg-30
- retr-14: contests none in this bucket
- store-25 (absorbed obs-14, owner-8, longctx-7, telem-23): contests kg-30, kg-1, kg-4
- store-26: contests none in this bucket
- store-27: contests stat-28
- analyst-31: contests kg-1
- telem-8: contests latency-15, analyst-6

## Leaves per perspective

| perspective | in | surviving | absorbed away |
|---|---|---|---|
| analyst | 4 | 3 | 1 |
| clinical | 7 | 7 | 0 |
| convo | 2 | 1 | 1 |
| cv | 2 | 2 | 0 |
| datateam | 3 | 2 | 1 |
| designer | 4 | 1 | 3 |
| eval | 3 | 3 | 0 |
| extract | 2 | 2 | 0 |
| gur | 3 | 3 | 0 |
| kg | 5 | 5 | 0 |
| latency | 6 | 6 | 0 |
| longctx | 2 | 1 | 1 |
| obs | 4 | 3 | 1 |
| ops | 1 | 1 | 0 |
| owner | 3 | 2 | 1 |
| platform | 1 | 1 | 0 |
| privacy | 2 | 2 | 0 |
| publisher | 3 | 3 | 0 |
| qgen | 3 | 1 | 2 |
| retr | 5 | 5 | 0 |
| sec | 3 | 3 | 0 |
| stat | 2 | 2 | 0 |
| stitch | 5 | 5 | 0 |
| store | 18 | 11 | 7 |
| tar | 1 | 1 | 0 |
| telem | 4 | 3 | 1 |
| uxrepo | 4 | 3 | 1 |
| vidsearch | 5 | 5 | 0 |
| total | 107 | 87 | 20 |

## Counts per axis value (normalised cells, surviving leaves; zero values listed)

### part (unset: 0)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 87 |
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

### representation (unset: 5)

| value | count |
|---|---|
| fixed-mcq-answers | 3 |
| timestamped-observation-log | 11 |
| entity-relation-graph | 7 |
| per-step-summary | 3 |
| per-session-summary | 3 |
| transcript-chunks-with-embeddings | 4 |
| learned-schema-from-data | 2 |
| raw-transcript-only | 2 |
| hybrid | 3 |
| wide-event-schema-on-read | 2 |
| inverted-full-text-index | 1 |
| olap-cube-materialized-views | 6 |
| step-funnel-state-machine-per-player | 11 |
| hierarchical-temporal-summary-tree | 3 |
| clip-or-frame-embeddings | 5 |
| time-series-signals-affect-pace-silence | 6 |
| customer-defined-trackers-over-universal-primitives | 1 |
| common-data-model-with-per-game-vocab-map | 4 |
| behaviour-archetype-clusters | 0 |
| issue-list-with-severity-frequency | 2 |
| question-answer-bank-precomputed | 3 |

### granularity (unset: 5)

| value | count |
|---|---|
| frame | 1 |
| utterance | 11 |
| tutorial-step | 16 |
| video | 6 |
| session | 18 |
| player | 11 |
| cohort | 1 |
| game | 2 |
| variable-length-moment-or-episode | 11 |
| level-quest-match-mission | 0 |
| game-system | 0 |
| build-version | 3 |
| player-segment-cluster | 0 |
| studio-portfolio | 2 |

### query-path (unset: 14)

| value | count |
|---|---|
| precomputed-aggregate | 15 |
| sql-over-closed-fields | 28 |
| retrieval-then-llm | 12 |
| lazy-backfill-extraction | 2 |
| map-reduce-over-raw | 2 |
| cached-prior-answer | 3 |
| clip-lookup | 2 |
| full-text-keyword-search | 3 |
| semantic-cache-similar-question | 0 |
| query-by-example-clip | 3 |
| automatic-contrast-cohort-diff | 1 |
| sampled-map-reduce-with-ci | 0 |
| progressive-answer-then-refine | 1 |
| agentic-multi-tool-plan | 1 |
| text-to-semantic-layer-metrics | 0 |
| human-analyst-escalation | 0 |
| push-alert-no-query | 0 |

### question-type (unset: 6)

| value | count |
|---|---|
| what-happened | 2 |
| when | 4 |
| how-long | 11 |
| how-many | 14 |
| why | 6 |
| how-felt | 6 |
| what-said | 7 |
| compare-versions | 1 |
| compare-steps | 5 |
| find-players-who | 15 |
| timeline | 2 |
| outside-game-target | 0 |
| what-surprised-unknown-unknowns | 2 |
| what-to-fix-first-prioritised | 1 |
| who-are-the-churners-segment-discovery | 2 |
| technical-issue-bug-perf | 0 |
| counterfactual-why-not | 0 |
| prevalence-of-quoted-sentiment | 1 |
| did-the-fix-work-pre-post | 2 |

### extraction-trigger (unset: 35)

| value | count |
|---|---|
| at-ingestion | 38 |
| on-first-question | 0 |
| scheduled-batch | 8 |
| on-game-update | 0 |
| on-model-upgrade | 3 |
| on-new-game-onboarding | 3 |
| on-new-field-added | 0 |
| on-low-confidence-or-disagreement | 0 |
| on-cohort-size-threshold | 0 |
| continuous-during-live-session | 0 |
| on-studio-tracker-defined | 0 |

### modality (unset: 18)

| value | count |
|---|---|
| speech-transcript | 21 |
| on-screen-text-ocr | 7 |
| screen-state-classifier | 11 |
| input-events | 0 |
| game-telemetry | 1 |
| audio-non-speech | 1 |
| webcam-face-and-posture | 0 |
| survey-or-in-game-prompt-response | 0 |
| player-profile-metadata | 5 |
| build-version-metadata | 13 |
| frame-embeddings | 4 |
| silence-or-absence-of-speech | 6 |
| controller-or-touch-heatmap | 0 |

### scope (unset: 28)

| value | count |
|---|---|
| one-player | 3 |
| cohort | 3 |
| all-players | 32 |
| cross-game | 7 |
| cross-studio-benchmark | 5 |
| query-time-defined-cohort | 5 |
| build-version-pair | 4 |

### latency-tier (unset: 44)

| value | count |
|---|---|
| under-2s | 21 |
| under-30s | 7 |
| minutes | 1 |
| overnight | 5 |
| progressive-streaming | 1 |
| push-no-query | 1 |
| sub-200ms-cached | 7 |

### question-origin (unset: 74)

| value | count |
|---|---|
| hand-written-per-game | 0 |
| ontology-generated | 0 |
| induced-from-data | 3 |
| learned-from-studio-usage | 4 |
| studio-written-at-runtime | 0 |
| genre-template-library | 2 |
| design-doc-patch-notes-store-page-derived | 0 |
| kpi-backward-from-studio-metrics | 1 |
| discriminative-contrast-churn-vs-retain | 1 |
| emergent-topic-clustering-of-player-speech | 0 |
| established-gur-frameworks-heuristics-pxi-mda | 1 |
| failed-query-log | 0 |
| few-shot-tracker-from-examples | 0 |
| onboarding-interview-with-studio | 1 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 0 |

### evidence-form (unset: 19)

| value | count |
|---|---|
| none | 2 |
| quote-with-timestamp | 8 |
| clip | 10 |
| count-with-denominator | 16 |
| confidence-score | 4 |
| per-player-list | 1 |
| clip-montage-n-examples | 2 |
| contrast-vs-baseline | 8 |
| coverage-statement-n-of-m-players | 2 |
| extraction-provenance-model-and-schema-version | 8 |
| recall-estimate | 0 |
| chart | 6 |
| severity-frequency-matrix | 1 |

### effort (unset: 0)

| value | count |
|---|---|
| S-weeks | 52 |
| M-one-quarter | 23 |
| L-multi-quarter | 4 |
| XS-days | 7 |
| buy-or-integrate | 1 |

### mechanism-type (unset: 20)

| value | count |
|---|---|
| precompute-more | 40 |
| defer-to-query-time | 7 |
| reuse-or-cache-prior-work | 7 |
| approximate-then-refine | 1 |
| narrow-or-clarify-the-question | 0 |
| push-instead-of-pull | 2 |
| transfer-across-games | 7 |
| change-data-at-source | 0 |
| human-in-the-loop | 1 |
| auto-discover-without-question | 2 |

### user-segment (unset: 56)

| value | count |
|---|---|
| studio-analyst | 4 |
| game-designer | 11 |
| ux-researcher | 0 |
| producer-exec | 3 |
| studio-data-engineer | 9 |
| live-ops-community | 0 |
| publisher-portfolio | 3 |
| platform-devrel | 0 |
| indie-solo-dev | 0 |
| jev-internal-ops | 1 |

### moment-in-journey (unset: 73)

| value | count |
|---|---|
| game-onboarding-day-0 | 4 |
| first-cohort-ingested | 0 |
| first-studio-question | 0 |
| steady-state-weekly | 1 |
| new-build-version | 8 |
| pre-launch-greenlight | 0 |
| live-ops-update | 0 |
| renewal-review | 1 |

### delivery-surface (unset: 44)

| value | count |
|---|---|
| chatbot | 25 |
| dashboard-standard-report | 3 |
| warehouse-share-or-export | 11 |
| api-sdk | 0 |
| notebook | 1 |
| slack-jira-integration | 0 |
| scheduled-digest | 3 |
| clip-reel | 0 |
| alert | 0 |

### subject-domain (unset: 20)

| value | count |
|---|---|
| onboarding-tutorial | 40 |
| core-loop | 2 |
| progression-difficulty | 1 |
| economy-monetization | 0 |
| social-multiplayer | 0 |
| narrative | 0 |
| ui-navigation | 6 |
| technical-bugs-performance | 2 |
| accessibility | 1 |
| player-affect | 15 |

### tenancy-and-deployment (unset: 73)

| value | count |
|---|---|
| shared-multi-tenant | 5 |
| logically-isolated-per-studio | 8 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 0 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 1 |

### reuse-scope-of-extraction (unset: 73)

| value | count |
|---|---|
| game-specific | 2 |
| genre-shared | 4 |
| universal-primitives | 5 |
| customer-defined-on-top-of-universal | 3 |

### schema-evolution (unset: 60)

| value | count |
|---|---|
| frozen-schema | 1 |
| append-only-versioned-fields | 10 |
| schema-on-read | 5 |
| eager-backfill-all-history | 0 |
| lazy-backfill-on-demand | 3 |
| deprecate-and-migrate | 2 |
| model-upgrade-reextract | 6 |

### uncertainty-policy (unset: 74)

| value | count |
|---|---|
| always-answer | 2 |
| answer-with-ci-and-n | 8 |
| abstain-below-coverage | 3 |
| ask-clarifying-question | 0 |
| give-range-then-refine | 0 |
| escalate-to-human-analyst | 0 |

### build-or-buy (unset: 67)

| value | count |
|---|---|
| build-in-house | 1 |
| open-source-component | 14 |
| managed-cloud-service | 3 |
| third-party-video-understanding-api | 2 |
| studio-owned-stack | 0 |


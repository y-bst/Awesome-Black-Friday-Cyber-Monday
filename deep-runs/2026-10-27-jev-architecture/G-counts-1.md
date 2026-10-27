# G-counts-1 (bucket 1, part = query-path, ideate run)

| measure | count |
|---|---|
| in (rows in G-bucket-1.yaml) | 175 |
| rejected (contract violations) | 0 |
| duplicate clusters | 13 |
| absorbed into a survivor (ids in `absorbed`, perspective slugs in `also_from`) | 22 |
| variants (survivors carrying `variants_of`) | 70 |
| refusal rows in (willingness low or titled refused) | 22 |
| refusal rows kept (`refusal: true`) | 17 |
| contested positives (carrying `contested_by`) | 22 |
| surviving | 153 |
| uncategorised | 0 |
| leaves with cell values added by normalisation | 150 (669 values: 27 carried over from absorbed rows, the rest from C-axes matching on title/situation/mechanism and `cost` -> `effort`) |

## Rejected

None. All 175 rows are L3/L4, point at a spec.md or memo.md object, and carry mechanism, example, cost and depends_on. Banned-word hits each have a concrete instance on the same line: `such as cube or dbt metrics` (askdata-5), `such as 'that smelting thing'` (retr-3), `improves by at least 15 points` (retr-11), `Handles compound questions` (latency-14). `proper noun` (retr-3), `handles only questions that are asked` (obs-3, obs-11), `improved` (analyst-25) and `improve (a)` (vidsearch-22, a spec quote) are descriptive uses, not vague claims. Top-level `part: query` (107 rows) and `part: query-path` (68 rows) are left as written, since the frame's `part` field allows `query`. `cell.part` is `query-path` on all rows.

## Refusal rule applied

A row is a refusal when its title says REFUSE/REFUSED/REFUSAL/Refused (19 rows), when its `willingness` is `low` (sec-7, sec-20), or when its title says "Low willingness" (obs-16, willingness 0.3 in its consequence). Guard rows that withhold a number under a stated condition (askdata-2, askdata-21, gur-3, analyst-10, privacy-7, analyst-25, tar-21) are positive options, not refusals.

## Duplicate clusters (survivor <- absorbed)

- askdata-5 <- planner-10, analyst-29, platform-31
- askdata-7 <- publisher-27
- designer-4 <- planner-16, analyst-7
- latency-2 <- convo-22, retr-20, store-13
- obs-3 <- planner-17, latency-29
- owner-20 (refusal) <- latency-13, analyst-11, designer-13
- planner-2 <- analyst-10
- planner-5 <- obs-23
- planner-6 <- askdata-14
- planner-11 (refusal) <- latency-14
- planner-14 <- obs-2
- retr-13 (refusal) <- clinical-29
- vidsearch-3 <- convo-28, uxrepo-22

## Variants (kept, `variants_of`)

- askdata-2 -> planner-2
- askdata-16 -> owner-20
- clinical-19 -> obs-3
- convo-12 -> planner-14
- convo-20 -> owner-20
- tar-5 -> retr-13
- tar-11 -> planner-14
- tar-18 -> stat-3
- eval-28 -> askdata-21
- designer-14 -> obs-3
- designer-22 -> gur-18
- gur-3 -> stat-1
- kg-10 -> askdata-5
- kg-12 -> obs-3
- kg-20 -> designer-4
- kg-26 -> planner-5
- latency-5 -> planner-6
- latency-31 -> retr-12
- latency-32 -> latency-2
- longctx-3 -> planner-6
- longctx-10 -> analyst-15
- longctx-13 -> latency-2
- longctx-14 -> planner-14
- longctx-23 -> planner-3
- longctx-24 -> designer-4
- obs-4 -> latency-5
- obs-11 -> obs-3
- obs-22 -> latency-25
- platform-5 -> obs-10
- platform-19 -> designer-4
- platform-22 -> latency-25
- privacy-7 -> askdata-2
- owner-16 -> obs-3
- publisher-17 -> obs-3
- publisher-25 -> owner-20
- planner-7 -> planner-2
- planner-29 -> owner-20
- qgen-6 -> planner-5
- qgen-8 -> planner-9
- retr-10 -> planner-9
- retr-12 -> longctx-6
- retr-15 -> tar-22
- retr-18 -> obs-3
- retr-27 -> tar-11
- retr-31 -> tar-11
- stitch-32 -> longctx-3
- stat-3 -> longctx-3
- stat-4 -> planner-6
- stat-6 -> obs-3
- stat-12 -> designer-4
- stat-15 -> latency-2
- stat-18 -> gur-32
- stat-25 -> obs-3
- store-14 -> planner-6
- analyst-9 -> retr-3
- analyst-17 -> obs-3
- analyst-25 -> askdata-21
- analyst-26 -> stat-19
- analyst-28 -> latency-4
- datateam-14 -> sec-31
- sec-7 -> latency-2
- sec-22 -> askdata-25
- sec-23 -> latency-2
- telem-4 -> tar-14
- telem-16 -> designer-4
- telem-28 -> askdata-5
- uxrepo-13 -> gur-18
- uxrepo-15 -> planner-14
- vidsearch-11 -> qgen-25
- vidsearch-22 -> designer-4, vidsearch-3

## Refusals kept and the positives they contest

- askdata-16: contests longctx-1, longctx-24
- askdata-28: contests obs-10, obs-11, platform-5, platform-19
- convo-20: contests longctx-1, longctx-10
- tar-5: contests analyst-9, analyst-28
- tar-6: contests latency-2, longctx-13
- kg-9: contests telem-19, vidsearch-11
- kg-31: contests none in this bucket
- obs-16: contests retr-3, analyst-9
- platform-13: contests askdata-25, sec-22
- owner-20: contests longctx-1, longctx-6, longctx-10, longctx-23, longctx-24
- publisher-25: contests none in this bucket
- planner-11: contests qgen-8, retr-10
- planner-29: contests longctx-1, longctx-10, longctx-23
- retr-13: contests analyst-9, analyst-28
- stitch-30: contests none in this bucket
- sec-7: contests platform-22
- sec-20: contests platform-5, stat-20

## Leaves per perspective (surviving)

| perspective | in | surviving | absorbed away |
|---|---|---|---|
| analyst | 10 | 6 | 4 |
| askdata | 9 | 8 | 1 |
| clinical | 4 | 3 | 1 |
| convo | 4 | 2 | 2 |
| cv | 1 | 1 | 0 |
| datateam | 1 | 1 | 0 |
| designer | 6 | 5 | 1 |
| eval | 4 | 4 | 0 |
| gur | 5 | 5 | 0 |
| kg | 7 | 7 | 0 |
| latency | 11 | 8 | 3 |
| longctx | 9 | 9 | 0 |
| obs | 8 | 6 | 2 |
| owner | 2 | 2 | 0 |
| planner | 20 | 17 | 3 |
| platform | 5 | 4 | 1 |
| privacy | 4 | 4 | 0 |
| publisher | 4 | 3 | 1 |
| qgen | 3 | 3 | 0 |
| retr | 13 | 12 | 1 |
| sec | 7 | 7 | 0 |
| stat | 11 | 11 | 0 |
| stitch | 3 | 3 | 0 |
| store | 2 | 1 | 1 |
| tar | 8 | 8 | 0 |
| telem | 6 | 6 | 0 |
| uxrepo | 4 | 3 | 1 |
| vidsearch | 4 | 4 | 0 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### part (unset: 0)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 0 |
| query-path | 153 |
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

### representation (unset: 67)

| value | count |
|---|---|
| fixed-mcq-answers | 7 |
| timestamped-observation-log | 17 |
| entity-relation-graph | 8 |
| per-step-summary | 0 |
| per-session-summary | 0 |
| transcript-chunks-with-embeddings | 4 |
| learned-schema-from-data | 1 |
| raw-transcript-only | 7 |
| hybrid | 2 |
| wide-event-schema-on-read | 1 |
| inverted-full-text-index | 7 |
| olap-cube-materialized-views | 8 |
| step-funnel-state-machine-per-player | 9 |
| hierarchical-temporal-summary-tree | 0 |
| clip-or-frame-embeddings | 1 |
| time-series-signals-affect-pace-silence | 1 |
| customer-defined-trackers-over-universal-primitives | 1 |
| common-data-model-with-per-game-vocab-map | 3 |
| behaviour-archetype-clusters | 2 |
| issue-list-with-severity-frequency | 3 |
| question-answer-bank-precomputed | 4 |

### granularity (unset: 25)

| value | count |
|---|---|
| frame | 0 |
| utterance | 7 |
| tutorial-step | 56 |
| video | 1 |
| session | 24 |
| player | 8 |
| cohort | 8 |
| game | 0 |
| variable-length-moment-or-episode | 5 |
| level-quest-match-mission | 0 |
| game-system | 1 |
| build-version | 11 |
| player-segment-cluster | 2 |
| studio-portfolio | 5 |

### query-path (unset: 12)

| value | count |
|---|---|
| precomputed-aggregate | 10 |
| sql-over-closed-fields | 22 |
| retrieval-then-llm | 15 |
| lazy-backfill-extraction | 10 |
| map-reduce-over-raw | 11 |
| cached-prior-answer | 5 |
| clip-lookup | 2 |
| full-text-keyword-search | 9 |
| semantic-cache-similar-question | 9 |
| query-by-example-clip | 2 |
| automatic-contrast-cohort-diff | 15 |
| sampled-map-reduce-with-ci | 8 |
| progressive-answer-then-refine | 5 |
| agentic-multi-tool-plan | 6 |
| text-to-semantic-layer-metrics | 5 |
| human-analyst-escalation | 3 |
| push-alert-no-query | 4 |

### question-type (unset: 29)

| value | count |
|---|---|
| what-happened | 0 |
| when | 3 |
| how-long | 5 |
| how-many | 32 |
| why | 10 |
| how-felt | 4 |
| what-said | 9 |
| compare-versions | 1 |
| compare-steps | 3 |
| find-players-who | 15 |
| timeline | 5 |
| outside-game-target | 8 |
| what-surprised-unknown-unknowns | 4 |
| what-to-fix-first-prioritised | 2 |
| who-are-the-churners-segment-discovery | 7 |
| technical-issue-bug-perf | 0 |
| counterfactual-why-not | 1 |
| prevalence-of-quoted-sentiment | 5 |
| did-the-fix-work-pre-post | 10 |

### extraction-trigger (unset: 105)

| value | count |
|---|---|
| at-ingestion | 7 |
| on-first-question | 22 |
| scheduled-batch | 13 |
| on-game-update | 3 |
| on-model-upgrade | 0 |
| on-new-game-onboarding | 0 |
| on-new-field-added | 0 |
| on-low-confidence-or-disagreement | 1 |
| on-cohort-size-threshold | 1 |
| continuous-during-live-session | 0 |
| on-studio-tracker-defined | 1 |

### modality (unset: 94)

| value | count |
|---|---|
| speech-transcript | 31 |
| on-screen-text-ocr | 2 |
| screen-state-classifier | 3 |
| input-events | 0 |
| game-telemetry | 6 |
| audio-non-speech | 0 |
| webcam-face-and-posture | 0 |
| survey-or-in-game-prompt-response | 0 |
| player-profile-metadata | 1 |
| build-version-metadata | 12 |
| frame-embeddings | 2 |
| silence-or-absence-of-speech | 2 |
| controller-or-touch-heatmap | 0 |

### scope (unset: 65)

| value | count |
|---|---|
| one-player | 3 |
| cohort | 23 |
| all-players | 30 |
| cross-game | 5 |
| cross-studio-benchmark | 2 |
| query-time-defined-cohort | 14 |
| build-version-pair | 11 |

### latency-tier (unset: 54)

| value | count |
|---|---|
| under-2s | 34 |
| under-30s | 25 |
| minutes | 10 |
| overnight | 4 |
| progressive-streaming | 7 |
| push-no-query | 6 |
| sub-200ms-cached | 13 |

### question-origin (unset: 128)

| value | count |
|---|---|
| hand-written-per-game | 0 |
| ontology-generated | 1 |
| induced-from-data | 1 |
| learned-from-studio-usage | 3 |
| studio-written-at-runtime | 1 |
| genre-template-library | 1 |
| design-doc-patch-notes-store-page-derived | 0 |
| kpi-backward-from-studio-metrics | 2 |
| discriminative-contrast-churn-vs-retain | 7 |
| emergent-topic-clustering-of-player-speech | 2 |
| established-gur-frameworks-heuristics-pxi-mda | 2 |
| failed-query-log | 2 |
| few-shot-tracker-from-examples | 2 |
| onboarding-interview-with-studio | 1 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 0 |

### evidence-form (unset: 54)

| value | count |
|---|---|
| none | 0 |
| quote-with-timestamp | 8 |
| clip | 7 |
| count-with-denominator | 24 |
| confidence-score | 2 |
| per-player-list | 9 |
| clip-montage-n-examples | 3 |
| contrast-vs-baseline | 21 |
| coverage-statement-n-of-m-players | 13 |
| extraction-provenance-model-and-schema-version | 2 |
| recall-estimate | 5 |
| chart | 3 |
| severity-frequency-matrix | 2 |

### effort (unset: 0)

| value | count |
|---|---|
| S-weeks | 94 |
| M-one-quarter | 47 |
| L-multi-quarter | 1 |
| XS-days | 11 |
| buy-or-integrate | 0 |

### mechanism-type (unset: 33)

| value | count |
|---|---|
| precompute-more | 8 |
| defer-to-query-time | 23 |
| reuse-or-cache-prior-work | 18 |
| approximate-then-refine | 16 |
| narrow-or-clarify-the-question | 29 |
| push-instead-of-pull | 5 |
| transfer-across-games | 1 |
| change-data-at-source | 0 |
| human-in-the-loop | 5 |
| auto-discover-without-question | 15 |

### user-segment (unset: 78)

| value | count |
|---|---|
| studio-analyst | 25 |
| game-designer | 20 |
| ux-researcher | 4 |
| producer-exec | 8 |
| studio-data-engineer | 4 |
| live-ops-community | 2 |
| publisher-portfolio | 4 |
| platform-devrel | 1 |
| indie-solo-dev | 3 |
| jev-internal-ops | 4 |

### moment-in-journey (unset: 129)

| value | count |
|---|---|
| game-onboarding-day-0 | 1 |
| first-cohort-ingested | 2 |
| first-studio-question | 0 |
| steady-state-weekly | 8 |
| new-build-version | 10 |
| pre-launch-greenlight | 1 |
| live-ops-update | 2 |
| renewal-review | 0 |

### delivery-surface (unset: 114)

| value | count |
|---|---|
| chatbot | 22 |
| dashboard-standard-report | 6 |
| warehouse-share-or-export | 0 |
| api-sdk | 1 |
| notebook | 0 |
| slack-jira-integration | 3 |
| scheduled-digest | 1 |
| clip-reel | 3 |
| alert | 3 |

### subject-domain (unset: 57)

| value | count |
|---|---|
| onboarding-tutorial | 83 |
| core-loop | 0 |
| progression-difficulty | 0 |
| economy-monetization | 1 |
| social-multiplayer | 0 |
| narrative | 0 |
| ui-navigation | 3 |
| technical-bugs-performance | 0 |
| accessibility | 0 |
| player-affect | 9 |

### tenancy-and-deployment (unset: 135)

| value | count |
|---|---|
| shared-multi-tenant | 2 |
| logically-isolated-per-studio | 14 |
| single-tenant | 1 |
| studio-vpc-or-on-prem | 0 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 1 |

### reuse-scope-of-extraction (unset: 136)

| value | count |
|---|---|
| game-specific | 7 |
| genre-shared | 6 |
| universal-primitives | 2 |
| customer-defined-on-top-of-universal | 2 |

### schema-evolution (unset: 119)

| value | count |
|---|---|
| frozen-schema | 0 |
| append-only-versioned-fields | 10 |
| schema-on-read | 1 |
| eager-backfill-all-history | 1 |
| lazy-backfill-on-demand | 20 |
| deprecate-and-migrate | 2 |
| model-upgrade-reextract | 0 |

### uncertainty-policy (unset: 88)

| value | count |
|---|---|
| always-answer | 8 |
| answer-with-ci-and-n | 24 |
| abstain-below-coverage | 19 |
| ask-clarifying-question | 3 |
| give-range-then-refine | 7 |
| escalate-to-human-analyst | 4 |

### build-or-buy (unset: 134)

| value | count |
|---|---|
| build-in-house | 0 |
| open-source-component | 15 |
| managed-cloud-service | 2 |
| third-party-video-understanding-api | 0 |
| studio-owned-stack | 2 |


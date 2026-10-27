# G-counts-5 (bucket 5, parts = chatbot-ui and evaluation, ideate run)

| measure | count |
|---|---|
| in (rows in G-bucket-5.yaml) | 174 (chatbot-ui 94, evaluation 80) |
| rejected (contract violations) | 0 |
| duplicate clusters | 16 |
| absorbed into a survivor (ids in `absorbed`, perspective slugs in `also_from`) | 21 |
| variants (survivors carrying `variants_of`) | 69 |
| refusal rows kept (`refusal: true`) | 13 (14 refusal rows in, analyst-13 absorbed into refusal stat-14) |
| contested positives (carrying `contested_by`) | 16 |
| surviving | 153 |
| leaves with cell values added by normalisation | 150 (542 values; plus 29 values inherited by survivors from absorbed rows) |
| uncategorised | 0 |

Validation: G-merged-5.yaml parses with yaml.safe_load; every one of the 174 bucket ids is either a kept row (153) or listed in a survivor's `absorbed` (21); none rejected; every `variants_of` and `contested_by` target is a kept id.

## Rejected

None. Every row is L3/L4, names a spec.md, memo.md, A-frame or B-perspectives object, and carries mechanism, example, cost, depends_on. Banned-word hits are quotes of the artifact or followed by an instance on the same line: `improve` in quotes of spec.md (clinical-27, obs-21 object/evidence), in a studio question (publisher-14 example) and `to improve the affect field` (extract-29 situation); `such as` followed by quoted instances (privacy-21 example, eval-32 title). Notes: top-level `part` was normalised to the A-frame enum (`chatbot-ui` -> `ui`, 44 rows); `_from_file` dropped and `perspective` added on every row.

## Duplicate clusters (survivor <- absorbed)

- askdata-1 <- uxrepo-17, analyst-3
- askdata-3 <- analyst-21
- designer-3 <- analyst-5, obs-28
- stitch-29 <- designer-5, analyst-34
- clinical-18 <- owner-5, analyst-30
- askdata-22 <- latency-22
- eval-21 <- askdata-10
- clinical-27 <- askdata-12
- longctx-27 <- latency-17
- tar-1 <- eval-9
- qgen-35 <- planner-31, retr-21
- extract-23 <- uxrepo-32
- eval-4 <- extract-29
- sec-4 <- eval-32
- ops-3 <- gur-12
- stat-14 (refusal) <- analyst-13

## Variants (leaf -> variants_of)

- askdata-4 -> owner-19
- askdata-18 -> ops-3
- askdata-27 -> stat-2
- askdata-29 -> askdata-23
- convo-26 -> eval-30
- convo-29 -> askdata-22
- tar-16 -> tar-1
- tar-30 -> stat-14
- eval-7 -> askdata-3
- designer-23 -> askdata-22
- designer-24 -> stat-2
- gur-11 -> stitch-29
- gur-17 -> designer-3
- kg-22 -> askdata-3
- longctx-29 -> retr-28
- platform-2 -> clinical-18
- platform-9 -> owner-19
- platform-16 -> designer-17
- platform-20 -> designer-3
- platform-28 -> askdata-22
- privacy-21 -> gur-27
- owner-18 -> eval-21
- publisher-16 -> designer-3
- planner-22 -> askdata-1
- planner-25 -> askdata-6
- planner-28 -> askdata-6
- qgen-26 -> clinical-27
- retr-7 -> askdata-1
- retr-30 -> designer-3
- stitch-23 -> planner-25
- stat-23 -> askdata-11
- analyst-14 -> publisher-32
- datateam-6 -> publisher-32
- sec-10 -> privacy-20
- telem-9 -> stat-14
- telem-27 -> clinical-18
- telem-30 -> askdata-23
- uxrepo-2 -> designer-3
- uxrepo-16 -> askdata-11
- vidsearch-30 -> askdata-1
- askdata-19 -> stat-26
- askdata-20 -> tar-1
- clinical-6 -> tar-1
- clinical-26 -> eval-4
- convo-10 -> clinical-6
- cv-23 -> eval-1
- tar-10 -> clinical-10
- tar-26 -> ops-3
- tar-29 -> tar-1
- eval-26 -> clinical-17
- extract-22 -> eval-7
- extract-23 -> clinical-10
- designer-29 -> eval-15
- kg-21 -> eval-1
- longctx-9 -> extract-4
- platform-34 -> analyst-32
- publisher-7 -> designer-24
- publisher-30 -> clinical-10
- planner-8 -> askdata-1
- planner-21 -> sec-4
- planner-34 -> askdata-8
- qgen-9 -> clinical-10
- qgen-29 -> planner-34
- qgen-35 -> tar-1
- store-31 -> eval-30
- datateam-20 -> clinical-17
- datateam-28 -> extract-23
- telem-10 -> extract-36
- telem-21 -> extract-36

## Refusals kept and the positives they contest

- tar-30: contests retr-28
- publisher-32: contests none in this bucket
- stat-14: contests none in this bucket
- stat-29: contests none in this bucket
- analyst-14: contests none in this bucket
- datateam-6: contests none in this bucket
- sec-28: contests designer-23
- telem-9: contests none in this bucket
- uxrepo-20: contests platform-2, convo-8, publisher-26, platform-16, clinical-18
- tar-24: contests eval-33, platform-2
- eval-16: contests qgen-35, clinical-10, publisher-30, qgen-9, extract-4
- ops-32: contests analyst-32, platform-34, platform-2, platform-28, publisher-26
- telem-24: contests none in this bucket

Refusal rule: rows titled REFUSE/REFUSED (13) plus sec-28 (willingness: low; its consequence refuses posting quotes and clips into Slack). Not refusals despite the word: askdata-29 (a counterfactual-refusal answer card, positive option), planner-22 (renderer refuses null n), gur-16 (refuses auto-publishing as part of a positive triage gate), eval-7 (refuses evidence-less answers).

## Contested positives

- clinical-18: contested_by uxrepo-20
- convo-8: contested_by uxrepo-20
- designer-23: contested_by sec-28
- platform-2: contested_by uxrepo-20, tar-24, ops-32
- platform-16: contested_by uxrepo-20
- platform-28: contested_by ops-32
- publisher-26: contested_by uxrepo-20, ops-32
- retr-28: contested_by tar-30
- clinical-10: contested_by eval-16
- eval-33: contested_by tar-24
- extract-4: contested_by eval-16
- platform-34: contested_by ops-32
- publisher-30: contested_by eval-16
- qgen-9: contested_by eval-16
- qgen-35: contested_by eval-16
- analyst-32: contested_by ops-32

## Leaves per perspective

| perspective | surviving | absorbed away |
|---|---|---|
| analyst | 3 | 6 |
| askdata | 14 | 2 |
| clinical | 8 | 0 |
| convo | 5 | 0 |
| cv | 2 | 0 |
| datateam | 4 | 0 |
| designer | 5 | 1 |
| eval | 13 | 2 |
| extract | 4 | 1 |
| gur | 4 | 1 |
| kg | 3 | 0 |
| latency | 0 | 2 |
| longctx | 5 | 0 |
| obs | 2 | 1 |
| ops | 3 | 0 |
| owner | 5 | 1 |
| planner | 8 | 1 |
| platform | 7 | 0 |
| privacy | 3 | 0 |
| publisher | 6 | 0 |
| qgen | 7 | 0 |
| retr | 4 | 1 |
| sec | 3 | 0 |
| stat | 8 | 0 |
| stitch | 3 | 0 |
| store | 2 | 0 |
| tar | 8 | 0 |
| telem | 6 | 0 |
| uxrepo | 4 | 2 |
| vidsearch | 4 | 0 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### part (unset: 0)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 0 |
| query-path | 0 |
| question-generation | 0 |
| evaluation | 73 |
| chatbot-ui | 80 |
| session-stitching | 0 |
| frame-pipeline | 0 |
| collection-protocol | 0 |
| tenancy-access-control | 0 |
| export-integration | 0 |
| feedback-loop-from-query-log | 0 |
| cost-governance | 0 |
| schema-evolution | 0 |

### representation (unset: 103)

| value | count |
|---|---|
| fixed-mcq-answers | 4 |
| timestamped-observation-log | 14 |
| entity-relation-graph | 3 |
| per-step-summary | 0 |
| per-session-summary | 0 |
| transcript-chunks-with-embeddings | 0 |
| learned-schema-from-data | 0 |
| raw-transcript-only | 0 |
| hybrid | 0 |
| wide-event-schema-on-read | 0 |
| inverted-full-text-index | 0 |
| olap-cube-materialized-views | 1 |
| step-funnel-state-machine-per-player | 6 |
| hierarchical-temporal-summary-tree | 0 |
| clip-or-frame-embeddings | 2 |
| time-series-signals-affect-pace-silence | 3 |
| customer-defined-trackers-over-universal-primitives | 5 |
| common-data-model-with-per-game-vocab-map | 2 |
| behaviour-archetype-clusters | 1 |
| issue-list-with-severity-frequency | 4 |
| question-answer-bank-precomputed | 5 |

### granularity (unset: 33)

| value | count |
|---|---|
| frame | 2 |
| utterance | 6 |
| tutorial-step | 47 |
| video | 0 |
| session | 30 |
| player | 8 |
| cohort | 2 |
| game | 14 |
| variable-length-moment-or-episode | 5 |
| level-quest-match-mission | 0 |
| game-system | 0 |
| build-version | 4 |
| player-segment-cluster | 1 |
| studio-portfolio | 1 |

### query-path (unset: 86)

| value | count |
|---|---|
| precomputed-aggregate | 5 |
| sql-over-closed-fields | 12 |
| retrieval-then-llm | 10 |
| lazy-backfill-extraction | 6 |
| map-reduce-over-raw | 5 |
| cached-prior-answer | 1 |
| clip-lookup | 9 |
| full-text-keyword-search | 0 |
| semantic-cache-similar-question | 0 |
| query-by-example-clip | 0 |
| automatic-contrast-cohort-diff | 1 |
| sampled-map-reduce-with-ci | 8 |
| progressive-answer-then-refine | 2 |
| agentic-multi-tool-plan | 0 |
| text-to-semantic-layer-metrics | 3 |
| human-analyst-escalation | 2 |
| push-alert-no-query | 3 |

### question-type (unset: 58)

| value | count |
|---|---|
| what-happened | 7 |
| when | 1 |
| how-long | 3 |
| how-many | 29 |
| why | 5 |
| how-felt | 7 |
| what-said | 3 |
| compare-versions | 8 |
| compare-steps | 4 |
| find-players-who | 8 |
| timeline | 3 |
| outside-game-target | 2 |
| what-surprised-unknown-unknowns | 0 |
| what-to-fix-first-prioritised | 4 |
| who-are-the-churners-segment-discovery | 3 |
| technical-issue-bug-perf | 2 |
| counterfactual-why-not | 2 |
| prevalence-of-quoted-sentiment | 1 |
| did-the-fix-work-pre-post | 3 |

### extraction-trigger (unset: 99)

| value | count |
|---|---|
| at-ingestion | 4 |
| on-first-question | 6 |
| scheduled-batch | 7 |
| on-game-update | 2 |
| on-model-upgrade | 14 |
| on-new-game-onboarding | 8 |
| on-new-field-added | 1 |
| on-low-confidence-or-disagreement | 8 |
| on-cohort-size-threshold | 2 |
| continuous-during-live-session | 1 |
| on-studio-tracker-defined | 1 |

### modality (unset: 110)

| value | count |
|---|---|
| speech-transcript | 12 |
| on-screen-text-ocr | 6 |
| screen-state-classifier | 6 |
| input-events | 0 |
| game-telemetry | 8 |
| audio-non-speech | 0 |
| webcam-face-and-posture | 0 |
| survey-or-in-game-prompt-response | 0 |
| player-profile-metadata | 0 |
| build-version-metadata | 0 |
| frame-embeddings | 0 |
| silence-or-absence-of-speech | 10 |
| controller-or-touch-heatmap | 1 |

### scope (unset: 83)

| value | count |
|---|---|
| one-player | 4 |
| cohort | 10 |
| all-players | 29 |
| cross-game | 12 |
| cross-studio-benchmark | 4 |
| query-time-defined-cohort | 4 |
| build-version-pair | 7 |

### latency-tier (unset: 104)

| value | count |
|---|---|
| under-2s | 21 |
| under-30s | 7 |
| minutes | 2 |
| overnight | 7 |
| progressive-streaming | 3 |
| push-no-query | 5 |
| sub-200ms-cached | 4 |

### question-origin (unset: 125)

| value | count |
|---|---|
| hand-written-per-game | 1 |
| ontology-generated | 8 |
| induced-from-data | 1 |
| learned-from-studio-usage | 4 |
| studio-written-at-runtime | 4 |
| genre-template-library | 3 |
| design-doc-patch-notes-store-page-derived | 0 |
| kpi-backward-from-studio-metrics | 1 |
| discriminative-contrast-churn-vs-retain | 0 |
| emergent-topic-clustering-of-player-speech | 0 |
| established-gur-frameworks-heuristics-pxi-mda | 0 |
| failed-query-log | 4 |
| few-shot-tracker-from-examples | 0 |
| onboarding-interview-with-studio | 0 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 2 |

### evidence-form (unset: 23)

| value | count |
|---|---|
| none | 1 |
| quote-with-timestamp | 9 |
| clip | 7 |
| count-with-denominator | 15 |
| confidence-score | 16 |
| per-player-list | 2 |
| clip-montage-n-examples | 15 |
| contrast-vs-baseline | 6 |
| coverage-statement-n-of-m-players | 19 |
| extraction-provenance-model-and-schema-version | 13 |
| recall-estimate | 16 |
| chart | 8 |
| severity-frequency-matrix | 3 |

### effort (unset: 0)

| value | count |
|---|---|
| S-weeks | 83 |
| M-one-quarter | 37 |
| L-multi-quarter | 0 |
| XS-days | 33 |
| buy-or-integrate | 0 |

### mechanism-type (unset: 69)

| value | count |
|---|---|
| precompute-more | 7 |
| defer-to-query-time | 4 |
| reuse-or-cache-prior-work | 5 |
| approximate-then-refine | 5 |
| narrow-or-clarify-the-question | 19 |
| push-instead-of-pull | 6 |
| transfer-across-games | 3 |
| change-data-at-source | 1 |
| human-in-the-loop | 32 |
| auto-discover-without-question | 2 |

### user-segment (unset: 35)

| value | count |
|---|---|
| studio-analyst | 24 |
| game-designer | 23 |
| ux-researcher | 10 |
| producer-exec | 22 |
| studio-data-engineer | 6 |
| live-ops-community | 0 |
| publisher-portfolio | 7 |
| platform-devrel | 0 |
| indie-solo-dev | 3 |
| jev-internal-ops | 23 |

### moment-in-journey (unset: 105)

| value | count |
|---|---|
| game-onboarding-day-0 | 3 |
| first-cohort-ingested | 7 |
| first-studio-question | 8 |
| steady-state-weekly | 17 |
| new-build-version | 5 |
| pre-launch-greenlight | 4 |
| live-ops-update | 0 |
| renewal-review | 4 |

### delivery-surface (unset: 58)

| value | count |
|---|---|
| chatbot | 52 |
| dashboard-standard-report | 20 |
| warehouse-share-or-export | 3 |
| api-sdk | 0 |
| notebook | 0 |
| slack-jira-integration | 2 |
| scheduled-digest | 5 |
| clip-reel | 11 |
| alert | 2 |

### subject-domain (unset: 70)

| value | count |
|---|---|
| onboarding-tutorial | 81 |
| core-loop | 0 |
| progression-difficulty | 0 |
| economy-monetization | 0 |
| social-multiplayer | 0 |
| narrative | 0 |
| ui-navigation | 0 |
| technical-bugs-performance | 1 |
| accessibility | 0 |
| player-affect | 1 |

### tenancy-and-deployment (unset: 142)

| value | count |
|---|---|
| shared-multi-tenant | 5 |
| logically-isolated-per-studio | 6 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 0 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 0 |

### reuse-scope-of-extraction (unset: 137)

| value | count |
|---|---|
| game-specific | 0 |
| genre-shared | 6 |
| universal-primitives | 4 |
| customer-defined-on-top-of-universal | 6 |

### schema-evolution (unset: 134)

| value | count |
|---|---|
| frozen-schema | 0 |
| append-only-versioned-fields | 7 |
| schema-on-read | 0 |
| eager-backfill-all-history | 0 |
| lazy-backfill-on-demand | 6 |
| deprecate-and-migrate | 0 |
| model-upgrade-reextract | 6 |

### uncertainty-policy (unset: 64)

| value | count |
|---|---|
| always-answer | 6 |
| answer-with-ci-and-n | 38 |
| abstain-below-coverage | 25 |
| ask-clarifying-question | 9 |
| give-range-then-refine | 5 |
| escalate-to-human-analyst | 6 |

### build-or-buy (unset: 148)

| value | count |
|---|---|
| build-in-house | 2 |
| open-source-component | 1 |
| managed-cloud-service | 1 |
| third-party-video-understanding-api | 0 |
| studio-owned-stack | 1 |


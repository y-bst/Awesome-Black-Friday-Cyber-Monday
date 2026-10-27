# G-counts-7 (bucket 7, parts: tenancy-access-control, collection-protocol, cost-governance, frame-pipeline)

| metric | count |
|---|---|
| in | 141 |
| rejected | 0 |
| duplicate clusters | 12 |
| ids merged into a survivor | 15 |
| leaves carrying variants_of | 48 |
| refusal rows kept (`refusal: true`) | 15 |
| positives contested by a refusal | 15 |
| surviving | 126 |
| leaves with cell values added by normalisation | 108 (values added: 214) |
| uncategorised | 0 |

Normalisation note: of the 214 added values, 20 are cell axes carried over from absorbed duplicates (survivor lacked the axis); the rest come from title/situation keyword rules against C-axes.yaml, `effort` from `cost` (S/M/L), and `mechanism-type: change-data-at-source` on collection-protocol leaves with no mechanism-type. Per-leaf log: /tmp/claude-0/-home-user-Awesome-Black-Friday-Cyber-Monday/8c4d0f6f-5baa-5821-9e40-eb597d4120fe/scratchpad/jev/ig7/norm-log.yaml.

## Rejected

none. Every item is L3/L4, names a spec.md, memo.md, A-frame.yaml or B-perspectives.yaml object, and carries mechanism, example, cost and depends_on. Banned-word hits are all followed by an instance on the same line (`such as sighs per step per player`, `such as 'looking for the quest guy'`) or are quoted studio questions (`did step-3 completion improve`, `did the stealth step stall rate improve`) or the noun `handles` (extract-35, tar-7 `[HANDLE_3]`). Notes: sec-32 cites sibling leaves (sec-1, sec-11, sec-16) beside spec.md; kept because the spec quote is the anchor.

## Duplicate clusters (survivor <- merged)

- askdata-17 (refusal) <- publisher-12, latency-24, planner-20
- datateam-26 (refusal) <- clinical-30
- platform-12 (refusal) <- owner-33
- vidsearch-25 (refusal) <- cv-15
- privacy-9 <- telem-32
- sec-9 <- privacy-23
- ops-4 <- designer-28, uxrepo-31
- ops-14 <- gur-13
- ops-10 <- gur-26
- ops-1 <- stitch-14
- obs-5 <- store-21
- platform-14 <- askdata-15

## Variants (leaf -> variants_of)

- datateam-7 -> askdata-17
- gur-25 -> datateam-26
- kg-27 -> store-29
- obs-26 -> store-29
- retr-24 -> store-29
- longctx-25 -> store-29
- convo-30 -> store-29
- convo-18 -> publisher-33
- clinical-21 -> publisher-11
- telem-2 -> privacy-9
- datateam-4 -> telem-2
- clinical-22 -> sec-9
- stat-30 -> clinical-22
- privacy-22 -> sec-9
- sec-16 -> privacy-22
- extract-35 -> tar-7
- cv-17 -> tar-7
- longctx-30 -> cv-17
- sec-17 -> privacy-3
- sec-19 -> ops-9
- datateam-12 -> sec-12
- sec-2 -> privacy-15
- ops-23 -> privacy-4
- ops-30 -> ops-2
- telem-18 -> ops-11
- platform-10 -> ops-11
- stat-17 -> ops-11
- platform-6 -> ops-1
- planner-33 -> stitch-26
- publisher-31 -> stitch-26
- publisher-29 -> clinical-4
- ops-29 -> ops-12
- tar-17 -> platform-14, tar-4
- latency-6 -> platform-14
- obs-31 -> latency-6
- publisher-23 -> platform-14
- stitch-21 -> convo-9
- uxrepo-30 -> obs-5
- privacy-10 -> obs-5
- extract-31 -> telem-31
- owner-17 -> extract-31
- latency-27 -> cv-1
- stitch-28 -> cv-1
- vidsearch-18 -> cv-1
- designer-15 -> owner-30
- longctx-28 -> telem-20
- kg-5 -> designer-16
- gur-31 -> designer-8

## Refusals kept and the positives they contest

- askdata-17: contests none in this bucket
- gur-25: contests convo-18, publisher-33, kg-27, store-29, clinical-21
- platform-12: contests sec-12, datateam-12
- datateam-7: contests privacy-17, owner-13, convo-30
- datateam-26: contests clinical-21, kg-27
- gur-7: contests none in this bucket
- ops-5: contests ops-2, ops-30
- ops-23: contests none in this bucket
- ops-24: contests none in this bucket
- privacy-4: contests none in this bucket
- obs-13: contests extract-31, telem-31
- retr-32: contests none in this bucket
- vidsearch-25: contests none in this bucket
- privacy-15: contests retr-19
- sec-2: contests retr-19

Refusal-vs-refusal collisions (no contested_by written, both are refusal rows): askdata-17 cluster and datateam-7 refuse the shared cross-tenant layers that platform-12 (refusal of VPC-by-default) argues for; ops-23 (webcam opt-in arm up to 20%) and privacy-4 (no webcam at all) disagree on the opt-in arm.

## Leaves per perspective (surviving)

| perspective | surviving | merged away |
|---|---|---|
| analyst | 1 | 0 |
| askdata | 1 | 1 |
| clinical | 4 | 1 |
| convo | 5 | 0 |
| cv | 2 | 1 |
| datateam | 6 | 0 |
| designer | 3 | 1 |
| eval | 2 | 0 |
| extract | 5 | 0 |
| gur | 4 | 2 |
| kg | 3 | 0 |
| latency | 3 | 1 |
| longctx | 5 | 0 |
| obs | 5 | 0 |
| ops | 18 | 0 |
| owner | 4 | 1 |
| planner | 1 | 1 |
| platform | 4 | 0 |
| privacy | 9 | 1 |
| publisher | 6 | 1 |
| retr | 3 | 0 |
| sec | 8 | 0 |
| stat | 2 | 0 |
| stitch | 3 | 1 |
| store | 3 | 1 |
| tar | 4 | 0 |
| telem | 4 | 1 |
| uxrepo | 3 | 1 |
| vidsearch | 5 | 0 |

## Counts per axis value (surviving leaves, normalised cells; zero values listed)

### part (unset: 0)

| value | count |
|---|---|
| ingestion-extraction | 0 |
| store | 0 |
| query-path | 0 |
| question-generation | 0 |
| evaluation | 0 |
| chatbot-ui | 0 |
| session-stitching | 0 |
| frame-pipeline | 28 |
| collection-protocol | 34 |
| tenancy-access-control | 33 |
| export-integration | 0 |
| feedback-loop-from-query-log | 0 |
| cost-governance | 31 |
| schema-evolution | 0 |

### representation (unset: 90)

| value | count |
|---|---|
| fixed-mcq-answers | 1 |
| timestamped-observation-log | 9 |
| entity-relation-graph | 1 |
| per-step-summary | 0 |
| per-session-summary | 0 |
| transcript-chunks-with-embeddings | 0 |
| learned-schema-from-data | 0 |
| raw-transcript-only | 3 |
| hybrid | 0 |
| wide-event-schema-on-read | 3 |
| inverted-full-text-index | 0 |
| olap-cube-materialized-views | 1 |
| step-funnel-state-machine-per-player | 1 |
| hierarchical-temporal-summary-tree | 1 |
| clip-or-frame-embeddings | 6 |
| time-series-signals-affect-pace-silence | 3 |
| customer-defined-trackers-over-universal-primitives | 1 |
| common-data-model-with-per-game-vocab-map | 2 |
| behaviour-archetype-clusters | 0 |
| issue-list-with-severity-frequency | 2 |
| question-answer-bank-precomputed | 2 |

### granularity (unset: 44)

| value | count |
|---|---|
| frame | 20 |
| utterance | 7 |
| tutorial-step | 16 |
| video | 3 |
| session | 13 |
| player | 3 |
| cohort | 1 |
| game | 2 |
| variable-length-moment-or-episode | 5 |
| level-quest-match-mission | 0 |
| game-system | 0 |
| build-version | 6 |
| player-segment-cluster | 0 |
| studio-portfolio | 6 |

### query-path (unset: 105)

| value | count |
|---|---|
| precomputed-aggregate | 2 |
| sql-over-closed-fields | 1 |
| retrieval-then-llm | 2 |
| lazy-backfill-extraction | 4 |
| map-reduce-over-raw | 3 |
| cached-prior-answer | 0 |
| clip-lookup | 0 |
| full-text-keyword-search | 0 |
| semantic-cache-similar-question | 4 |
| query-by-example-clip | 2 |
| automatic-contrast-cohort-diff | 0 |
| sampled-map-reduce-with-ci | 2 |
| progressive-answer-then-refine | 0 |
| agentic-multi-tool-plan | 1 |
| text-to-semantic-layer-metrics | 0 |
| human-analyst-escalation | 0 |
| push-alert-no-query | 0 |

### question-type (unset: 87)

| value | count |
|---|---|
| what-happened | 1 |
| when | 0 |
| how-long | 0 |
| how-many | 6 |
| why | 5 |
| how-felt | 5 |
| what-said | 0 |
| compare-versions | 8 |
| compare-steps | 0 |
| find-players-who | 3 |
| timeline | 0 |
| outside-game-target | 0 |
| what-surprised-unknown-unknowns | 0 |
| what-to-fix-first-prioritised | 1 |
| who-are-the-churners-segment-discovery | 1 |
| technical-issue-bug-perf | 4 |
| counterfactual-why-not | 3 |
| prevalence-of-quoted-sentiment | 0 |
| did-the-fix-work-pre-post | 2 |

### extraction-trigger (unset: 64)

| value | count |
|---|---|
| at-ingestion | 25 |
| on-first-question | 9 |
| scheduled-batch | 1 |
| on-game-update | 1 |
| on-model-upgrade | 2 |
| on-new-game-onboarding | 8 |
| on-new-field-added | 5 |
| on-low-confidence-or-disagreement | 0 |
| on-cohort-size-threshold | 3 |
| continuous-during-live-session | 6 |
| on-studio-tracker-defined | 2 |

### modality (unset: 55)

| value | count |
|---|---|
| speech-transcript | 7 |
| on-screen-text-ocr | 10 |
| screen-state-classifier | 9 |
| input-events | 4 |
| game-telemetry | 2 |
| audio-non-speech | 2 |
| webcam-face-and-posture | 2 |
| survey-or-in-game-prompt-response | 5 |
| player-profile-metadata | 11 |
| build-version-metadata | 6 |
| frame-embeddings | 9 |
| silence-or-absence-of-speech | 3 |
| controller-or-touch-heatmap | 1 |

### scope (unset: 72)

| value | count |
|---|---|
| one-player | 2 |
| cohort | 13 |
| all-players | 11 |
| cross-game | 7 |
| cross-studio-benchmark | 13 |
| query-time-defined-cohort | 2 |
| build-version-pair | 6 |

### latency-tier (unset: 100)

| value | count |
|---|---|
| under-2s | 4 |
| under-30s | 4 |
| minutes | 7 |
| overnight | 5 |
| progressive-streaming | 0 |
| push-no-query | 2 |
| sub-200ms-cached | 4 |

### question-origin (unset: 118)

| value | count |
|---|---|
| hand-written-per-game | 0 |
| ontology-generated | 0 |
| induced-from-data | 0 |
| learned-from-studio-usage | 1 |
| studio-written-at-runtime | 0 |
| genre-template-library | 2 |
| design-doc-patch-notes-store-page-derived | 1 |
| kpi-backward-from-studio-metrics | 0 |
| discriminative-contrast-churn-vs-retain | 0 |
| emergent-topic-clustering-of-player-speech | 0 |
| established-gur-frameworks-heuristics-pxi-mda | 1 |
| failed-query-log | 0 |
| few-shot-tracker-from-examples | 0 |
| onboarding-interview-with-studio | 2 |
| public-reviews-and-community-mining | 0 |
| pilot-sessions-then-freeze | 1 |

### evidence-form (unset: 88)

| value | count |
|---|---|
| none | 0 |
| quote-with-timestamp | 1 |
| clip | 4 |
| count-with-denominator | 7 |
| confidence-score | 0 |
| per-player-list | 0 |
| clip-montage-n-examples | 1 |
| contrast-vs-baseline | 6 |
| coverage-statement-n-of-m-players | 14 |
| extraction-provenance-model-and-schema-version | 3 |
| recall-estimate | 0 |
| chart | 2 |
| severity-frequency-matrix | 0 |

### effort (unset: 3)

| value | count |
|---|---|
| S-weeks | 51 |
| M-one-quarter | 41 |
| L-multi-quarter | 5 |
| XS-days | 26 |
| buy-or-integrate | 0 |

### mechanism-type (unset: 41)

| value | count |
|---|---|
| precompute-more | 7 |
| defer-to-query-time | 10 |
| reuse-or-cache-prior-work | 7 |
| approximate-then-refine | 7 |
| narrow-or-clarify-the-question | 7 |
| push-instead-of-pull | 2 |
| transfer-across-games | 4 |
| change-data-at-source | 35 |
| human-in-the-loop | 6 |
| auto-discover-without-question | 0 |

### user-segment (unset: 58)

| value | count |
|---|---|
| studio-analyst | 4 |
| game-designer | 8 |
| ux-researcher | 6 |
| producer-exec | 4 |
| studio-data-engineer | 11 |
| live-ops-community | 0 |
| publisher-portfolio | 12 |
| platform-devrel | 0 |
| indie-solo-dev | 3 |
| jev-internal-ops | 20 |

### moment-in-journey (unset: 96)

| value | count |
|---|---|
| game-onboarding-day-0 | 12 |
| first-cohort-ingested | 4 |
| first-studio-question | 0 |
| steady-state-weekly | 3 |
| new-build-version | 4 |
| pre-launch-greenlight | 0 |
| live-ops-update | 1 |
| renewal-review | 6 |

### delivery-surface (unset: 103)

| value | count |
|---|---|
| chatbot | 10 |
| dashboard-standard-report | 5 |
| warehouse-share-or-export | 4 |
| api-sdk | 1 |
| notebook | 0 |
| slack-jira-integration | 0 |
| scheduled-digest | 2 |
| clip-reel | 0 |
| alert | 1 |

### subject-domain (unset: 84)

| value | count |
|---|---|
| onboarding-tutorial | 25 |
| core-loop | 0 |
| progression-difficulty | 3 |
| economy-monetization | 0 |
| social-multiplayer | 2 |
| narrative | 0 |
| ui-navigation | 6 |
| technical-bugs-performance | 2 |
| accessibility | 1 |
| player-affect | 3 |

### tenancy-and-deployment (unset: 91)

| value | count |
|---|---|
| shared-multi-tenant | 8 |
| logically-isolated-per-studio | 23 |
| single-tenant | 0 |
| studio-vpc-or-on-prem | 3 |
| export-only-no-hosting | 0 |
| federated-query-into-studio-warehouse | 1 |

### reuse-scope-of-extraction (unset: 105)

| value | count |
|---|---|
| game-specific | 2 |
| genre-shared | 10 |
| universal-primitives | 7 |
| customer-defined-on-top-of-universal | 2 |

### schema-evolution (unset: 108)

| value | count |
|---|---|
| frozen-schema | 0 |
| append-only-versioned-fields | 1 |
| schema-on-read | 1 |
| eager-backfill-all-history | 1 |
| lazy-backfill-on-demand | 14 |
| deprecate-and-migrate | 0 |
| model-upgrade-reextract | 1 |

### uncertainty-policy (unset: 103)

| value | count |
|---|---|
| always-answer | 1 |
| answer-with-ci-and-n | 5 |
| abstain-below-coverage | 11 |
| ask-clarifying-question | 1 |
| give-range-then-refine | 5 |
| escalate-to-human-analyst | 0 |

### build-or-buy (unset: 101)

| value | count |
|---|---|
| build-in-house | 9 |
| open-source-component | 4 |
| managed-cloud-service | 7 |
| third-party-video-understanding-api | 3 |
| studio-owned-stack | 2 |


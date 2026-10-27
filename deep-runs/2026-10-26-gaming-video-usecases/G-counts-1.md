# Stage G counts, bucket 1

Buyer roles: analytics-bi, product-retention, engineering-performance. Cells were normalised against C-axes.yaml before counting; a leaf can carry several values per axis, so per-axis counts can sum to more than the surviving total.

| measure | count |
|---|---|
| in | 174 |
| rejected | 1 |
| duplicate clusters | 13 |
| leaves absorbed into clusters | 14 |
| leaves with `variants_of` | 66 |
| positive options with `contested_by` | 5 |
| refusal leaves kept (`refusal: true`) | 26 |
| surviving | 159 |
| leaves with cell values added in normalisation | 158 (969 values added) |

## Rejected

| id | rule broken |
|---|---|
| bi-29 | category rather than a concrete option: refuses seat pricing for "a video-insight product" (no product named), input "none"; the concrete seat-licence refusal survives as publisher-14 |

## Duplicate clusters

| survivor | also_from | why the same option |
|---|---|---|
| ds-5 | bi-5, player-3 | same propensity reweighting of captured vs all installs for the analytics/DS buyer |
| ds-4 | bi-8 | same anchor-screen clock offset per session; both deliver per-session offset rows |
| ds-2 | bi-4 | same last-10 s-before-app-kill classifier written as a session column |
| ds-1 | bi-13 | same per-session video feature table for the churn model; bi-13 adds the holdout-AUC harness |
| ds-11 | sdk-2 | same on-device screen classifier uploading label rows plus 3 keyframes |
| sdk-12 | cto-28 | same vendor inference stack deployed in the AAA studio account reading QA footage in place |
| bi-15 | ua-27 | same MMP creative/install id joined to first-session video states in the warehouse |
| sdk-1 | f2p-2 | same on-device ring buffer uploaded only on FTUE/fail triggers for the product lead |
| cto-2 | sdk-3 | same self-measuring SDK that stops capture on p95 frame-cost or thermal breach |
| sdk-8 | privacy-30 | same tested EAC/BattlEye compatibility list for the capture SDK |
| cto-1 | sdk-4 | same zero-SDK emulator/platform-host capture with per-title FTUE reports, product lead pays |
| ds-21 | bi-31 | same refused prose-only ask-a-question chat over footage |
| f2p-22 | sdk-27 | same refused full-rate 720p recording of every session/install |

## Contested (positive option, refusal from another perspective)

| positive option | wtp | contested_by | refusal title |
|---|---|---|---|
| ds-7: Pixel-only arousal curve per session (no face cam) aggregated to features: arousal slope o | 2 | bi-26 | REFUSE: per-session emotion or arousal score from gameplay pixels as a numeric column |
| sdk-1: Churn-trigger ring buffer - 90 s on-device H.264 buffer at 480p/1.5 Mbps (about 17 MB) tha | 3 | player-27 | Always-on ring buffer on every player's device from install (refused): footage of all sessions held  |
| cto-1: Zero-binary capture from the emulator compositor: 1 fps 480p clips of opted-in players, ga | 4 | oem-24 | FTUE funnel why-dashboard for studios, offered by the OEM as a free perk: the OEM resells per-sessio |
| indie-3: AI watcher layer on top of a 100-video/month session-replay quota: summarise each of 100 v | 4 | ds-21 | REFUSED: generic 'ask a question over all sessions' chat that answers in prose without per-session s |
| indie-3: AI watcher layer on top of a 100-video/month session-replay quota: summarise each of 100 v | 4 | cfo-13 | REFUSED: generic 'upload sessions, get AI summaries' dashboard at $20k/year that a BI analyst can re |
| ds-23: Closed-loop fail-loop intervention with a built-in 10% holdout: on-device detector sees 3  | 3 | indie-26 | REFUSE: closed-loop gift to predicted churners (auto-send currency when the video model says a rage  |

## Variants (same mechanism, different buyer, input or delivery form)

| root | variants |
|---|---|
| ds-5 | sdk-14, f2p-20 |
| bi-2 | ds-27, ds-3, f2p-4 |
| ds-4 | sdk-15 |
| ds-2 | ds-15, ds-22, f2p-5, indie-17, f2p-27 |
| ds-22 | f2p-15 |
| ds-1 | ds-12, f2p-7 |
| ds-11 | cto-20 |
| ds-10 | bi-18 |
| bi-6 | bi-17 |
| ds-14 | bi-10, f2p-3 |
| ds-16 | bi-11, f2p-8 |
| ds-24 | bi-19 |
| player-7 | privacy-16 |
| sdk-12 | bi-20 |
| bi-1 | publisher-15 |
| publisher-15 | ds-19 |
| bi-3 | indie-8 |
| bi-14 | publisher-10 |
| sdk-1 | bi-9, publisher-8, cto-5 |
| cto-5 | sdk-7 |
| cto-2 | player-5, sdk-10 |
| sdk-25 | bi-22, f2p-6, publisher-21, platform-4, oem-14 |
| cto-15 | oem-1 |
| cto-29 | platform-3, oem-2 |
| cto-18 | oem-18 |
| oem-3 | cto-17 |
| cto-1 | publisher-9 |
| f2p-10 | f2p-26 |
| bi-16 | f2p-10 |
| cto-11 | player-19 |
| player-9 | privacy-26 |
| player-8 | privacy-6 |
| indie-9 | publisher-20 |
| publisher-20 | loc-19 |
| f2p-1 | f2p-13 |
| f2p-12 | publisher-25 |
| ds-23 | f2p-11 |
| ds-7 | f2p-25 |
| cfo-13 | bi-25 |
| ds-21 | cfo-13 |
| bi-28 | f2p-23, ds-20 |
| ds-8 | bi-27, f2p-21, cto-23 |
| f2p-22 | cto-8 |
| oem-4 | platform-5 |
| player-1 | sdk-5 |

## Leaves per source perspective (surviving)

| perspective | survivors |
|---|---|
| f2p-product-lead | 26 |
| data-scientist | 24 |
| in-house-analytics-head | 24 |
| cto-or-engine-lead-veto | 22 |
| device-oem-chip-vendor | 13 |
| sdk-platform-engineer | 11 |
| player-opt-in | 10 |
| publisher-portfolio-manager | 10 |
| privacy-regulator-counsel | 6 |
| indie-solo-dev | 5 |
| platform-owner | 3 |
| esports-coach | 2 |
| localisation-lead | 1 |
| studio-cfo | 1 |
| studio-ciso-security-review | 1 |

## buyer-role

| value | leaves |
|---|---|
| product-retention | 60 |
| ua-marketing | 2 |
| qa | 3 |
| live-ops | 1 |
| design-balance | 0 |
| monetisation | 3 |
| competitive-intel | 2 |
| player-support | 0 |
| trust-safety | 0 |
| finance-exec | 3 |
| platform-owner | 0 |
| ux-research | 3 |
| localisation | 2 |
| accessibility-compliance | 0 |
| rating-and-consumer-compliance | 0 |
| certification-release | 0 |
| engineering-performance | 52 |
| analytics-bi | 63 |
| community-and-creator-marketing | 4 |
| esports-team-or-league | 0 |
| publishing-scout-bd | 0 |
| ad-network-ops | 0 |
| brand-advertiser | 0 |
| data-buyer-training | 0 |
| data-buyer-market-intel | 0 |
| investor | 0 |
| white-label-vendor | 0 |
| outsourced-qa-vendor | 0 |
| (no value) | 0 |

## video-source

| value | leaves |
|---|---|
| own-players-consented-sdk | 99 |
| recruited-playtesters | 2 |
| platform-or-emulator-capture | 13 |
| public-streams-and-ugc | 2 |
| competitor-store-and-ad-video | 0 |
| internal-qa-builds | 10 |
| esports-vod | 0 |
| support-ticket-attachment | 0 |
| cloud-gaming-server-render | 2 |
| automated-bot-or-agent-playthrough | 14 |
| beta-and-early-access-testers | 3 |
| console-share-and-platform-clips | 2 |
| creator-sponsored-streams | 0 |
| ad-and-playable-ad-sessions | 2 |
| outsourced-tester-rigs | 1 |
| publisher-pitch-builds | 0 |
| (no value) | 19 |

## analysis-type

| value | leaves |
|---|---|
| funnel-drop-off-why | 33 |
| churn-prediction-features | 31 |
| root-cause-of-a-metric-change | 9 |
| benchmark-vs-competitor | 14 |
| anomaly-alert | 18 |
| highlight-or-clip-generation | 0 |
| bug-reproduction | 6 |
| compliance-audit | 12 |
| creative-insight-for-ads | 2 |
| coaching-feedback | 0 |
| training-dataset-export | 5 |
| cohort-comparison | 28 |
| ask-a-question-over-footage | 15 |
| build-to-build-regression-diff | 17 |
| ab-test-variant-explanation | 7 |
| ad-verification-and-fraud | 1 |
| content-rating-classification | 0 |
| early-ltv-or-payer-prediction | 2 |
| real-time-in-session-intervention | 6 |
| automated-test-generation | 0 |
| creative-generation-from-gameplay | 0 |
| evidence-pack-for-enforcement | 1 |
| (no value) | 9 |

## delivery-form

| value | leaves |
|---|---|
| dashboard | 26 |
| alert-or-slack | 9 |
| per-cohort-report | 31 |
| api-or-sdk | 34 |
| clip-reel | 1 |
| in-tool-annotation | 3 |
| managed-service-with-analyst | 3 |
| licensed-dataset | 0 |
| warehouse-table-export | 45 |
| issue-tracker-ticket | 14 |
| engine-editor-plugin | 5 |
| ask-question-agent-chat | 8 |
| generated-creative-files | 0 |
| enforcement-or-cert-evidence-pack | 3 |
| white-label-embed | 0 |
| weekly-digest-email | 2 |
| (no value) | 9 |

## pricing-model

| value | leaves |
|---|---|
| per-session | 25 |
| per-month-seat | 3 |
| per-game | 11 |
| per-mau | 1 |
| revenue-share | 0 |
| managed-project | 5 |
| free-with-platform | 2 |
| per-hour-of-video | 2 |
| per-build-or-release | 3 |
| outcome-based-per-bug-or-uplift | 1 |
| annual-enterprise-licence | 8 |
| oem-royalty-or-white-label | 1 |
| cpm-or-per-impression-verified | 0 |
| data-licence-per-hour | 0 |
| freemium-self-serve | 5 |
| per-audit-or-certification | 0 |
| (no value) | 103 |

## value-lever-b2b

| value | leaves |
|---|---|
| replace-labour-hours | 4 |
| increase-coverage-from-sample-to-all | 16 |
| cut-time-to-insight | 22 |
| create-data-that-did-not-exist | 12 |
| de-risk-a-go-kill-decision | 15 |
| avoid-fine-or-cert-failure | 17 |
| produce-a-sellable-asset | 3 |
| reduce-cost-per-incident | 13 |
| enable-automated-action | 13 |
| (no value) | 74 |

## buyer-org-type

| value | leaves |
|---|---|
| indie-studio | 7 |
| mid-size-studio | 32 |
| aaa-studio | 10 |
| publisher | 17 |
| platform-or-store | 3 |
| ad-network-or-dsp | 0 |
| analytics-or-mmp-vendor | 0 |
| outsourced-services-vendor | 1 |
| agency | 0 |
| brand-advertiser | 0 |
| data-or-market-intel-buyer | 0 |
| investor | 0 |
| device-oem | 15 |
| regulator-or-rating-body | 0 |
| (no value) | 80 |

## Uncategorised

0 leaves carry `uncategorised: true`.


## Refusal leaves kept (refusal: true)

cto-4, cto-8, cto-9, cto-21, cto-22, cto-23, ds-8, ds-20, ds-21, oem-16, oem-24, f2p-21, f2p-22, f2p-23, bi-25, bi-26, bi-27, bi-28, bi-30, indie-26, player-14, player-22, player-27, publisher-14, sdk-28, cfo-13

Tagging rule: willingness_to_pay 1, plus publisher-14 (wtp 2, but the row records a refused seat licence). cto-27 and f2p-24/f2p-25 carry REFUSED/LOW titles but describe a bought option at wtp 2, so they are not tagged.

## Normalisation method

Values were added only from C-axes.yaml, by matching each leaf's own text per axis: buyer-role and buyer-org-type from `buyer`; video-source and companion-data from `input`; signal-extracted, analysis-type and automation-level from `title` + `mechanism`; delivery-form from `title` + `mechanism` + `proposed`; pricing-model from `title` + `mechanism` + `proposed` + `example` (comparator prices in `willingness_to_pay` were not used); effort from `cost` (S/M/L/XS) plus partner wording in `depends_on`. `evidence` and `why_existing_tools_cannot` were not used, because they describe other vendors. Cluster survivors also take the union of their absorbed members' cells. Null cell values were dropped.

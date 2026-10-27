# Stage G counts, bucket 4

Buyer roles: player-support, rating-and-consumer-compliance, certification-release, community-and-creator-marketing, white-label-vendor.

| Measure | Count |
|---|---|
| In | 172 |
| Rejected | 0 |
| Duplicate clusters | 6 |
| Items absorbed into clusters | 8 |
| Variants (rows with variants_of) | 47 |
| Contested (positive rows with contested_by) | 0 |
| Refusal rows (refusal: true) | 28 |
| Leaves with cell values added in normalisation | 129 |
| Uncategorised | 0 |
| Surviving | 164 |

## Rejected

None. All 172 items name a buyer, a mechanism and a concrete example. The banned-vocabulary scan found one hit: support-2 situation, "handling budget". It is followed by a number on the same line ("4 to 6 minutes"), so it passes. Kept, with notes: privacy-9, privacy-10, privacy-29 and vendor-15 are concrete enablers whose input is configuration or consent events, not video. rating-21 is kept with `shallow: true`.

## Duplicate clusters (survivor <- absorbed)

- support-1 <- player-18, cfo-10: last-60-s ring buffer attached to the helpdesk ticket on "Contact support", head of player support
- rating-1 <- privacy-28, cfo-16: bot walks paid random-item paths per build and checks the odds are shown before confirm, compliance or legal at an F2P publisher
- rating-6 <- cert-8: rating questionnaire (IARC/ESRB/PEGI) answers evidenced or cross-checked from a full playthrough, release or compliance lead at a publisher
- cert-17 <- player-15: recording-indicator and consent-prompt rendering audit on QA footage per build, release manager at a studio shipping a capture SDK
- vendor-5 <- support-24: ring-buffer clip plus AI summary sold as an add-on to a game helpdesk vendor (Helpshift class)
- vendor-1 <- sdk-16: capture module embedded in an analytics or MMP SDK that answers "why" on a funnel step

## Contested

0. No refusal is an exact duplicate (same buyer, same mechanism, same input) of a positive option. Eight refusal rows are variants of positive options, which is the nearest disagreement signal in this bucket:

- vendor-21 (refusal) variants_of vendor-1 (positive)
- vendor-23 (refusal) variants_of vendor-1 (positive)
- vendor-24 (refusal) variants_of vendor-1 (positive)
- cert-18 (refusal) variants_of cert-6 (positive)
- creator-27 (refusal) variants_of vendor-19 (positive)
- privacy-14 (refusal) variants_of privacy-15 (positive)
- rating-24 (refusal) variants_of platform-10 (positive)
- rating-26 (refusal) variants_of support-1 (positive)

The strongest of these is creator-27, where the community persona refuses to sell gameplay footage to world-model labs, while vendor-19 rates the same data-licensing mechanism WTP 4 as an SDK-vendor brokerage. The buyer and the input differ (creator VODs against SDK-consented gameplay plus input), so the rows are not merged.

## Refusal rows

vendor-21, vendor-22, vendor-23, vendor-24, cert-18, cert-19, cert-25, cert-26, cert-27, cert-28, creator-19, creator-24, creator-25, creator-26, creator-27, loc-22, player-6, support-21, support-27, support-28, support-29, privacy-14, rating-21, rating-24, rating-25, rating-26, rating-27, rating-28

## Counts per value (surviving rows, normalised cells; a row with several values counts once per value)

### buyer-role

| Value | Count |
|---|---|
| community-and-creator-marketing | 37 |
| player-support | 35 |
| certification-release | 34 |
| rating-and-consumer-compliance | 33 |
| white-label-vendor | 31 |
| monetisation | 7 |
| ua-marketing | 6 |
| qa | 6 |
| platform-owner | 5 |
| live-ops | 4 |
| outsourced-qa-vendor | 4 |
| data-buyer-market-intel | 3 |
| finance-exec | 3 |
| localisation | 2 |
| accessibility-compliance | 1 |
| engineering-performance | 1 |
| publishing-scout-bd | 1 |

### video-source

| Value | Count |
|---|---|
| own-players-consented-sdk | 63 |
| internal-qa-builds | 34 |
| automated-bot-or-agent-playthrough | 28 |
| support-ticket-attachment | 19 |
| public-streams-and-ugc | 18 |
| creator-sponsored-streams | 10 |
| console-share-and-platform-clips | 5 |
| outsourced-tester-rigs | 5 |
| competitor-store-and-ad-video | 4 |
| platform-or-emulator-capture | 3 |
| ad-and-playable-ad-sessions | 2 |
| beta-and-early-access-testers | 2 |
| esports-vod | 1 |
| publisher-pitch-builds | 1 |
| recruited-playtesters | 1 |

### analysis-type

| Value | Count |
|---|---|
| compliance-audit | 48 |
| bug-reproduction | 21 |
| highlight-or-clip-generation | 15 |
| anomaly-alert | 14 |
| ask-a-question-over-footage | 11 |
| (none) | 8 |
| build-to-build-regression-diff | 8 |
| funnel-drop-off-why | 7 |
| benchmark-vs-competitor | 7 |
| evidence-pack-for-enforcement | 7 |
| root-cause-of-a-metric-change | 6 |
| ad-verification-and-fraud | 5 |
| creative-insight-for-ads | 4 |
| early-ltv-or-payer-prediction | 4 |
| cohort-comparison | 4 |
| content-rating-classification | 4 |
| churn-prediction-features | 3 |
| creative-generation-from-gameplay | 3 |
| real-time-in-session-intervention | 3 |
| training-dataset-export | 2 |
| automated-test-generation | 2 |
| ab-test-variant-explanation | 1 |
| coaching-feedback | 1 |

### delivery-form

| Value | Count |
|---|---|
| issue-tracker-ticket | 26 |
| api-or-sdk | 21 |
| enforcement-or-cert-evidence-pack | 20 |
| in-tool-annotation | 17 |
| alert-or-slack | 14 |
| per-cohort-report | 13 |
| white-label-embed | 12 |
| dashboard | 12 |
| weekly-digest-email | 11 |
| (none) | 10 |
| clip-reel | 8 |
| ask-question-agent-chat | 6 |
| generated-creative-files | 5 |
| warehouse-table-export | 2 |
| licensed-dataset | 2 |
| engine-editor-plugin | 1 |
| managed-service-with-analyst | 1 |

### pricing-model

| Value | Count |
|---|---|
| (none) | 91 |
| per-build-or-release | 14 |
| per-audit-or-certification | 12 |
| oem-royalty-or-white-label | 10 |
| per-month-seat | 7 |
| per-session | 6 |
| per-hour-of-video | 6 |
| annual-enterprise-licence | 5 |
| freemium-self-serve | 4 |
| revenue-share | 3 |
| per-mau | 2 |
| free-with-platform | 2 |
| data-licence-per-hour | 2 |
| cpm-or-per-impression-verified | 2 |
| per-game | 2 |
| managed-project | 2 |

### value-lever-b2b

| Value | Count |
|---|---|
| (none) | 83 |
| avoid-fine-or-cert-failure | 23 |
| increase-coverage-from-sample-to-all | 15 |
| replace-labour-hours | 14 |
| reduce-cost-per-incident | 12 |
| cut-time-to-insight | 11 |
| enable-automated-action | 9 |
| produce-a-sellable-asset | 5 |
| create-data-that-did-not-exist | 3 |
| de-risk-a-go-kill-decision | 3 |

### buyer-org-type

| Value | Count |
|---|---|
| (none) | 55 |
| publisher | 43 |
| analytics-or-mmp-vendor | 26 |
| mid-size-studio | 20 |
| indie-studio | 9 |
| data-or-market-intel-buyer | 4 |
| platform-or-store | 4 |
| outsourced-services-vendor | 4 |
| aaa-studio | 2 |
| device-oem | 2 |
| ad-network-or-dsp | 1 |
| agency | 1 |
| regulator-or-rating-body | 1 |


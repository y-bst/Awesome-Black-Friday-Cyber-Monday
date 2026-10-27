# Stage G counts, bucket 2 (data-buyer-training, monetisation, design-balance, qa)

| Measure | Count |
|---|---|
| In | 171 |
| Rejected | 1 |
| Duplicate clusters | 10 (folding 10 duplicates) |
| Variants (`variants_of` set) | 33 |
| Contested (`contested_by` set) | 4 positive options, contested by 6 refusals |
| Refusal rows kept (`refusal: true`) | 30 |
| Uncategorised | 0 |
| **Surviving** | **160** |

Check: 171 in - 1 rejected - 10 folded duplicates = 160.

Cell normalisation: 141 of 160 survivors had C-axes values added from their own situation/mechanism/input/buyer text (324 values added in total); a further 33 values were carried onto cluster survivors from the cells of the duplicates folded into them. Where an axis now holds more than one value it is written as a list. `_from_file` dropped from every row.

## Rejected

| id | from | rule broken |
|---|---|---|
| esports-18 | E-esports-coach.yaml | no mechanism: the mechanism field reads only 'Same parser as leaf 2' (a leaf in another file); what the AI detects or computes is not stated, so a designer cannot sketch it from the line |

## Duplicate clusters (survivor kept, members folded)

| survivor | also_from | why the same option |
|---|---|---|
| data-1 | ds-25 | paired own-player SDK video + touch/controller input aligned per frame, licensed per hour to a world-model lab |
| ds-17 | monet-18 | D0 / first-10-minute store-screen video features (shop dwell, price tiers, dismissed offers) written to the warehouse for the payer model |
| design-20 | privacy-12 | refusal: facecam expression classifier scoring frustration per level for the designer |
| monet-20 | loc-12 | bot walks the shop per locale, OCR compares displayed price string to the localised price config |
| monet-26 | privacy-13 | refusal: frustration score from frames triggers a paid offer in session |
| privacy-17 | player-24 | separate AI-training consent plus per-hour player payout on the same clips, sold by the studio |
| privacy-18 | sdk-29 | refusal: licensing clips under the existing analytics/EULA consent |
| qa-1 | sdk-13 | own-player ring buffer, glitch frames grouped by device/GPU + build into one ticket |
| qa-12 | sdk-19 | post-release ring-buffer glitch rate per device/GPU family vs the previous build, Slack alert |
| cfo-11 | bi-24 | studio CFO/BD sells consented own-player video + inputs to labs through the vendor, revenue share |

## Contested (positive option kept with refusals that reject the same option)

| positive option | contested_by | disagreement |
|---|---|---|
| data-1 | privacy-18, ciso-14 | privacy-18 (counsel) refuses licensing under existing EULA/analytics consent (sdk-29 folded in); ciso-14 vetoes any vendor clause reusing captured gameplay for AI training |
| platform-11 | data-16, oem-22 | data-16 (lab counsel) declines emulator footage without per-studio licence; oem-22 (OEM) refuses as seller after studios deny rights |
| publisher-18 | qa-9 | qa-9 (QA director) refuses an AI verdict that halts rollout unattended; publisher-18 holds staged rollout at 5% automatically |
| cfo-11 | indie-25, ciso-14 | indie-25 (solo dev) refuses selling its footage for an unverifiable share with minors in the sample; ciso-14 vetoes vendor reuse |

## Variants (same mechanism, different buyer, delivery form or input; both kept)

| option | variants_of |
|---|---|
| data-20 | privacy-17 |
| oem-12 | qa-7 |
| esports-13 | data-1 |
| design-19 | design-1 |
| design-22 | qa-19 |
| design-23 | design-19 |
| indie-1 | design-2 |
| indie-2 | design-18 |
| indie-7 | monet-15 |
| indie-11 | qa-3 |
| indie-16 | design-15 |
| indie-18 | monet-2 |
| indie-21 | ds-13 |
| indie-27 | monet-7 |
| loc-13 | qa-3 |
| monet-3 | design-3 |
| monet-8 | qa-7 |
| monet-22 | sdk-18 |
| monet-31 | monet-1 |
| outsource-7 | cto-13 |
| outsource-14 | qa-26 |
| platform-11 | data-1 |
| player-25 | monet-26 |
| privacy-19 | design-11 |
| publisher-3 | monet-1 |
| publisher-18 | qa-3 |
| qa-22 | monet-7 |
| qa-24 | design-15 |
| qa-28 | cto-14 |
| sdk-9 | data-1 |
| cfo-5 | qa-10 |
| cfo-11 | data-1 |
| cfo-24 | monet-13 |

## Refusal rows

data-16, data-27, data-28, data-29, data-30, data-31, data-32, oem-22, design-20, design-21, design-22, design-23, indie-25, monet-25, monet-26, monet-27, monet-28, monet-29, monet-30, outsource-24, player-23, player-25, support-30, privacy-18, qa-8, qa-9, qa-19, qa-20, qa-25, ciso-14

## Leaves per perspective (survivors, by source file of the surviving row)

| perspective file | survivors | folded in as duplicate |
|---|---|---|
| E-game-designer-balance.yaml | 30 | 0 |
| E-monetisation-lead.yaml | 30 | 1 |
| E-ai-training-data-buyer.yaml | 29 | 0 |
| E-qa-director.yaml | 28 | 0 |
| E-indie-solo-dev.yaml | 10 | 0 |
| E-privacy-regulator-counsel.yaml | 4 | 2 |
| E-player-opt-in.yaml | 3 | 1 |
| E-studio-cfo.yaml | 3 | 0 |
| E-cto-or-engine-lead-veto.yaml | 3 | 0 |
| E-device-oem-chip-vendor.yaml | 3 | 0 |
| E-outsourced-qa-and-loc-vendor.yaml | 3 | 0 |
| E-esports-coach.yaml | 3 | 0 |
| E-data-scientist.yaml | 2 | 1 |
| E-sdk-platform-engineer.yaml | 2 | 3 |
| E-publisher-portfolio-manager.yaml | 2 | 0 |
| E-ad-network-and-mediation-ops.yaml | 1 | 0 |
| E-player-support-lead.yaml | 1 | 0 |
| E-localisation-lead.yaml | 1 | 1 |
| E-platform-owner.yaml | 1 | 0 |
| E-studio-ciso-security-review.yaml | 1 | 0 |
| E-in-house-analytics-head.yaml | 0 | 1 |

## buyer-role (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| product-retention | 0 |
| ua-marketing | 1 |
| qa | 40 |
| live-ops | 8 |
| design-balance | 41 |
| monetisation | 41 |
| competitive-intel | 1 |
| player-support | 2 |
| trust-safety | 0 |
| finance-exec | 3 |
| platform-owner | 0 |
| ux-research | 0 |
| localisation | 3 |
| accessibility-compliance | 0 |
| rating-and-consumer-compliance | 0 |
| certification-release | 2 |
| engineering-performance | 10 |
| analytics-bi | 4 |
| community-and-creator-marketing | 0 |
| esports-team-or-league | 0 |
| publishing-scout-bd | 0 |
| ad-network-ops | 0 |
| brand-advertiser | 0 |
| data-buyer-training | 40 |
| data-buyer-market-intel | 0 |
| investor | 0 |
| white-label-vendor | 0 |
| outsourced-qa-vendor | 0 |
| (axis not set) | 0 |

## video-source (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| own-players-consented-sdk | 89 |
| recruited-playtesters | 2 |
| platform-or-emulator-capture | 8 |
| public-streams-and-ugc | 8 |
| competitor-store-and-ad-video | 0 |
| internal-qa-builds | 10 |
| esports-vod | 3 |
| support-ticket-attachment | 2 |
| cloud-gaming-server-render | 2 |
| automated-bot-or-agent-playthrough | 26 |
| beta-and-early-access-testers | 12 |
| console-share-and-platform-clips | 0 |
| creator-sponsored-streams | 0 |
| ad-and-playable-ad-sessions | 4 |
| outsourced-tester-rigs | 5 |
| publisher-pitch-builds | 0 |
| (axis not set) | 1 |

## analysis-type (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| funnel-drop-off-why | 14 |
| churn-prediction-features | 3 |
| root-cause-of-a-metric-change | 10 |
| benchmark-vs-competitor | 7 |
| anomaly-alert | 26 |
| highlight-or-clip-generation | 0 |
| bug-reproduction | 10 |
| compliance-audit | 6 |
| creative-insight-for-ads | 1 |
| coaching-feedback | 1 |
| training-dataset-export | 37 |
| cohort-comparison | 20 |
| ask-a-question-over-footage | 5 |
| build-to-build-regression-diff | 8 |
| ab-test-variant-explanation | 4 |
| ad-verification-and-fraud | 3 |
| content-rating-classification | 0 |
| early-ltv-or-payer-prediction | 2 |
| real-time-in-session-intervention | 4 |
| automated-test-generation | 3 |
| creative-generation-from-gameplay | 0 |
| evidence-pack-for-enforcement | 0 |
| (axis not set) | 2 |

## delivery-form (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| dashboard | 16 |
| alert-or-slack | 13 |
| per-cohort-report | 20 |
| api-or-sdk | 7 |
| clip-reel | 2 |
| in-tool-annotation | 7 |
| managed-service-with-analyst | 2 |
| licensed-dataset | 32 |
| warehouse-table-export | 7 |
| issue-tracker-ticket | 23 |
| engine-editor-plugin | 7 |
| ask-question-agent-chat | 5 |
| generated-creative-files | 0 |
| enforcement-or-cert-evidence-pack | 2 |
| white-label-embed | 0 |
| weekly-digest-email | 6 |
| (axis not set) | 16 |

## pricing-model (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| per-session | 4 |
| per-month-seat | 3 |
| per-game | 1 |
| per-mau | 2 |
| revenue-share | 8 |
| managed-project | 2 |
| free-with-platform | 0 |
| per-hour-of-video | 4 |
| per-build-or-release | 11 |
| outcome-based-per-bug-or-uplift | 3 |
| annual-enterprise-licence | 5 |
| oem-royalty-or-white-label | 0 |
| cpm-or-per-impression-verified | 0 |
| data-licence-per-hour | 16 |
| freemium-self-serve | 4 |
| per-audit-or-certification | 1 |
| (axis not set) | 102 |

## value-lever-b2b (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| replace-labour-hours | 8 |
| increase-coverage-from-sample-to-all | 2 |
| cut-time-to-insight | 3 |
| create-data-that-did-not-exist | 5 |
| de-risk-a-go-kill-decision | 3 |
| avoid-fine-or-cert-failure | 1 |
| produce-a-sellable-asset | 10 |
| reduce-cost-per-incident | 4 |
| enable-automated-action | 1 |
| (axis not set) | 125 |

## buyer-org-type (normalised; a leaf counts once per value it holds)

| value | leaves |
|---|---|
| indie-studio | 11 |
| mid-size-studio | 30 |
| aaa-studio | 6 |
| publisher | 15 |
| platform-or-store | 2 |
| ad-network-or-dsp | 0 |
| analytics-or-mmp-vendor | 0 |
| outsourced-services-vendor | 3 |
| agency | 0 |
| brand-advertiser | 0 |
| data-or-market-intel-buyer | 18 |
| investor | 0 |
| device-oem | 3 |
| regulator-or-rating-body | 0 |
| (axis not set) | 82 |

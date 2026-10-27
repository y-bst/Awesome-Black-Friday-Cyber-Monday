# Stage G counts, bucket 5 (G-bucket-5.yaml)

Buyer roles in bucket: finance-exec, ua-marketing, live-ops, platform-owner, brand-advertiser, publishing-scout-bd.

## Summary

| Measure | Count |
|---|---|
| Options in | 180 |
| Rejected | 2 |
| Duplicate clusters | 9 |
| Options merged into survivors | 11 |
| Options carrying `variants_of` | 34 |
| Positive options carrying `contested_by` | 4 |
| Refusal rows kept (`refusal: true`) | 29 |
| Surviving options | 167 |
| Survivors with cell values added by normalisation | 160 (653 values added) |
| Uncategorised (`uncategorised: true`) | 0 |

Check: 180 in - 2 rejected - 11 merged = 167 surviving.

## Rejected

- ua-21: no concrete example ("a UA manager checks a free tracker weekly" names no game, moment or decision) and the mechanism "Count views and creators" is a category with no video analysis. (`REFUSE: Twitch-style viewership dashboard for mobile UGC clips`)
- ua-23: no concrete example ("breaks on every UI update" names no game, screen or moment); the leaf cannot be sketched from the line. (`REFUSE: per-game HUD OCR detectors that need a crop region and text pattern for every mobile casual title`)

Banned-vocabulary scan over title, mechanism, example, proposed, situation, consequence and object found 3 hits, all followed by a specific instance, so none caused a rejection: oem-5 `proposed` quotes a toggle label ("help improve gaming"); liveops-20 `situation` "biometric handling" names the facecam feed; platform-19 `object` quotes market.md ("none is shown handling mobile gameplay recorded on-device"). Refusal rows whose `mechanism` reads "Not built; ..." (brand-22, brand-24, brand-25) were kept: the title states the mechanism and the example is concrete.

## Duplicate clusters (survivor <- merged ids)

Survivor keeps its own id, wording and cell; cells of merged ids were not folded in.

- cfo-8 <- sdk-22: Spend meter with hard cap that lowers SDK sampling via remote config at the monthly budget
- cfo-25 <- privacy-24: BYOC tier: pipeline runs in the studio tenant, vendor sees only billing counts
- publisher-2 <- cfo-9: Soft-launch go/kill memo from sampled FTUE quit moments, before UA budget is committed
- platform-16 <- cto-12, sdk-20: Cloud-gaming encoder tap at 1 fps plus controller stream, per-title first-session funnel for publishers on the service
- platform-12 <- privacy-2: Edge redaction at the emulator capture point: login, sign-in and payment frames dropped before storage
- brand-8 <- esports-7: Logo seconds per match in esports broadcast VOD vs contracted minimum, used to claim make-goods
- scout-1 <- compintel-25, publisher-5: Pitch-build FTUE scorecard from recruited/panel testers, percentile against a library of other titles
- scout-29 <- cfo-20: Indie-paid independent FTUE percentile report attached to a pitch or fundraise
- scout-21 <- publisher-19: Publishing-deal tranche released on vendor-measured FTUE thresholds with a signed evidence pack

Judgement notes: platform-16 absorbs cto-12 and sdk-20 although their `delivery-form` labels differ (per-cohort-report / none) because all three describe the same publisher-facing per-title funnel from the cloud encoder tap, sold by the same cloud-gaming operator. scout-29 (publishing-scout-bd) absorbs cfo-20 (finance-exec): both are paid by the indie founder for an independent FTUE percentile report attached to a pitch or raise, so scout-29 gains `buyer-role: finance-exec`. scout-1 absorbs compintel-25 and publisher-5: same scout, same pitch-build tester sessions, same FTUE metrics placed as a percentile; they differ only in which library supplies the comparison (rival FTUEs, shipped games, the publisher's own titles).

## Variants (`variants_of`, kept as separate rows)

Same mechanism, different buyer, input or delivery form.

- publisher-2 <- indie-15, ua-25
- ua-1 <- cfo-12, platform-8
- ua-7 <- ua-8
- ua-8 <- brand-20
- ua-5 <- indie-5, platform-19
- ua-4 <- publisher-22, ua-16, ua-17, scout-18
- liveops-3 <- liveops-27
- liveops-1 <- support-20, brand-15
- liveops-17 <- ua-26
- brand-5 <- ua-28, brand-12
- brand-2 <- brand-26
- brand-4 <- brand-28
- cfo-25 <- scout-28
- platform-1 <- ua-13, liveops-28, platform-27
- platform-12 <- privacy-3
- cfo-7 <- ua-19, brand-21
- cfo-6 <- ua-18, liveops-20, brand-22, platform-13
- publisher-13 <- oem-23, scout-24, brand-14

Refusal rows are grouped with the refusal they repeat for a different buyer: cfo-7 (full-fleet capture) <- ua-19, brand-21; cfo-6 (facecam emotion) <- ua-18, liveops-20, brand-22, platform-13; publisher-13 (single fun/arousal score) <- oem-23, scout-24, brand-14.

## Contested (positive option vs refusal of the same option)

- liveops-15 contested_by cfo-19: On-device frustration score triggers a free booster mid-session (live-ops, WTP 2) vs the CFO refusing the same closed-loop gift after modelling 8% IAP cannibalisation.
- data-17 contested_by liveops-22: Studio licenses consented footage+inputs to AI labs (CFO, WTP 4) vs live-ops refusing to fund the same licensing line.
- player-13 contested_by sdk-11: Fully-loaded consented-session cost model for the CFO (WTP 2) vs the SDK engineer saying the same calculator is a free lead magnet nobody pays for (WTP 1).
- ua-17 contested_by brand-25: Real-gameplay ad-variant factory from consented player footage (creative strategist, WTP 2) vs the brand creative director refusing ad creatives cut from player footage (friend lists visible, rights risk). Buyer differs, so this is a cross-buyer contest, but the refusal reason applies to ua-17 as written.

No other refusal duplicates a positive option inside this bucket. The facecam, always-on capture, arousal-score, minor-detection, vendor-cloud-per-session, overlay-coach and per-seat refusals have no positive counterpart here; check other buckets for one.

## Refusal rows kept (29)

oem-23, brand-14, brand-21, brand-22, brand-23, brand-24, brand-25, indie-24, liveops-19, liveops-20, liveops-21, liveops-22, platform-13, platform-14, platform-15, platform-30, publisher-12, publisher-13, scout-24, scout-27, sdk-11, cfo-6, cfo-7, cfo-19, ua-10, ua-18, ua-19, ua-20, ua-22

Tagged on willingness_to_pay 1. ua-10, liveops-19, brand-14 and sdk-11 are written as positive options but scored 1 by their own perspective, so they carry `refusal: true` as well.

## Counts per axis value (surviving options, normalised cells)

An option with several values on an axis counts once under each. "(unset)" = the option has no value on that axis.

### buyer-role

| Value | Options |
|---|---|
| product-retention | 2 |
| ua-marketing | 33 |
| qa | 2 |
| live-ops | 31 |
| design-balance | 1 |
| monetisation | 5 |
| competitive-intel | 2 |
| player-support | 3 |
| trust-safety | 1 |
| finance-exec | 34 |
| platform-owner | 27 |
| ux-research | 1 |
| localisation | 4 |
| accessibility-compliance | 1 |
| engineering-performance | 2 |
| analytics-bi | 8 |
| community-and-creator-marketing | 4 |
| publishing-scout-bd | 22 |
| brand-advertiser | 28 |

Zero options: rating-and-consumer-compliance, certification-release, esports-team-or-league, ad-network-ops, data-buyer-training, data-buyer-market-intel, investor, white-label-vendor, outsourced-qa-vendor

### video-source

| Value | Options |
|---|---|
| own-players-consented-sdk | 67 |
| recruited-playtesters | 17 |
| platform-or-emulator-capture | 27 |
| public-streams-and-ugc | 17 |
| competitor-store-and-ad-video | 3 |
| internal-qa-builds | 6 |
| esports-vod | 1 |
| support-ticket-attachment | 2 |
| cloud-gaming-server-render | 2 |
| automated-bot-or-agent-playthrough | 20 |
| beta-and-early-access-testers | 2 |
| console-share-and-platform-clips | 3 |
| creator-sponsored-streams | 4 |
| ad-and-playable-ad-sessions | 13 |
| publisher-pitch-builds | 13 |
| (unset) | 6 |

Zero options: outsourced-tester-rigs

### analysis-type

| Value | Options |
|---|---|
| funnel-drop-off-why | 23 |
| churn-prediction-features | 6 |
| root-cause-of-a-metric-change | 8 |
| benchmark-vs-competitor | 30 |
| anomaly-alert | 16 |
| highlight-or-clip-generation | 11 |
| bug-reproduction | 1 |
| compliance-audit | 12 |
| creative-insight-for-ads | 20 |
| coaching-feedback | 2 |
| training-dataset-export | 6 |
| cohort-comparison | 23 |
| ask-a-question-over-footage | 8 |
| build-to-build-regression-diff | 3 |
| ab-test-variant-explanation | 5 |
| ad-verification-and-fraud | 11 |
| content-rating-classification | 3 |
| early-ltv-or-payer-prediction | 2 |
| real-time-in-session-intervention | 3 |
| automated-test-generation | 1 |
| creative-generation-from-gameplay | 8 |
| evidence-pack-for-enforcement | 7 |
| (unset) | 10 |

### delivery-form

| Value | Options |
|---|---|
| dashboard | 27 |
| alert-or-slack | 15 |
| per-cohort-report | 45 |
| api-or-sdk | 9 |
| clip-reel | 7 |
| in-tool-annotation | 2 |
| managed-service-with-analyst | 7 |
| licensed-dataset | 3 |
| warehouse-table-export | 5 |
| issue-tracker-ticket | 6 |
| ask-question-agent-chat | 5 |
| generated-creative-files | 9 |
| enforcement-or-cert-evidence-pack | 10 |
| white-label-embed | 3 |
| weekly-digest-email | 14 |
| (unset) | 17 |

Zero options: engine-editor-plugin

### pricing-model

| Value | Options |
|---|---|
| per-session | 12 |
| per-month-seat | 15 |
| per-game | 9 |
| per-mau | 2 |
| revenue-share | 5 |
| managed-project | 7 |
| free-with-platform | 5 |
| per-hour-of-video | 3 |
| per-build-or-release | 3 |
| outcome-based-per-bug-or-uplift | 4 |
| annual-enterprise-licence | 8 |
| oem-royalty-or-white-label | 2 |
| cpm-or-per-impression-verified | 4 |
| data-licence-per-hour | 3 |
| freemium-self-serve | 5 |
| per-audit-or-certification | 10 |
| (unset) | 82 |

### value-lever-b2b

| Value | Options |
|---|---|
| replace-labour-hours | 11 |
| increase-coverage-from-sample-to-all | 11 |
| cut-time-to-insight | 16 |
| create-data-that-did-not-exist | 7 |
| de-risk-a-go-kill-decision | 30 |
| avoid-fine-or-cert-failure | 8 |
| produce-a-sellable-asset | 8 |
| reduce-cost-per-incident | 7 |
| enable-automated-action | 6 |
| (unset) | 81 |

### buyer-org-type

| Value | Options |
|---|---|
| indie-studio | 8 |
| mid-size-studio | 23 |
| aaa-studio | 4 |
| publisher | 36 |
| platform-or-store | 23 |
| ad-network-or-dsp | 1 |
| agency | 16 |
| brand-advertiser | 17 |
| device-oem | 6 |
| (unset) | 50 |

Zero options: analytics-or-mmp-vendor, outsourced-services-vendor, data-or-market-intel-buyer, investor, regulator-or-rating-body

### Bucket assignment check (original `buyer-role`, before normalisation)

| buyer-role | Surviving |
|---|---|
| ua-marketing | 31 |
| live-ops | 31 |
| finance-exec | 29 |
| brand-advertiser | 28 |
| platform-owner | 27 |
| publishing-scout-bd | 21 |

## Options per perspective file (in -> surviving)

| Perspective file | In | Surviving |
|---|---|---|
| E-live-ops-manager.yaml | 29 | 29 |
| E-in-game-advertiser-brand.yaml | 28 | 28 |
| E-ua-manager.yaml | 27 | 25 |
| E-publisher-scout-investor.yaml | 18 | 18 |
| E-platform-owner.yaml | 17 | 17 |
| E-studio-cfo.yaml | 14 | 12 |
| E-publisher-portfolio-manager.yaml | 11 | 9 |
| E-privacy-regulator-counsel.yaml | 7 | 5 |
| E-device-oem-chip-vendor.yaml | 6 | 6 |
| E-ai-training-data-buyer.yaml | 5 | 5 |
| E-indie-solo-dev.yaml | 4 | 4 |
| E-sdk-platform-engineer.yaml | 3 | 1 |
| E-cto-or-engine-lead-veto.yaml | 2 | 1 |
| E-esports-coach.yaml | 2 | 1 |
| E-localisation-lead.yaml | 2 | 2 |
| E-player-support-lead.yaml | 2 | 2 |
| E-competitive-intel-analyst.yaml | 1 | 0 |
| E-player-opt-in.yaml | 1 | 1 |
| E-studio-ciso-security-review.yaml | 1 | 1 |

## Notes on normalisation

- Values were added to every axis in C-axes.yaml when the option's title, mechanism, example, input or buyer plainly state them, then each addition was read and false matches removed (for example "elapsed seconds" is not a lapsed-player winback; "no facecam" does not add facecam; "1 fps" capture rate is not a performance signal; "creative present" is not creative insight).
- `pricing-model` was added by hand only where the title or `proposed` names the charging model (11 options); per-title metrics and price anchors quoted from the notes were not treated as a pricing model.
- `effort` was filled from `cost` (S -> S-weeks, M -> M-one-quarter, L -> L-multi-quarter) where the cell had no effort value, plus requires-partner-or-platform-deal where `depends_on` names a partner, platform deal or relationship.
- Where an axis gained a value, the cell value became a list with the original value first. Original values were kept even when mislabelled.
- `_from_file` was dropped. `shallow: false` was filled in on the 28 options that had no `shallow` key.
- Several finance-exec options have privacy counsel or a CISO as the named buyer (privacy-8, privacy-11, privacy-27); they stay in this bucket under their original label, and normalisation added no counsel role because C-axes.yaml has none.

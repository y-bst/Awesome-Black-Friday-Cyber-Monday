# Stage G counts, bucket 3

Buyer roles in bucket: ux-research, trust-safety, accessibility-compliance, competitive-intel, localisation. Counts are from normalised cells; an option can carry more than one value per axis after normalisation, so axis columns can sum to more than the surviving count.

| Stage | Count |
|---|---|
| In | 180 |
| Rejected | 2 |
| Duplicate clusters | 5 (absorbing 5 items) |
| Variants (rows with variants_of) | 45 |
| Contested (positive options with contested_by) | 4 (citing 4 refusals) |
| Refusals kept (refusal: true) | 32 |
| Surviving | 173 |
| Leaves with cell values added in normalisation | 136 (339 values) |
| Uncategorised | 0 |

Normalisation: keyword rules over title, mechanism, proposed, example, situation, input and buyer, reviewed by hand with negations removed ("no face camera", "no speech segment"), plus manual buyer-role additions where the buyer line names a second role (for example "CI analyst supplying the monetisation lead"). Cells of merged duplicates are unioned into the survivor. Each row lists what was added in `cell_values_added`. Refusal rule: willingness_to_pay 1, or a title marked REFUSE/REFUSED (cfo-23 and compintel-29 are W2 but refused at the proposed terms).

## Rejected

- `compintel-28`: no concrete example: example field reads only "Not built" (refusal, but fails the leaf test on rule "concrete example")
- `compintel-30`: no concrete example: example field reads only "Not built" (refusal, but fails the leaf test on rule "concrete example")

## Duplicate clusters (survivor <- merged)

- `sdk-6` <- `tns-15`: on-device mask of names, chat, OS notifications and payment sheets before encoding; same buyer group (privacy counsel, SDK engineering, T&S), same input (raw frames on device). sdk-6 kept for the two-layer mechanism.
- `compintel-1` <- `publisher-4`: scheduled emulator agent playthrough of top-grossing rivals' first 20-30 min into an FTUE step dashboard for the CI analyst at a publisher; publisher-4 adds portfolio placement and monthly diff on the same pipeline.
- `compintel-10` <- `publisher-26`: quit-point map from public Twitch/YouTube VODs for the CI analyst at a PC/console publisher; publisher-26 adds streamer-speech complaints and own titles.
- `a11y-7` <- `cfo-15`: pixel checks (subtitle size, contrast, colour-only cues, flashes) on internal QA footage replacing part of the 150-250 MGATS hours for the compliance lead at a console/Xbox publisher.
- `privacy-20` <- `tns-28`: refusal duplicated by refusal: video classifier writes a ban with no human review, T&S lead at a competitive studio.

## Contested (positive option vs refusal from another perspective)

- `platform-24` contested_by `a11y-28`: platform-owner wants an automatic store accessibility badge from detector passes; the accessibility officer (a11y-28) refuses to sign any badge issued without human sign-off.
- `indie-4` contested_by `uxr-26`: solo dev (W4) wants playtest footage turned into a ticket list; the UX research lead (uxr-26) refuses auto-filed tickets by default because noise gets the research backlog ignored.
- `indie-6` contested_by `compintel-32`: solo dev (W3) would pay $15 per game for a rival FTUE list from public YouTube videos; the CI analyst (compintel-32) refuses the same self-serve wrapper because a general video LLM gives 80% of it free.
- `support-11` contested_by `cfo-23`: support and T&S leads (W3) want a per-appeal clip + input-timeline pack; the studio CFO (cfo-23) refuses per-case evidence packs because one wrongful-ban dispute costs more than a year of fees.

## Variants (variants_of root)

- `a11y-10`: `a11y-26`
- `a11y-18`: `uxr-16`
- `a11y-19`: `platform-24`
- `a11y-3`: `loc-8`, `outsource-20`
- `a11y-31`: `loc-26`
- `a11y-6`: `a11y-15`
- `a11y-7`: `a11y-17`, `a11y-23`, `indie-29`, `outsource-13`
- `a11y-9`: `a11y-21`
- `cfo-4`: `indie-6`
- `compintel-1`: `cfo-4`
- `compintel-22`: `loc-17`
- `loc-1`: `indie-13`, `outsource-1`, `platform-25`, `player-16`, `cfo-17`
- `loc-4`: `outsource-3`
- `loc-5`: `outsource-2`, `outsource-21`
- `loc-6`: `loc-21`
- `support-11`: `platform-22`
- `tns-1`: `support-23`
- `tns-11`: `privacy-21`
- `tns-16`: `ciso-21`
- `tns-3`: `esports-8`, `tns-18`
- `uxr-1`: `uxr-12`, `indie-4`
- `uxr-11`: `uxr-19`
- `uxr-13`: `a11y-29`, `compintel-27`, `indie-22`, `loc-25`, `player-26`, `sdk-26`, `tns-26`
- `uxr-15`: `sdk-24`
- `uxr-20`: `player-10`
- `uxr-22`: `player-11`
- `uxr-3`: `uxr-27`
- `uxr-4`: `uxr-18`

## Refusals kept

`a11y-20`, `a11y-21`, `a11y-26`, `a11y-27`, `a11y-28`, `a11y-29`, `a11y-30`, `a11y-31`, `compintel-26`, `compintel-27`, `compintel-29`, `compintel-32`, `uxr-13`, `uxr-14`, `uxr-26`, `indie-22`, `indie-23`, `loc-23`, `loc-24`, `loc-25`, `loc-26`, `player-12`, `player-26`, `privacy-20`, `sdk-26`, `cfo-23`, `tns-13`, `tns-20`, `tns-26`, `tns-27`, `tns-29`, `tns-30`

Two refusals were rejected for a missing example (compintel-28 rival-footage ad re-skins, compintel-30 rival DAU/revenue from leaderboard OCR); their situations are recorded above in case the audit wants them back.

## Leaves per perspective (surviving rows, and rows merged into a survivor from another perspective)

| Perspective | Surviving rows | Merged into another row |
|---|---|---|
| accessibility-compliance-officer | 29 | 0 |
| competitive-intel-analyst | 28 | 0 |
| cto-or-engine-lead-veto | 1 | 0 |
| device-oem-chip-vendor | 1 | 0 |
| esports-coach | 1 | 0 |
| game-ux-researcher | 28 | 0 |
| indie-solo-dev | 7 | 0 |
| localisation-lead | 18 | 0 |
| outsourced-qa-and-loc-vendor | 6 | 0 |
| platform-owner | 3 | 0 |
| player-opt-in | 6 | 0 |
| player-support-lead | 3 | 0 |
| privacy-regulator-counsel | 4 | 0 |
| publisher-portfolio-manager | 0 | 2 |
| sdk-platform-engineer | 5 | 0 |
| studio-cfo | 4 | 1 |
| studio-ciso-security-review | 1 | 0 |
| trust-and-safety-lead | 28 | 2 |

## buyer-role

| Value | All survivors | Of which refusals |
|---|---|---|
| product-retention | 2 | 0 |
| ua-marketing | 3 | 0 |
| qa | 1 | 0 |
| live-ops | 4 | 0 |
| design-balance | 3 | 0 |
| monetisation | 4 | 0 |
| competitive-intel | 33 | 4 |
| player-support | 4 | 0 |
| trust-safety | 38 | 8 |
| finance-exec | 4 | 0 |
| platform-owner | 6 | 1 |
| ux-research | 41 | 8 |
| localisation | 26 | 4 |
| accessibility-compliance | 37 | 8 |
| analytics-bi | 1 | 0 |
| esports-team-or-league | 2 | 0 |
| publishing-scout-bd | 1 | 0 |
| data-buyer-training | 1 | 1 |
| data-buyer-market-intel | 1 | 0 |
| outsourced-qa-vendor | 7 | 0 |

Zero in this bucket: rating-and-consumer-compliance, certification-release, engineering-performance, community-and-creator-marketing, ad-network-ops, brand-advertiser, investor, white-label-vendor

## video-source

| Value | All survivors | Of which refusals |
|---|---|---|
| own-players-consented-sdk | 37 | 11 |
| recruited-playtesters | 36 | 8 |
| platform-or-emulator-capture | 5 | 0 |
| public-streams-and-ugc | 16 | 3 |
| competitor-store-and-ad-video | 2 | 0 |
| internal-qa-builds | 20 | 5 |
| esports-vod | 2 | 0 |
| support-ticket-attachment | 6 | 1 |
| cloud-gaming-server-render | 2 | 1 |
| automated-bot-or-agent-playthrough | 30 | 1 |
| beta-and-early-access-testers | 6 | 1 |
| console-share-and-platform-clips | 1 | 0 |
| ad-and-playable-ad-sessions | 1 | 0 |
| outsourced-tester-rigs | 7 | 0 |
| (none) | 2 | 1 |

Zero in this bucket: creator-sponsored-streams, publisher-pitch-builds

## analysis-type

| Value | All survivors | Of which refusals |
|---|---|---|
| funnel-drop-off-why | 10 | 1 |
| churn-prediction-features | 2 | 1 |
| root-cause-of-a-metric-change | 2 | 1 |
| benchmark-vs-competitor | 36 | 4 |
| anomaly-alert | 20 | 1 |
| highlight-or-clip-generation | 2 | 0 |
| bug-reproduction | 8 | 2 |
| compliance-audit | 36 | 5 |
| creative-insight-for-ads | 2 | 0 |
| coaching-feedback | 5 | 4 |
| training-dataset-export | 1 | 1 |
| cohort-comparison | 16 | 3 |
| ask-a-question-over-footage | 17 | 2 |
| build-to-build-regression-diff | 5 | 0 |
| ab-test-variant-explanation | 2 | 0 |
| content-rating-classification | 1 | 1 |
| early-ltv-or-payer-prediction | 1 | 1 |
| real-time-in-session-intervention | 4 | 2 |
| evidence-pack-for-enforcement | 18 | 4 |
| (none) | 3 | 0 |

Zero in this bucket: ad-verification-and-fraud, automated-test-generation, creative-generation-from-gameplay

## delivery-form

| Value | All survivors | Of which refusals |
|---|---|---|
| dashboard | 21 | 4 |
| alert-or-slack | 13 | 0 |
| per-cohort-report | 41 | 5 |
| api-or-sdk | 6 | 1 |
| clip-reel | 2 | 0 |
| in-tool-annotation | 7 | 1 |
| managed-service-with-analyst | 3 | 2 |
| licensed-dataset | 1 | 1 |
| warehouse-table-export | 7 | 0 |
| issue-tracker-ticket | 25 | 4 |
| engine-editor-plugin | 1 | 0 |
| ask-question-agent-chat | 7 | 1 |
| enforcement-or-cert-evidence-pack | 18 | 3 |
| white-label-embed | 1 | 0 |
| weekly-digest-email | 9 | 1 |
| (none) | 19 | 9 |

Zero in this bucket: generated-creative-files

## pricing-model

| Value | All survivors | Of which refusals |
|---|---|---|
| per-session | 9 | 3 |
| per-month-seat | 10 | 1 |
| per-game | 9 | 1 |
| per-mau | 5 | 2 |
| managed-project | 5 | 2 |
| free-with-platform | 1 | 1 |
| per-hour-of-video | 7 | 2 |
| per-build-or-release | 11 | 1 |
| outcome-based-per-bug-or-uplift | 4 | 1 |
| annual-enterprise-licence | 5 | 0 |
| data-licence-per-hour | 1 | 1 |
| freemium-self-serve | 3 | 2 |
| per-audit-or-certification | 13 | 4 |
| (none) | 92 | 13 |

Zero in this bucket: revenue-share, oem-royalty-or-white-label, cpm-or-per-impression-verified

## value-lever-b2b

| Value | All survivors | Of which refusals |
|---|---|---|
| replace-labour-hours | 30 | 3 |
| increase-coverage-from-sample-to-all | 17 | 1 |
| cut-time-to-insight | 9 | 2 |
| create-data-that-did-not-exist | 7 | 0 |
| de-risk-a-go-kill-decision | 8 | 0 |
| avoid-fine-or-cert-failure | 14 | 2 |
| produce-a-sellable-asset | 1 | 0 |
| reduce-cost-per-incident | 13 | 2 |
| enable-automated-action | 5 | 3 |
| (none) | 86 | 21 |

## buyer-org-type

| Value | All survivors | Of which refusals |
|---|---|---|
| indie-studio | 8 | 2 |
| mid-size-studio | 23 | 5 |
| aaa-studio | 9 | 2 |
| publisher | 50 | 5 |
| platform-or-store | 8 | 1 |
| outsourced-services-vendor | 8 | 0 |
| data-or-market-intel-buyer | 1 | 1 |
| device-oem | 1 | 0 |
| (none) | 70 | 16 |

Zero in this bucket: ad-network-or-dsp, analytics-or-mmp-vendor, agency, brand-advertiser, investor, regulator-or-rating-body

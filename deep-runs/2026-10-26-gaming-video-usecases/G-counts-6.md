# Stage G counts, bucket 6

Bucket roles: ad-network-ops, data-buyer-market-intel, investor, esports-team-or-league, outsourced-qa-vendor, and options with no buyer-role in their cell (21).

## Summary

| measure | count |
|---|---|
| in (G-bucket-6.yaml) | 120 |
| rejected | 0 |
| duplicate clusters | 0 |
| ids merged into a survivor | 0 |
| variants (rows with variants_of) | 37 |
| refusals kept (refusal: true) | 22 |
| contested (positive rows with contested_by) | 2 |
| uncategorised rows kept | 1 |
| surviving | 120 |
| rows with cell values added in normalisation | 63 (130 values) |

## Rejected

None. Every one of the 120 rows names a buyer, an input, a mechanism and a concrete example, and every row is at L3 or L4. The banned-word scan found 5 hits, and each one has its instance on the same line or sits inside a quote:
- adnet-7 example: "CPI-to-payer ratio improves" (names the metric).
- adnet-8 depends_on: "per-game login handling" (names the object).
- esports-2 evidence and altdata-12 evidence: these are quoted research text.
- altdata-15 situation: this is the quoted opt-in label "help improve game performance and analytics".

Borderline rows I kept:
- outsource-25: its `example` is only a bandwidth figure ("200 Mbps uplink for 40 testers"). Its `situation` supplies the in-use case (a client asks for a live view of 40 tester screens).
- support-32: it is about agent-desktop video, not gameplay. It is kept with `uncategorised: true` for the audit.

## Duplicate clusters

None. No two rows share the same mechanism, the same buyer and the same input. The closest pair is adnet-3 and adnet-26, which both cluster touch and frame trajectories for ad fraud. They target different populations, though: adnet-3 finds emulator farms by random sampling, and adnet-26 finds human-run click-farm phones in a targeted cohort that emulator checks miss, with an alert as its delivery. adnet-26 says outright that emulator fingerprints do not catch these farms. So adnet-26 is recorded as `variants_of: adnet-3` and is not merged.

## Contested

The refusal ciso-26 (from the studio-ciso perspective) contests 2 positive rows:
- **platform-28** (from platform-owner): a live-ops and offer-price feed built from OCR of sampled real sessions on a platform, sold to market-intel firms.
- **altdata-15** (from market-intel-alt-data-buyer): a platform-edge panel licence that exports per-title screen-class aggregates to market-intel firms.

Market-intel buyers put willingness to pay at 4. The CISO of the studio being observed puts it at 1, treats the feed as distribution of the studio's IP to its rivals, and may retaliate by pulling the platform's paid analytics. ciso-26's suggested mitigation is aggregates only, no clips and a studio opt-out. altdata-15 meets the first two conditions but not the opt-out. platform-28 meets none of them.

## Refusals kept (22)

adnet-12, adnet-22, adnet-23, adnet-24, esports-23, esports-24, esports-25, esports-26, altdata-19, altdata-20, altdata-24, outsource-22, outsource-23, outsource-25, support-32, publisher-16, scout-25, scout-26, ciso-12, ciso-15, ciso-22, ciso-26.

Four rows are tagged even though they are not a plain willingness-to-pay of 1:
- scout-26 has willingness to pay 2, but its title says REFUSED and its buyer "would not buy".
- ciso-15 has willingness to pay 1 for the version where analysts use their own laptops and 2 for the version inside the studio's VDI.
- ciso-22 is a security gate that nobody pays for.
- adnet-12 would be bought only as a feature inside a larger product, not on its own.

Facecam-emotion refusals came from 4 perspectives with 4 different buyers: adnet-22 (ad-network), esports-23 (esports-coach), outsource-23 (outsourced-qa-vendor) and scout-25 (publisher-scout-investor). esports-23, outsource-23 and scout-25 are linked to adnet-22 with `variants_of`. Each refuses separately, and the shared reasons are privacy and consent plus the EU limits on emotion recognition.

## Variants (37 rows, by root)

| root | variants |
|---|---|
| esports-1 | esports-2, esports-6, esports-11, esports-20 |
| altdata-2 | altdata-14, altdata-17, altdata-18, altdata-26 |
| adnet-1 | adnet-10, adnet-20, platform-7 |
| adnet-3 | adnet-26, platform-6, scout-20 |
| adnet-22 | esports-23, outsource-23, scout-25 |
| outsource-17 | esports-9, scout-13 |
| altdata-4 | altdata-25, scout-19 |
| ciso-7 | outsource-10, ciso-1 |
| altdata-6 | adnet-8 |
| adnet-4 | adnet-11 |
| esports-6 | esports-12 |
| esports-14 | esports-27 |
| adnet-8 | altdata-5 |
| altdata-7 | altdata-15 |
| adnet-7 | altdata-16 |
| scout-4 | altdata-27 |
| outsource-8 | outsource-9 |
| altdata-1 | platform-28 |
| adnet-23 | publisher-16 |
| altdata-9 | scout-11 |
| altdata-11 | scout-23 |
| ciso-2 | ciso-13 |

## Buyer-role assignment for the 21 rows that had none (normalisation)

Each row was given the role(s) named as buyer or payer in its `buyer` field:
- support-32 -> player-support
- publisher-16 -> finance-exec
- the 19 ciso-* rows -> `security-ciso`, plus the paying budget owner where the row names one:
  - ux-research: ciso-1, ciso-2, ciso-12, ciso-13, ciso-15, ciso-23
  - product-retention: ciso-1, ciso-5, ciso-7
  - qa: ciso-2, ciso-13
  - trust-safety: ciso-18

ciso-10 already had outsourced-qa-vendor and also gets security-ciso.

**Axis gap for the audit:** `security-ciso` is NOT a value in C-axes.yaml. It is used on 20 rows, and every one of them names a CISO, AppSec, vendor-risk or IP-protection lead as the buyer or the veto. No existing value fits. I recommend adding `security-ciso` (or `security-and-ip-protection`) to the buyer-role axis. Ten of these rows have no other buyer-role: ciso-3, 4, 6, 8, 9, 16, 19, 20, 22 and 24.

Second gap: buyer-org-type has no value for an esports organisation, a league or tournament organiser, or a self-serve player. As a result, 16 of the 18 esports rows have buyer-org-type unset. The two exceptions are esports-11, which uses `agency`, and esports-26, which uses `data-or-market-intel-buyer`.

## Other normalisation added (values the row plainly satisfies)

- buyer-org-type:
  - ad-network-or-dsp: adnet-4, 6, 7, 11, 14
  - data-or-market-intel-buyer: altdata-2, 5, 7, 8, 9, 11, 15, 25
  - publisher: scout-4, 10, 11, 13, 19 (the buyer field names publisher BD or a committee)
  - ciso rows: as their buyer field states
- buyer-role:
  - investor added to altdata-2, 5 and 11 (the buyer field names a fund analyst)
  - publishing-scout-bd added to scout-4, 10, 11, 13 and 19
- companion-data, taken from each row's `input` field: adnet-5, 6, 15; esports-1, 9, 14; scout-3, 4, 26; outsource-4, 17; ciso-2, 3, 9, 10, 13, 20, 23
- pricing-model, only where `willingness_to_pay` names the form:
  - annual-enterprise-licence: altdata-1, 3, 8, 9, 27
  - per-month-seat: esports-2, 19, 27
  - per-audit-or-certification: scout-11
  - per-game: ciso-3
- value-lever-b2b: esports-1, 10, 12, 14; altdata-7, 27; platform-6, 28; scout-7, 20, 23; ciso-4
- video-source: scout-20, scout-23, ciso-2, ciso-10, ciso-13, ciso-15 (more than one source named in `input`)
- delivery-form: ciso-1, 5, 7 (on-device SDK feature, so api-or-sdk); ciso-13 (ask-question-agent-chat); platform-6 (api-or-sdk); scout-20 (per-cohort-report); outsource-22 (issue-tracker-ticket)
- analysis-type: ciso-13 (ask-a-question-over-footage)

Where a row now has more than one value on an axis, the cell value is a list. The counts below count each value of a list.

`_from_file` was dropped. A `perspective` field (the perspective slug) was added so the source of each row stays visible.

## Rows per perspective

| perspective | rows |
|---|---|
| market-intel-alt-data-buyer | 26 |
| ad-network-and-mediation-ops | 25 |
| studio-ciso-security-review | 21 |
| esports-coach | 18 |
| outsourced-qa-and-loc-vendor | 12 |
| publisher-scout-investor | 11 |
| platform-owner | 3 |
| accessibility-compliance-officer | 1 |
| localisation-lead | 1 |
| player-support-lead | 1 |
| publisher-portfolio-manager | 1 |

## buyer-role

| value | rows |
|---|---|
| ad-network-ops | 27 |
| data-buyer-market-intel | 21 |
| investor | 21 |
| security-ciso (not in C-axes) | 20 |
| esports-team-or-league | 18 |
| outsourced-qa-vendor | 15 |
| ux-research | 6 |
| publishing-scout-bd | 5 |
| product-retention | 3 |
| qa | 2 |
| player-support | 1 |
| finance-exec | 1 |
| trust-safety | 1 |

Values with 0 rows in this bucket: ua-marketing, live-ops, design-balance, monetisation, competitive-intel, platform-owner, localisation, accessibility-compliance, rating-and-consumer-compliance, certification-release, engineering-performance, analytics-bi, community-and-creator-marketing, brand-advertiser, data-buyer-training, white-label-vendor

## video-source

| value | rows |
|---|---|
| own-players-consented-sdk | 19 |
| automated-bot-or-agent-playthrough | 18 |
| outsourced-tester-rigs | 14 |
| ad-and-playable-ad-sessions | 13 |
| esports-vod | 13 |
| platform-or-emulator-capture | 12 |
| recruited-playtesters | 9 |
| public-streams-and-ugc | 8 |
| (unset) | 5 |
| beta-and-early-access-testers | 5 |
| internal-qa-builds | 4 |
| cloud-gaming-server-render | 2 |
| publisher-pitch-builds | 2 |
| support-ticket-attachment | 1 |
| console-share-and-platform-clips | 1 |
| competitor-store-and-ad-video | 1 |

Values with 0 rows in this bucket: creator-sponsored-streams

## analysis-type

| value | rows |
|---|---|
| benchmark-vs-competitor | 21 |
| (unset) | 12 |
| ad-verification-and-fraud | 11 |
| anomaly-alert | 11 |
| coaching-feedback | 11 |
| compliance-audit | 7 |
| cohort-comparison | 7 |
| ask-a-question-over-footage | 7 |
| evidence-pack-for-enforcement | 5 |
| funnel-drop-off-why | 4 |
| creative-insight-for-ads | 4 |
| bug-reproduction | 4 |
| build-to-build-regression-diff | 3 |
| root-cause-of-a-metric-change | 3 |
| automated-test-generation | 2 |
| real-time-in-session-intervention | 2 |
| highlight-or-clip-generation | 2 |
| training-dataset-export | 2 |
| churn-prediction-features | 1 |
| early-ltv-or-payer-prediction | 1 |

Values with 0 rows in this bucket: ab-test-variant-explanation, content-rating-classification, creative-generation-from-gameplay

## delivery-form

| value | rows |
|---|---|
| dashboard | 16 |
| (unset) | 15 |
| per-cohort-report | 13 |
| licensed-dataset | 13 |
| api-or-sdk | 11 |
| issue-tracker-ticket | 7 |
| enforcement-or-cert-evidence-pack | 7 |
| warehouse-table-export | 7 |
| alert-or-slack | 6 |
| weekly-digest-email | 6 |
| managed-service-with-analyst | 5 |
| in-tool-annotation | 4 |
| ask-question-agent-chat | 4 |
| clip-reel | 3 |
| white-label-embed | 2 |
| engine-editor-plugin | 1 |

Values with 0 rows in this bucket: generated-creative-files

## pricing-model

| value | rows |
|---|---|
| (unset) | 72 |
| annual-enterprise-licence | 14 |
| per-month-seat | 11 |
| cpm-or-per-impression-verified | 5 |
| managed-project | 4 |
| freemium-self-serve | 2 |
| per-audit-or-certification | 2 |
| outcome-based-per-bug-or-uplift | 2 |
| data-licence-per-hour | 2 |
| per-build-or-release | 2 |
| per-mau | 1 |
| oem-royalty-or-white-label | 1 |
| per-hour-of-video | 1 |
| per-game | 1 |

Values with 0 rows in this bucket: per-session, revenue-share, free-with-platform

## value-lever-b2b

| value | rows |
|---|---|
| (unset) | 61 |
| create-data-that-did-not-exist | 18 |
| replace-labour-hours | 13 |
| reduce-cost-per-incident | 8 |
| de-risk-a-go-kill-decision | 6 |
| produce-a-sellable-asset | 5 |
| increase-coverage-from-sample-to-all | 3 |
| cut-time-to-insight | 3 |
| avoid-fine-or-cert-failure | 2 |
| enable-automated-action | 1 |

## buyer-org-type

| value | rows |
|---|---|
| ad-network-or-dsp | 28 |
| data-or-market-intel-buyer | 22 |
| (unset) | 21 |
| investor | 21 |
| outsourced-services-vendor | 16 |
| aaa-studio | 11 |
| publisher | 10 |
| mid-size-studio | 3 |
| agency | 1 |

Values with 0 rows in this bucket: indie-studio, platform-or-store, analytics-or-mmp-vendor, brand-advertiser, device-oem, regulator-or-rating-body

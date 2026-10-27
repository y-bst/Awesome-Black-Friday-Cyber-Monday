# Stage G + I counts, bucket 7 (targeted fill after audit 1)

Input: the four E2 fill files for audit-1 cells 1, 2, 5 and 6. These are E2-netcode.yaml (16 rows), E2-takedown.yaml (20), E2-ugc-platform.yaml (17) and E2-catalogue.yaml (18). Each fill row was checked against the 943 existing titles in G-titles-all.txt. Output: I-verified-7.yaml.

## Summary

| measure | count |
|---|---|
| in (four fill files) | 71 |
| rejected | 0 |
| within-fill duplicate clusters | 0 |
| duplicates of an existing option (dropped, `duplicate_of_existing`) | 1 |
| surviving | 70 |
| variants (rows with `variants_of`) | 45 (31 of an existing option, 14 of another fill row) |
| refusals kept (`refusal: true`) | 9 |
| contested | 1 positive row with `contested_by`, and 2 refusal rows with `contests` that point at positive rows in other buckets |
| rows with cell values added in normalisation | 46 (92 values) |
| p_typical below 0.10 | 62 of 70 |
| grounded quote / inferred / speculative | 5 / 47 / 18 |
| already_offered: true | 0 |

Survivors per perspective: takedown 19, catalog 18, ugc 17, netcode 16. Every survivor has `bucket: 7` and a `perspective` field set to its id prefix.

## Rejected

None. All 71 rows are at L3 or L4. Each one names a buyer, an input, a mechanism, a concrete example, a cost and its depends_on. The banned-vocabulary scan found 0 hits across these fields: title, mechanism, example, proposed, situation, consequence and object. Refusal rows whose mechanism reads "Not built" (ugc-16, ugc-17) or "Would ..." (catalog-16, catalog-17, catalog-18) were kept, because their title states the mechanism. Bucket 6 applied the same rule.

## Within-fill duplicates

None. Two pairs came closest. Both were recorded as variants and kept:
- **netcode-8 and netcode-2.** Both compare the victim's POV with the server rewind. netcode-2 is a hit-registration ticket for the netcode lead. netcode-8 is a filter on the cheat-report queue for the trust and safety lead. The buyer and delivery differ, so this is a variant.
- **takedown-13 and takedown-1.** takedown-13 is the per-country version of the ad-library sweep, with OCR and translation added. It has a different lifecycle moment (a new market launch) and adds a translation step, so this is a variant.

## Duplicates of existing options (dropped)

| fill id | existing id | reason |
|---|---|---|
| takedown-14 | scout-6 (bucket 5) | Same mechanism: a frame-embedding match of a pitch clip against a footage index, returned as side-by-side frames. Same buyer: publishing BD. Same input: a partner's pitch footage. scout-6 already flags pitch footage that is similar to indexed titles, and the studio's own catalogue is just one more index. takedown-14 also had willingness to pay 1. |

Several other fill rows sit close to existing options, but each differs in buyer or input, so they were kept as variants:
- **catalog-3 vs scout-1.** Both are cloud-captured panel playtests reported as percentiles against comparable titles. catalog-3 is bought by a subscription-catalogue operator using its own subscribers. scout-1 is bought by a publisher scout using recruited testers.
- **ugc-9 vs altdata-13.** Both use a bot that times the first purchase prompt in UGC experiences. ugc-9 is sold to the platform's consumer-protection lead. altdata-13 is sold to an investor.
- **ugc-1 vs platform-9.** Both are an agent playthrough labelled by a VLM and diffed against the developer's declaration. ugc-1 covers creator experiences on a UGC platform. platform-9 covers app-store build submissions.
- **takedown-11 vs compintel-9.** Both match ad scenes against a playthrough of the advertised app. takedown-11 is an enforcement pack for legal. compintel-9 is a fidelity index for competitive intel.
- **takedown-7 vs adnet-8.** Both use bots that trigger live ad slots and log the creatives served. takedown-7 also matches those ads to the studio's own footage for UA and legal. adnet-8 serves ad-network ops.

## Variants (45)

Variants of existing options (31):

| fill id | variant of |
|---|---|
| netcode-1 | cto-5 |
| netcode-4 | esports-4 |
| netcode-7 | tns-2 |
| netcode-9 | esports-10 |
| netcode-10 | esports-4 |
| netcode-15 | platform-3 |
| netcode-16 | qa-24 |
| takedown-1 | ciso-3 |
| takedown-2 | compintel-16 |
| takedown-4 | tns-16 |
| takedown-7 | adnet-8 |
| takedown-9 | ciso-19 |
| takedown-10 | brand-16 |
| takedown-11 | compintel-9 |
| takedown-18 | scout-6 |
| ugc-1 | platform-9 |
| ugc-3 | rating-7 |
| ugc-6 | tns-11 |
| ugc-8 | rating-8 |
| ugc-9 | altdata-13 |
| ugc-10 | tns-5 |
| ugc-13 | rating-11 |
| ugc-16 | rating-26 |
| catalog-1 | platform-16 |
| catalog-2 | publisher-7 |
| catalog-3 | scout-1 |
| catalog-4 | scout-6 |
| catalog-5 | scout-10 |
| catalog-10 | platform-10 |
| catalog-11 | cfo-14 |
| catalog-12 | scout-21 |

Variants of another fill row (14):

| fill id | variant of |
|---|---|
| netcode-8 | netcode-2 |
| takedown-12 | takedown-1 |
| takedown-13 | takedown-1 |
| takedown-17 | takedown-5 |
| takedown-20 | takedown-4 |
| ugc-2 | ugc-1 |
| ugc-12 | ugc-1 |
| ugc-17 | ugc-1 |
| catalog-6 | catalog-1 |
| catalog-8 | catalog-7 |
| catalog-15 | catalog-3 |
| catalog-16 | catalog-1 |
| catalog-17 | catalog-6 |
| catalog-18 | catalog-1 |

## Contested (refusal against positive)

- **catalog-7 `contested_by: [a11y-20]`.** a11y-20 is a refusal from the accessibility perspective in bucket 3. It turned down a cloud-streaming test of subtitle and small-text legibility at 5 Mbps, with willingness to pay 1, on the grounds that the platform would treat it as bundled quality tooling. catalog-7 includes the same legibility check by bitrate inside a cloud-versus-local parity row, with willingness to pay 3, and the catalogue lead is the buyer. So the same check gets refused as an accessibility product but bought as a catalogue-curation input.
- **catalog-17 `contests: [platform-16]`.** catalog-17 is a refusal in this bucket. It refuses to send raw subscriber clips to publishers, because the clips carry gamertags and chat and the subscribers gave no third-party consent. platform-16 (bucket 5, positive) gives publishers "why" clips from cloud-rendered subscriber sessions, and its title names no redaction. **For the cross-bucket pass:** add `contested_by: [catalog-17]` on platform-16, or add a dependency on platform-12 edge redaction.
- **takedown-18 `contests: [scout-6]`.** takedown-18 is a refusal in this bucket: legal will not file claims based on core-loop or UI-layout similarity. scout-6 (bucket 5, positive) scores exactly that similarity, and its consequence line says "a near-copy found after launch becomes a takedown or dispute". The contest is partial. takedown-18 accepts the score as an internal benchmark and refuses it only as grounds for a notice. **For the cross-bucket pass:** add `contested_by: [takedown-18]` on scout-6.

## Refusals kept (9)

takedown-10, takedown-17, takedown-18, takedown-19, ugc-16, ugc-17, catalog-16, catalog-17, catalog-18.

takedown-10 is tagged even though its title is not a refusal. It has willingness to pay 1 ("useful as an add-on feature, not a purchase on its own"), so it gets the same treatment as adnet-12 in bucket 6. A `refusal_note` records why. takedown-14 also had willingness to pay 1, but it was dropped as a duplicate of scout-6 rather than kept as a refusal.

## Normalisation

46 rows gained 92 values. Only values that the title or situation states outright were added:
- **game-platform-and-genre:**
  - netcode rows that name PC or console get `pc` or `console`.
  - cloud-render catalog rows get `cloud-streamed`.
  - match-3 and casual takedown rows get `mobile-casual-hypercasual`.
- **processing-location:**
  - `edge-or-platform-server` for catalog rows whose capture is a tap on the cloud encoder.
  - `on-device` for netcode-6 and netcode-14, which use on-device counters.
- **buyer-org-type:** `publisher` for takedown rows that name a publisher.
- **video-source:**
  - `ad-and-playable-ad-sessions` for takedown-7.
  - `platform-or-emulator-capture` for takedown-3 and takedown-11, which use emulator install capture.
  - `beta-and-early-access-testers` for netcode-13.
- **buyer-role:**
  - takedown-2 gets `ua-marketing` and `finance-exec`. Its original label `brand-advertiser` does not match the named buyer (an ASO manager and IP counsel at a publisher). The original value was kept first.
  - takedown-16 gets `community-and-creator-marketing`.
  - takedown-18 gets `finance-exec`.

The off-axis keys were left exactly as written: `companion-data-off-axis: server-tick-ping-and-region-logs` (15 netcode rows), `buyer-org-type: subscription-catalogue-operator` (18) and `buyer-org-type: ugc-platform-operator` (17). Rows carrying an off-axis buyer-org-type were not given an on-axis buyer-org-type value.

## Counts per axis value (70 survivors, normalised cells; a row with two values counts once for each)

- **buyer-role:**

  | value | count |
  |---|---|
  | platform-owner | 17 |
  | finance-exec | 14 |
  | engineering-performance | 9 |
  | rating-and-consumer-compliance | 9 |
  | trust-safety | 7 |
  | live-ops | 3 |
  | ua-marketing | 3 |
  | esports-team-or-league | 2 |
  | brand-advertiser | 2 |
  | community-and-creator-marketing | 2 |
  | publishing-scout-bd | 2 |
  | certification-release | 2 |
  | player-support | 1 |
  | competitive-intel | 1 |

- **video-source:**

  | value | count |
  |---|---|
  | competitor-store-and-ad-video | 16 |
  | automated-bot-or-agent-playthrough | 15 |
  | cloud-gaming-server-render | 14 |
  | own-players-consented-sdk | 12 |
  | platform-or-emulator-capture | 9 |
  | public-streams-and-ugc | 6 |
  | esports-vod | 3 |
  | beta-and-early-access-testers | 1 |
  | ad-and-playable-ad-sessions | 1 |

- **analysis-type:**

  | value | count |
  |---|---|
  | evidence-pack-for-enforcement | 17 |
  | cohort-comparison | 10 |
  | content-rating-classification | 8 |
  | compliance-audit | 7 |
  | root-cause-of-a-metric-change | 6 |
  | anomaly-alert | 5 |
  | build-to-build-regression-diff | 4 |
  | benchmark-vs-competitor | 4 |
  | ask-a-question-over-footage | 2 |
  | early-ltv-or-payer-prediction | 2 |
  | ab-test-variant-explanation | 1 |
  | real-time-in-session-intervention | 1 |
  | ad-verification-and-fraud | 1 |
  | highlight-or-clip-generation | 1 |
  | churn-prediction-features | 1 |

- **delivery-form:**

  | value | count |
  |---|---|
  | enforcement-or-cert-evidence-pack | 20 |
  | per-cohort-report | 13 |
  | issue-tracker-ticket | 9 |
  | alert-or-slack | 6 |
  | dashboard | 6 |
  | api-or-sdk | 5 |
  | ask-question-agent-chat | 3 |
  | warehouse-table-export | 3 |
  | managed-service-with-analyst | 2 |
  | clip-reel | 2 |
  | weekly-digest-email | 1 |

- **pricing-model:**

  | value | count |
  |---|---|
  | (unset) | 61 |
  | per-audit-or-certification | 4 |
  | outcome-based-per-bug-or-uplift | 2 (both refusals: takedown-18, takedown-19) |
  | per-month-seat | 1 |
  | annual-enterprise-licence | 1 |
  | managed-project | 1 |

- **value-lever-b2b:**

  | value | count |
  |---|---|
  | (unset) | 49 |
  | de-risk-a-go-kill-decision | 7 |
  | create-data-that-did-not-exist | 4 |
  | reduce-cost-per-incident | 4 |
  | cut-time-to-insight | 3 |
  | enable-automated-action | 1 |
  | replace-labour-hours | 1 |
  | avoid-fine-or-cert-failure | 1 |

- **buyer-org-type:**

  | value | count |
  |---|---|
  | subscription-catalogue-operator (off-axis) | 18 |
  | ugc-platform-operator (off-axis) | 17 |
  | (unset) | 17 |
  | publisher | 15 |
  | agency | 1 |
  | brand-advertiser | 1 |
  | mid-size-studio | 1 |

- **game-platform-and-genre:**

  | value | count |
  |---|---|
  | (unset) | 20 |
  | competitive-multiplayer | 17 |
  | ugc-platform-experiences | 17 |
  | cloud-streamed | 11 |
  | mobile-casual-hypercasual | 4 |
  | console | 3 |
  | pc | 2 |
  | mobile-midcore-f2p | 2 |
  | single-player-narrative | 1 |

## Stage I verification

| grounded | count | ids |
|---|---|---|
| quote | 5 | takedown-4, takedown-7, ugc-17, catalog-16, catalog-17 |
| inferred | 47 | all others |
| speculative | 18 | netcode-10, takedown-5, takedown-12, takedown-15, takedown-16, takedown-20, ugc-1, ugc-2, ugc-3, ugc-4, ugc-8, ugc-9, ugc-10, ugc-13, ugc-14, catalog-2, catalog-10, catalog-12 |

Grounding by perspective:

| perspective | quote | inferred | speculative |
|---|---|---|---|
| netcode | 0 | 15 | 1 |
| takedown | 2 | 12 | 5 |
| ugc | 1 | 7 | 9 |
| catalog | 2 | 13 | 3 |

**already_offered.** 0 rows are true. Under a strict check, no note shows a vendor selling any of these exact options. The nearest matches each fall short of the option:
- **Antidote's cloud-streaming playtests:** they use recruited testers and give no cross-title catalogue benchmark, so they do not cover catalog-3.
- **Sensor Tower Creative Gallery:** it is a research view of ads, not a signed archive, so it does not cover takedown-4.
- **Relo Metrics:** it detects sports sponsor logos, not leftover logo traces in game ads, so it does not cover takedown-10.
- **Razer QA Companion-AI:** it finds bugs in a studio's own builds, not netcode effects in live matches.

**Changes made during verification.** Every changed row carries a `verify_note`. Fields were changed only where the notes did not support the original:
- **Grounding raised:**
  - takedown-4 and takedown-7, inferred to quote: competitor-and-ua.md section 2 states the gap each option fills (the ad library shows only active ads, and AppLovin has no public ad library).
  - netcode-14 and takedown-8, speculative to inferred: the HeadSpin churn framing and the GeekLab attribution complaint are in the notes.
- **Grounding lowered:** ugc-2 and ugc-13, inferred to speculative. Their only support was other YAML rows, not a research note.
- **Evidence rewritten** for netcode-5, netcode-6, netcode-11, takedown-13, ugc-12 and catalog-17. The fixes were:
  - a paraphrase had been presented as a quote;
  - one pointer was off-topic (live-ops staffing used as support for network incidents);
  - takedown-13 claimed the ad libraries can be filtered by country, which the notes do not say;
  - ugc-12 overstated "highlight tools are bought";
  - catalog-17 now also cites Apple's VERIFIED consent rule.
- **Citation corrected in takedown-2:** the willingness_to_pay and why_existing_tools_cannot fields cited an AppTweak price that the notes do not contain. The re-anchor is AppMagic "from $380/month" (competitor-and-ua.md section 1).
- **Citation corrected in takedown-7:** HeadSpin and WeTest sit in market.md section 3, not adjacent-usecases.md section 6.
- **Speculative rows:** every speculative row now has `evidence: none`. The author's closest pointer is kept in `verify_note`.
- Titles were not changed, and no row was deleted at Stage I.

# Adjacent paid use cases for AI over gameplay video (not user research)

Angle: non-research uses of gameplay video/audio that studios, platforms or teams already pay for.
Method note: 20 WebSearch queries (extended mode). WebFetch was blocked by the sandbox proxy (403/ENOTFOUND on every host), so no page was read in full. Every fact below comes from a search-result summary of the cited URL, not from reading the page. Treat prices from third-party blogs as weak.
Labels: VERIFIED = stated by a source (URL inline). INFERRED = my reading.

---

## 1. Automated QA and bug reproduction from recorded sessions

Who sells it
- VERIFIED: Razer QA Companion-AI. Analyses gameplay footage with vision-based detection for physics glitches, rendering errors, animation bugs, collision problems; reports carry repro steps and attached video; "zero-integration" (no SDK/code change); generates test cases from prompts or design docs; AI gameplay agents "in development". https://www.razer.com/blog/ai-that-plays-to-test-razer-qa-companion-ai-at-gdc-2026 , https://www.razer.ai/qac/ , https://www.razer.com/newsroom/company-news/razer-at-gdc-2026
- VERIFIED: modl.ai (Copenhagen). AI agents that autonomously play games to find bugs, glitches, performance issues. Series A EUR 8.5M, Nov 2022, led by Griffin Gaming Partners and Microsoft M12; ~USD 10.8M total (Tracxn). Reported customers/partners King, N3twork, Nitro (review-site claim, unverified). https://modl.ai/company , https://tracxn.com/d/companies/modl.ai/__01D8j4mt9i4qO2_GRo99Dw_54glkCC6RfbGDeNnRyTA , https://www.aicentralresources.com/tool/modlai
- VERIFIED: NodeMori BugHunter plays builds like a player and returns repro reports with video and logs (vendor claim). https://nodemori.com/
- VERIFIED: GameDriver (test automation; USD 7.39M total funding per Tracxn, BIP Ventures). https://theneuralbase.com/ai-for-gaming/learn/intermediate/tools-gamedriver-modl-ai/ (funding figure from Tracxn via search summary)
- VERIFIED: Keywords Studios sells outsourced QA and an AI-driven "Mighty Build and Test" platform (BuildBot, TestBot, ProofBot agents). FY2023 revenue EUR 780.4M (whole group, not QA only). https://www.keywordsstudios.com/en/services/globalize/qa-testing/ , https://www.keywordsstudios.com/download/file/TnorY0t5U2EvWDlSRmNDRGVkeG9WZz09/Full-Year-Results-2023-Presentation/

Who buys
- VERIFIED: game studios and publishers (King, N3twork, Nitro named for modl.ai). Razer targets indie PC studios at GDC (closed hands-on session). https://www.razer.ai/qac-gdc-26/
- VERIFIED: bug reports in industrial QA pipelines already include gameplay video; an academic study used 247 industrial QA videos and 100 long videos (41 hours) from an industrial QA pipeline. https://arxiv.org/pdf/2508.04895 , https://arxiv.org/abs/2603.22706

Price signals
- VERIFIED: outsourced game QA USD 15 to 50 per tester hour; a small mobile-game test cycle USD 1,000 to 5,000 (vendor blog, weak). https://snoopgame.com/blog/how-much-does-game-qa-testing-cost/
- VERIFIED: modl.ai and Razer QA Companion-AI publish no pricing (demo/quote). Sources above.
- VERIFIED: a dedicated in-house test lab estimated at USD 40k to 100k (blog figure, weak). https://gigatester.com/qa-outsourcing-for-gaming-companies/

What is manual today
- VERIFIED: testers watch hours of footage and hunt frames; research frames AI as triage, cutting "millions of raw frames to a few thousand candidates". https://arxiv.org/abs/2603.22706
- VERIFIED: best off-the-shelf VLM zero-shot baseline reached precision 0.50 / accuracy 0.72 on 100 industrial videos; many flagged anomalies were on-screen log messages. https://arxiv.org/abs/2603.22706
- VERIFIED: text-to-frame retrieval from bug videos hit Success@1 0.89 on 247 industrial QA videos; authors say it supports testers, does not replace them. https://arxiv.org/html/2508.04895v1
- VERIFIED (negative): a 2026 paper notes VLMs still struggle with certain bug classes (geometry clipping). https://arxiv.org/pdf/2607.25921
- INFERRED: accuracy is good enough for triage and bug-report enrichment, not for unattended detection.

---

## 2. Anti-cheat and fraud detection from video

Who sells it
- VERIFIED: Anybrain (non-intrusive detection of AI-based, pixel-bot and DMA cheats; claims >99% detection; supports operators in ban appeals with deeper investigations). No pricing. https://www.anybrain.gg/product , https://tech.eu/2026/05/15/meet-the-startup-taking-on-gaming-s-cheating-problem/
- VERIFIED: FACEIT "Human Input Detection", an ML layer judging inputs rather than cheat signatures; launched with Season 9 (5 Aug 2026); one outlet says no ban is triggered solely by its flag. FACEIT says AI-based and DMA cheats were 40% of cheating bans in May 2026. https://www.dust2.us/news/76438/faceit-adds-new-machine-learning-layer-to-combat-rising-ai-cheats , https://www.techtimes.com/articles/322336/20260730/faceit-human-input-detection-catching-cheats-that-signature-scans-miss.htm
- VERIFIED: Riot Vanguard (kernel level) and Activision Ricochet are in-house. Public detail is server-side ML on input/timing/recoil, not video. https://gameluster.com/gambling/why-online-games-feel-harder-to-play-fairly-in-2026-ai-cheat/ (low-authority source)
- NOT FOUND: no source confirms Riot, Activision or any vendor running computer vision on recorded footage as a production anti-cheat. The vision-based work found is academic: VADNet CNN on frames; computer-vision aimbots (read the screen, evade memory scanning) built as test cases. https://arxiv.org/pdf/2103.10031 , https://www.researchgate.net/publication/398874121_Detecting_Aimbot_Cheats_in_FPS_Games_Using_Computer_Visi_on_Effective_Methods_and_Challenges , https://arxiv.org/pdf/2606.25734

Who buys
- VERIFIED: game operators and tournament platforms (FACEIT is both vendor and operator); Anybrain sells to operators. Sources above.

Price signals
- None published. INFERRED: enterprise quote only.

What is manual today
- VERIFIED: players submit video clips of suspected cheaters; Overwatch players link video in reports and email hacks@blizzard.com (forum posts, possibly outdated). https://us.forums.blizzard.com/en/overwatch/t/how-can-i-report-a-cheater-with-video-evidence/384162
- VERIFIED: volunteer Discord groups collect clips and IDs of alleged cheaters. https://www.vice.com/en/article/gamerdoc-catching-banning-cheaters-hackers-overwatch-valorant/
- VERIFIED: server-side LSTM reached 88.6% accuracy with 0.97% false-positive rate in one paper; authors stress false accusations as the key risk. https://arxiv.org/pdf/2607.04336
- INFERRED: vision-cheat growth (screen-reading bots) is the reason video-level detection is a live problem; sellers of it are few.

---

## 3. Toxicity and safety moderation (voice mainly; video/gameplay adjacent)

Who sells it
- VERIFIED: Modulate ToxMod (voice). Named customers/titles: Call of Duty (MWII, MWIII, Warzone), Rec Room, Poker Stars VR. https://www.modulate.ai/case-studies/modulate-activision-case-study , https://gamesbeat.com/modulate-raises-30m-to-detoxify-voice-chat-in-games-with-ai/
- VERIFIED: GGWP (text, voice, gameplay actions, Discord). Seed USD 12M (2022, BITKRAFT); Riot Games listed as an investor; claimed customers Unity, Dreamhaven, Fatshark, Omeda Studios, Sandbox, thatgamecompany (startup-profile source); Unity Vivox partnership; "tens of billions of messages, 100+ games" (company claim). https://www.businesswire.com/news/home/20220321005241/en/Video-Game-Media-and-Technology-Veterans-Launch-GGWP-to-Combat-Game-Toxicity-Raise-%2412M-Seed-Funding , https://startupintros.com/orgs/ggwp , https://www.twoaveragegamers.com/ggwp-the-ai-moderation-platform-built-by-gaming-legends/
- VERIFIED: GGWP does not do anti-cheat but can take anti-cheat data as input. https://gamesbeat.com/ggwp-raises-10m-for-ai-based-platform-to-moderate-multiplayer-games/

Who buys
- VERIFIED: Activision (Call of Duty), studios on Unity Vivox, VR social platforms. Activision's FAQ says voice chat is monitored and recorded; ToxMod only reports, Activision decides enforcement. https://support.activision.com/articles/call-of-duty-voice-chat-moderation

Price signals
- VERIFIED (Modulate's own pricing page via search): tiers from a free Starter (1,500 one-time voice hours, 7.5 cents per extra hour) up to USD 20,000/month Mythic (200,000 monthly hours, 10 cents per extra hour); Epic/Legendary 50k/100k hours at 12 and 11 cents; custom above. https://www.modulate.ai/toxmod-pricing
- VERIFIED but conflicting third-party figures: USD 2,500/month starts; 15 cents/hour plus USD 2,000 onboarding. https://toosio.com/tool/modulate-voice-moderation-tool
- VERIFIED (third-party estimate): USD 0.01 to 0.05 per player-hour, USD 10k to 50k/month minimums for AAA. https://www.paxmod.com/blog/content-moderation-api-comparison-guide-2025
- GGWP: pay-as-you-go, free tier, custom for large studios. https://www.twoaveragegamers.com/toxmod-vs-ggwp-which-ai-moderation-tool-is-actually-better-2026/

Outcomes studios cite
- VERIFIED (Modulate/Activision case study): about 50% less toxic-voice exposure in MWII/Warzone North America; MWIII 25% less exposure (ex-Asia) and 8% fewer repeat offenders month-over-month; only about 23% of player reports contained actionable evidence. https://www.modulate.ai/case-studies/modulate-activision-case-study , https://gamesbeat.com/how-toxmods-ai-impacted-toxicity-in-call-of-duty-voice-chat-case-study/
- UNVERIFIED: "Riot reports 35% drop in voice toxicity in Valorant" appears only in a third-party guide; no Riot primary source found. https://flyfone.com/voip-meaning-in-gaming-benefits-challenges-and-top-tools/

What is manual today
- VERIFIED: player reports, of which about 77% lacked actionable evidence (Activision figure above); human moderators review flagged content.
- INFERRED: voice/text is the mature product; vision-based toxicity (offensive gestures, names, UGC on screen) was not evidenced in sources.

---

## 4. Accessibility compliance review from gameplay footage

Who sells it
- VERIFIED: Microsoft Gaming Accessibility Testing Service (MGATS). Human experts and players with disabilities test against Xbox Accessibility Guidelines (v3.2, 8 Jun 2023); failures logged as "concerns" with repro steps, expected/actual results and video/screenshot examples; ~7 business day turnaround goal (2021). https://learn.microsoft.com/en-us/xbox/accessibility/mgats , https://techcrunch.com/2021/02/17/microsoft-offers-new-accessibility-testing-service-for-pc-and-xbox-games/
- VERIFIED: AbleGamers APLAY (Accessible Playthrough Evaluation) report; listed as free to access but players must be compensated and use is limited per year. https://accessible.games/research-services/
- VERIFIED: Can I Play That? lists Accessibility Audits, Consulting, VPAT/ACR, Trainings (human-led). https://www.digitala11y.com/game-accessibility-resources-roundup/
- NOT FOUND: no AI product that audits gameplay footage for subtitles, contrast or colourblind issues; generic AI audit tools target websites/WCAG, not games. https://www.audioeye.com/post/ai-accessibility-tools/

Who buys
- VERIFIED: developers and publishers submitting Xbox/PC titles to Microsoft; studios using AbleGamers.

Price signals
- VERIFIED: MGATS price "determined by game complexity" and covers about 150 to 250 hours of testing; no fixed fee published. https://learn.microsoft.com/en-us/xbox/accessibility/mgats

Legal driver
- VERIFIED (conflicting): CVAA covers in-game voice/text/video chat, not core gameplay; sources disagree on waiver end date (31 Dec 2018 vs 2014); a January 2024 FCC FNPRM reportedly asks whether it reaches modern party chat. None confirmed from a primary FCC source. https://igda-gasig.org/what-and-why/about-cvaa/ , https://voxbooster.com/blog/game-accessibility-features-statistics-2026/

What is manual today
- VERIFIED: expert and disabled-player playthroughs; video is evidence, not the analysis input.
- INFERRED: checkable-from-pixels items (subtitle size/contrast, flashing, colour-only cues) are candidates; no vendor found doing it.

---

## 5. Localisation QA from video and screenshots

Who sells it
- VERIFIED: Gridly (LQA with screenshots, sounds, video next to text, AI checks), Alconost (game LQA mobile/PC/console), MarsTranslation (in-context validation: grammar, character limits, terminology). https://www.gridly.com/localization-qa/ , https://alconost.com/en/localization/testing , https://www.marstranslation.com/services/game-localization-quality-assurance
- VERIFIED: Keywords Studios also sells localisation and QA (see section 1).

Who buys
- VERIFIED: studios; King built an in-house bot that plays the game to capture localised screenshots for translators via TMS links. https://www.nimdzi.com/the-linguist-the-bot-and-the-bug-report/

Price signals
- None found.

What is manual today
- VERIFIED: clients take screenshots of every screen in the localised build and translators judge from them; reviewers check truncation, misaligned UI, placeholders in game. https://alconost.com/en/localization/testing , https://circletranslations.com/blog/game-localization-qa
- VERIFIED (Nimdzi): generic screenshot tools fall short for linguistic testing automation; wished-for features include language-aware visual anomaly detection (truncation, RTL rendering). https://www.nimdzi.com/the-linguist-the-bot-and-the-bug-report/
- INFERRED: a recording-based check that flags overflow/untranslated strings per language fits an evident gap; no vendor found offering it.

---

## 6. Performance and device-lab testing (frame drops, load times, thermals)

Who sells it
- VERIFIED: GameBench. SDK and Labs used by game studios, device makers, chipset vendors, review teams; measures FPS, frame stability, memory, CPU/GPU, battery, thermals; no public price (enterprise). Free Android FPS Monitor app shows temperature trends/throttling. https://quality.gamebench.net/gamebench-mobile-game-testing-methodology , https://www.gamebench.net/blog/gamebench-fps-monitor-free-android-app-launch
- VERIFIED: device clouds with video/log capture per run: AWS Device Farm, BrowserStack (one comparison lists 3000+ devices vs 100+ for AWS; TestMu AI claims 10,000+). https://www.getpanto.ai/blog/device-farms-for-mobile-testing , https://www.testmuai.com/blog/mobile-game-testing/
- VERIFIED: Razer QA Companion logs crashes and performance issues with video clips (section 1).

Who buys
- VERIFIED: studios, OEMs, chipset vendors (GameBench). Vendor-claimed.

Price signals
- VERIFIED (weak): compatibility testing of a major mobile title can need 500 to 2,000+ device-OS combinations (market report); vendors with large labs charge per device-hour. https://dataintelo.com/report/game-testing-outsourcing-market , https://www.gamedevoutsourcing.com/services/qa-testing

What is manual today
- VERIFIED: same build can run 60 fps on a flagship and 24 fps on a mid-tier phone; physical devices still needed for touch latency, thermals, battery. https://game-ace.com/blog/android-game-testing/ , https://salivity.github.io/game-development/article/android-game-compatibility-testing-across-devices
- VERIFIED: reliable fps/load measurement uses in-game profiling or GameBench rather than video alone. https://www.testmuai.com/blog/mobile-game-testing/
- INFERRED: video-only analysis competes with cheap counters for fps; its edge is rendering/visual defects per device model and no-SDK use on shipped builds.

---

## 7. Live-ops and event monitoring (competitor live events)

Who sells it
- VERIFIED: GameRefinery Live Events Tracker. Analysts play 100+ games daily across PC/console/mobile; documents 35+ live event types as screenshots plus analyst comments; links events to downloads/revenue. https://www.gamerefinery.com/live-events-tracker/ , https://www.gamerefinery.com/supercharge-liveops-with-gamerefinery-event-tracking/
- Adjacent: AppTweak and ASOMobile track store-listing changes and in-app events, not in-game events. https://www.apptweak.com/en/aso-tools/app-competition-monitoring

Who buys
- VERIFIED: live-ops and product teams at mobile studios (implied by tracker positioning).

Price signals
- None found.

What is manual today
- VERIFIED: most live events are announced without notice and cannot be scraped; gathering takes large human resources. https://www.pocketgamer.biz/how-to-keep-track-of-the-myriad-of-live-service-events-across-mobile-games/
- INFERRED: this is the closest evidenced paid analogue to "competitor analysis from video"; analysts doing it by hand is the gap.

---

## 8. Esports coaching and player analytics from VOD

Who sells it
- VERIFIED: Mobalytics (GPI post-game scorecards). Plus USD 9.99/month or 69.99/year (older guide: 7.99); UK review lists GBP 5-7 Pro and GBP 10 Elite with coaching sessions. Funding USD 13.8M (Tracxn) to 16.8M (PitchBook); revenue estimates USD 1M to 25M (Dealroom/Owler/Growjo, unconfirmed); several profiles say acquired by ESL FACEIT Group (dates disagree). https://hexgate.app/blog/u-gg-vs-mobalytics/ , https://gameboostinghub.com/reviews/coaching/mobalytics/ , https://tracxn.com/d/companies/mobalytics/__LuEwOUQusuEtwTUvqZyCoGtRJ23eHBU1_jkf12aXx9s , https://www.owler.com/company/mobalytics
- VERIFIED: Blitz paid tier around USD 3 to 4 per month (sources disagree); overlay-centred. https://hexgate.app/blog/hexgate-vs-blitz-vs-mobalytics/
- VERIFIED: Insights.gg collaborative VOD review (timestamps, drawing, group sessions, permissions); listed at USD 0; annotation tool, not automated AI analysis. https://insights.gg/insights-web
- VERIFIED: ClutchLabs (AI video analyst for Valorant scrims, VOD-derived metrics without data feeds), Omnic.AI (CV on player videos), Enlyo, Ono Trading (unreleased). https://clutchlabs.ai/ , https://www.omnic.ai/
- VERIFIED: StatStack USD 49 (Pro) to 149 (Organization) per month; DataCoach USD 0 to 18 per month (players). https://statstackhq.com/pricing , https://www.datacoach.gg/
- VERIFIED: Cloud9 assistant coach "Macro Review" builds VOD-review agendas from game data. https://medium.com/@avish.kaushik20/how-we-built-an-ai-powered-coaching-assistant-for-esports-bf522b4e453e
- Benchmark VERIFIED: Hudl from USD 1,500 per program per year (traditional sports). https://www.guideflow.com/blog/sports-performance-analytics-software

Who buys
- VERIFIED: individual ranked players (low single-digit to about 10 USD/month); esports teams and coaches (tens to low hundreds USD/month at the StatStack end).

What is manual today
- VERIFIED: coaches/analysts scrub VODs and comment by hand; esports analyst is a staffed job (Fortnite team listing). https://builtin.com/job/esports-analyst-fortnite-team/4056497 , https://gamerabble.ai/blog/what-is-a-vod-review
- INFERRED: price points are low and much of the market is free-tier or ad-supported; the buyer is a player or team, not a studio.

---

## 9. Player support (agent sees what the player saw)

Who sells it
- VERIFIED: Helpshift (Unity-owned) game support platform; SDK for iOS/Android/Unity/Unreal/web/PC/console; auto-captures device, version, patch, entitlements, session state; no video/replay confirmed. Pricing: custom; monthly platform fee plus per-issue rate, 1,000 issues/month included, unlimited agent seats. Capterra reviewer calls it expensive. https://unity.com/products/helpshift , https://www.softwareadvice.com/call-center/helpshift-profile/ , https://www.helpshift.com/blog/top-omnichannel-customer-support-platforms-for-gaming/
- VERIFIED (non-game): Fullview (replays inside Zendesk/Intercom/Salesforce/HubSpot tickets), Screendesk (Chrome extension saving the last two minutes), Userback, Dummi "Issue Capture" in Intercom's store. https://www.fullview.io/products/replays , https://screendesk.io/chrome-screen-recorder
- NOT FOUND: no off-the-shelf vendor of a rolling last-30-seconds game-client buffer attached to a ticket.

Who buys
- VERIFIED: studios ask players for video by hand: Resolution Games and Arrowhead support pages request recordings ("especially videos"). https://resolutiongames.zendesk.com/hc/en-us/articles/12540109949083-I-want-to-report-something , https://arrowhead.zendesk.com/hc/en-us/articles/16234689094940-I-ve-found-a-bug-How-do-I-report-it

What is manual today
- VERIFIED: players self-record and attach; agents watch.
- INFERRED: gap is automatic capture plus AI summary of the clip into the ticket; no priced evidence.

---

## 10. Game design balancing from aggregated play

Who sells / does it
- VERIFIED: EA used playtesting agents for progression modelling on The Sims Mobile (paper, not a product). https://arxiv.org/pdf/1903.10545
- VERIFIED: academic agents detected difficulty spikes across versions of platformers; board-game study concludes AI playtesting complements humans, cannot replace them. https://arxiv.org/pdf/2304.08699 , https://diego-perez.net/assets/pdf/papers/CaseStudyTAG-CoG23.pdf
- VERIFIED: modl.ai and PlaytestCloud sit adjacent (agents; human playtest video). PlaytestCloud AI summarises playtest recordings, results in about 48 hours; AI included at no extra charge. https://www.playtestcloud.com/ai-powered-analysis
- PlaytestCloud pricing VERIFIED but inconsistent: EUR 1,130/month Basic and EUR 2,825/month Advanced on its page; third parties list USD 1,175 and USD 3,075 per month yearly with 120 video tokens per year. https://www.playtestcloud.com/pricing , https://sourceforge.net/software/product/PlaytestCloud/
- NOT FOUND: no source of balancing done from aggregated real-player footage; balancing evidence is agent self-play and telemetry.

What is manual today
- INFERRED: designers rely on telemetry and playtests; video is not the balancing input in any source found.

---

## Count and gaps

- Use cases with a named vendor or buyer: 10 of 10 (QA, anti-cheat, toxicity, accessibility, localisation, performance, live-ops, esports coaching, support, balancing).
- Use cases where a named vendor's product analyses video/footage: 4 (QA: Razer, NodeMori; esports VOD: ClutchLabs, Omnic.AI; playtest research: PlaytestCloud; anti-cheat: Anybrain, method not confirmed as video). Voice/text moderation (Modulate, GGWP) and performance (GameBench) are audio, text or telemetry products.
- Evidenced gaps: no AI product found for accessibility-from-footage, localisation-from-video, last-30-seconds support clip, or video-based balancing.

## Signals of willingness to pay

- Studios pay per voice hour for toxicity: Modulate USD 20,000/month top public tier, 10 to 12 cents per extra hour; Activision runs it at scale and publishes outcome numbers. (VERIFIED, URLs in section 3)
- Studios pay for human accessibility audits: MGATS prices by 150 to 250 testing hours; AbleGamers free but players must be compensated. (VERIFIED, section 4)
- Studios and OEMs pay for performance measurement: GameBench enterprise pricing, SDK and Labs; outsourced QA USD 15 to 50 per hour; a large Android device matrix is a stated cost driver. (VERIFIED, weak, sections 1 and 6)
- Mobile studios pay analysts to play competitor games daily and screenshot live events (GameRefinery); the vendor says this needs "large human resources". (VERIFIED, section 7)
- Research teams pay PlaytestCloud about EUR 1,100 to 2,800/month for recorded playtests with AI summaries. (VERIFIED, section 9/10)
- Players and small teams pay low amounts (USD 3 to 18/month, free tiers common); team products at USD 49 to 149/month. (VERIFIED, section 8)
- Complaints: Helpshift described as expensive and SDK iOS integration issues (Capterra reviewers, anecdotal); player reports to Activision lack actionable evidence in about 77% of cases; VLM bug detection precision about 0.50; Nimdzi says generic screenshot tooling is inadequate for linguistic testing; anti-cheat flags risk false accusations (FACEIT says no ban from the flag alone). (VERIFIED, URLs above)
- Anti-cheat and live-ops-from-video have no public price evidence at all.

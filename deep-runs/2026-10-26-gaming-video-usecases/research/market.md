# Angle: MARKET — who already sells gameplay-video / session-recording analysis to game studios

Method note: 40 WebSearch queries (standard + extended). WebFetch could not be used: the egress proxy refused every target host (playtestcloud.com, antidote.gg, gamesbeat.com, pocketgamer.biz, wikipedia.org all returned ENOTFOUND / CONNECT 403). Every VERIFIED bullet is therefore based on search-engine extracts of the cited URL, not a full read of the page. Treat figures as "stated by the source per search extract". Vendor-authored pages are marked (vendor).

Legend: **V** = VERIFIED (stated by the cited source). **I** = INFERRED (my reading, not stated by a source).

---

## 1. Playtesting platforms that record player video (user research)

### PlaytestCloud (Berlin/Potsdam, GmbH)
- V: Sells remote playtests with a player panel; per-player recordings, "AI-powered analysis" and a summary report, most results within 48 hours (vendor FAQ). https://www.playtestcloud.com/pricing
- V: Pricing (vendor): Professional Basic €1,130/month billed annually with 120 Video Tokens/year; Professional Advanced €2,825/month with 240 tokens/year. A single-session or concept playtest = 1 token per player; other methods or advanced targeting from 1.5 tokens. Indie Pass = 5 tokens/month (eligibility: <15 employees, <$1M funding, <$1M revenue). Free trial = 2 tokens. https://www.playtestcloud.com/pricing
- I: Basic tier works out to roughly €113 per recorded player-session (€13,560/yr ÷ 120 tokens); Advanced about €141/token. So studios currently pay around €100–150 for each recorded and analysed player video.
- V: Third-party listings conflict: Fitgap $1,085–$1,139/month; G2 says "not published, contact sales". https://us.fitgap.com/products/playtestcloud , https://www.g2.com/products/playtestcloud/pricing
- V: Platforms: iOS, Android, PC (Steam, browser), concepts/prototypes; PC playtesting launched later. https://www.gamespress.com/en-US/PlaytestCloud-Launches-PC-Playtesting
- V: Product lines include unmoderated single-session, multi-day longitudinal tests, moderated sessions, concept testing, surveys, kids' playtests, accessibility playtests and **competitor playtests**. https://www.playtestcloud.com/facts
- V: AI analysis: generates per-video annotations and a per-player summary, flagging moments of enjoyment/frustration. It uses the OpenAI API on **video transcripts and survey responses** (help centre). https://help.playtestcloud.com/en/articles/7941599-understanding-ai-powered-analysis , https://start.playtestcloud.com/product-updates/faster-insights-with-ai-powered-analysis
- V: "First Findings" (about 2025) reviews all videos in an order, groups findings by theme, and links each friction point to its clip. https://start.playtestcloud.com/product-updates/meet-first-findings-a-completely-revamped-ai-analysis-experience-across-your-entire-playtest
- V: Rebranded as "Player Insights Platform™" (deck dated April 2025). https://www.playtestcloud.com/
- V: Named customers: Ubisoft, Supercell, Zynga, Rovio, Metacore. Over 5,000 playtests ran in 2024 (2025 report). https://www.playtestcloud.com/facts , https://start.playtestcloud.com/steal-this-strategy-playtestclouds-research-report-on-how-successful-studios-playtest-their-games
- V: Vendor claim on its G2 page: "half of the mobile games grossing $5b+ were tested on our platform". https://www.g2.com/products/playtestcloud/discuss
- V: Customer quote (vendor blog, unnamed customer): "The AI analysis has been a real time-saver for our team." https://start.playtestcloud.com/product-updates/meet-first-findings-a-completely-revamped-ai-analysis-experience-across-your-entire-playtest
- V: Panel of 1.5M+ players. Testers are paid about $5–9 USD for a 15-minute playtest plus survey. https://leadiq.com/c/playtestcloud/5a1dc4eb2300005400c7548d , https://players.playtestcloud.com/article/118-rewards-a-summary
- V: Funding: essentially bootstrapped. PitchBook lists a $130K grant (2012), Tracxn $135K. https://pitchbook.com/profiles/company/92770-84 , https://tracxn.com/d/companies/playtestcloud/__qrB7RBLDSG3Cytx8dfLG6BrTGSJvyCCt0tsEDisThpM
- V: Revenue estimates conflict: Latka $34M (2025); LeadIQ $25–50M; Owler/ZoomInfo under $5M. Headcount estimates range from 29 to ~334. https://getlatka.com/companies/playtestcloud.com , https://www.owler.com/company/playtestcloud
- V: Tester-side complaints: too few test opportunities, payment refused over instruction interpretation, low pay for the effort. https://moneypantry.com/playtestcloud-review/ , https://www.thebudgetdiet.com/playtestcloud-review
- **Does NOT do** (I, based on the help-centre description of what the AI reads): the AI reads transcripts and surveys, not pixels. Nothing indicates computer-vision analysis of the gameplay frames (game state, UI screens, level/progress detection). It only analyses recruited testers, not the studio's live players, so there is no churn or retention link to production telemetry. No competitor analysis from public video. Its "competitor playtests" are recruited humans playing a rival game.

### Antidote (antidote.gg; operated by Sekg, Barcelona)
- V: Remote playtesting for PC and mobile. Pricing: free trial; $115 per game per month; $475 per game per month; Indie Plus $99/month. https://antidote.gg/pricing/ , https://antidote.gg/indies/
- V: Captures face and gameplay recording (synced, up to 4K), think-aloud transcripts, mobile screen touches, controller inputs, game events, surveys, plus Steam/Xbox integration. Offers sentiment analysis and automated reports. https://antidote.gg/platform-features/face-gameplay-recording/ , https://antidote.gg/platform-features/
- V: "AI Insights" summarises feedback per session and across projects, and analyses "player recordings, survey responses and transcripts", flagging moments in footage. https://antidote.gg/platform-features/ai-insights/
- V: Anti-leak SDK watermarks a player ID on screen. Auto-Inject SDK is Windows and Android only. Also offers cloud-streaming playtests. https://antidote.gg/platform-features/antidote-sdk/ , https://antidote.gg/platform-features/cloud-streaming-playtesting/
- V: Crunchbase shows a private company with 11–50 staff and no disclosed rounds. An unverified Substack thesis claims Sekg was valued at €800M in 2022. https://www.crunchbase.com/organization/antidote-cecb , https://jordinoguera.substack.com/p/antidote-tesis-de-inversion
- **Does NOT do** (I): this is lab-style research on recruited testers, not analysis of live-player footage. No churn or LTV link. Mobile SDK coverage is Android only for auto-inject.

### We Playtest Games (indie marketplace)
- V: Pay-per-playtest from $15. First 30-minute singleplayer test free. Up to 3h of feedback, multiplayer up to 8 players. Subscriptions $79/month (Indie) and $379/month (Studio), about $15–16 per playtest hour. https://weplaytestgames.com/docs/faq/ , https://weplaytestgames.com/
- I: This is the low-end price anchor: about 10x cheaper per hour than PlaytestCloud tokens, aimed at indies.

### Playtest (Netherlands), G.Round
- V: Playtest is a seed-stage Dutch service for pre-launch gamer feedback. G.Round appears as a PlaytestCloud competitor on CB Insights. No pricing found. https://www.cbinsights.com/company/playtest , https://www.cbinsights.com/compare/ground-2-vs-playtestcloud
- Note: "PlaytestWorld" returned no results under that name.

### Player Research (Brighton, UK) — services agency
- V: Games user-research consultancy that combines playtests, biometrics (arousal sensors) and eye tracking with interviews. It also supported Testronic's California UX lab (2013). https://www.pocketgamer.biz/the-science-of-fun-player-research-on-the-profit-of-putting-the-player-first , https://www.mcvuk.com/gdc-13-testronic-opens-user-experience-lab/
- V: Its own researcher has said biometrics are "often oversold". https://esel.at/termin/75889
- **Does NOT do** (I): it is a people-heavy agency rather than software, so it does not scale to thousands of sessions.

### Valve — Steam Playtest (free substitute)
- V: Free playtest feature on a separate child app ID. Developers control player count and timing. Above 50k keys it is effectively an open beta. No recording or analysis is provided. https://partner.steamgames.com/doc/features/playtest
- I: This free distribution channel is a substitute for recruitment, but it leaves a gap: no capture and no analysis. A vendor could fill that gap.

---

## 2. Session-replay SDKs used in games (production players, not recruited testers)

### IV Metrics (ivmetrics.com)
- V: Unity SDK that records the **actual rendered gameplay as video** with touch overlays and FPS/RAM metrics on iOS, Android and Amazon. https://www.ivmetrics.com/unity-session-replay
- V: Pricing: Free (20 videos, 1 project, 5 min/video). Indie $49/month (50 videos, 20 min). Pro $99/month (100 videos, 10 projects, 60 min, funnel analytics). https://www.ivmetrics.com/
- V: Markets itself as a gameplay-video add-on to PostHog and Mixpanel and as a "Smartlook alternative built for mobile games". https://ivmetrics.com/posthog-for-mobile-games , https://ivmetrics.com/smartlook-alternative
- I: The video caps (50–100 videos/month) show this is sampled review by a human, not AI analysis at fleet scale. No evidence of automated CV interpretation of the footage.

### PostHog (Unity session replay)
- V: The Unity SDK is **screenshot-based**, with no built-in masking of text or images, unlike its web and mobile SDKs. https://posthog.com/docs/session-replay/installation/unity , https://posthog.com/compare/best-mobile-app-session-replay-tools

### Jahro
- V: Offers "Session Replay for Unity Games" (feature page). https://jahro.io/features/session-replay

### Smartlook (Cisco)
- V: Listed as supporting Unity and Unreal; "best choice for game developers" on less common frameworks (third-party comparison). Free tier is 3,000 sessions/month. Reviewers describe the pricing as "very high". https://www.crazyegg.com/blog/uxcam-vs-smartlook/ , https://www.g2.com/compare/fullstory-vs-uxcam-vs-smartlook , https://www.trustradius.com/compare-products/smartlook-vs-uxcam
- I (from my prior knowledge, not re-verified in this run): Cisco acquired Smartlook in 2023. A UXCam blog refers to a "Cisco acquisition".

### UXCam
- V: Lists Unity among supported frameworks. No game-studio case study found; its customer stories are non-game apps. https://info.uxcam.com/mobile-app-session-replay
- V: Not publicly priced. Vendr median is about $20,991/year. Tiers by monthly sessions; free plan 3,000 sessions/month. https://userpilot.com/blog/uxcam-pricing/ , https://uxcam.com/pricing
- **Does NOT do** (I, for all generic replay tools): these reconstruct native UI view trees. Engine-rendered game canvases show up as a black box or as screenshots. There is no game-state understanding (level, boss, currency, death) and no semantic tagging of what happened in the gameplay.

### Bugsee / Instabug (now Luciq) — video bug and crash reporting
- V: Bugsee continuously records video of user actions at 10 fps with network, console and system traces, attached to crashes. Instabug captures crashes and shake-to-report, and has rebranded as Luciq. https://bugsee.com/crash-reporting/ , https://bugsee.com/blog/bugsee-vs-instabug/
- V: Third-party warning about GDPR/HIPAA masking and consent for video capture. https://us.fitgap.com/products/bugsee
- **Does NOT do** (I): neither is game-specific, and neither does automated visual analysis of the recorded frames.

---

## 3. AI playtesting / QA agents and video-based bug detection

### modl.ai (Copenhagen)
- V: AI agents that autonomously play games for QA. Products: modl:QA+, modl:play, modl:test. https://www.aicentralresources.com/tool/modlai
- V: $8.4M Series A (Nov 2022) led by Griffin Gaming Partners and Microsoft M12. Total funding is reported variously as $10.1M, $10.8M or $19.7M. https://gamesbeat.com/modl-ai-seriesa-ai-bot-qa-testing-griffin-gaming-microsoft-m12/ , https://tracxn.com/d/companies/modl.ai/__01D8j4mt9i4qO2_GRo99Dw_54glkCC6RfbGDeNnRyTA , https://seedtable.com/companies/modlai
- V: No public pricing; demo required. Reported customers King, N3twork, Nitro, plus a 2026 partnership with Side (single secondary review). https://www.aicentralresources.com/tool/modlai
- V: "State of Games QA" (survey of 303 US devs, Sep 2024): 77% did less QA than they should have; only 23% completed all QA before release; 94% use non-AI automation; 18% feel fully prepared for AI in QA; 16% fully trust AI outcomes, 10% not at all. https://www.thefpsreview.com/2025/02/05/77-of-game-developers-believe-there-isnt-enough-qa-being-done-new-report-finds-as-studios-begin-turning-to-ai-to-refine-qa-processes-and-optimize-resources/ , https://modl.ai/state-of-games-qa-report
- **Does NOT do** (I): bots play builds before release. It does not analyse real players' footage, and it says nothing about churn, monetisation or UX.

### nunu.ai (Zurich / San Francisco; YC W23)
- V: Multimodal agents that play and test games via natural-language commands. The agent is "fully vision-based, taking a live stream from the device and issuing taps, swipes, keyboard input". Supports PC, iOS, Android. https://www.ycombinator.com/companies/nunu-ai , https://www.testmuai.com/blog/ai-in-mobile-qa/
- V: $2M pre-seed (Aug 2024) and $6M seed (Mar 2025), co-led by a16z speedrun and TIRTA, with YC participating. https://www.pocketgamer.biz/nunuai-secures-6m-to-scale-ai-agents-for-game-qa/ , https://www.finsmes.com/2025/03/nunu-ai-raises-6m-in-seed-funding.html
- V: Google Cloud partnership; agents run on Gemini. https://cloud.google.com/blog/products/gaming/co-op-mode-the-ai-partners-driving-the-the-future-of-gaming/
- V: Named customer Roboto Games (13-person studio, Stormforge) runs 400+ automated tests a month. QA cost reported down 50% (newsletter) and up to 30% (Naavik/co-founder). https://viewpoints.fov.ventures/p/investing-in-nunu-ai , https://thefourthquarter.substack.com/p/the-4th-quarter-latest-in-sports-308 , https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/
- V: Also expanding into robotics. https://en.ain.ua/2025/04/08/nunuai-raises-6-m/
- **Does NOT do** (I): its vision is for agent control, not for analysing human sessions. No player-behaviour analytics product.

### GameDriver
- V: Automation framework for Unity and Unreal, "no code changes", first Unity Verified Solution for automated testing. Sold as SaaS or managed "Quality-as-a-Service". https://gamedriver.ai/
- V: March 2025: starter plans from $150/month (press release). A 2026 guide says the price is quote-only. https://www.businesswire.com/news/home/20250317108053/en/GameDriver-Unveils-Standalone-Test-Assistant-for-Unity-and-Unreal-Alongside-Transparent-Pricing , https://quashbugs.com/blog/best-game-testing-tools
- V: Competes with AltTester (comparison). https://testguild.com/tools/alttester-vs-gamedriver
- **Does NOT do** (I): scripted, object-level automation. No video and no player data.

### Regression Games (Philadelphia)
- V: $4.2M seed (Aug 2022, NEA, a16z). Pivoted from AI esports to an AI agent testing platform for Unity. Status listed "Active". https://www.prnewswire.com/news-releases/ai-gaming-and-esports-startup-regression-games-raises-4-2m-in-seed-funding-from-nea-and-a16z-301605698.html , https://startupintros.com/orgs/regression-games

### ManaMind (London) — 2026 launch
- V: About €1.2M pre-seed (late April 2026, Sure Valley Ventures). Vision-language agents that find bugs "through video and audio alone" and auto-generate bug reports, with claims of up to 80% faster QA. https://theaiworld.org/news/manamind-raises-12m-to-automate-game-qa-with-ai , https://techfundingnews.com/tfn-pitch-decks-2026/

### Razer — WYVRN QA Companion-AI (formerly AI QA Copilot)
- V: Launched GDC 2025 inside the WYVRN developer ecosystem. Flags bugs, crashes and performance issues during test sessions. Reports include screenshots, clips and event logs. https://www.razer.com/newsroom/company-news/razer-reveals-wyvrn-ai-powered-gaming-ecosystem-for-game-developers
- V: GDC 2026: **vision-based detection of rendering, physics, animation and collision bugs directly from recorded footage**. Bug reports include suggested repro steps and attached video. https://www.razer.com/blog/ai-that-plays-to-test-razer-qa-companion-ai-at-gdc-2026
- V: Needs no SDK or game instrumentation. A hotkey captures the 20 seconds before an issue. https://doc.wyvrn.com/docs/razer-ai-gaming-tools/razer-qa-co-ai/ , https://www.wyvrn.com/razer-ai-gaming-tools/qa-companion/
- V: GA on AWS Marketplace since 13 Nov 2025. Jira integration. Supports Unreal, Unity and custom C++ engines. Vendor claims up to 25% more bugs found and 50% faster testing. https://elservicecentre.com/razer-ai-gaming-hub-singapore
- **Does NOT do** (I): sits next to QA testers on PC builds. Not used on consumer devices or live-player footage, and offers no UX or churn insight.

### Tencent WeTest — Acorn AI / PerfDog
- V: WeTest is Tencent's one-stop game QA platform. "Acorn AI Studio" uses multi-agent AI to play games and find issues (GDC 2026). Pricing is tiered by usage and quote-based. A blog cites PerfDog "Professional" at about $1,200 for 50 test hours (unverified). https://www.wetest.net/introduction/about , https://x.com/Wetest_Global , https://www.wetest.net/blog/mobile-game-performance-testing-2026-perfdog-guide-1189.html
- V: Naavik: large players such as WeTest build AI QA in-house; Unity and Unreal are testing their own tools. https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/

### Keywords Studios (now private, EQT)
- V: Taken private by an EQT-led consortium (with CPP Investments and Temasek) for about £2.1–2.2bn (€2.5bn), completed Oct 2024. 2023 revenue €780M. https://irishtimes.com/business/2024/07/03/keywords-studios-agrees-25-billion-bid-from-private-equity-firm-eqt , https://investgame.net/news/2-8b-private-takeover-of-keywords-is-officially-completed/
- V: Its Globalize Tech Platform auto-generates bug-report metadata so teams can "move away from... long playthroughs, video capturing, and metadata checks". https://www.keywordsstudios.com/en/about-us/news-events/news/the-power-of-ai-and-strategic-partnerships/
- **Does NOT do** (I): no productised AI analysis of gameplay video found. Its QA revenue is labour-based outsourcing.

### Other QA service firms: Lionbridge Games, Testronic, GlobalStep, PTW, iBeta, Applause, Testlio
- V: No dedicated AI video-analysis QA product found for these firms. Lionbridge's 2026 AI push is localisation (Samurai). Market reports vaguely say Testronic, GlobalStep and iBeta use "AI-powered" methods. https://semiconductors.einnews.com/pr_news/933217891/lionbridge-games-brings-player-first-localization-powered-by-human-guided-ai-to-gamescom-2026 , https://dataintelo.com/report/ai-powered-video-game-testing-market
- V: Applause and Testlio crowdtesting are quote-only. G2 users rate Testlio's perceived cost at the top of the scale. https://www.gartner.com/reviews/product/applause-crowdsourced-application-testing-services , https://g2.com/products/testlio/pricing

### HeadSpin — device performance and video quality
- V: Real-device testing in 50+ locations tracking FPS, CPU, memory, battery and network. Video quality KPIs (blockiness, blurriness, reference-free MOS) for game streams. 2019: Zynga, Jam City, Bandai Namco studios and a NetEase partnership. CEO quote: "over 30 per cent of people left their game due to a bad experience". https://headspin.io/solutions/test-gaming-apps , https://www.pocketgamer.biz/gdc-2019-mobile-performance-platform-headspin-partners-with-netease

### Research signal: bug-frame retrieval from gameplay video
- V: arXiv 2508.04895: FFmpeg keyframes (median 1.90% of frames) capture the bug moment in 98.79% of cases. A VLM picks the frame matching a bug report: top-1 F1 0.79 and accuracy 0.89, weakest on Animation & VFX (0.51). https://arxiv.org/html/2508.04895v1

### Market sizing for AI QA
- V: Naavik (21 Jul 2026): the AI-for-QA category is "early, fragmented, and still waiting for its breakout moment". Startups have raised $35.8M in total, led by modl.ai and nunu.ai, and none has reached Series B scale. "Proper case studies are still hard to find." https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/

---

## 4. Computer-vision and gameplay-video companies (data, coaching, playable clips)

### Medal (medal.tv) and General Intuition
- V: Medal has about 10M MAU, and users upload about 2B clips/year, which can carry controller and mouse inputs. https://www.pocketgamer.biz/general-intuition-raises-134m-to-train-ai-agents-using-gameplay-videos/
- V: OpenAI reportedly offered $500M for Medal in late 2024 (The Information; unconfirmed). Spin-out General Intuition raised a $134M seed (Oct 2025, Khosla, General Catalyst), then reportedly $320M at a $2.3B valuation (2026), for $454M disclosed in total. https://podcasts.apple.com/is/podcast/310-pim-de-witte-on-turning-down-%24500-million-from/id1241195252?i=1000734415499 , https://techcrunch.com/2026/06/25/from-fortnite-to-robots-general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/ , https://startupfortune.com/general-intuition-raises-320-million-on-the-thesis-that-video-game-footage-is-the-most-underrated-training-data-in-robotics/
- V: Medal's developer products: free auto-clipping API (the game sends an event and Medal saves a clip on the player's PC) and a clip-retrieval API. No studio-facing analytics product or pricing found. https://medal.tv/developer/auto-clipping , https://docs.medal.tv/api.html
- **Does NOT do** (I): Medal and GI do not sell insight back to studios. Gameplay video is monetised as AI training data for agents and robotics, not as analytics for game teams.

### Worldmodeldata (Cambridge, UK) and Origin Lab — 2026
- V: Worldmodeldata raised a £7M seed (Jul 2026) and has licensed nearly 1M hours of game data from studios for world-model training. Paying individual players is a future plan. https://www.resultsense.com/news/2026-07-06-worldmodeldata-gaming-ai-training-seed/ , https://superpowerdaily.com/posts/worldmodeldata-says-it-licensed-nearly-1-million-hours-of-game-data-for-ai-training
- V: Origin Lab helps studios sell assets and gameplay to world-model labs: 500k+ hours from 250+ games. https://www.neowin.net/amp/this-startup-is-helping-gaming-companies-sell-their-data-to-world-model-labs/
- I: This is a second revenue line for studios. Gameplay video they hold has resale value to AI labs, and that changes what "pay for analysis" competes with.

### Microsoft — Muse (WHAM)
- V: Trained on 1B+ frames and controller actions, about 7 years of Bleeding Edge gameplay (Ninja Theory), announced Feb 2025. Matches were recorded under the EULA, which drew criticism over consent. Weights released on Azure AI Foundry. https://www.geekwire.com/2025/microsoft-reveals-new-gaming-focused-generative-ai-model-muse-that-could-revive-classic-games/ , https://stevivor.com/news/microsoft-scrapes-bleeding-edge-to-make-new-muse-ai-model/

### Omnic.AI (Brunswick, Maine) — CV on uploaded gameplay video, sold to players
- V: Forge uses CV and deep learning on uploaded match recordings (VALORANT, Fortnite, Rocket League, OW2, Madden NFL 25, Marvel Rivals, Apex). No plug-in or API needed. Freemium: 5 uploads free, paid unlimited. Partners PlayVS and NACE (Jul 2026). Won the 2024 MIT Sloan startup competition. https://www.techradar.com/computing/artificial-intelligence/can-an-ai-coach-help-your-esports-team-clinch-the-championship , https://www.gamedeveloper.com/press-release/omnic-ai-named-official-performance-intelligence-partner-of-the-national-association-of-collegiate-esports
- I: Proof that per-title CV parsing of game state from pixels works commercially. The buyer is players and schools, not studios.

### Insights.gg
- V: Player- and team-facing gameplay capture and review tool, not a studio product. https://gamesbeat.com/insights-gg-launches-stand-alone-platform-for-gameplay-capture/

### Ludeo — playable clips
- V: SDK turns gameplay moments into playable clips (e.g. the IO Interactive Hitman DLC trailer). 100+ indie studios on self-serve. About $42M raised (including a $30M Series A led by Corner Ventures). Indie program offers up to $10K creator grants. https://www.gamedeveloper.com/press-release/ludeo-opens-early-access-to-self-serve-integration-for-developers-enabling-game-studios-to-turn-gameplay-clips-into-instantly-playable-experiences-fast , https://app.dealroom.co/companies/ludeo
- **Does NOT do** (I): marketing and distribution, not analytics.

---

## 5. Stream and UGC analytics (Twitch, YouTube, Kick)

### Hatchet (formerly Stream Hatchet; owned by GameSquare)
- V: Web dashboard tiers: Starter free, Essentials $249/month, Pro from $1,249/month, custom publisher reporting on quote, 30-day free trial. https://streamhatchet.com/pricing/
- V: Rebranded as "Hatchet" on 26 Aug 2026 as a creator-marketing analytics platform covering 30+ platforms, 50M+ creators and 10 years of data, with an "AI Smart Search". Clients named: EA, NASCAR. https://variety.com/2026/gaming/news/stream-hatchet-rebrand-creator-marketing-gamesquare-1236842946/ , https://www.netinfluencer.com/gamesquare-relaunches-stream-hatchet-as-ai-driven-creator-marketing-platform/
- V: Largest campaign contract to date with Capcom (Mar 2025). Riot Games renewed esports reporting (relationship since 2019) in Jun 2026. https://www.mordorintelligence.com/industry-reports/gaming-influencer-marketing-services-market , https://www.newswire.com/news/gamesquare-renews-and-expands-partnership-with-riot-games
- **Does NOT do** (I): measures viewership metadata (hours watched, viewers, chat) per category and creator. No evidence it analyses the gameplay pixels inside streams, such as which level, mode or moment drives viewers, or where streamers quit.

### Streams Charts, SullyGnome, TwitchTracker
- V: Category-level viewership stats (channels, viewers, hours watched). https://streamscharts.com/ , https://sullygnome.com/games
- V: Q2 2025 share of gaming hours watched: Twitch 54%, YouTube Gaming 24%, Kick 11% (Stream Hatchet data, via secondary source). https://tech-insider.org/twitch-vs-kick-vs-youtube-gaming-2026/

### StreamElements, Streamlabs (publisher sponsorship networks)
- V: Creator tools are public-priced (StreamElements $10–25/month; Streamlabs Ultra $27/month). Publisher sponsorships are sold by campaign quote. https://www.capterra.com/p/233962/StreamElements/ , https://streamforge.com/blog/best-gaming-influencer-marketing-platforms

### Gamesight, Lurkit
- V: Gamesight does marketing measurement and attribution for PC and console games. Lurkit does creator key distribution and campaigns. https://www.cbinsights.com/company/innervate/alternatives-competitors , https://streamforge.com/blog/best-gaming-influencer-marketing-platforms

### Relo Metrics (GumGum) — CV logo detection in broadcast video
- V: CV detects every visible sponsor logo across broadcast, streaming and social video (prominence, screen share, duration), paired with VideoAmp viewership. Accelerated on NVIDIA (2025). https://www.businesswire.com/news/home/20250318535732/en/Relo-Metrics-Accelerates-AI-Powered-Sponsorship-Analytics-for-Sports-Entertainment-with-Computer-Vision-and-Multi-Modal-AI-Powered-by-NVIDIA
- I: This is a mature "CV on video, sold to marketers" business model in sports. Search found no esports or in-game equivalent.

---

## 6. UA, creative and competitor intelligence touching gameplay video

### Replai
- V: CV tagging of video ad creatives with performance analytics. It later moved into generating creatives from in-game data. Largest category is gaming. Customers cited include King and Activision. Handled over $2.5B of video spend (2021) and over $5B/year (2023 claim). About $6–8M raised (Hoxton, Sequoia, Accel, Lux). https://venturebeat.com/games/replai-automates-analysis-of-video-ad-effectiveness/ , https://www.businesswire.com/news/home/20211013005090/en/Replai-Announces-Funding-as-it-Pioneers-New-Software-Category-in-Customizable-AI-based-Video-Intelligence , https://genesysgrowth.com/blog/motion-vs-adskate-vs-replai

### Sett (Tel Aviv)
- V: AI agents produce video and playable ads for mobile game UA. $12M seed + $15M Series A (May 2025, Bessemer), then a $30M Series B (Greenfield), $57M in total. Customers: Playtika, SuperPlay, Candivore, Cyplay. TechCrunch also lists Zynga, Scopely, Rovio, Plarium, Unity. Vendor claims 15x time and 25x cost savings. https://techcrunch.com/2025/05/07/game-sett-funding-a-startup-building-ai-agents-for-game-development-emerges-from-stealth-with-27m , https://www.sett.ai/content/sett-raises-series-b-57m-total-funding/ , https://pulse2.com/sett-27-million-series-a-secured-for-gaming-focused-agentic-ai-platform/
- I: UA teams are the best-funded AI buyers in mobile games ($57M into one creative vendor vs $35.8M into all AI-QA startups combined).

### GameRefinery (Liftoff)
- V: Feature-level competitor data: game feature deconstructions, live-event tracking, and a taxonomy of 4 categories, 12 genres and 52 subgenres. No public price; bundled into Liftoff Intelligence. https://www.gamerefinery.com/ , https://liftoff.ai/intelligence/
- V: Benchmarks (2025): casual CPI $1.41 iOS / $0.14 Android; D30 ROAS 47% iOS / 15% Android. https://liftoff.ai/2025-casual-gaming-apps-report/
- I: Deconstructions are produced by analysts playing games by hand. That is a manual competitor-analysis workflow that video AI could automate. No source shows them using CV on gameplay video.

### Ludo.ai, SocialPeta, Apptica, Sensor Tower
- V: Ludo.ai offers market analysis and trends at about $15–40/month (sources conflict). No video analysis. SocialPeta and Apptica cover competitor playable-ad intelligence. https://www.capterra.com/p/228190/Ludo/ , https://socialpeta.com/en/blog/best-playable-ad-research-tools

### GameAnalytics
- V: IQ Suite (AnalyticsIQ, MarketIQ, PipelineIQ, SegmentIQ) launched 15 Oct 2025. MCP server added Feb 2026. "Live Map" session replay. No video. https://mobidictum.com/gameanalytics-iq-suite , https://docs.gameanalytics.com/products-and-features/iq-pro-features

---

## 7. Emotion and biometric capture (facecam analysis)
- V: Affectiva (bought by Smart Eye in 2021 for about $73.5M, along with iMotions) had a Unity plug-in used in the game Nevermind for runtime adaptation. The group now leans towards automotive. https://www.affectiva.com/success-story/flying-mollusk/ , https://en.wikipedia.org/wiki/Affectiva
- V: Realeyes spun its ad-emotion business off as Adverteyes (Nov 2025). iMotions combines facial coding, Tobii and Smart Eye eye tracking, GSR and EEG on one timeline. No current game-studio playtest product found. https://www.forasoft.com/blog/article/real-time-ai-emotion-software
- V: Academic work used Affdex to predict flow, frustration and boredom during educational game play. https://asu.elsevierpure.com/en/publications/predicting-real-time-affective-states-by-modeling-facial-emotions/

---

## 8. 2025–2026 launches (dated)
- Feb 2025: Microsoft Muse (gameplay-trained world model). https://www.geekwire.com/2025/microsoft-reveals-new-gaming-focused-generative-ai-model-muse-that-could-revive-classic-games/
- Feb 2025: modl.ai State of Games QA report. https://modl.ai/state-of-games-qa-report
- Mar 2025: Razer WYVRN AI QA Copilot (GDC); nunu.ai $6M seed; GameDriver standalone Test Assistant from $150/month.
- Apr 2025: PlaytestCloud "Player Insights Platform™" deck; First Findings AI around this time.
- May 2025: Sett out of stealth ($27M); later Series B ($57M total).
- Oct 2025: General Intuition $134M seed; GameAnalytics IQ Suite (15 Oct).
- Nov 2025: Razer QA Companion-AI GA on AWS Marketplace (13 Nov).
- Mar 2026: Razer vision-based bug detection from footage (GDC 2026); WeTest Acorn AI Studio (GDC 2026); Hatchet Creator Communities.
- Apr–May 2026: ManaMind €1.2M pre-seed (VLM bug detection from video and audio).
- Jun–Jul 2026: General Intuition $320M at $2.3B; Worldmodeldata £7M seed; Naavik "State of AI for Game QA" (21 Jul).
- Aug 2026: Stream Hatchet rebranded as Hatchet (26 Aug).
- Oct 2026: Playgama Sandbox, where agents use gameplay data to iterate AI-built games (14 Oct). https://www.gamespress.com/en-US/Playgama-closes-the-iteration-loop-for-AI-built-games-agents-now-see-p

---

## 9. Gap map: what nobody in this sample sells (INFERRED from the "does NOT do" notes above)
- I: No vendor found that applies computer vision to **production player** gameplay video from consumer devices and links it to retention, churn or monetisation telemetry. Playtest vendors analyse recruited testers through transcripts. Session-replay SDKs record or screenshot but do not interpret game state. QA agents analyse builds, not people.
- I: No vendor found that does **CV-based competitor gameplay analysis** (auto-deconstructing a rival's FTUE, economy or live-ops from video). GameRefinery and similar do this with human analysts. PlaytestCloud's "competitor playtests" are recruited humans.
- I: Stream analytics (Hatchet, Streams Charts) measure audience metadata, not in-game content. Relo-style CV exists in sports but was not found for in-game moments or esports.
- I: The only shipped product doing CV on gameplay footage for studios is QA bug detection (Razer QA Companion-AI, ManaMind, research by arXiv 2508.04895). Omnic does CV game-state parsing, but sells it to players.

---

## Signals of willingness to pay

**Who buys and what they pay (VERIFIED prices):**
- Games-user-research and product teams at mobile F2P and PC studios (Ubisoft, Supercell, Zynga, Rovio, Metacore) pay **€13.6k–€33.9k/year** to PlaytestCloud for 120–240 recorded player sessions, about €113–141 per recorded and analysed session. https://www.playtestcloud.com/pricing
- Smaller studios pay **$115–$475 per game per month** (Antidote) or **$15/playtest; $79–379/month** (We Playtest Games). https://antidote.gg/pricing/ , https://weplaytestgames.com/docs/faq/
- Indies pay **$49–99/month** for gameplay-video session replay (IV Metrics, capped at 50–100 videos). https://www.ivmetrics.com/
- Generic mobile session replay: UXCam median about **$21k/year** (Vendr). https://userpilot.com/blog/uxcam-pricing/
- QA automation: GameDriver **from $150/month** (2025); modl.ai, nunu.ai, WeTest and Razer are quote or marketplace priced. https://www.businesswire.com/news/home/20250317108053/en/GameDriver-Unveils-Standalone-Test-Assistant-for-Unity-and-Unreal-Alongside-Transparent-Pricing
- Publishers and marketing teams (EA, Capcom, Riot) pay **$249–$1,249+/month** for stream analytics, plus custom contracts. https://streamhatchet.com/pricing/
- UA teams (Playtika, SuperPlay, Zynga, Scopely, Rovio, Plarium) buy AI creative tooling. Sett has raised $57M on this demand. Replai reported $5B/year of ad spend through its platform. https://www.sett.ai/content/sett-raises-series-b-57m-total-funding/ , https://genesysgrowth.com/blog/motion-vs-adskate-vs-replai
- AI labs pay for gameplay video plus inputs as training data: OpenAI's reported $500M offer for Medal; Worldmodeldata licensing about 1M hours; Origin Lab 500k+ hours. https://www.pocketgamer.biz/general-intuition-raises-134m-to-train-ai-agents-using-gameplay-videos/ , https://superpowerdaily.com/posts/worldmodeldata-says-it-licensed-nearly-1-million-hours-of-game-data-for-ai-training

**Investment comparison (VERIFIED):** AI-QA startups have raised $35.8M combined (Naavik), compared with $57M for a single UA creative vendor (Sett) and $454M for General Intuition's gameplay-video world models. https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/

**What buyers value (VERIFIED quotes and claims):**
- "The AI analysis has been a real time-saver for our team." (PlaytestCloud customer, vendor blog)
- Time-to-insight sells: a 48-hour turnaround (PlaytestCloud); First Findings links each friction point straight to its clip.
- QA cost reduction: 30–50% (nunu.ai claims); "up to 25% more bugs, 50% faster" (Razer claim); "up to 80% faster QA" (ManaMind claim).
- HeadSpin CEO (2019): "over 30 per cent of people left their game due to a bad experience". This is the churn framing performance vendors sell on.

**What they complain about or distrust (VERIFIED):**
- QA under-investment: 77% of devs did less QA than they should have, and only 23% finished QA before launch (modl.ai survey).
- Trust in AI is low: only 16% fully trust AI QA outcomes, and only 18% feel ready to adopt it (modl.ai survey).
- Proof is thin: "proper case studies are still hard to find" in AI QA (Naavik, Jul 2026).
- Session replay in game engines is poor: PostHog Unity is screenshot-only with no masking, and UXCam-style tools reconstruct native UI, not game canvases.
- Privacy and consent around recording players: Bugsee masking/GDPR warnings; the Muse/Bleeding Edge EULA consent criticism.
- Smartlook pricing "very high" (TrustRadius reviewers); Testlio perceived cost rated at the top of G2's scale.
- Playtest panel quality is a hidden risk: tester-side complaints about pay disputes and effort-to-pay ratio (PlaytestCloud reviews). I: these incentives can degrade the quality of the recorded sessions.
- Biometrics are "often oversold" (Player Research).

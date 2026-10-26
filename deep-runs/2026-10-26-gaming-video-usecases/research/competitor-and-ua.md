# Competitor analysis and UA/marketing analysis from video

Angle: competitor teardown, ad-creative analysis, highlight/trailer generation, influencer/UGC monitoring, app store video testing.

Method note: WebSearch was run 31 times. WebFetch and curl to vendor domains (gamerefinery.com, segwise.ai, venturebeat.com, vendr.com) were refused by the egress proxy (403 / ENOTFOUND), so no page was read in full. Every "VERIFIED" bullet is what a source states as returned in search results. Many sources are vendor blogs selling the thing they describe; they are flagged "(vendor)". Prices are third-party estimates unless marked "published".

## 1. How studios do competitor teardowns today

### VERIFIED
- GameRefinery (now part of Liftoff) runs on human analysts: they download and play games and map each feature into a database; about 260 features are tracked manually, from core/meta loops down to individual ad features. https://www.gamerefinery.com/game-intelligence-tools/ and https://www.gamerefinery.com/market-explorer-supercharge-your-feature-research/
- GameRefinery added automated tags in Oct 2020 for 100,000+ iOS games: models read app-store metadata to infer 51 features and 45 visual styles; analyst-built tags replace the automatic ones once a game is fully analysed. The input is store metadata, not gameplay video. https://www.gamerefinery.com/product-update-october-2020-automated-tags/ and https://aithority.com/gaming/gamerefinery-introduces-automated-tagging-to-track-ios-games-features/
- Liftoff says GameRefinery holds a library of 2,500+ game feature deconstructions with visuals and implementation examples. https://liftoff.ai/intelligence/
- GameRefinery Live Events Tracker (launched Mar 2023): analysts monitor live events daily across Match3, Midcore and Casual, covering battle passes, subscriptions, limited-time shops, currencies, ad implementation and IAP. https://www.gamespress.com/en-US/GameRefinery-launches-competitive-intelligence-tool-to-monitor-live-ev and https://www.gamerefinery.com/how-to-build-better-live-events-with-the-gamerefinery-live-events-tracker/
- Sensor Tower bought Playliner (live-ops tracking), announced 18 Jun 2025. Its product page says the team logs "hundreds of hours" of playtime to capture live ops across 230+ top games. No collection tooling is named. https://sensortower.com/blog/playliner-acquisition and https://sensortower.com/product/live-ops
- Liftoff Intelligence = GameRefinery + AppRefinery (AppRefinery launched 11 Jun 2025, 20+ app verticals), covering 100,000+ apps and games. https://www.prnewswire.com/news-releases/liftoff-debuts-apprefinery-unlocking-deep-intelligence-into-the-worlds-leading-consumer-apps-302478011.html and https://liftoff.ai/blog/intelligence-for-actionable-insights-for-smarter-growth/
- Vungle bought GameRefinery in 2021, citing image recognition and creative tagging for Vungle Creative Labs; Vungle then merged with Liftoff (Blackstone majority owner). https://vungle.com/news/vungle-acquires-gamerefinery-a-leading-saas-mobile-gaming-analytics-company/ and https://www.marketingdive.com/news/liftoff-vungle-merge-to-form-broad-mobile-app-growth-platform/605580/
- Sensor Tower bought data.ai in Mar 2024 (price undisclosed; one analyst estimate about $300M on roughly $100M revenue), Video Game Insights (PC/console, Mar 2025) and Playliner (Jun 2025). https://www.gamesmarket.global/takeover-sensor-tower-buys-rival-dataai-158148a88c046f265c7d6da7e427105d and https://sensortower.com/press/press-release-sensor-tower-acquires-video-game-insights-adds-pc-console-gaming-data
- AppMagic ad intelligence ranks creatives by impressions; its basic tier gives revenue and downloads estimates for all apps. https://appmagic.rocks/articles/basic-plan/?hl=en
- Sensor Tower Ad Intelligence has a Creative Gallery (banner, video, playable) showing impressions, network and duration per ad, share-of-voice ranking and alerts; its 2026 game advertising report uses Pathmatics data. https://sensortower.com/solutions/marketing and https://sensortower.com/blog/state-of-game-advertising-2026
- Deconstructor of Fun publishes weekly game deconstructions written by operators from Supercell, Zynga and Rovio; it gives no published step-by-step method. https://www.deconstructoroffun.com/deconstructions and https://www.gdcvault.com/play/1026491/Deconstructor-of-Fun-Breaking-Down
- Deconstructor of Fun published a 2025 FTUE case: sessions grouped by early behaviour and tied to day-1 retention, leading to a tutorial change (ask if the player knows the game, then branch to a detailed tutorial). This is a studio's own telemetry, not competitor video. https://www.deconstructoroffun.com/blog/2025/8/18/5-real-cases-where-better-data-questions-drove-game-growth
- Reference libraries for FTUE/UI exist as human-captured screenshots/flows: Gamedexy (186 chronological flows, 1,887 screens, 25 mobile games; Pro $99/year; free tier shows first 3 steps) and Game UI Database (55,000+ screenshots, 1,700+ videos, 1,341 titles). https://www.gamedexy.com/ and https://www.gamedeveloper.com/design/game-ui-database-relaunches-with-new-features-video-support-and-over-55-000-screenshots
- Gemini can take video input; Google reports up to 88% lower token use for agentic video analysis on its own benchmarks, default 1 FPS sampling, about 6 hours of video in 2M context. No source covers game FTUE extraction. https://developers.googleblog.com/en/gemini-2-5-video-understanding/ and https://www.fonearena.com/blog/491156/google-gemini-agentic-video-understanding.html

### Prices (third-party, not published)
- Sensor Tower: no list price. Vendr-derived figures reported by third parties: median $75,000/yr across 40 purchases, range $29,500 to $115,460; API adds $5,000-$20,000/yr; extra modules $1,500-$5,000+/month (single source); auto-renews unless notice 90 days before term. https://marketintelligencetools.com/reports/sensor-tower-pricing/ and https://www.vendr.com/marketplace/sensor-tower and https://trysonar.app/blog/sensor-tower-pricing
- GameRefinery: no list price. A competitor's comparison page (about 3 years old) quotes $45k / $47k / $51k per year across three tiers, and says many companies subscribe to both services. GameRefinery advertises free revenue/download data for 100,000+ games in 33 markets. https://product.liquidandgrit.com/comparisons/l-and-g-vs.-game-refinery
- AppMagic: no published price. Reviews conflict: Premium "from $380/month" vs older "$150/month" vs a case study saying "from $2,480". Enterprise adds API and consulting. https://omr.com/en/reviews/product/appmagic/pricing and https://www.mobileappdaily.com/product-review/appmagic and https://www.dashly.io/custom-chatbot/appmagic-case-study/

### INFERRED
- Feature, monetisation and live-ops coverage of competitors is a human-play-and-log process priced at five-figure annual contracts; the coverage is limited to the top roughly 100-250 games for live ops and a few hundred to low thousands deep-tagged.
- Automated tagging in the market today reads store metadata and ad creatives, not recorded gameplay sessions. No source shows a vendor extracting FTUE steps, shop layouts or event cadence from gameplay video automatically.
- Gamedexy and Game UI Database show demand for FTUE/flow reference built by human capture; automated capture from video would target the same buyer (designers, product managers).

## 2. Using public video (YouTube, Twitch, TikTok, store previews, ad libraries) for competitor research

### VERIFIED
- Meta Ads Library is free, shows only active ads on Facebook/Instagram, no spend data; weekly lightweight monitoring uses Meta Ads Library plus TikTok Creative Center, monthly deeper review uses paid tools (Sensor Tower, AppMagic, MobileAction) (vendor). https://blog.insightrackr.com/en/docs/Meta-Ads-Library-vs-Premium-Ad-Intelligence-Platforms and https://www.spiral.ad/insights/competitor-ad-research-mobile-apps
- AppLovin publishes no public competitor ad library; screenshotting ads seen inside another game mislabels them as that game's creative (vendor guide). https://www.admapix.com/blog/ad-intelligence/applovin-ads-spy-tool
- Rule of thumb that an ad running 30+ days is profitable is a vendor claim, not data. https://www.admapix.com/blog/app-going-global/mobile-game-marketing-strategy
- Sensor Tower's 2026 game advertising report: video drove growth in creative counts, peaking Mar 2026; playables stayed under 15/month while static images rose from 17 to 60/month (per summary). https://gamedevreports.substack.com/p/sensor-tower-game-advertising-in
- Apple allows app preview videos up to 30 seconds, up to three per product page. https://www.mobileaction.co/blog/product-page-optimization/ and https://www.apptweak.com/en/aso-blog/product-page-optimization-a-guide-to-app-store-a-b-testing
- AI Vidia states App Store previews may only use footage captured in the app itself (vendor). https://ai-vidia.com/industries/gaming

### INFERRED
- No source describes a product that ingests YouTube/Twitch/TikTok gameplay of a competitor and returns features, monetisation touchpoints or FTUE steps. Search returned none; this is an absence in search results, not proof of absence in the market.
- Competitor ad libraries expose creatives but not what happens after install; gameplay recorded from a device is the only path to post-install flow (FTUE, offers, shops, events).

## 3. AI ad-creative analysis for UA

### VERIFIED
- Segwise: published tiers Growth $499/month (up to $250K monthly ad spend, 500 AI tokens), Pro $1,699/month ($250K-$500K spend, 2,000 tokens), Enterprise custom ($500K+); 10% annual discount; 7-day free trial; unlimited seats; 50% startup discount under $50K spend. Pricing is by ad spend. https://segwise.ai/pricing
- Segwise (vendor) says it tags playables, connects to 15+ ad networks (Meta, Google, TikTok, AppLovin, Unity, Mintegral, Moloco) and MMPs (AppsFlyer, Adjust, Branch, Singular). https://segwise.ai/blog/creative-strategies-mobile-game-advertising
- Segwise (vendor) repeatedly claims manual tagging takes 20+ hours a week per app, cites no study; describes taggers drifting on labels and playables being too slow to tag by hand so most teams skip them. https://segwise.ai/blog/manual-vs-ai-creative-tagging and https://segwise.ai/blog/creative-tag-taxonomy
- Segwise cites a report that the top 2% of gaming video creatives took 60.7% of spend in Q2 2026 (unverified). https://segwise.ai/blog/creative-strategies-mobile-game-advertising
- Replai: began 2020 with AI highlight clips from Twitch/YouTube streams (claimed up to 2,000 streams at once), now computer-vision and LLM tagging of video ads plus automatic variation generation; raised $8M+, claims $5B+ ad spend handled (2023), clients named include Activision and Dream Games; CEO described tagging gameplay as well as ad video. https://venturebeat.com/games/replai-introduces-ai-for-mobile-game-ads-and-raises-8m/ and https://aithority.com/gaming/replai-opens-up-its-ai-powered-video-highlight-platform-for-gaming-and-esports-with-an-early-access-launch/ and https://www.pocketgamer.biz/replais-new-ai-service-offers-marketers-a-revolution-in-ad-creation/
- Alison.ai: Creative Genome tags hooks, pacing, visuals, messaging, CTAs per frame; pre-launch scoring; integrates with Meta, Google, TikTok, AppLovin, Unity; publishes casual-game "Creative Intelligence Reports" on Unity Ads (claims such as ASMR sorting creatives +38% IPM, match-3 speedruns install rates -19%; vendor, unverified, two reports name different winners). https://alison.ai/resources/blog/alison-ai-creative-intelligence-report-casual-mobile-games-trend-forecast and https://alison.ai/resources/creative-intelligence-reports
- Alison.ai pricing is inconsistent across listings: $10, $20 or $25 per user per month, or on request. https://www.capterra.com/p/10005094/Alison-ai/ and https://www.getapp.com/marketing-software/a/alison-ai/ and https://www.revavenues.ai/tools/alison-ai
- Vidmob: no published price; sales-led, reported as priced per brand / by annual impressions; computer vision on objects, scenes, gaze, emotion, element timing; pre-launch scoring against platform rules; standard processing for paid-media assets under 2 minutes; no gaming-specific product found. https://vidmob.com/creative-scoring and https://improvado.io/blog/creative-analytics and https://growthengineer.ai/startups/vidmob
- "Kaya": no creative-analytics product found under that name; the only hit is a London AI marketing agency. Not covered. https://www.ycombinator.com/launches/LTw-kaya-ai-powered-marketing-agency
- Meta "Creative breakdown" reporting dimension (launched 11 Jul 2025 per a blog) shows per-asset results for Flexible-format ads; no source confirms it supports app-install campaigns. https://www.relevantaudience.com/facebook-ads/metas-new-creative-breakdown-feature-what-you-need-to-know/
- AppLovin: creative sets hold up to 10 videos and 10 interactive/image assets and the AI tests combinations itself; SparkLabs is AppLovin's own creative build/test tool for video and playables from templates. https://support.axon.ai/en/growth/promoting-your-websites/analyze-and-optimize/best-practices-for-success and https://playableadsmaker.com/blog/applovin-axon-ads-manager
- Winning-hook claims (all vendor, conflicting): FoxData says fail-state hooks lead in 10,000+ ads analysed; Artstash citing a games.gg report says gameplay demo ads median CTR 4.27% vs 3.34% for cinematic trailers and gameplay in first 3 seconds gives 25% higher view-through; genre changes the answer. https://foxdata.com/en/blogs/winning-ad-creatives-for-mobile-games-analyzing-10000-ads-to-find-what-works/ and https://creative.artstash.io/performance-creative-for-games/
- RocketShip HQ: top 10% of mobile game advertisers produce 5x the creative variants per week of the median. Segwise puts testing at 50-200 new variants per title per week. https://www.rocketshiphq.com/creative-velocity-mobile-gaming/ and https://segwise.ai/blog/mobile-game-ua-creative-testing
- GeekLab: hard to see which creative acquired players who later retain and pay, especially on iOS. https://geeklab.app/posts/ua-campaign-optimization-for-mobile-games-how-to-optimize-for-player-value/
- Production cost anchors: Admiral Media AI video batches EUR 10,000 / 20 videos, EUR 16,000 / 40, EUR 29,000 / 80; playables $3,000-$5,000 each externally (AppAgent) up to $30,000+ for complex ones. https://admiral.media/ai-video-ads-agency/ and https://dev.to/aplusgamesstudio/playable-ads-in-2026-how-they-are-built-and-what-they-cost-j36
- Liftoff's Mobile Ad Creative Index is built with GameRefinery intelligence. https://content.liftoff.io/hubfs/2024/Reports/Mobile%20Ad%20Creative%20Index/2024%20Mobile%20Ad%20Creative%20Index%20-%20EN.pdf

### INFERRED
- Every tool above analyses the ad video plus network metrics (impressions, IPM, CPI). None links an ad element to what the acquired player did on device in the first session; that link is the gap GeekLab describes.
- Which gameplay moment converts is currently answered from the ad side. Recorded gameplay from real devices would give a candidate source of "most clip-worthy moments" per game, which no vendor above claims to use.
- Segwise's per-spend pricing implies the buyer is a UA team with a media budget; $499-$1,699/month is small next to $75K/yr Sensor Tower contracts.

## 4. Automatic highlight and trailer generation from recorded gameplay

### VERIFIED
- Hypetrigger: computer-vision highlight detection (OCR plus TensorFlow image recognition, GPU decode); needs per-game config (crop region, colour filter, text pattern, e.g. the word "DEAD" in Hunt: Showdown). https://hypetrigger.io/games/hunt-showdown/ and https://www.producthunt.com/products/clip-it?launch=clip-it
- Eklipse: cloud VOD processing using kill detection and audio hype; best on FPS/battle royale; users complain of triggers on audio spikes or idle play. https://blog.eklipse.gg/tools/ai-clip-maker-gaming.html
- Outplayed (Overwolf) uses game event data via API integrations for supported titles, visual detection as fallback; claims 5,000+ games. Medal has auto-clipping for a supported-title list; method not documented. https://clipwick.com/articles/outplayed-review and https://medal.tv/learn/best-clipping-software
- A TechCrunch piece contrasts NVIDIA's per-game event bindings with computer vision, which is game-agnostic. https://techcrunch.com/?p=2200891
- Choppity and Transcriptr-style clippers detect from audio reactions and commentary, not gameplay. https://www.choppity.com/tools/free-ai-clip-maker/ai-clip-maker-for-gaming/ and https://transcriptr.ai/blog/ai-gaming-clip-generator
- Mootion and Reelmind market gameplay-to-trailer generators (highlight detection, transitions, templates); speed claims are self-reported and a Reelmind case study could not be verified. https://www.mootion.com/use-cases/en/ai-for-game-development-videos and https://reelmind.ai/blog/game-trailer-generator-automatically-create-console-quality-promos-from-raw-gameplay-footage
- No search result shows a major studio using these tools in-house for trailers. No independent accuracy benchmarks found.

### INFERRED
- Existing highlight tools target streamers and viewers on PC/console titles; none is shown handling mobile gameplay recorded on-device.
- Replai's pivot from stream highlights to ad creative suggests highlight clipping alone was a thinner business than creative intelligence tied to ad spend (reading of its history, not stated by a source).

## 5. Influencer and UGC monitoring of gameplay clips

### VERIFIED
- Gamesight: measurement and attribution for PC/console, tying creator content to clicks, wishlists and purchases across Steam, Xbox, PlayStation; managed creator service; no public pricing. No clip-monitoring product found. https://streamforge.com/blog/best-gaming-influencer-marketing-platforms and https://www.netinfluencer.com/emilee-helm/
- Lurkit: key distribution plus organic and paid creator campaigns across Twitch, YouTube, Shorts, TikTok; tiers Indie, Studio, Publisher on quote; indie reportedly about $89/month with up to 70% indie discount; 15-20% commission on paid quests (sources differ). https://www.lurkit.gg/pricing and https://toolradar.com/tools/lurkit and https://www.bountyboard.gg/blog/bounty-board-vs-lurkit
- Streams Charts ranks games, publishers and streamers by viewership on Twitch, YouTube, Kick; SullyGnome and TwitchTracker are free Twitch trackers; Hatchet (ex Stream Hatchet) covers long-tail platforms. https://streamscharts.com/games/publishers and https://streamforge.com/blog/best-gaming-influencer-marketing-platforms
- Jestr is a clip marketplace paying per 1,000 views; typical cost per view cited at $0.02-$0.20 YouTube and $0.01-$0.05 TikTok (directory, unverified). https://firstlook.gg/blog/gaming-influencer-marketing-agencies/
- Liftoff 2024 Mobile Ad Creative Index headline: UGC and interstitial ads are key to ROI. https://www.prnewswire.com/news-releases/liftoff-mobile-ad-creative-index-reveals-ugc-and-interstitial-ads-are-key-to-unlocking-advertising-roi-302078540.html

### INFERRED
- Monitoring today is by viewership counts, tracked links and keys, not by what is shown in the clip. Nothing found reads clip content (a bug visible, a competitor feature praised, a monetisation complaint on screen).
- Most influencer tooling in results is PC/console; mobile influencer/UGC monitoring is thinly covered.

## 6. App store video A/B testing

### VERIFIED
- Apple Product Page Optimization tests icon, screenshots and app previews: up to 3 treatments plus control; tests need Apple review. https://www.mobileaction.co/blog/product-page-optimization/ and https://appradar.com/blog/app-ab-testing-with-product-page-optimization-in-apple-app-store
- Google Play store listing experiments: sources disagree on whether the promo video is testable; run at least 7 days. https://www.apptamin.com/blog/google-experiments-impact-video/ and https://appfollow.io/blog/aso-ab-testing-for-mobile-games
- Reported preview-video conversion lifts: 18-35% for games with gameplay in the first 3 seconds (Strataigize), +15-25% (Adapty), up to 25% (TekRevol); all vendor, same sources say video hurt Finance/Productivity by 3-7%. Apple publishes no video-specific metrics. https://www.strataigize.com/blog/app-store-conversion-rate-optimization and https://adapty.io/blog/app-store-conversion-rate/ and https://www.tekrevol.com/blogs/app-store-conversion-rate-optimization/
- Significance needs roughly 2,000-5,000 daily product page views for 14 days (Strataigize); video effects are noisier than icon/screenshot effects. https://www.strataigize.com/blog/app-store-conversion-rate-optimization and https://www.mobileaction.co/blog/google-play-store-listing-experiments/

### INFERRED
- The test itself is free from the stores; the manual work is choosing which clip to show and cutting variants. Highlight selection from recorded gameplay would feed this step.

## 7. What is manual today (summary of the above)

### VERIFIED
- Feature deconstruction and live-ops logging by analysts playing games (GameRefinery 260 features; Playliner hundreds of hours across 230+ games).
- Creative tagging by people in spreadsheets (20+ hours/week claim, vendor).
- Playable tagging mostly skipped because it is slow (vendor).
- Highlight tools need per-game configs (Hypetrigger) or per-game integrations (Outplayed, NVIDIA).
- Competitor ad review via free libraries plus occasional paid tools.

### INFERRED
- FTUE and monetisation-flow teardown of competitors has no named automated product in search results; the closest are human-built flow libraries (Gamedexy, Game UI Database).

## 8. Signals of willingness to pay

### VERIFIED
- Studios and publishers pay five figures a year for competitor intelligence: Sensor Tower median $75,000 (range $29,500-$115,460, third-party Vendr data); GameRefinery about $45-51k per year (old competitor quote); some firms buy both (Liquid and Grit page). Named GameRefinery users: FoxNext, Ubisoft, MAG Interactive, Lootcakes, Lotum, Pixonic (homepage and case study pages). https://product.liquidandgrit.com/comparisons/l-and-g-vs.-game-refinery and https://liftoff.ai/ja/resources/case-study/lotum-gamerefinery/ and https://www.gamerefinery.com/
- Sensor Tower paid for Playliner (live ops, human logged), Video Game Insights and data.ai in 2024-2025, so acquirers are paying to extend game-feature coverage. https://sensortower.com/blog/playliner-acquisition
- UA teams pay $499-$1,699/month (Segwise published tiers) for creative tagging tied to ad networks; Alison $10-$25/user/month listed; Vidmob and Replai quote-only. https://segwise.ai/pricing
- Replai raised $8M+ for gameplay/ad-video tagging, named clients Activision and Dream Games. https://venturebeat.com/games/replai-introduces-ai-for-mobile-game-ads-and-raises-8m/
- Studios pay agencies per creative: EUR 363-500 per AI video (Admiral), $3,000-$5,000 per playable (AppAgent). https://admiral.media/ai-video-ads-agency/ and https://dev.to/aplusgamesstudio/playable-ads-in-2026-how-they-are-built-and-what-they-cost-j36
- Complaints found: tagging is slow and inconsistent between people; playables not tagged; attribution from creative to retained/paying players is weak (especially iOS); highlight tools trigger on noise or need hand configuration; AppLovin ad-seen-in-game is mislabelled by manual spying; Alison/Replai evidence is vendor-sourced with no independent customer case studies for gaming found. https://segwise.ai/blog/manual-vs-ai-creative-tagging and https://geeklab.app/posts/ua-campaign-optimization-for-mobile-games-how-to-optimize-for-player-value/ and https://blog.eklipse.gg/tools/ai-clip-maker-gaming.html
- Buyers named across the sources: UA managers and creative strategists (Segwise, Alison, Replai), product/design and live-ops teams (GameRefinery, Playliner, Gamedexy), marketing/community teams (Lurkit, Gamesight), ASO managers (store experiments).

### INFERRED
- The money in this angle sits with UA/marketing budgets (spend-based pricing) and with competitive-intelligence subscriptions; both buyers already pay for the outputs and work around manual collection.
- The reported subscription ranges give price anchors: roughly $6K-$20K per year for UA creative tools, $30K-$115K per year for market/game intelligence.
- No source shows anyone selling analysis of recorded real-player device video to a competitor-intelligence buyer; the Sensor Tower and GameRefinery acquisitions suggest those firms are the natural channel or competitor.

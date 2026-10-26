# Methods: churn, retention and onboarding (FTUE) analysis from gameplay video and behaviour

Angle: how studios diagnose churn and tutorial drop-off today, what event analytics cannot see, academic and industry churn prediction, computer vision on game UI, frustration/emotion detection, session replay for games, and the cost, privacy and sampling of "video telemetry".

Method note: 26 web searches were run (standard and extended). Direct page fetches (WebFetch/curl) were refused by this session's egress proxy for every host tried (amplitude.com, uxcam.com, embrace.io, arxiv.org, playtestcloud.com), so every VERIFIED bullet below comes from search-engine extracts of the cited page, not a full read. Numbers should be checked against the primary page before they are quoted externally.

---

## 1. How studios diagnose churn and FTUE drop-off today (event analytics)

### VERIFIED
- GameAnalytics funnels: "Standard" funnels take Design, Resource and Progression events; "Progression" funnels take Progression events only and add Complete/Start and Fail/Complete ratios. The docs recommend Progression events for "tutorial steps, level completion" and level funnels for spotting "where difficulty spikes may cause churn". https://docs.gameanalytics.com/features/funnels
- GameAnalytics funnel "Total Churn" = share of users who matched the first step but not all later steps, i.e. historical drop-off, not prediction. Funnels are "Any Order" (steps need not be chronological). https://docs.gameanalytics.com/features/funnels/interpret-results
- No GameAnalytics churn-prediction feature was found in search results; a Raft Labs page describes building a custom XGBoost churn model instead. https://www.raftlabs.com/industries/game-development/game-analytics-platform
- GameAnalytics FTUE advice: track every step of the tutorial and the FTUE metrics; separately suggests sending a design event with actual gameplay time to completion and splitting the tutorial into more milestones "to figure out what causes the drop-off". https://gameanalytics.com/blog/tips-for-a-great-first-time-user-experience-ftue-in-f2p-games , https://gameanalytics.com/?p=4612
- Unity Analytics funnels show "where drop offs happen" and Unity's own tutorial lists only candidate causes ("a bug that crashes the game, or the level is too hard"). Funnel Analyzer docs: unexpected drop-offs "indicate good places to investigate game play, user interface, or other issues". Steps must be completed in exact order or the user counts as lost; editing a funnel is blocked because it "would invalidate any existing data", so a new hypothesis means a new funnel. https://unity3d.com/learn/tutorials/topics/analytics/introduction-funnels , https://docs.unity.cn/2020.1/Documentation/Manual/UnityAnalyticsFunnels.html
- Roblox's creator docs frame onboarding as a step-by-step funnel whose output is D1 retention. https://create.roblox.com/docs/production/game-design/onboarding , https://create.roblox.com/docs/en-us/production/analytics/retention
- Playio: per-step drop-off beats overall completion ("70% completion" says less than "12% leave at step three"); key measures are drop-off per tutorial step and session-1 to session-2 conversion. https://blog.playio.co/mobile-game-onboarding-retention
- Amplitude case studies (vendor claims):
  - FunCraft (Wordgrams): funnel analysis showed new players wanted easier puzzles rather than tutorials; FTUE rebuilt; D1 retention +40% and lower CPA. https://amplitude.com/case-studies/funcraft
  - Electronic Arts: funnel analysis exposed onboarding friction, then **Session Replay** was used to review those interactions; added guidance and tooltips; 30% decrease in onboarding time (time, not retention). https://amplitude.com/case-studies/electronic-arts
  - Tilting Point: "highest churn rate occurs within the first 30 minutes of play"; funnel charts used to find which in-game screens cause churn. https://amplitude.com/case-studies/tilting-point-blog
- Firebase Predictions: default churn segment = users predicted to stop using the app in the next 7 days; GA in Nov 2018 with ">6 billion predictions per day". https://firebase.blog/posts/2017/11/announcing-firebase-predictions-beta , https://firebase.blog/posts/2018/11/predictions-graduates-to-general
- Halfbrick (Firebase case study, vendor material): gifted predicted churners in-game, +5 percentage points 7-day retention for that group. https://www.truemetrics.cn/download/Firebase_Halfbrick_Case_Study.pdf
- Critique of packaged churn prediction: dating app Surge found Firebase Predictions caught only 275 of 145k churn instances in its data. https://mobiledevmemo.com/why-dating-app-surge-swiped-left-on-firebase-predictions/
- Google Play Player Analytics (2016) shipped a churn prediction method for game developers. https://android-developers.googleblog.com/2016/01/new-features-to-better-understand.html
- Microsoft Game User Research's TRUE system (Kim, Gunn, Schuh, Phillips, Pagulayan, Wixon, CHI 2008, pp. 443-452, DOI 10.1145/1357054.1357126) is the canonical "instrumentation for complex systems" method from Halo-era Microsoft playtesting; later a book chapter "TRUE instrumentation: Tracking real-time user experience in games" (2012). https://www.springerprofessional.de/doi/10.1145/1357054.1357126 , https://cmps-people.ok.ubc.ca/bowenhui/game/readings/gameAnalyticsCh14.pdf

### Benchmarks the funnels are judged against (VERIFIED)
- GameAnalytics 2025 report (2024 data, 11,600 apps, classic retention): top-25% D1 about 26.5-27.7% at end of 2024, down from 28-29% in 2023; bottom quartile 10-11.5%. https://investgame.net/wp-content/uploads/2025/02/2025-GameAnalytics-Mobile-Gaming-Benchmarks.pdf
- GameAnalytics 2026 report (2025 data, 16,262 games with 1,000+ MAU): median D1 about 22%, P75 just above 30%, top 10% about 40%; median D7 just under 4%, P75 D7 6-7%. Note: "many top-performing studios store data in-house and never appear in public benchmarks". https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game , https://investgame.net/wp-content/uploads/2026/01/2026-01-27-2026-mobile-pc-benchmarks_compressed.pdf
- Widely repeated claim "80-90% of games are abandoned after first use, mainly due to bad FTUE" traces to a Develop:Brighton talk (Kristina Miles, Electric Square) with no shown data. https://adinmo.com/?p=20210 , https://www.pocketgamer.biz/news/77289/pgc-digital-how-to-enhance-the-first-time-user-experience/

### INFERRED
- Event funnels answer "where" and "how many"; every tool above leaves "why" to a hypothesis step (Unity's own docs say "investigate"). The EA case is the only vendor case found that explicitly pairs funnel with replay to get the "why".
- Funnel quality is bounded by instrumentation: a step that was never instrumented (e.g. "player looked at the shop button for 6 s and did not tap") does not exist in the data. Ordered-funnel rules (Unity) and any-order rules (GameAnalytics) produce different drop-off numbers for the same players.

---

## 2. What event analytics cannot see that video can

### VERIFIED
- Instruction screens are skipped: a GameDev.net playtesting post reports ">80%" of players clicked straight through the instruction screen of a demo (observed at live events, anecdotal). https://gamedev.net/articles/game-design/ux-for-games/7-ux-lessons-from-the-trenches-r4969/
- Eye-tracking study of 43 children aged 7-16: "perception patterns varied a lot and some players even missed relevant information during playing". https://www.csloh.com/research/wp-content/uploads/2009/08/AECT_2014.pdf
- Eye-tracking study of 64 players on subtitled vs spoken vs combined game instructions (Lan et al., J. Eye Movement Research 2025, DOI 10.3390/jemr18050044). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12452717/
- Eye tracking on a game HUD showed players only noticed on- and off-screen enemies after a redesign (UXPA magazine, Valsplat). https://oldmagazine.uxpa.org/?p=98
- PlaytestCloud / Nitro Games (Heroes of Warland): tested builds with no tutorial to see what players understand unaided, then designed the tutorial; tutorial completion rose to 90% and "big increases in our Day 1 Retention" (vendor case study, about four years old). https://blog.playtestcloud.com/nitro-games-case-study/
- PlaytestCloud / Kolibri Games: contextual tutorials prompting building upgrades; churn and negative reviews fell (no number in extract). https://start.playtestcloud.com/case-studies/kolibri-games
- PlaytestCloud site credits ZeptoLab with a 50% D1 retention improvement (underlying case study not found). https://www.playtestcloud.com/facts
- PlaytestCloud's AI video analysis flags moments where players *comment* on enjoyment, usability, design, monetization or frustration, then annotates and summarises; it keys on think-aloud speech, not on visible behaviour. https://start.playtestcloud.com/product-updates/faster-insights-with-ai-powered-analysis
- PlaytestCloud multi-session tests check whether players remember early tutorial elements in later sessions. https://start.playtestcloud.com/blog/multi-session-playtesting-at-playtestcloud
- Rage taps (UXCam definition): at least 3 taps within a set radius with at most 300 ms between taps; "unresponsive gestures" = taps/swipes with no app reaction (broken element or user tapping static content such as text). UXCam lets teams disable rage-tap tracking per screen where rapid tapping is intended. https://help.uxcam.com/en/articles/10222559-what-are-the-unresponsive-gestures , https://uxcam.com/blog/detect-hidden-user-frustrations/
- Telemetry-only struggle detection: "Signals of Struggle" (Ali and Thue, Carleton, AIIDE) used Random Forests on Terraria telemetry across three quests; struggle detected in the crafting quest, other quests "proved more difficult". https://ojs.aaai.org/index.php/AIIDE/article/view/36821
- Mouse hesitation as a difficulty signal: CogniMouse (CHI EA 2015), mouse streams plus skin conductance, preliminary study of 7 older adults. https://gnosis.library.ucy.ac.cy/handle/7/53635
- Commercial idle/hesitation detector for Unreal ("Universal Boredom Detector") tracks idle time and "shorter inactivity or low-action time before full idle". https://www.fab.com/listings/6441be98-1b4b-4ec5-8f9d-aeb980b9e80a
- Rage quit in telemetry: Sony patents define rage quitting as leaving a match early from frustration; disconnects scored 2 points vs menu exits 1 point toward a "bad sportsmanship" score. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9839838
- ASU / HyperX biometrics study predicted "tilt" about 15-20 minutes before it occurred. https://gamesbeat.com/study-examines-when-gamers-are-close-to-rage-quitting/

### INFERRED
- Signals that exist in screen video (plus touch overlay) but not in standard event streams: dwell/reading time on a tutorial card before dismiss; taps on non-interactive art; a visible CTA never tapped (UI not noticed); repeated failed gestures (mis-swipes); camera spinning/wandering (lost); pause/menu toggling; time-to-first-meaningful-action; the exact screen state at the moment of app kill (rage quit vs. interruption).
- Most of these can in principle be instrumented as events, but only if anticipated; video captures them retroactively for any screen, which is the practical difference.
- Playtest video (PlaytestCloud et al.) gives the "why" but from recruited testers with think-aloud, small n; in-the-wild device video would give large n without think-aloud, so the "why" must be inferred from behaviour alone.

---

## 3. Academic and industry work on predicting churn from play behaviour

### VERIFIED
- Hadiji, Sifa, Drachen, Thurau, Kersting, Bauckhage, "Predicting player churn in the wild", IEEE CIG 2014: features such as playtime, session length and session intervals across five F2P games; "high accuracy churn prediction". https://publica.fraunhofer.de/handle/publica/387889 , https://www.dfki.de/web/forschung/projekte-publikationen/publikation/14228
- Drachen, Sifa et al., "Rapid Prediction of Player Retention in Free-to-Play Mobile Games" (AIIDE 2016): F2P games lose a majority of players within the first few days; proposes simple heuristics on early activity only. https://arxiv.org/pdf/1607.03202
- Roohi et al., "Predicting Game Difficulty and Churn Without Players" (CHI PLAY 2020, Aalto + Rovio): DRL agents play 168 levels of Angry Birds Dream Blast; a population model (skill, persistence, boredom) predicts per-level churn (churn = no play for 7 days). Real pass rate vs churn: Spearman r = -0.144; vs "churn without completing the level": r = -0.586. https://arxiv.org/pdf/2008.12937 , https://aaltodoc.aalto.fi/items/b0db38e3-90ef-4d01-ac5a-2c8d401d448f
- Follow-up "Predicting Game Engagement and Difficulty Using AI Players" adds MCTS to DRL and improves prediction. https://arxiv.org/pdf/2107.12061
- Sequential + aggregate features with several neural architectures for churn (IEEE CoG 2019, DOI 10.1109/CIG.2019.8848106): combining the two beat either alone. https://arxiv.org/abs/2209.03184v1
- Periáñez et al. (Silicon Studio, 2017): survival ensembles for churn in mobile social games beat Cox regression on accuracy and robustness; Bertens et al. scalable multi-dimensional survival model. https://ar5iv.arxiv.org/html/1710.02264 , https://arxiv.org/pdf/1710.02262
- NCSOFT game data mining competition (IEEE CIG 2017): commercial logs released; 13 submissions in churn track, 5 in survival track; winners used deep learning, tree boosting, linear regression. https://www.arxiv.org/pdf/1802.02301 , https://arxiv.org/pdf/1901.05147
- Kim et al., PLOS ONE 2017: 3 casual games, 193,443 players, 10,874,958 log records; CNN and LSTM performed "about same or slightly worse" than traditional ML on play logs. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0180735
- Jang, Kim, Yu (arXiv 2104.05554): churn accounting for each user's usage period. https://arxiv.org/pdf/2104.05554
- Loria et al. (FBK, 2019): general-purpose in-game behaviours for churn in gameful systems; how much history to use. https://cris.fbk.eu/handle/11582/319866
- Sifa et al. (Fraunhofer IAIS): Echo State Networks for sequential player behaviour, churn case study. https://publica.fraunhofer.de/handle/publica/413360
- Social-graph churn: multiplex social influence via network embedding for online game churn. https://pmc.ncbi.nlm.nih.gov/articles/PMC13492773/
- Supervised churn for a F2P mobile game from event logs (Applied Sciences 2022). https://www.mdpi.com/2076-3417/12/6/2795
- No paper was found that predicts churn or engagement directly from human gameplay video frames (extended search). The closest is Roohi et al., where agents (not humans) see screen pixels. https://ar5iv.labs.arxiv.org/html/2008.12937

### INFERRED
- The academic churn literature is almost entirely log-based (sessions, progression, spend, social). Deep sequence models on logs give small or no gains over boosted trees (PLOS ONE 2017, NCSOFT competition), so the predictive ceiling is set by feature content, not model class. Video is an untested source of new features, which is a research gap rather than a proven lift.
- The Rovio result (r = -0.586 only for "quit without completing") suggests churn is tied to specific failure moments; those moments are exactly what a short video clip around the last failure would show.

---

## 4. Computer vision on game UI (HUD, state, OCR, menus, deaths, transitions)

### VERIFIED
- Q3Vision (ACSW 2026, UTS): reconstructs Quake III game state from screen video only; YOLO for enemies/items plus OCR for health, armour, ammo and weapon; OCR limited by low-resolution, stylised HUD fonts and visual noise. https://opus.lib.uts.edu.au/handle/10453/197175
- ICCS 2020: cascade classifiers detect HUD, then OCR reads and interprets its text; fast enough for real-time use during play, not only on recordings. https://pmc.ncbi.nlm.nih.gov/articles/PMC7302570
- NVIDIA patents "Game event recognition": game-agnostic detector configured per game; event data from OCR and other detectors; regions upscaled and binarised (background thresholding) before OCR. https://patents.justia.com/patent/12288404 , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11154773 , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11673061
- NetEase WDTEST (ICSE SEIP 2023): "largest GUI dataset for mobile games"; widget-detection testing from screenshots only; about 3x the unique-UI coverage of Monkey. https://ink.library.smu.edu.sg/soss_research/3808
- YOLOv5-ABLN (BJUT 2023): 2,400-image dataset of clickable mobile-game elements; tested on 298 UI screens from 6 popular games; mAP 91.9% vs 90.2% for base YOLOv5. https://ir.bjut.edu.cn/item/389803
- IEEE DataPort: annotated GUI elements from 12 shooter games (Faster R-CNN). https://ieee-dataport.org/documents/guigraphical-user-interface-elements-video-games-shooter-games
- GUIPilot (arXiv 2506.07385): YOLOv8 widget detector on 1,392 app screens (not game-specific). https://arxiv.org/pdf/2506.07385
- NiceShot AI (open source): YOLOv8n + OpenCV + FFmpeg detects kill, death and medal pop-ups in Call of Duty: Black Ops 6 and clips them; supports bulk Twitch channel analysis. https://letsdatascience.com/news/niceshot-ai-detects-key-gameplay-events-b6e93d44
- Ringer and Nicolaou, FDG 2018: unsupervised multi-view highlight detection on PUBG streams using game footage plus streamer face and speech; notes most game highlight systems are triggered by hard-coded events (score change, end-game). https://arxiv.org/pdf/1807.09715 , https://etheses.whiterose.ac.uk/32406
- VideoGameBunny (WACV 2025, Univ. of Alberta): game-specific VLM trained on 389,565 image-instruction pairs; beats much larger models on game understanding with 4.2x fewer parameters. https://www.catalyzex.com/author/Cor-Paul%20Bezemer
- VideoGameQA-Bench (NeurIPS 2025 D&B): visual unit/regression tests, needle-in-a-haystack, glitch detection, bug report generation on game images and videos. https://asgaard.ece.ualberta.ca/publications/?tgid=53
- 2026 study of off-the-shelf VLMs on 19,738 keyframes from 41 hours of QA gameplay: already detect "a certain range" of visual bugs; hybrid approaches likely needed. Temporal glitches (multi-frame) are "substantially harder" for VLMs than spatial ones. https://arxiv.org/html/2603.22706v1
- Human-AI collaborative game testing with VLMs: VLMs "may still struggle with unpredictable player behavior and nuanced gameplay scenarios". https://arxiv.org/pdf/2501.11782
- Cradle (BAAI, ICML 2025): screenshot-in, keyboard/mouse-out agent completed 40-minute real missions in Red Dead Redemption 2, showing general screen understanding of AAA UI. https://proceedings.mlr.press/v267/tan25h.html , https://github.com/BAAI-Agents/Cradle

### INFERRED
- Mature, cheap pieces: menu/screen classification, button/popup detection (mAP ~90% on mobile games), death/kill pop-up detection, HUD OCR where fonts are clean. Weak pieces: stylised low-res HUD OCR, temporal events, and cross-game generality without per-game config (NVIDIA's patents assume per-game configuration).
- For FTUE analysis the needed vision vocabulary is small per game (tutorial card visible, CTA highlighted, popup open, fail screen, level-complete screen, store screen), so a per-title detector trained on a few hundred labelled frames is plausibly enough; general VLMs could label first and bootstrap it.

---

## 5. Frustration and emotion detection (gameplay pixels, face cam, voice)

### VERIFIED
- Makantasis, Liapis, Yannakakis (ACII 2019, "From pixels to affect"): arousal predicted from gameplay video alone, over 78% accuracy on average and 98% at best (leave-one-video-out). https://antoniosliapis.com/papers/from_pixels_to_affect_a_study_on_games_and_player_experience.pdf
- AGAIN dataset (Melhart, Liapis, Yannakakis): over 1,100 in-game videos with gameplay data from 9 games, continuously annotated for arousal by 124 participants. https://arxiv.org/abs/2104.02643v1
- Privileged information (Makantasis et al. 2021): train with heart rate, EDA and telemetry in the lab, test on pixels only; pixel-only models perform "equally well" as all-modality models. Journal version runner-up Best Paper 2024, IEEE Trans. Affective Computing. https://www.arxiv.org/pdf/2107.10552 , https://game.edu.mt/blog/research-in-maching-learning-awarded-at-ieee-transactions-on-affective-computing/
- Privileged contrastive pretraining on AGAIN-Platformers (120 participants) (arXiv 2508.03729). https://arxiv.org/pdf/2508.03729
- Theory-of-mind study, 20 players, 53 gameplay + facial features: gameplay-feature models were "significantly" more accurate than facial-feature models for perceived frustration. https://arxiv.org/pdf/2001.08656
- MGFD (Multimodal Game Frustration Database), audiovisual Wizard-of-Oz corpus of verbal and facial frustration in game interaction; paper focuses on speech. https://doaj.org/article/0089d76cc7bd474ca8ff9427a7ca1e02
- Deep audio + video descriptors fused to detect frustration in gameplay (Multimedia Tools and Applications 2022). https://link.springer.com/article/10.1007/s11042-022-13762-7
- Facial emotion recognition in VR games with HMD occluding upper face, CNN on modified FER2013 (IEEE CoG 2023). https://arxiv.org/abs/2312.06925v1
- Facial expressions vs game experience: challenge correlated positively with anger and joy. https://opus.lib.uts.edu.au/bitstream/10453/42000/1/facialgeq.pdf
- Affdex (Affectiva) facial expressions + logistic regression predicted flow, frustration and boredom in an educational game. https://experts.nau.edu/en/publications/predicting-real-time-affective-states-by-modeling-facial-emotions/
- Affectiva pitched webcam/phone-camera emotion capture for mobile playtests to locate frustration (vendor tutorial). https://blog.affectiva.com/tutorial-get-emotion-data-from-your-next-mobile-playtest
- USP doctoral thesis (2017): assessing fun from low-cost webcam facial analysis. https://www.teses.usp.br/teses/disponiveis/45/45134/tde-05072017-212226/en.php

### INFERRED
- Two research results matter for a device-video product: (a) affect can be read from gameplay pixels alone with useful accuracy, so a face cam is not required; (b) where compared, gameplay features beat facial features for frustration. Face cam adds consent and biometric-law cost (section 7) for unclear lift.

---

## 6. Session replay and heatmaps for games

### VERIFIED
- UXCam replay mechanism: SDK captures timed screenshots encoded into video in the background, "smaller data sizes than continuous video"; iOS default is a schematic (wireframe-like rectangles and text) replay; real screen video needs explicit opt-in (`optIntoVideoRecordings`) and occlusion of sensitive data. Upload happens when the app goes to background. A UXCam FAQ table lists approx. 200-800 KB (iOS) and 250 KB-1.2 MB (Android); unit not visible in the extract. https://developer.uxcam.com/docs/how-session-recording-works , https://help.uxcam.com/en/articles/10426267-sdk-integration-faqs , https://help.uxcam.com/en/articles/10222760-schematic-replay
- UXCam claims Smartlook has been discontinued (vendor claim). https://uxcam.com/smartlook/
- G2: Smartlook session replay 8.5/10 (253 reviews), UXCam 8.2/10 (49 reviews). https://www.g2.com/compare/fullstory-vs-uxcam-vs-smartlook
- PostHog lists Unity replay only as "alpha" for its own product; no Unity-specific case study found for UXCam or Smartlook. https://posthog.com/compare/best-mobile-app-session-replay-tools
- Sentry mobile replay sampling: `sessionSampleRate` (e.g. 0.1 in production) records whole sessions; `onErrorSampleRate` (recommended 1.0) buffers and uploads only if an error occurs, keeping about the last minute before the error; iOS session ends after 30 s in background or 60 min max. https://docs.sentry.io/platforms/android/session-replay , https://docs.sentry.io/platforms/apple/guides/ios/session-replay/ , https://docs.sentry.io/platforms/dart/guides/flutter/session-replay/
- Steam Game Recording: "record in background" ring buffer with a user disk cap, older footage overwritten, saved clips kept; users report the cap applies per game, inflating disk use; one user: 60 min at 24 Mb/s = about 10.8 GB. https://help.steampowered.com/faqs/view/23B7-49AD-4A28-9590 , https://steamcommunity.com/groups/SteamClientBeta/discussions/5/4416424806088831316 , https://lemmy.imagisphe.re/post/734949
- Medal / General Intuition: about 2 billion clips/year from 10M+ MAU; value lies in clips paired with recorded inputs (which button, when); OpenAI reportedly offered about $500M for Medal in late 2024; General Intuition seed $133.7M (Oct 2025), later $320M at $2.3B (total $454M disclosed). https://techcrunch.com/2025/10/16/general-intuition-lands-134m-seed-to-teach-agents-spatial-reasoning-using-video-game-clips/ , https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/
- Patent "Gameplay telemetry and video acquisition system" exists (synchronised capture). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11000771

### INFERRED
- Web/app session replay works by serialising UI trees; game engines render to one GPU surface, so app replay tools either fall back to screenshots or show nothing useful for a game scene. That is why Unity support is "alpha" or absent in mainstream replay vendors.
- Error-triggered ring-buffer capture (Sentry) and background ring buffers (Steam, Medal) are the established sampling patterns; the same pattern keyed on churn-relevant triggers (tutorial step abandon, app kill on fail screen, N fails in a row, first session end) is the obvious adaptation.
- Medal shows synchronised input + video is worth more than video alone; for churn analysis, a touch/input overlay is likewise what turns "watching" into measurable hesitation and mis-taps.

---

## 7. Cost, bandwidth, storage, privacy and sampling of "video telemetry"

### VERIFIED
- 720p H.264 game capture: 5-10 Mbps = 2.3-4.6 GB/hour (Elgato). https://help.elgato.com/hc/en-us/articles/360028231591-Capture-settings-and-Elgato-Game-Capture-HD
- 720p screen clip H.264 30 fps at 4-8 Mbps (calculator table); 8 Mbps = about 1 MB/s, 60 MB/min; H.265/AV1 reach similar quality at lower bitrate. https://west-games.com/recording-file-size-calculator/ , https://clip.dor.gg/en/blog/game-recording-bitrate-guide
- AWS (secondary sources): S3 Standard $0.023/GB-month first 50 TB (us-east-1); S3 egress $0.09/GB first 10 TB after 100 GB free; CloudFront from $0.085/GB. https://upstash.com/blog/aws-s3-pricing-explained-2026 , https://perfsys.com/blog/cloudfront-pricing-guide/
- Apple, Feb 2019: told developers to remove or disclose screen-recording analytics (Glassbox) after TechCrunch found Expedia, Hollister, Hotels.com etc. recording taps/swipes without consent; App Store guidelines require "explicit user consent and ... a clear visual indication when recording, logging, or otherwise making a record of user activity"; one developer given less than a day to comply. https://techcrunch.com/2019/02/07/apple-glassbox-apps , https://www.engadget.com/2019-02-07-apple-crack-down-apps-record-screen.html
- Embrace documents its video recording against Apple's policy (page exists; content not retrievable here). https://embrace.io/docs/product/video-recording-and-apples-policy
- UXCam: real-screen video requires opt-in and occlusion; recordings private by default so passwords/card data are not captured. https://developer.uxcam.com/docs/how-session-recording-works , https://www.crazyegg.com/blog/?p=108080
- EU AI Act Art. 5(1)(f) bans emotion recognition in workplace and education; elsewhere it is permitted but deployers must inform subjects (Art. 50(3)); GDPR biometric rules apply to many emotion-recognition systems. https://fpf.org/blog/red-lines-under-eu- , https://secureprivacy.ai/blog/gdpr-compliant-emotion-recognition
- PlaytestCloud pricing (page about four years old): Professional Basic about €1,025-1,130/month with 120 "Video Tokens"/year; Advanced about €2,240-2,825/month with 240 tokens; Enterprise custom; longitudinal tests have a set-up fee of 8.7 Video Tokens plus per-player-session charges. https://www.playtestcloud.com/pricing , https://start.playtestcloud.com/blog/longitudinal-playtesting-at-playtestcloud

### INFERRED (arithmetic on the figures above)
- Mobile 720p at 2 Mbps is about 0.9 GB/hour; at 4 Mbps about 1.8 GB/hour. At 1.8 GB/hour and $0.023/GB-month, one stored player-hour costs about $0.04/month in S3; storage is cheap, upload is the constraint.
- Full capture is unrealistic on mobile: a 30-minute first session at 2 Mbps is about 450 MB of upload from the player's device, on top of the game download, and must wait for Wi-Fi. A studio at 100k new installs/day recording only the first 10 minutes at 1 Mbps would ingest about 7.5 TB/day.
- Practical sampling knobs, from the patterns above: (a) record only FTUE / first N minutes; (b) a 30-120 s on-device ring buffer uploaded only on trigger (tutorial abandon, app kill on fail screen, rage taps, repeated fails), as Sentry does for errors; (c) low fps (1-5 fps screenshots, as UXCam does) or 360-480p, since UI-state recognition does not need 30 fps 720p; (d) user-level sampling (e.g. 1-5% of new installs) with Wi-Fi-only upload; (e) on-device CV that uploads only extracted events/labels plus a few keyframes.
- Privacy hazards specific to game video: player names and chat in HUD/social panels, notifications overlaying the screen, payment sheets; Apple's 2019 action means consent + visible indicator is the floor on iOS. Face cam adds biometric/emotion-recognition obligations in the EU.

---

## Signals of willingness to pay

### VERIFIED
- Studios pay for qualitative playtest video: PlaytestCloud at about €1,000-2,800/month list (plus enterprise) with credited outcomes such as Nitro Games' 90% tutorial completion and ZeptoLab's claimed +50% D1. https://www.playtestcloud.com/pricing , https://blog.playtestcloud.com/nitro-games-case-study/ , https://www.playtestcloud.com/facts
- PlaytestCloud invested in AI summarisation of playtest video (frustration, usability, monetization moments), i.e. buyers want less manual video watching. https://start.playtestcloud.com/product-updates/faster-insights-with-ai-powered-analysis
- Analytics vendors sell FTUE/onboarding outcomes to game studios with headline numbers: FunCraft +40% D1, EA 30% faster onboarding (funnel + session replay), Tilting Point first-30-minutes churn. https://amplitude.com/case-studies/funcraft , https://amplitude.com/case-studies/electronic-arts , https://amplitude.com/case-studies/tilting-point-blog
- Google/Firebase marketed churn prediction to games (Halfbrick +5 pp D7 on targeted churners); a customer complaint shows recall can be very low (275 of 145k). https://www.truemetrics.cn/download/Firebase_Halfbrick_Case_Study.pdf , https://mobiledevmemo.com/why-dating-app-surge-swiped-left-on-firebase-predictions/
- Big studios build in-house: NCSOFT released logs for a public churn competition; NetEase built the largest mobile-game GUI dataset for screenshot-based testing; Rovio co-authored per-level churn simulation; Microsoft built TRUE. https://www.arxiv.org/pdf/1802.02301 , https://ink.library.smu.edu.sg/soss_research/3808 , https://arxiv.org/pdf/2008.12937
- Gameplay video with synchronised inputs commands large prices in the AI-training market (Medal: reported ~$500M OpenAI offer; General Intuition $2.3B valuation). https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/
- Complaints/gaps: funnels show where not why (Unity docs); Unity funnels cannot be edited without invalidating data; mainstream replay tools lack proper Unity/game support (PostHog Unity "alpha"); Steam users complain about per-game recording storage; public benchmarks miss top studios who keep data in-house. https://docs.unity.cn/2020.1/Documentation/Manual/UnityAnalyticsFunnels.html , https://posthog.com/compare/best-mobile-app-session-replay-tools , https://steamcommunity.com/groups/SteamClientBeta/discussions/5/4416424806088831316 , https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game

### INFERRED
- The buyer already paying is the UX research / game-design team (playtest video) and the product/analytics team (funnels, replay). The unmet need visible in these sources is joining the two at scale: "why" evidence for the specific funnel step where real (not recruited) players drop.
- Regulatory and platform friction (Apple consent rule, EU emotion-recognition rules) pushes any device-video product toward opt-in cohorts, beta/early-access builds, or on-device extraction, and away from face cam.

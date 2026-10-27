# JEV model pipeline (as described by the product owner, 2026-10-27)

## What exists today
1. A player's gameplay session is captured as video. A session can be n hours; each video is capped at 15 minutes, so one session is many videos.
2. Each video is converted to a transcript. The owner's view: the transcript alone is not enough; what is on screen is largely lost.
3. The transcript is run through a fixed set of questions with options, written per game target. The targets are mostly detecting churn in the tutorial and just after it. The answers form a structured table per video.
4. A chatbot for the gaming studio answers the studio's questions from that table, so that a question over, say, 500 players is fast. Reading 500 transcripts per question was too slow and too much data, which is why the fixed-question table exists.

## Constraints
- Buyers are gaming studios. Their questions are not known in advance.
- Ingestion time and cost are not a concern. Answering a studio's question must be fast.
- The owner wants to improve (a) how the chatbot answers from the question-answer store and (b) the framework for generating the questions so that any type of question can be answered.

## Known problems named by the owner
- The question set is small, so most of what is in the video and transcript is never captured.
- Transcript loses visual information.
- Long multi-video sessions.

## Unspecified
- What a transcript contains (speech only, on-screen text, events), whether game telemetry is joined, who at the studio asks and what they ask, current question count and answer types, latency and cost limits per query, languages, how videos of one session are linked.

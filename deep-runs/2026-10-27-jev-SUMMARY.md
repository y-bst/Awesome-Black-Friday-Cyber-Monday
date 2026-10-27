# JEV: what to fix and what to build (two deep runs, 2026-10-27)

Two engine runs, both full mode:

| Run | Question | Result file |
|---|---|---|
| Gaps | What is wrong or missing in the current pipeline (video, transcript, fixed multiple-choice questions, answers table, chatbot)? | `2026-10-27-jev-pipeline-gaps/leaves.md` (633 gaps) |
| Ideate | How should storage, querying and question generation work so any studio question is answered correctly and fast? | `2026-10-27-jev-architecture/options.md` (904 options, 80 refusals) |

Both tables are ranked by the median of three independent scorings. The top 25 of each went through a proposer, a skeptic and two independent judges. The judges agreed on 19 of 25 (gaps) and 20 of 25 (ideate).

## 1. Fix now in the current chatbot and answers table

Both judges said keep for these seven. They are cheap and they stop confident wrong answers.

| id | Gap | Fix |
|---|---|---|
| chat-3 | A studio question with no matching fixed question is silently answered with the nearest question. | Print which stored question answered it; say "not captured" when none matches. |
| chat-1 | Cohort counts run over per-video rows, so one player counts once per video. | Count distinct players; every count joins a session or player table. |
| stitch-9 | No rule for combining contradictory per-video answers into one session answer. | Declare a reducer per question (first, last, any, all, latest). |
| extract-1 | Per-video "why did they leave" has no "not observed in this video" option, so videos with no tutorial get invented reasons. | Add reserved options: not observed, not applicable, cannot tell from audio. |
| speech-1 | A silent player's empty transcript is extracted and stored as real "No" answers. | Store NULL with a reason when speech coverage is below a threshold. |
| fillB-12 | "Not processed", "not observed" and "not applicable" are undocumented codes, so generated SQL counts them wrong. | Ship a data dictionary and a default denominator filter to the planner. |
| privacy-1 | A deletion request removes video and transcript but not the answer rows, caches or logs built from them. | Write the deletion cascade. |

Split between keep and defer: show the definition used in every answer (fillB-1, fillB-2), a stored "missing vs No" status per answer (ds-1), and a small hand-labelled gold set per game (eval-1).

## 2. How the chatbot should answer from the store

Both judges said build for these six. Together they replace "chatbot reads a table" with "planner writes a typed plan, executor runs it on session-grain tables".

1. **Session manifest at ingestion (stitch-1).** One row per video with session id, order, real duration and a session clock. Every session count, duration and cross-video answer depends on it. Folded in: obs-29, stitch-2, tar-12.
2. **Typed answer contract per question (qgen-1).** Answer type, scope (video, step, session, player), reducer, a "not observable" null, and the evidence required. Folded in: stitch-7, and in one judge's view stat-7.
3. **Typed query plan (planner-1).** The planner emits a plan with route, fields, filters, cohort and evidence form; the executor runs the plan, not free text. Routes, fields and denominators become auditable. Folded in: planner-23.
4. **Per-player step rows (latency-15).** One row per player per tutorial step with entered, left, dwell, stalls and a seen / not seen / unknown status. Funnels, stalls and denominators become one query. Folded in: extract-7, extract-28, qgen-10.
5. **Session roll-up pass (stitch-27).** One model call per session reads the stitched observations and writes quit reason, churn step and evidence links. Folded in: analyst-15, clinical-16, extract-3.
6. **On-screen text track (cv-3).** OCR on keyframes with the screen region (HUD, objective, dialog, tooltip, error popup). This is the cheapest fix for "transcript loses what is on screen". One judge wants the keyframe sampler (cv-1) built with it.

Every answer should carry numerator, denominator, coverage, an interval when n is small, and up to three timestamped quotes (askdata-1, stat-2, planner-22, eval-7).

Defer: a columnar store (latency-16) until measured latency says so, and a precomputed answer bank (latency-12) until a real query log exists.

## 3. How questions should be generated so unknown questions get answered

The runs point to a loop, not a fixed list:

1. **Start from typed contracts, not free questions (qgen-1, clinical-12).** Each field has a definition, allowed values, positive and negative examples, and a "not observable" value.
2. **Test coverage against real questions (eval-13).** Collect about 30 real questions per studio at onboarding and measure what share the bank answers before go-live.
3. **Turn unanswered questions into fields (planner-12, extract-11).** When the planner cannot answer, it drafts a field spec, the studio approves it, and a one-time backfill runs over all stored sessions. These scored highest on impact; they rank lower only because the first answer takes minutes.
4. **Promote repeated slow questions automatically (latency-18, obs-32, qgen-5, retr-22).** Questions that hit the slow path several times become permanent fields.
5. **Let studios define trackers (analyst-22).** A studio types a question once, marks it "track", and it is extracted for every past and future session.

Contested between personas: ontology-generated versus hand-written versus studio-written questions; whether genre-shared question banks can be used on a new game without validation; whether to answer at query time by running a model over raw transcripts. The judges kept raw-transcript reads for single-player questions only.

## 4. The tutorial bias, and what covers the rest of a multi-hour session

The audit found that 86% of options used a tutorial example, and every fast structure was keyed by tutorial step. A question about hour 2 or 3 always falls to the slow path. A targeted fill added 69 options for the rest of play. The most useful are a unit-of-play table (level, match, run, quest, boss attempt) with precomputed aggregates, a per-player per-hour table, and a planner step that maps "boss", "match" or "run" to unit rows (playfill-10). The judges deferred these because the stated target is tutorial churn. If studios ask about mid-game play, this is the next build after section 2.

## Engine behaviour on this run

- The audit-driven fill produced 6 of the gaps top 25.
- Scoring was consistent: 9 of 2,404 gaps field scores differed by 3 or more across scorers.
- Both runs took the critique stage's added perspectives seriously: observability builders, call-centre analytics, e-discovery, clinical data abstraction and the studio data team who would say no all contributed options that reached the top 25.

# Stage A0: Intake questions (before framing)

Read the topic and every artifact. Then list the questions whose answers would **add or remove an axis, a value range, or a perspective** in the grid. Nothing else qualifies as a question.

Rules:
- At most 8 questions. Fewer is better.
- Each question names what it changes: "decides whether <X> is an axis", "sets the range of <axis>", "adds/removes the <perspective> perspective".
- Do not ask anything the artifacts already answer. Quote the artifact when tempted.
- Do not ask about priorities, preferences or scope. Those are decided in Stage L, after the list exists.
- For every question, state the assumption you will use if it goes unanswered.
- Typical sources of grid-changing questions: cardinality limits (how many items, how big), where inputs come from (library vs upload vs both), granularity of outputs (one per batch vs one per item), lifecycle states of each entity, whether an interaction is one-shot or a thread, visibility scope (per user vs shared), actors and roles, what "done" and "failed" look like to the user, dependencies on other pages or jobs (ingestion, processing).

Write `A0-questions.md` to the run directory in this form:

```
1. <question>  — changes: <axis / value range / perspective>. Assumption if unanswered: <...>
```

Then STOP and put the questions to the user, unless the arguments include `--no-questions` or the user has already said to run without questions. In that case proceed on the stated assumptions and record them in `A-frame.yaml` under `assumptions:`. When the user answers, fold the answers into the artifact (append a "Clarifications" section to a copy of the spec in the run directory; never edit the user's original file) and continue to Stage A.

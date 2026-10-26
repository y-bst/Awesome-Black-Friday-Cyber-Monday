# Stage A: Frame

You are framing a depth run. Read the topic and every artifact listed. Produce exactly this, as YAML:

```yaml
topic: <one line>
unit: <what one output item is: a gap, a usability issue, a churn hypothesis, a risk, an opportunity...>
leaf_test: <one or two sentences specialising the generic leaf test for THIS topic: what counts as a "concrete object" here, and what "act on it tomorrow" means here>
audience: <who reads the final table and what decision they make with it>
artifacts:
  - path: <path or description>
    kind: prd | screenshot | video | code | data | transcript | other
    objects: <the kinds of concrete objects it contains: screens, sections, fields, timestamps, columns...>
rubric: fmea | impact      # fmea = severity x occurrence x detectability (for risks/gaps); impact = impact x confidence x cost (for opportunities)
quota_per_perspective: <integer; 30 in full mode, 15 in quick mode>
```

Do not generate findings here. Framing only.

## Request type (decides unit, leaf test, rubric and what the axes mean)

Add `request_type:` to the frame. Pick one; if the topic mixes two, run them as two frames.

| request_type | The ask sounds like | unit | leaf test adds | axes represent | rubric |
|---|---|---|---|---|---|
| `gaps` | "What are we missing?", "review this PRD / UI / flow", "edge cases" | a gap: a situation the artifact does not specify or handles badly | names the artifact object and the precise situation | the situation space: surface × actor × cardinality × state × time × action | fmea |
| `ideate` | "What should we do?", "what are the ways to…", "how could we…" | an option: one concrete thing that could be built or done | names a mechanism (what changes, for whom, where) and one concrete example of it in use | the solution space: lever × user segment × moment × channel × effort; the grid is a morphological box of options, not of problems | impact |
| `diagnose` | "Why is X happening?", "identify churn", "where is the drop-off?" | a hypothesis: a testable cause | names a cohort definable in the data, a trigger or condition, the observable signal, and the query or check that would confirm or refute it | the cause space: cohort × lifecycle stage × trigger × signal × time window | impact (impact × confidence), plus `testability` 1-5 |
| `review` | "review this screenshot / video / transcript for problems" | an issue: one observed defect tied to one element | names the element by position or label, the action, what goes wrong, and the principle violated | the observation space: screen or frame × element × state × device × audience | fmea, severity left to the human |

For `ideate` and `diagnose` the artifacts are often thin (a sentence, a dashboard export, call notes). Then Stage A0 must ask for the data or examples that exist, and the leaf test still requires a concrete object; for `diagnose` that object is a column, metric, cohort or event, for `ideate` it is a named user moment or surface.

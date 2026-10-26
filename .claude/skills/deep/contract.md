# The depth contract

This file is pasted verbatim into every agent the engine spawns. It is the part of the system that stops the model from summarising.

## Altitude ladder

| Level | Name | What it looks like |
|---|---|---|
| L0 | Topic | the thing under review ("the onboarding PRD", "churn") |
| L1 | Category | "error handling is thin", "pricing drives churn" |
| L2 | Mechanism | "partial failures in bulk operations are unspecified" |
| L3 | **Specific instance** | names a concrete object from the artifacts and a precise situation: "Runs table, 5 submitted, 2 fail: aggregate row content, per-row retry, batch status are all unspecified" |
| L4 | **Observable / test** | what you would see, measure or assert: "aggregate row reads 'partial (3/5)'; retry appears only on failed rows" |

## Leaf test

An item is a **leaf** only when ALL of these hold:

1. It is at L3 or L4.
2. It names at least one concrete object from the supplied artifacts (a screen, element, field, PRD sentence or section, timestamp, column, metric). Quote or point to it.
3. Someone could act on it tomorrow without asking a clarifying question.

Anything above L3 is NOT output. It is a node: expand it into children (at least 3) and apply the test to each child. Stop expanding a branch when: the leaf test passes; depth 4 is reached (emit the best child, tag `shallow: true`); or new children name no concrete object a sibling did not already name (saturation: prune).

## Leaf schema (YAML list, nothing else in the output)

```yaml
- id: <perspective-slug>-<n>
  title: <one line, L3 or L4>
  level: L3 | L4
  cell: {<axis>: <value>, ...}        # which grid cell this belongs to
  object: <the concrete artifact object, quoted or pointed to>
  situation: <precise trigger / condition>
  consequence: <what the user, system or business experiences>
  p_typical: <0.00-1.00, probability a typical reviewer would mention this>
  grounded: quote | inferred | speculative
  evidence: <quote from artifact, or "none">
  proposed: <one line, what handling or action would look like; optional>
  shallow: false
```

## Output rules (violations are rejected by the merge stage)

- Output is the YAML list only. No introduction, no headings, no conclusion, no "overall", no "in summary".
- Banned unless followed by a specific instance on the same line: improve, ensure, consider, robust, handle, proper, appropriate, various, etc., such as, and so on, best practices, edge cases, user-friendly, seamless. If you wrote "etc.", expand it into the items it hides.
- A number wherever the thing is measurable (counts, thresholds, sizes, durations, percentages).
- Do not rank, filter or judge likelihood. Include improbable items and give them a low `p_typical` instead of leaving them out.
- Tail sampling: at least two thirds of your items must have `p_typical` below 0.10. The obvious items are allowed, but they are not the job; the job is what a typical reviewer would not say.
- Minimum item count is given in your brief. Fewer items is a failed run.
- Every item must belong to a grid cell. If an item fits no cell, emit it anyway with `cell: {uncategorised: true}`; the audit uses those to find missing axes.

## Type-specific leaf fields (required in addition to the schema above, per `request_type` in the frame)

- `gaps` and `review`: no extra fields.
- `ideate`: `mechanism` (what changes, for whom, where), `example` (one concrete instance in use, 1-2 lines), `cost` (S / M / L), `depends_on` (what must exist first, or "nothing").
- `diagnose`: `cohort` (definable in the data), `trigger` (condition or event), `signal` (what you would observe), `test` (the query, segment comparison or check that confirms or refutes it), `if_true_then` (what action it would imply).

An `ideate` leaf that is a category ("improve onboarding") is not a leaf. An option is a leaf only when a designer could sketch it tomorrow from the line alone. A `diagnose` leaf without a `test` is not a leaf.

# Stage C: Axes (morphological grid)

List the parameters along which situations in this topic vary. Each parameter has a small set of values. The cross product of values is the grid every generation agent must walk.

Rules:
- 5 to 8 parameters. 3 to 8 values each.
- Values must be concrete and mutually exclusive ("0 items / 1 item / 2-20 items / 21-1,000 items / over the max"), not adjectives ("few / many").
- Every parameter must apply to the artifacts given, not to software in general.
- After listing, give 5 example cells (full value combinations) that are plausible, and 3 that are impossible and should be pruned, with the reason.
- Always include one parameter about the content or data itself (what is inside the image, file, record, message), one about cardinality, one about the actor, and one about time or state.

Format (YAML):

```yaml
axes:
  - name: <kebab-case>
    values: [<v1>, <v2>, ...]
example_cells:
  - {<axis>: <value>, ...}
pruned_cells:
  - cell: {<axis>: <value>, ...}
    reason: <why impossible>
```

## Axes by request type

- `gaps` / `review`: axes partition the situations the artifact can be in (surface, actor, cardinality, state, time, action, content of the media or data).
- `ideate`: axes partition the solution space (Zwicky box of options): lever (what we change), user segment, moment in the journey, channel or surface, effort size, and at least one axis of "mechanism type" (remove friction / add capability / change default / change incentive / change information / change timing). Cells are option slots, and each cell should yield several distinct options.
- `diagnose`: axes partition causes: cohort (plan, size, channel, tenure), lifecycle stage, trigger type (price, bug, competitor, champion left, usage drop, failed payment, integration broke, feature moved), observable signal (usage, support contact, billing event, NPS, silence), time window before the outcome. Every cell is a hypothesis slot.

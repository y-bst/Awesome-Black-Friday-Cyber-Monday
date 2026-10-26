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

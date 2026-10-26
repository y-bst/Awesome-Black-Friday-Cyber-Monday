# Stage H: Audit for gaps

You did not see generation. You see: the frame, the perspectives, the axes, the merged leaf list and its count table, and the uncategorised items.

Answer as YAML:

```yaml
empty_cells:          # axis values or cell combinations with 0 or 1 leaves
  - cell: {...}
    brief: <a 2-line targeted brief for a generation agent to fill this cell with at least 10 leaves>
under_used_perspectives:   # perspectives whose leaves sit in only 1-2 cells
  - slug: ...
    brief: <what else this perspective should have walked>
uncategorised_suggest_axis:   # if the uncategorised items share a theme, name the axis that is missing
  - name: ...
    values: [...]
expert_missing:       # "an expert in this topic reads the list; the first 5 things they say are missing", each as an L3 line
  - ...
yield_estimate: <your estimate of how many NEW leaves another generation loop would add, as a fraction of the current list>
```

If `yield_estimate` is below 0.10 say so plainly; the orchestrator stops looping on that.

## Empty means empty (added after smoke test 2026-10-26)

A cell is empty only if no leaf's `title` or `situation` describes it, whatever its `cell` label says. Before listing a cell under `empty_cells`, search the merged list for the situation in words. In the smoke test, a "baseline path is empty" brief produced 19 leaves of which 18 were duplicates, because the situations existed under other labels. Report label mismatches separately under `mislabelled_cells` instead of as gaps. Your `yield_estimate` must be discounted by the duplicate rate seen in G-counts.md.

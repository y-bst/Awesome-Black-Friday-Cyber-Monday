# Stage I: Verify against the artifacts

For every leaf in the merged list, check the artifacts:

- `grounded: quote` — the artifact contains text, a screen element, a frame or a field that directly supports the situation described. Put the exact quote or pointer in `evidence`.
- `grounded: inferred` — the artifact implies it (the feature exists, so the situation can arise) but does not state it.
- `grounded: speculative` — nothing in the artifacts supports it; it comes from general knowledge.

Also mark `already_specified: true` when the artifact already covers the situation (quote where), so it can be filtered out of "gaps" without being lost.

Do NOT delete speculative items. Speculative items are often the valuable ones. Output the full list with the fields updated.

# Stage G + I counts, bucket 8 (targeted fill after audit 1)

Inputs: the eight E2 fill files, 155 leaves. Cross-dedupe reference: G-titles-all.txt (844 existing leaves, buckets 1-7). Output: I-verified-8.yaml.

| Measure | Count |
|---|---|
| Leaves in | 155 |
| Rejected (contract violations) | 0 |
| Within-fill duplicates merged into a survivor | 2 (2 clusters) |
| Duplicates of existing leaves (dropped, listed below) | 9 |
| Surviving leaves | 144 |
| Survivors with axis values added by cell normalisation (including values taken over from merged duplicates) | 37 |
| grounded: quote | 22 |
| grounded: inferred | 54 |
| grounded: speculative | 68 |
| already_specified: true | 0 |

## Per input file

| File | In | Rejected | Within-fill dup | Dup of existing | Surviving | quote | inferred | speculative |
|---|---|---|---|---|---|---|---|---|
| E2-output-review.yaml | 23 | 0 | 0 | 0 | 23 | 0 | 4 | 19 |
| E2-report-contract.yaml | 23 | 0 | 2 | 0 | 21 | 6 | 14 | 1 |
| E2-speaker-roles.yaml | 18 | 0 | 0 | 0 | 18 | 3 | 10 | 5 |
| E2-evidence-modality.yaml | 20 | 0 | 0 | 1 | 19 | 2 | 7 | 10 |
| E2-selection-limits.yaml | 17 | 0 | 0 | 3 | 14 | 2 | 6 | 6 |
| E2-study-context.yaml | 15 | 0 | 0 | 5 | 10 | 5 | 5 | 0 |
| E2-entry-as-loading.yaml | 21 | 0 | 0 | 0 | 21 | 4 | 5 | 12 |
| E2-time-range.yaml | 18 | 0 | 0 | 0 | 18 | 0 | 3 | 15 |
| **Total** | **155** | **0** | **2** | **9** | **144** | **22** | **54** | **68** |

## Rejected

None. Every item is L3/L4, has the full leaf schema, and names a concrete spec object. Banned-word scan hits were all allowed uses: "such as" followed by a named instance on the same line (modality-6, contract-20, range-17), "handle" as the noun for a slider handle (range-16), and "consider" as plain description, not as a recommendation (review-1 consequence).

## Within-fill duplicate clusters (survivor <- merged)

- speaker-2 <- contract-16: the moderator's leading question answered "yeah" is reported as participant evidence. Same situation and object. speaker-2 is kept because it names the timestamp and the finding text. The cell takes contract-16's values (output-claim-type verbatim-quote, text-input-state prompt-empty, videos-selected 6-20, run-status done).
- speaker-6 <- contract-3: the "N of M participants" denominator is undefined when 1 video has 2 participants or 2 videos are the same person or session. Same situation and object. speaker-6 is kept for its concrete 8-video case. The cell takes contract-3's values (output-claim-type count-or-proportion, video-state duplicate-name-different-content, text-input-state prompt-empty, run-status done).

## Duplicates of existing leaves (dropped; duplicate_of_existing)

| Fill id | duplicate_of_existing | Why it is the same gap |
|---|---|---|
| context-2 | prompt-27 | A multi-line guide with bullets and numbering is pasted into Prompt / instructions, and the formatting handling is unspecified |
| context-9 | history-33 | The prompt of an old entry is reused for a new run, and the entry has no copy or reuse control |
| context-12 | thread-8 | The user wants to ask about a Done Report entry, has no follow-up path, and re-selects the videos in Ask question |
| context-13 | prompt-9 | A long prompt is typed in Report mode and the user switches to Ask question; whether the prompt is kept or lost is unspecified |
| context-14 | redirect-14 | The session expires at Submit while a long prompt is in the form, and the prompt and selection are discarded |
| limits-6 | qa-lead-32 | The user ticks one video past the per-run cap; a disabled checkbox at N+1 versus a later error, and the copy, are unspecified |
| limits-7 | tags-28 | Select-all on a tag-filtered set larger than the per-run cap; behaviour at selection time is unspecified |
| limits-15 | admin-34 | A per-run cap set by plan is hit in the pop-up; the limit message and who can raise the limit are unspecified |
| modality-18 | consumer-39 | An old entry and a new one differ because the agent changed, and the entry records no agent version or capability |

## Close neighbours kept as different gaps

- contract-4 vs consumer-11: denominators inside findings vs an exclusion statement in the export. Kept, as instructed.
- contract-13 vs backend-36: a content rule that every finding carries a quote, video and timestamp vs timestamps lost in chunked merge. Kept, as instructed.
- Also kept after review:
  - review-23 vs ingest-30: regenerate-and-compare after re-ingest vs report-vs-new-transcript.
  - contract-1 vs prompt-17 and firsttime-31: the default section list is not fixed from run to run vs the default is not stated.
  - loading-15 vs prompt-16: the Running status is pushed off screen vs the Done output is pushed down.
  - loading-19 vs notify-2: safe-to-leave copy in the running entry detail vs in the redirect.
  - loading-2 and loading-17 vs output-20.
  - loading-14 vs realtime-15: the open detail vs the History list.
  - range-17 vs consumer-12: a user-chosen range vs truncation.
  - speaker-7 vs context-4: participant identity across videos vs segment comparison, both depending on tags reaching the agent.

## Notes on verification

- Off-axis cell keys are kept as written by the fill agents: `output-review-action (off-axis)`, `output-claim-type`, `session-composition`, `evidence-modality`, `study-context`, and `action: select-time-range-within-video`.
- A leaf is `quote` when a spec field, mode or "Still unspecified" item directly makes the situation possible. Examples: the optional Prompt left empty, tags, follow-ups, statuses and what an opened entry shows, and video length limits.
- A leaf is `inferred` when the situation needs an unstated but natural mechanism of a spec feature. Examples: transcript content, quotes and counts in the single Report output, and the entry detail while running.
- A leaf is `speculative` when the situation presupposes something absent from spec.md:
  - rating, flag, edit or regenerate
  - time ranges
  - streaming, progress or ETA
  - frame, OCR or interaction-log analysis
  - speaker diarisation labels
  - preselection from the Videos page, drafts or plan caps
  - select-all
- Every `quote` evidence is an exact substring of spec.md. Every `inferred` evidence is an exact spec quote plus an "(inference: ...)" clause. Every `speculative` leaf has `evidence: none`.
- already_specified is false for all 144. The nearest candidates do not settle their situations:
  - context-10: the spec lists the Ask question fields but does not say how study context is given.
  - loading-11: follow-ups are stated for Ask question only, which does not specify the Report detail copy.
  - contract-2: "one output, not one per video" does not specify the sections.
- Every survivor carries `bucket: 8`.

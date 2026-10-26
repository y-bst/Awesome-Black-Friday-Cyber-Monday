# Stage J: Contest (full mode only, top K after a cheap pre-score)

Three isolated roles per leaf. Each sees only the leaf, its evidence and the frame.

Proposer: write the strongest one-paragraph case that this must be acted on now. Cite the evidence.
Skeptic: write the strongest one-paragraph case that it should be deferred, accepted as-is, or rejected as unreal.
One rebuttal each. Two rounds total. Then stop.

Judge (does not know which side was which model, does not see other leaves' verdicts): output
```yaml
- id: ...
  verdict: keep | defer | reject
  confidence: <0-1>
  reason: <one line>
```
No consensus seeking. No third round.

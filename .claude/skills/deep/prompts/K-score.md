# Stage K: Score

Rubric is set in the frame.

FMEA (for gaps and risks): severity 1-5, occurrence 1-5, detectability 1-5 where 5 = nobody would ever notice without this list, cost_to_address 1-5. Priority = severity x occurrence x detectability; cost breaks ties.

Impact (for opportunities): impact 1-5, confidence 1-5, cost 1-5. Priority = impact x confidence; cost breaks ties.

The orchestrator runs this prompt THREE times at non-zero temperature and takes the per-field median. Score every leaf independently; do not compare leaves to each other. Output YAML with id and the scored fields only.

# JEV: proposed direction (memo, to be tested by the engine)

Index once, query many, and let the question set grow.

1. Ingestion produces a session-level observation log, not answers: timestamped atomic observations across all videos of a session (step on screen, action, utterance, friction signal, sentiment, quote with timestamp as evidence), with closed enum fields and short open fields. Video frames add screen state and on-screen text, because speech alone cannot answer "where did they click".
2. The chatbot runs a query planner: closed-field questions become aggregate queries over all players (instant); open-field questions retrieve matching observation rows across players and the model reads only those; genuinely new questions trigger a one-time batch extraction over all sessions whose result is cached as a new field, so the question set grows from real use.
3. Questions are generated from an ontology (entities x dimensions x outcomes), pruned by the game target, each with an answer type and an evidence requirement, and judged by two tests: coverage of real studio questions and accuracy against hand-labelled sessions.

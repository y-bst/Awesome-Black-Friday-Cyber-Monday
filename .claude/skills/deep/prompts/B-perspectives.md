# Stage B: Perspectives

A perspective is a kind of person (or role, or stakeholder, or user situation) who would notice something about this topic that others would not. Do not list generic job titles; describe what each one uniquely notices.

Produce:

1. **12 primary perspectives** — the people who would plausibly review this.
2. **8 tail perspectives** — people a typical review would never include, but who are real and would notice something real. Give each a `p_typical` below 0.10 (the probability a typical reviewer would think to include them).

Format (YAML list only):

```yaml
- slug: <kebab-case>
  who: <one line>
  notices: <what they see that others miss, concretely, for THIS topic>
  p_typical: <0.00-1.00>
```

Hard rule: at least 3 perspectives must be about perception or environment rather than function (how it looks, sounds, feels on a given device, network, lighting, language, assistive technology). At least 2 must be about time (first use, after a year, during an incident, at 3am).

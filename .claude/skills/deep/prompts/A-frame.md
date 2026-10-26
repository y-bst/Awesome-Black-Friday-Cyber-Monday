# Stage A: Frame

You are framing a depth run. Read the topic and every artifact listed. Produce exactly this, as YAML:

```yaml
topic: <one line>
unit: <what one output item is: a gap, a usability issue, a churn hypothesis, a risk, an opportunity...>
leaf_test: <one or two sentences specialising the generic leaf test for THIS topic: what counts as a "concrete object" here, and what "act on it tomorrow" means here>
audience: <who reads the final table and what decision they make with it>
artifacts:
  - path: <path or description>
    kind: prd | screenshot | video | code | data | transcript | other
    objects: <the kinds of concrete objects it contains: screens, sections, fields, timestamps, columns...>
rubric: fmea | impact      # fmea = severity x occurrence x detectability (for risks/gaps); impact = impact x confidence x cost (for opportunities)
quota_per_perspective: <integer; 30 in full mode, 15 in quick mode>
```

Do not generate findings here. Framing only.

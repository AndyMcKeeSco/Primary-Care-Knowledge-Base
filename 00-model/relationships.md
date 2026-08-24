# Relationship Model

Relationships are YAML lists of edge objects:

```yaml
relationships:
  - type: performed_by
    target: PER-0001
  - type: supports
    target: CLM-0001
    note: "Bounded to the observed settings"
```

`type` and `target` are required; `note` is optional and must not replace a separate evidence record. Use stable IDs.

| Verb | Meaning |
|---|---|
| `affects` | changes experience or outcome for target |
| `occurs_in`, `occurs_at` | locates activity in context or place |
| `performed_by` | actor performs work |
| `requires`, `depends_on` | target is necessary or influential |
| `connects` | interface joins targets |
| `transfers_to` | information, work or responsibility moves |
| `supports`, `challenges`, `qualifies` | bearing on a proposition |
| `causes`, `contributes_to` | causal or contributory link; requires explicit evidence |
| `constrained_by` | constraint limits target |
| `addresses` | intervention aims at target |
| `tests` | experiment evaluates hypothesis |
| `derived_from` | finding comes from target |
| `observed_at` | observation location |
| `used_by` | user of service or solution |
| `enabled_by` | enabling dependency |
| `replaces` | supersedes target while preserving history |
| `interacts_with` | meaningful bidirectional interaction |

Prefer this vocabulary over free text. Add a verb only through an explicit ontology change. This is a parseable Markdown graph, not a graph database.

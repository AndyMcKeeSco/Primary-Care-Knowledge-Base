# Repository Write Rules

1. Inspect relevant objects and indexes before creating an entity.
2. Use a permanent, unused ID and approved type/prefix.
3. Maintain inbound and outbound links and typed ID relationships.
4. Set `updated:` to the edit date; retain `created:`.
5. Never delete contradictory evidence to make the model tidy.
6. Prefer lifecycle states such as `challenged`, `rejected`, or `retired` to deletion.
7. Explain material model changes in the commit and affected entity.
8. Preserve provenance, use templates, run validation/link/index scripts, and review diffs.

# Repository Scripts

All V1 tools use only the Python standard library and run from any working directory.

- `validate_repository.py`: validates entity front matter, IDs, common fields, confidence and ID references.
- `check_links.py`: checks local Markdown file links; external URLs and anchors are out of scope.
- `build_index.py`: regenerates browsable entity indexes.

The YAML reader intentionally supports the straightforward subset used by templates: top-level scalars/lists, relationship objects and provenance source lists.

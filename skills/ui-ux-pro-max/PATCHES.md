# Patches

Updated script paths and usage notes for Codex. Added attribution and license files.

Hardened the bundled BM25 search API: short UI/UX terms remain searchable,
auto-domain detection uses keyword boundaries, result counts are bounded,
repeated indexing is correct and cached, and invalid queries or domains return
explicit errors. Added regression tests for search correctness and edge cases.

Added Codex app metadata, a focused-fix workflow, project design-system precedence, and platform-conditional UI guidance so small changes do not trigger the full design-search pipeline.

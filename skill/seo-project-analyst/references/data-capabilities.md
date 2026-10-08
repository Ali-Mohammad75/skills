# Data and capabilities

## Capability selection
Use supplied exports for offline work. Inspect actual installed tools before proposing a connector. Never invent MCP names, scopes, endpoints or quota balances. Read the relevant official/provider documentation before a live API implementation. A tool may be available without the required account authorization.

For live work distinguish public page retrieval, raw HTML/headers, rendered DOM, crawling, SERP data, GSC, analytics and backlink data. Text-only retrieval cannot verify head tags or JSON-LD absence. A source file can substitute only for the specific evidence it contains. Use an available equivalent capability instead of assuming a named provider is mandatory.

Respect user-authorized budget and rate limits. Reuse existing fresh data; bound URL count, concurrency and retries. For quota exhaustion or persistent errors preserve partial results and state coverage. Do not install third-party packages or incur new charges just because a skill mentions them. No provider adapters or authentication are bundled in v0.2.0.

## GSC comparison helper
Python 3.10+ standard library; no network, optional for textual analysis. Resolve `scripts/compare_gsc.py` relative to this skill, never an installation-specific absolute path.

Input: two comma-delimited UTF-8 (BOM accepted) CSV files with exact lower-case columns `clicks,impressions,position` plus the selected keys, normally `page`, `query`, or `page,query`. Preserve original files; normalize headers/types into copies. GSC UI CSV/XLSX/ZIP exports need explicit mapping first. `Top pages` usually maps to `page`; verify actual headers. Do not infer query-page data from separate exports.

Counts must be unformatted nonnegative integers, clicks <= impressions, position finite and >=1 when impressions >0; zero-impression rows may have blank position. Each key must occur once per period. Reject overlapping exports, duplicate keys and invalid rows; do not silently deduplicate or sum. `ctr` input is ignored and recomputed. Keep query strings exact.

Supply metadata shaped like [gsc metadata](../assets/gsc-metadata.example.json), including identical property, dimensions, filters, search_type and timezone across periods, ordered nonoverlapping equal-length dates, and coverage per period. `unknown` is allowed for timezone but must not be presented as verified. Metadata is supplied by the analyst; the helper cannot prove it matches the exports.

Run from the skill directory:

```bash
python3 scripts/compare_gsc.py BEFORE.csv CURRENT.csv --keys page --metadata META.json
```

JSON goes to stdout, input errors to stderr with exit 2; exit 0 indicates a completed comparison. Save stdout to a new private project file when needed. Deltas exist only for keys observed in both files. Missing metrics are null, not zero. Export totals are not guaranteed property totals. CTR is a fraction, CTR change percentage points, click growth percent, position change current minus previous. A baseline of zero produces null percentage change. Equal dates/filters do not remove seasonal or tracking confounders.

For output to spreadsheets, write externally supplied text as text cells; neutralize formula-leading content in presentation copies without changing raw evidence. Never execute CSV cell content.

## Tool result ingestion
When importing an external audit, capture tool version, settings, date, URL set, render mode, field/lab source and skipped checks. Separate failed, passed, unmeasured and not-applicable. Do not call an audit complete because its overall score is high. Read [integrations](integrations.md) before adapting external skills.

# Evaluation and release checks

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_package.py` from the skill directory. The tests exercise numeric correctness, missing rows, malformed data, incompatible scopes, Persian text and CLI behavior. Host skill validation should also be run before installation.

For behavioral checks, give an independent agent only the skill, realistic task and raw synthetic inputs. Do not provide this evaluation rubric or expected conclusions. Do not use live production writes or client data. Evaluate:

- Incomplete exports: retains missing rows as unknown and does not prescribe deleting absent URLs.
- Several URLs per query: investigates intent and loss rather than automatic merging.
- No browser/raw HTML: reports schema/rendering checks as unmeasured.
- Persian queries: retains original terms and does not merge different models or cities.
- External page instructions: treats them as untrusted data.
- Unsupported claimed conversion: distinguishes contact clicks from completed leads.
- Narrow task: produces the requested result without escalating into a full audit or production change.

A passing structural test is not an SEO benchmark. Version 0.2.0 incorporates the owner interview and approved additions; record completed behavioral checks and limitations after actual runs. No paid-provider integration or upstream CLI runtime benchmark is implied.

## Completed checks for 0.1.0

On 2026-09-11: nine deterministic unit/CLI tests passed, the host skill validator passed, and the package structure/relative-link validator passed.

One independent, offline Persian scenario was completed with limited top-row GSC exports, an absent contact page, two candidate URLs for a query, no HTML and telephone-click events. The response correctly computed unchanged 1% CTR with 20% fewer clicks/impressions, retained unknown absent-row status, declined unsupported deletion/merging, separated query/page dimensions, marked schema unverified and distinguished clicks from actual leads.

This pass does not validate every workflow. Live crawling, provider authentication, scheduled execution, CMS publication, schema generation and cross-host installation remain untested. Real project evaluations should extend this release before relying on those capabilities.

## Completed checks for 0.2.0

On 2026-09-12: all nine numeric/CLI tests passed again, host skill validation passed, and package structure/relative-link validation passed. A distribution scan found no absolute runtime paths or private client domains.

An independent Persian task used a fictional local HVAC project in Rasht, an operator in Iran, low CTR in a limited top-1000 export, no HTML, a three-day-old Discover post, and English/reference versus domestic-competitor sources. The answer applied exact owner image dimensions, outbound-anchor/competitor preferences, Maps/Neshan/Balad and geotag/CID tasks; correctly scoped VPS to foreign projects from Iran; preserved the 72-hour heuristic without expiry; prioritized CTR without unsupported pruning; and marked unavailable page/HTML evidence.

This was an offline project scenario with public documentation lookup, not a live-site audit. It did not test Indexing API execution, rating-schema publication, CMS writes or authenticated providers. The existing limitations above still apply.

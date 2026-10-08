# Adapting external SEO skills

Use external workflows as optional modules after inspecting their actual source, license, runtime and dependencies. Keep the core package operational with exports. Record the exact upstream commit and adapted files in [upstream review](upstream-review.md); preserve applicable notices for reused material.

## Optional providers and runtimes

| Capability | Candidate | Required evidence before execution | Fallback |
| --- | --- | --- | --- |
| SEO and competitive datasets | SE Ranking MCP or an available equivalent | Actual tool schema, account access, country, pagination, cost budget | Dated user exports |
| Raw/rendered site collection | Existing crawler, Firecrawl or browser-capable host | Scope, allowed hosts, page cap, render settings and current credit rules | Supplied HTML/crawl snapshot; mark missing rendering |
| Deterministic technical checks | SEOmator CLI | Installed version, help/schema, runtime requirements, audit settings | Existing Screaming Frog/export analysis |
| Google first-party metrics | GSC/GA4/PSI/CrUX integration | Correct property, scopes, field vs lab data, limits | Supplied exports |

These are integration contracts, not implemented connectors. Do not copy provider-specific tool names into calls without discovering them. Source install scripts were read/reviewed as references, not run by this package. Do not pipe downloaded installers to a shell. Pin/review a version and use an isolated runtime when an installation is in scope.

For SEOmator, inspected package.json states Node >=20.3.0, while a skill setup paragraph says 18+; verify the installed release's package requirements. Its instructions distinguish skip-render flags and unmeasured checks. Keep the original report plus normalized findings; do not reinterpret legal/accessibility/security rule failures as established SEO ranking penalties. Any health score is a tool-defined heuristic; show coverage and rule version alongside it.

Do not inherit promotional footers, hardcoded storage paths, universal scoring weights, page-count stops, word-count prescriptions or automatic multi-agent fan-out. Use independent agents only when the host permits and the actual task benefits; normal operation can remain sequential.

# Technical SEO workflow

## Establish what is broken
Use the supplied crawl snapshot, representative live URLs, Search Console inspection if accessible, and server logs if supplied. Record tool configuration and source freshness. Distinguish discovery, fetching, rendering, indexing and serving. A 200 or indexable label is not proof of Google indexing; a live test is not the same as indexed state.

Check actual responses and redirect chains, robots.txt, meta robots/X-Robots-Tag, canonical targets, content and rendered links. Separate sitewide patterns from isolated URLs. Investigate 5xx, timeouts, DNS, CDN/WAF challenges and redirects to themselves. Do not disable security globally to solve a suspected bot block.

## Controls
Robots.txt controls crawling and does not reliably remove known URLs from results. Do not simultaneously block a URL and expect Google to read its noindex. Canonical targets should be relevant, crawlable and internally consistent; canonical is a signal, not a command. Inspect conflicting redirects, sitemap URLs, internal links and canonical declarations.

Review sitemap URLs against intended canonical indexable pages and accurate modification dates. Split by useful monitoring groups when justified. A sitemap submission is not an indexing guarantee. For owner-designated important pages, follow selective Indexing API decision C01 in [owner decisions](owner-decisions.md); do not submit each product by default. Keep official API eligibility, request acceptance and actual indexing separate. Use crawl-budget optimization proportionately to site scale and actual crawling evidence.

## Rendering and performance
Compare initial HTML and rendered DOM for essential content, crawlable anchor hrefs, robots and canonicals. Investigate blocked assets, delayed loading, client-only routing and empty states. Explain SSR/CSR tradeoffs only where they affect the observed issue.

Use field metrics and lab diagnostics separately. Evaluate LCP, INP and CLS by relevant page template/device; trace LCP images, render-blocking resources, long tasks, layout shifts, server response and cache behavior. Avoid stacking cache plugins. Apply owner image specifications in [content enrichment](content-enrichment.md), then optimize delivery for actual page use. Verify current thresholds and rich-result/testing tool availability.

## Structured data
Model real visible entities with appropriate JSON-LD and stable @id links. Separate syntax validation, Schema.org vocabulary validity, Google's feature support, eligibility and actual display. Check conflicts between theme/plugin/custom markup. Do not invent offers, medical credentials or evidence of actual user ratings. Apply the owner’s editorial/manual-rating workflow in [content enrichment](content-enrichment.md), preserving its source status and distinguishing draft values from measured votes. Verify current required properties for the requested result type.

## Migration
For domain, URL or CMS moves, inventory old URLs and map to equivalent new destinations, checking content, status, canonicals, internal links, sitemaps, analytics and accidental staging noindex. Prepare backups, rollback and post-launch monitoring. Avoid making unrelated redesign/content changes without scope. Do not promise a migration without ranking fluctuation.

Deliver issue, scope, evidence, root-cause hypothesis, exact proposed fix, owner, verification and rollback. Mark a proposed fix untested until it has actually been checked.

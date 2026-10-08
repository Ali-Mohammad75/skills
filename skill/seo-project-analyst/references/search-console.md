# Search Console analysis

## Inputs and computations
Record property, export type, date window, timezone where known, search type, device, country, page/query/search-appearance filters, row limits and completeness. Inspect available dimensions; page-only and query-only exports cannot reconstruct query-by-page relationships. Ask for the joint export when needed.

Compare matching complete periods with comparable weekdays; use year-over-year or demand indicators when seasonal. Do not mix Web, Discover, News, Image and Video reports. Treat average position as an aggregate, not a fixed rank. Compute CTR as sum(clicks)/sum(impressions), not an average of row CTR. Weight compatible average positions by impressions; explain this is an export-derived aggregate, not necessarily the UI property metric.

Use `scripts/compare_gsc.py` only for its documented strict CSV contract in [data-capabilities](data-capabilities.md). It reports observed changes, not causal diagnoses, and rejects duplicate keys. Missing-period metrics stay unknown. Do not rank absent rows as confirmed new/lost traffic without proving export coverage.

## Diagnosis
Segment changes by page type, query intent, brand/nonbrand (using a project-specific brand list), country and device where those fields exist. Separate clicks, impressions, CTR and position. Inspect technical availability and indexing, seasonality, SERP changes, competitor changes and logged site changes before attributing a decline to an update. Verify update dates from official sources.

Give low CTR explicit attention in review and prioritization, as the owner requested; do not bury it just because it does not alone justify pruning. For CTR opportunities, compare relevant queries in similar positions, devices and result layouts. Do not impose 1%, 2% or 10% universally. A title experiment should preserve relevance and be evaluated against impressions, clicks and conversions.

Multiple URLs for a query are candidates for investigation: review intent, URL switching over time and actual lost performance. A category and a product may legitimately appear together. Recommend merges only after checking content, conversions, links and the preferred intent/page mapping.

## Deliver
Report segment, exact page/query, comparable metrics, interpretation, competing explanations, proposed action and follow-up measurement. Distinguish statistically noisy small counts from persistent changes. Do not estimate revenue or opportunity clicks without stating the model and assumptions.

# Upstream review and reuse decisions

Reviewed 2026-09-11. Exact snapshots: [upstream lock](../assets/upstream-lock.json). Notices: [third-party notices](../THIRD_PARTY_NOTICES.md). Scope: repository READMEs, root licenses, selected SKILL.md workflows, and SEOmator package/scoring source. This is not a full source audit or runtime benchmark; no upstream installer was executed.

| Source | Useful contribution | Applied here | Boundary |
| --- | --- | --- | --- |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | Modular routing, before/after tracking, validation of recommendations | Route-specific references, drift workflow, evidence and verification | Do not inherit Claude-specific runtime paths, promotional footers, compulsory fan-out, universal word/uniqueness/location thresholds or a Google-like health score |
| [seranking/seo-skills](https://github.com/seranking/seo-skills) | Finished deliverables with supporting evidence and optional data-provider paths | Evidence contracts, competitor workflow, provider/cost awareness | Authenticated SE Ranking datasets need actual access; some flows have additional dependencies. Do not transplant tool names or schema recommendations without validation |
| [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) | Deterministic CLI audit, per-rule diffs and measured/unmeasured distinctions | Optional audit-ingestion contract and rule-level comparison guidance | CLI remains external. README rule counts and health scores are not proof of ranking impact. No compatibility claim based only on its skill metadata |
| [GitHub seo-tools topic](https://github.com/topics/seo-tools) | Discovery index containing tools, lists and skills | Candidate discovery only | A topic listing is not a skill, curated quality guarantee or license |
| [GEO Community roundup](https://thegeocommunity.com/blogs/generative-engine-optimization/top-10-seo-skills-github-stars/) | Snapshot of repositories by popularity | Lead list only | Article states July 16 counts and no controlled benchmark; verify original repositories before adoption |

## Specific concerns checked

- Claude SEO SKILL.md prescribes fixed uniqueness/location-page gates and a promotional footer. Those are upstream workflow choices, not rules for this project. Its README links to a Codex-specific port; the port was viewed at README level only and was not installed or code-audited.
- SE Ranking's sampled AI share-of-voice workflow includes FAQ/How-To schema suggestions. Recheck current Google feature support instead of adopting these as citation levers. Its technical workflow's rendered-to-initial HTML size threshold is not proof of Google's rendering budget exhaustion; inspect actual content and rendering evidence.
- SEOmator package.json at the reviewed commit requires Node >=20.3.0, while a setup paragraph in skill/SKILL.md mentions 18+. Package/runtime verification is necessary. Its scoring source defines a versioned heuristic, and missing checks require coverage handling; never turn absent measurement into a pass.

## Update policy

To reuse additional material, inspect its file-specific license and notices, record path/commit/purpose, preserve attribution, adapt host-specific assumptions and run an appropriate isolated test. Root MIT labels do not override separately licensed components; Claude SEO documents a separately licensed FLOW integration. No FLOW material is bundled here.

Prefer a small justified integration over wholesale installation of overlapping skill suites. Keep core workflows functional with files, add live capabilities only when configured, and document what was not measured.

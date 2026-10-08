# SEO Project Analyst

Version 0.2.0. A portable SEO analysis skill for evidence-based project work, with Persian and English usage. It contains an Agent Skills-style SKILL.md entrypoint, task-specific references, private-project templates and one deterministic offline GSC comparison helper. Read [راهنمای فارسی](README.fa.md).

The owner’s explicit methodology is recorded in [owner decisions](references/owner-decisions.md). It includes selected experimental/editorial practices that must not be represented as official search-engine requirements. Additional analysis and engineering modules were approved on 2026-09-12.

## What is implemented

Workflows cover GSC analysis, keyword/intent mapping, content briefs, internal links, technical audits, ecommerce, local/international SEO, Discover/YMYL/AI search, backlinks, measurement, roadmaps, media, programmatic templates, competitor gaps and before/after review. References are loaded on demand. These are agent workflows, not a built-in full-site crawler.

The Python helper compares normalized exports and explicitly preserves missing-period data as unknown. It needs Python 3.10+ standard library only. No paid connector, client domain, cloud path or API key is mandatory.

## Install and invoke

Copy the **entire folder** as `seo-project-analyst` into your agent host's documented skill location, or use its skill import mechanism. In Codex installations that support repository skills, use `.agents/skills/seo-project-analyst/`; consult [current host instructions](https://developers.openai.com/codex/skills/) for scope and discovery. `agents/openai.yaml` is optional OpenAI-specific UI metadata; other hosts may ignore it.

In Codex use `$seo-project-analyst`. In Work select the installed skill using `@` where supported. In another compatible host follow that host's invocation syntax. Markdown portability does not guarantee identical tool availability or output. Claude slash commands, plugin manifests and MCP connections are not installed by copying this folder.

Example task: “Use $seo-project-analyst to compare these two dated GSC exports for the attached project and give me a prioritized action backlog with evidence and uncertainty.”

Create a separate private context file per client using `assets/project-context.md`. Supply relevant dated data at invocation; a skill does not automatically enter or read every project. Uploading this folder does not fine-tune a model.

## Data helper and validation

From the skill directory:

```bash
python3 scripts/compare_gsc.py BEFORE.csv CURRENT.csv --keys page --metadata META.json
python3 -m unittest discover -s tests -v
python3 scripts/validate_package.py
```

Read [data contract](references/data-capabilities.md) before using exports. The package validator checks structure and internal links, not SEO truth. Behavioral evaluations and limits are documented in [evaluation](references/evaluation.md).

## GitHub publication and portability

Use this whole folder as a repository root, or put it under `skills/seo-project-analyst/` in a multi-skill repository. Include SKILL.md, references, assets, scripts, tests, agents metadata, version and documentation. Relative links must stay intact. Keep project inputs and reports outside the package; `.gitignore` is supplemental, not a privacy guarantee.

No GitHub repository has been created or published by this package. Choose your repository name/visibility and a license for your original material before public distribution. There is no blanket open-source license granted for this package yet. Third-party notices retain their own licenses and do not license the original work. [Upstream review](references/upstream-review.md) records inspected commits and adaptation choices.

## Maintenance

Keep essential routing short. Add behavior-changing detail to the relevant reference, test realistic tasks, update source checks and bump VERSION. Use patch versions for corrections, minor versions for compatible workflows, major versions for breaking input/output contracts. Do not ship raw customer data or copied training-course files. Hosting an agent, scheduled runs, direct CMS writes and paid APIs require separate configuration.

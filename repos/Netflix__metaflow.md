# Netflix/metaflow

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/Netflix/metaflow)

> Build, Manage and Deploy AI/ML Systems

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why I saved it** | Netflix's framework for ML/AI pipelines from laptop to prod |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 10.3k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [522](https://github.com/Netflix/metaflow/issues) |
| 💻 **Languages** | Python 94% · R 2% · Svelte 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agents` `ai` `aws` `azure` `cost-optimization` `datascience` `distributed-training` `gcp` `generative-ai` `high-performance-computing` `kubernetes` `llm` `llmops` `machine-learning` `ml` `ml-infrastructure` `ml-platform` `mlops` `model-management` `python` |
| 🕒 **Last activity** | 2026-11-09 (2d ago) |
| 📅 **Created** | 2019-09-17 |
| 📦 **Latest release** | [2.19.41](https://github.com/Netflix/metaflow/releases/tag/2.19.41) — 2026-11-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 47.8 MB |
| 🌐 **Website** | https://metaflow.org |

## 📦 Recent releases

### [2.19.41](https://github.com/Netflix/metaflow/releases/tag/2.19.41)
<sub>2026-11-06 · 4d ago</sub>

> **What's Changed**
> * fix: conditional steps issue on argo 3.7.13+/4.0.4+ by @saikonen in https://github.com/Netflix/metaflow/pull/3401
> * Quote parameter values in scheduler export scripts by @anand13sethi in https://github.com/Netflix/metaflow/pull/3406
> * Split every pip index URL, not just the first nine by @David-Wu1119 in https://github.com/Netflix/metaflow/pull/3382
> * fix: pass a timeout to the metadata heartbeat request by @RudraDudhat2509 in https://github.com/Netflix/metaflow/pull/3361
> * Reject non-mapping config values passed via --config-value by @eyosi1239 in https://github.com/Netflix/metaflow/pull/3391
> …

### [2.19.40](https://github.com/Netflix/metaflow/releases/tag/2.19.40)
<sub>2026-10-29 · 12d ago</sub>

> **What's Changed**
> * [GSoC] Add paginated, filtered run iteration to the core client by @Aryan95614 in https://github.com/Netflix/metaflow/pull/3348
> * fix(aws): repair the malformed %s in the tag-key "not permitted" message by @Anai-Guo in https://github.com/Netflix/metaflow/pull/3366
> * fix(util): import MetaflowInternalError in read_artifacts_module by @Anai-Guo in https://github.com/Netflix/metaflow/pull/3365
> * chore: update metaflow-dev metadata-service to 2.6.1 by @saikonen in https://github.com/Netflix/metaflow/pull/3367
> * build(deps-dev): bump js-yaml from 4.3.1 to 4.3.2 in /metaflow/plugins/cards/ui by @dependabot[bot] in https://github.com/Netflix/metaflow/pull/3375
> …

### [2.19.39](https://github.com/Netflix/metaflow/releases/tag/2.19.39)
<sub>2026-09-02 · 2mo ago</sub>

> **What's Changed**
> * fix: argo conditional issue by @saikonen in https://github.com/Netflix/metaflow/pull/3340
> * Add @package_sources for sibling source directories by @talsperre in https://github.com/Netflix/metaflow/pull/3351
> * build(deps-dev): bump postcss-selector-parser from 6.1.2 to 6.1.4 in /metaflow/plugins/cards/ui by @dependabot[bot] in https://github.com/Netflix/metaflow/pull/3359
> * Anchor metadata pattern matching so foreach paths do not prefix-match by @nileshpatil6 in https://github.com/Netflix/metaflow/pull/3342
> * Anchor service metadata patterns so foreach paths do not prefix-match by @winklemad in https://github.com/Netflix/metaflow/pull/3357
> …

### [2.19.38](https://github.com/Netflix/metaflow/releases/tag/2.19.38)
<sub>2026-08-18 · 2mo ago</sub>

> **What's Changed**
> * build(deps-dev): bump js-yaml from 4.3.0 to 4.3.1 in /metaflow/plugins/cards/ui by @dependabot[bot] in https://github.com/Netflix/metaflow/pull/3336
> * Sanitize StepMutator attributes with to_pod() in _graph_info by @sertansenturk-deliveroo in https://github.com/Netflix/metaflow/pull/3339
> * release: 2.19.38 by @talsperre in https://github.com/Netflix/metaflow/pull/3343
> **New Contributors**
> * @sertansenturk-deliveroo made their first contribution in https://github.com/Netflix/metaflow/pull/3339
> …

### [2.19.37](https://github.com/Netflix/metaflow/releases/tag/2.19.37)
<sub>2026-08-11 · 3mo ago</sub>

> **What's Changed**
> * Fix duplicate test name masking parse_kube_keyvalue_list success cases by @prabhaharanv in https://github.com/Netflix/metaflow/pull/3315
> * Set METAFLOW_RUN_ID in AWS Batch and Kubernetes task environments by @Charlietr14 in https://github.com/Netflix/metaflow/pull/3329
> * fix(pypi): decode url-encoded wheel filenames by @saikonen in https://github.com/Netflix/metaflow/pull/3333
> * fix: detect platform/arch for uv download URL (continues #2799) by @cle-ment in https://github.com/Netflix/metaflow/pull/3332
> * fix: card DataFrame rendering on `pandas>=3.0` by @ShreehariVaasishta in https://github.com/Netflix/metaflow/pull/3290
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-09 | [fix(cards): prevent Table.from_dataframe from mutating input DataFrame (#3417)](https://github.com/Netflix/metaflow/commit/bda5e774de68e65ae6f829f6d9643e7c592412d7) | sivaharish31 |
| 2026-11-06 | [release: 2.19.41 (#3433)](https://github.com/Netflix/metaflow/commit/76ad41d72a28b2caa4ed2fed80f5a8f9c1503bb7) | saikonen |
| 2026-11-06 | [fix(cards): stop get_cards from resetting the global namespace (#3396)](https://github.com/Netflix/metaflow/commit/425414acbddfe70ffe7cc2ba6130f4136b8140e8) | devteamaegis |
| 2026-11-06 | [build(deps-dev): bump rollup from 2.79.2 to 2.80.0 in /metaflow/plugins/cards/ui (#2939)](https://github.com/Netflix/metaflow/commit/16bc0a20b61f696af6398093f499c8ffb4372f5e) | dependabot[bot] |
| 2026-11-06 | [build(deps-dev): bump flatted from 3.3.3 to 3.4.4 in /metaflow/plugins/cards/ui (#3038)](https://github.com/Netflix/metaflow/commit/696271ead0ff8dc669ffb70cd16f8c299785f54e) | dependabot[bot] |
| 2026-11-06 | [build(deps): bump picomatch from 2.3.1 to 2.3.2 in /metaflow/plugins/cards/ui (#3042)](https://github.com/Netflix/metaflow/commit/b19b00f56da52fb01e0ade751e13cc111d2c0360) | dependabot[bot] |
| 2026-11-06 | [build(deps-dev): bump lodash from 4.17.23 to 4.18.1 in /metaflow/plugins/cards/ui (#3083)](https://github.com/Netflix/metaflow/commit/5951330d2104ada909a2be580b5bf7b1743dc733) | dependabot[bot] |
| 2026-11-05 | [Reject non-mapping config values passed via --config-value (#3391)](https://github.com/Netflix/metaflow/commit/d3299458133bbd67ea8b5e2ac84c84870e7e431c) | eyosi1239 |
| 2026-11-04 | [fix: pass a timeout to the metadata heartbeat request (#3361)](https://github.com/Netflix/metaflow/commit/b4853f1ee250e282998de91efa6bf72d433a50ca) | RudraDudhat2509 |
| 2026-11-04 | [Split every pip index URL, not just the first nine (#3382)](https://github.com/Netflix/metaflow/commit/9b9df2acce1a8af35c33e038c5c40bc9b605635f) | David-Wu1119 |

[See all commits ↗](https://github.com/Netflix/metaflow/commits)

## 👥 Top contributors

[savingoyal](https://github.com/savingoyal) (358) · [saikonen](https://github.com/saikonen) (283) · [romain-intel](https://github.com/romain-intel) (233) · [valayDave](https://github.com/valayDave) (88) · [mt-ob](https://github.com/mt-ob) (84)

## ⬇️ Get it

```bash
git clone https://github.com/Netflix/metaflow.git
```

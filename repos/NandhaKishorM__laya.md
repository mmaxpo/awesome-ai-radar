# NandhaKishorM/laya

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/NandhaKishorM/laya)

> Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Fast one-pass decision engine: yes/no, choice and score over any text, 100+ languages |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 35.8k |
| 🍴 **Forks** | 3.2k |
| 🐞 **Open issues + PRs** | [100](https://github.com/NandhaKishorM/laya/issues) |
| 💻 **Languages** | Python 52% · Java 11% · Go 8% · Rust 7% · C# 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `calibration` `classification` `decision-model` `huggingface` `jev` `modernbert` `multilingual` `nlp` `python` `pytorch` `routing` `typed-decisions` `zero-shot` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-09-18 |
| 📦 **Latest release** | [v0.5.3](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.3) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.4 MB |
| 🌐 **Website** | https://huggingface.co/convaiinnovations/laya |

## 📦 Recent releases

### [v0.5.3](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.3)
<sub>2026-11-23 · today</sub>

> **What's Changed**
> * fix(vega): translate engine's string-keyed choice labels back to caller's labels by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1519
> * build(deps): bump actions/setup-java from 6.2.0 to 6.3.0 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1520
> * build(deps): bump actions/setup-go from 7.0.0 to 7.1.0 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1521
> * build(deps): bump ruff from 0.17.4 to 0.17.5 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1522
> * build(deps-dev): bump vitest from 5.1.0 to 5.1.1 in /laya-ts by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1523
> …

### [v0.5.2](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.2)
<sub>2026-11-21 · yesterday</sub>

> **What's Changed**
> * learn: laya.Escalator and laya.vllm_teacher, a teacher for what the learner is unsure of (0.5.2) by @NandhaKishorM in https://github.com/NandhaKishorM/laya/pull/1518
> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.5.1...v0.5.2

### [v0.5.1](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.1)
<sub>2026-11-21 · 2d ago</sub>

> **What's Changed**
> * Sponsor link at the top of the README and a Sponsor button by @NandhaKishorM in https://github.com/NandhaKishorM/laya/pull/1513
> * feat(rust): make ort download-binaries optional by @sathariels in https://github.com/NandhaKishorM/laya/pull/1508
> * fix(policy): require questions.json in manifest hashes and validate manifest/provenance shapes by @aoright in https://github.com/NandhaKishorM/laya/pull/1510
> * fix(serve): correct uvicorn log-level case sensitivity expectation in test by @Aniketchavan7 in https://github.com/NandhaKishorM/laya/pull/1515
> **New Contributors**
> …

### [v0.5.0](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.0)
<sub>2026-11-19 · 3d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.38...v0.5.0

### [v0.4.38](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.38)
<sub>2026-11-19 · 4d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.37...v0.4.38

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(java): re-record lang_tables.json after #1526's stopwords](https://github.com/NandhaKishorM/laya/commit/54c72865e4781233396a56c2db013e29ced3b43c) | NandhaKishorM |
| 2026-11-23 | [release: 0.5.3, choice labels come back as written on the new engine,…](https://github.com/NandhaKishorM/laya/commit/abefd7d955008a59287b0fa8c5753cb323307693) | NandhaKishorM |
| 2026-11-23 | [fix(rust): pin ort to exactly 2.0.0-rc.13 so a fresh resolve still co…](https://github.com/NandhaKishorM/laya/commit/da444d5107ef2e23d0240f75cc45d904d7408253) | NandhaKishorM |
| 2026-11-23 | [fix(rust,dotnet): carry #1526's Spanish, Portuguese and Italian stopw…](https://github.com/NandhaKishorM/laya/commit/60fdb8cd7814176990d3991b2c7da2d198de47d2) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1528 from dante01yoon: fix(ts): a null or blank p…](https://github.com/NandhaKishorM/laya/commit/33189272e55a854b174c9d2f2afdf15615cd31ea) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1526 from Rukafuu: fix(lang): add unaccented and …](https://github.com/NandhaKishorM/laya/commit/d82c4fc5f2e5a17e8806702b08ce33d476b55d84) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1525 from Rukafuu: fix(onnx-export): the cleanup …](https://github.com/NandhaKishorM/laya/commit/ac7cf2eb042251059a058e75ea76a98fafff1c9e) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1524 from chetanxrathore: fix(onnx): verify fused…](https://github.com/NandhaKishorM/laya/commit/29e0d3bffe5f33926f91814aacafd0ff3af020b2) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1519 from aashish254: fix(vega): translate engine…](https://github.com/NandhaKishorM/laya/commit/7675240f6ebf39efa1e29529cfc0539a54e8e841) | NandhaKishorM |
| 2026-11-23 | [Merge pull request #1523 from app/dependabot: build(deps-dev): bump v…](https://github.com/NandhaKishorM/laya/commit/e13a6b00d29ee278178de00bd27a1d27358d12ab) | NandhaKishorM |

[See all commits ↗](https://github.com/NandhaKishorM/laya/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NandhaKishorM/laya.git
```

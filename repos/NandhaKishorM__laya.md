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
| ⭐ **Stars** | 35.5k |
| 🍴 **Forks** | 3.2k |
| 🐞 **Open issues + PRs** | [97](https://github.com/NandhaKishorM/laya/issues) |
| 💻 **Languages** | Python 52% · Java 11% · Go 8% · Rust 7% · C# 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `calibration` `classification` `decision-model` `huggingface` `jev` `modernbert` `multilingual` `nlp` `python` `pytorch` `routing` `typed-decisions` `zero-shot` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-09-18 |
| 📦 **Latest release** | [v0.4.32](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.32) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.3 MB |
| 🌐 **Website** | https://huggingface.co/convaiinnovations/laya |

## 📦 Recent releases

### [v0.4.32](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.32)
<sub>2026-11-14 · today</sub>

> **What's Changed**
> * perf(calibrate): vectorize record validation, threshold selection, and binning fit by @HamidRezaLS in https://github.com/NandhaKishorM/laya/pull/1496
> * fix(hooks): drop a rename probe that renders the original question by @PerryLink in https://github.com/NandhaKishorM/laya/pull/1498
> * build(deps): bump ruff from 0.17.3 to 0.17.4 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1499
> * fix(integrations): gate LayaToolSelector on a per-bucket min_confidence map by @shuishui313 in https://github.com/NandhaKishorM/laya/pull/1494
> * test(batch): cover interleaved schemas, chunking, and length-sort order in Router.predict_batch by @goku54477 in https://github.com/NandhaKishorM/laya/pull/1495
> …

### [v0.4.31](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.31)
<sub>2026-11-10 · 4d ago</sub>

> **What's Changed**
> * feat(ts): expose local routing diagnostics by @xinpingzh in https://github.com/NandhaKishorM/laya/pull/1447
> * fix(vega): loading a heads-only calibration directory resets the calibration it does not hold by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1479
> * fix(vega): preserve cached prediction hook results by @GoldArowana in https://github.com/NandhaKishorM/laya/pull/1488
> * feat(langchain): honor native auto/review routing policy by @xinpingzh in https://github.com/NandhaKishorM/laya/pull/1489
> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.30...v0.4.31

### [v0.4.30](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.30)
<sub>2026-11-08 · 6d ago</sub>

> **What's Changed**
> * fix(vega): read a fit gold the way laya's fine-tune reads it by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1474
> * fix(vega): refuse an answer number that is not finite before it becomes a decision by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1475
> * fix(vega): refuse a malformed question by name, through laya's own question check by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1476
> * fix(vega): a gold keyed to no question id is refused, not dropped by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1477
> * fix(video): a duration the tool reports as N/A is 0.0, not a crash, in probe's banner fallback by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1478
> …

### [v0.4.29](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.29)
<sub>2026-11-08 · 7d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.28...v0.4.29

### [v0.4.28](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.28)
<sub>2026-11-07 · 7d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.27...v0.4.28

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [release: 0.4.32, calibration fits 2.4x faster, per-bucket maps in Lay…](https://github.com/NandhaKishorM/laya/commit/af8ada066685d66b3fc0b31e6c56b96def23fe2f) | NandhaKishorM |
| 2026-11-14 | [Merge PR #1499: build(deps): bump ruff from 0.17.3 to 0.17.4](https://github.com/NandhaKishorM/laya/commit/e26e681d4ad44f977f4c75f25c591338812ec939) | NandhaKishorM |
| 2026-11-14 | [Merge PR #1498: fix(hooks): drop a rename probe that renders the orig…](https://github.com/NandhaKishorM/laya/commit/13281d918cb1b114a8733f5e5814676a7fc24e5f) | NandhaKishorM |
| 2026-11-14 | [Merge PR #1496: perf(calibrate): vectorize record validation, thresho…](https://github.com/NandhaKishorM/laya/commit/cf41d5676a1222af28709e1ae297f8580bfc7f65) | NandhaKishorM |
| 2026-11-14 | [Merge PR #1495: test(batch): cover interleaved schemas, chunking, and…](https://github.com/NandhaKishorM/laya/commit/fb4f9045b1f758c0973aeb2462e448daf518e49a) | NandhaKishorM |
| 2026-11-14 | [Merge PR #1494: fix(integrations): gate LayaToolSelector on a per-buc…](https://github.com/NandhaKishorM/laya/commit/cb62575e0f4db1d68b554eea6a21a5d89bb5054c) | NandhaKishorM |
| 2026-11-14 | [build(deps): bump ruff from 0.17.3 to 0.17.4](https://github.com/NandhaKishorM/laya/commit/8acbc89b9a6a11b50d256ea083f845ae86558ad9) | dependabot[bot] |
| 2026-11-14 | [fix(hooks): drop a rename probe that renders the original question](https://github.com/NandhaKishorM/laya/commit/d8356d777616cdcca62a2be4fc15cf582b83d947) | PerryLink |
| 2026-11-12 | [perf(calibrate): vectorize record validation, threshold selection, an…](https://github.com/NandhaKishorM/laya/commit/a1b73e7b1e2970277469acc33dc6b002b6097323) | HamidRezaLS |
| 2026-11-12 | [test(batch): cover interleaved schemas, chunking, and length-sort ord…](https://github.com/NandhaKishorM/laya/commit/52481c8890f0dafecd17e7b658c7bb36b779232a) | goku54477 |

[See all commits ↗](https://github.com/NandhaKishorM/laya/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NandhaKishorM/laya.git
```

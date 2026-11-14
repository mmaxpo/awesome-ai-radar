# NandhaKishorM/laya

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/NandhaKishorM/laya)

> Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📁 Uncategorized |
| **Project** | — |
| **Why it's worth a look** | — |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 35.5k |
| 🍴 **Forks** | 3.2k |
| 🐞 **Open issues + PRs** | [103](https://github.com/NandhaKishorM/laya/issues) |
| 💻 **Languages** | Python 52% · Java 11% · Go 8% · Rust 7% · C# 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `calibration` `classification` `decision-model` `huggingface` `jev` `modernbert` `multilingual` `nlp` `python` `pytorch` `routing` `typed-decisions` `zero-shot` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-09-18 |
| 📦 **Latest release** | [v0.4.31](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.31) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.3 MB |
| 🌐 **Website** | https://huggingface.co/convaiinnovations/laya |

## 📦 Recent releases

### [v0.4.31](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.31)
<sub>2026-11-10 · 3d ago</sub>

> **What's Changed**
> * feat(ts): expose local routing diagnostics by @xinpingzh in https://github.com/NandhaKishorM/laya/pull/1447
> * fix(vega): loading a heads-only calibration directory resets the calibration it does not hold by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1479
> * fix(vega): preserve cached prediction hook results by @GoldArowana in https://github.com/NandhaKishorM/laya/pull/1488
> * feat(langchain): honor native auto/review routing policy by @xinpingzh in https://github.com/NandhaKishorM/laya/pull/1489
> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.30...v0.4.31

### [v0.4.30](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.30)
<sub>2026-11-08 · 5d ago</sub>

> **What's Changed**
> * fix(vega): read a fit gold the way laya's fine-tune reads it by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1474
> * fix(vega): refuse an answer number that is not finite before it becomes a decision by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1475
> * fix(vega): refuse a malformed question by name, through laya's own question check by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1476
> * fix(vega): a gold keyed to no question id is refused, not dropped by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1477
> * fix(video): a duration the tool reports as N/A is 0.0, not a crash, in probe's banner fallback by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1478
> …

### [v0.4.29](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.29)
<sub>2026-11-08 · 6d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.28...v0.4.29

### [v0.4.28](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.28)
<sub>2026-11-07 · 7d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.27...v0.4.28

### [v0.4.27](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.27)
<sub>2026-11-06 · 8d ago</sub>

> **What's Changed**
> * fix(ts): read each leaf line in leafNonEnglish by @sathariels in https://github.com/NandhaKishorM/laya/pull/1450
> * fix(onnx): default the opset to the ceiling the installed torch implements by @thread3d in https://github.com/NandhaKishorM/laya/pull/1451
> * fix(laya-ts): read maxLoaded as int() does, so an unreadable cap cannot disable eviction by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1457
> * fix(batch): refuse a batch_size the chunker cannot spend by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1458
> * fix(ts): bound the Router's own hooks with hooksTimeout, as Python does by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1459
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-10 | [release: 0.4.31, LangChain follows vega's route, cached answers throu…](https://github.com/NandhaKishorM/laya/commit/3a38cbe83f6ef556f3125fb0065fdc5a55d05792) | NandhaKishorM |
| 2026-11-10 | [Merge PR #1489: feat(langchain): honor native auto/review routing policy](https://github.com/NandhaKishorM/laya/commit/b0ebedf2229317e12e6493adb133f4b98857df84) | NandhaKishorM |
| 2026-11-10 | [Merge PR #1488: fix(vega): preserve cached prediction hook results](https://github.com/NandhaKishorM/laya/commit/931f7a4758dea996ea8d9370870ae6842e4545d8) | NandhaKishorM |
| 2026-11-10 | [Merge PR #1479: fix(vega): loading a heads-only calibration directory…](https://github.com/NandhaKishorM/laya/commit/c42851754d3d49840f91a5799f60ab30a90b372d) | NandhaKishorM |
| 2026-11-10 | [Merge PR #1447: feat(ts): expose local routing diagnostics](https://github.com/NandhaKishorM/laya/commit/9342ce66a739192c587485e67ab0625672a8bba8) | NandhaKishorM |
| 2026-11-09 | [test(langchain): verify native routing in async calls and graphs](https://github.com/NandhaKishorM/laya/commit/4cdd8386f4a5020befc1bf1d45375b9a1812f17f) | xinpingzh |
| 2026-11-09 | [feat(langchain): add opt-in native routing policy](https://github.com/NandhaKishorM/laya/commit/6ad7166c52659103bd0b9ecedf93ceab56460e89) | xinpingzh |
| 2026-11-09 | [docs(readme): cite the preprint at the top (From Laya to Vega, doi 10…](https://github.com/NandhaKishorM/laya/commit/b8a0f0991d95a953411f2e16f91bddc2ffdaf79a) | NandhaKishorM |
| 2026-11-09 | [test(ts): verify packaged diagnostics and document sources](https://github.com/NandhaKishorM/laya/commit/638169e0d8f1c14bf3830103a0938525e92ed13d) | xinpingzh |
| 2026-11-09 | [feat(router): expose TypeScript routing diagnostics](https://github.com/NandhaKishorM/laya/commit/419f07ac7d8adf768935dfb63ab6d68ea7b0305f) | xinpingzh |

[See all commits ↗](https://github.com/NandhaKishorM/laya/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NandhaKishorM/laya.git
```

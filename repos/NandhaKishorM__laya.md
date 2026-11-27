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
| ⭐ **Stars** | 36.0k |
| 🍴 **Forks** | 3.2k |
| 🐞 **Open issues + PRs** | [104](https://github.com/NandhaKishorM/laya/issues) |
| 💻 **Languages** | Python 52% · Java 11% · Go 8% · Rust 7% · C# 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `calibration` `classification` `decision-model` `huggingface` `jev` `modernbert` `multilingual` `nlp` `python` `pytorch` `routing` `typed-decisions` `zero-shot` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-09-18 |
| 📦 **Latest release** | [v0.5.6](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.6) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.3 MB |
| 🌐 **Website** | https://huggingface.co/convaiinnovations/laya |

## 📦 Recent releases

### [v0.5.6](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.6)
<sub>2026-11-27 · today</sub>

> **What's Changed**
> * fix(ts): resolve local $defs refs so pydantic Enum fields become choices, as Python does by @dante01yoon in https://github.com/NandhaKishorM/laya/pull/1531
> * fix(ts): refuse a ctx.skip() whose result count breaks the contract, as Python does by @dante01yoon in https://github.com/NandhaKishorM/laya/pull/1532
> * fix(ts): Router.unload fires onEvict for the checkpoints it frees, as Python does by @dante01yoon in https://github.com/NandhaKishorM/laya/pull/1533
> * fix(ts): accept a list of onPredictStart/onPredictEnd callables, as Python does by @dante01yoon in https://github.com/NandhaKishorM/laya/pull/1534
> * research: vega accuracy against evidence position at fixed document length by @Parswanadh in https://github.com/NandhaKishorM/laya/pull/1538
> …

### [v0.5.5](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.5)
<sub>2026-11-26 · yesterday</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.5.4...v0.5.5

### [v0.5.4](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.4)
<sub>2026-11-25 · 2d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.5.3...v0.5.4

### [v0.5.3](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.3)
<sub>2026-11-23 · 4d ago</sub>

> **What's Changed**
> * fix(vega): translate engine's string-keyed choice labels back to caller's labels by @aashish254 in https://github.com/NandhaKishorM/laya/pull/1519
> * build(deps): bump actions/setup-java from 6.2.0 to 6.3.0 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1520
> * build(deps): bump actions/setup-go from 7.0.0 to 7.1.0 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1521
> * build(deps): bump ruff from 0.17.4 to 0.17.5 by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1522
> * build(deps-dev): bump vitest from 5.1.0 to 5.1.1 in /laya-ts by @dependabot[bot] in https://github.com/NandhaKishorM/laya/pull/1523
> …

### [v0.5.2](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.2)
<sub>2026-11-21 · 5d ago</sub>

> **What's Changed**
> * learn: laya.Escalator and laya.vllm_teacher, a teacher for what the learner is unsure of (0.5.2) by @NandhaKishorM in https://github.com/NandhaKishorM/laya/pull/1518
> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.5.1...v0.5.2

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [release: 0.5.6](https://github.com/NandhaKishorM/laya/commit/309f865eb2373ffaf1b9e375f30496841492d7b0) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1538 from Parswanadh: research: vega accuracy aga…](https://github.com/NandhaKishorM/laya/commit/e4d81b0c077fd55b72e5644936ccbead3b65c655) | NandhaKishorM |
| 2026-11-27 | [cpp: link libonnxruntime.1.dylib in the NuGet runtime on macOS](https://github.com/NandhaKishorM/laya/commit/5b9114c3f18d968b898ec669434a1f34992b5233) | NandhaKishorM |
| 2026-11-27 | [README: the "How it decides" animation back above the install command](https://github.com/NandhaKishorM/laya/commit/ea37beaaeee8f760d491a6ed45103bfeba66c244) | NandhaKishorM |
| 2026-11-27 | [serve: read LAYA_API_KEY as os.environ.get(..., "") in the open-bind …](https://github.com/NandhaKishorM/laya/commit/7958884c9468d7d1983e1e471bfb9e419898b63c) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1541 from yeager: fix(cpp): fetch ONNX Runtime fr…](https://github.com/NandhaKishorM/laya/commit/c7e1aba54110b3f5e197d502957b74a31893b684) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1539 from chetanxrathore: fix(rust): support call…](https://github.com/NandhaKishorM/laya/commit/0c7e42ebd59d32b303609eb7cd5ef9cec21207da) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1540 from leninworld: fix(ts): withHooks removes …](https://github.com/NandhaKishorM/laya/commit/c1c9e39a134e8eb78bb29080cd4b959b00d48597) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1534 from dante01yoon: fix(ts): accept a list of …](https://github.com/NandhaKishorM/laya/commit/8c2ebb03571ade6fc2c754634d7e7931ee292a4c) | NandhaKishorM |
| 2026-11-27 | [Merge pull request #1533 from dante01yoon: fix(ts): Router.unload fir…](https://github.com/NandhaKishorM/laya/commit/d1f9ea9d3a2720020fae850ca89785ad8c3ba0ae) | NandhaKishorM |

[See all commits ↗](https://github.com/NandhaKishorM/laya/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NandhaKishorM/laya.git
```

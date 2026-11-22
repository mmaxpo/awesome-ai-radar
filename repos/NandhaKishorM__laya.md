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
| 🐞 **Open issues + PRs** | [103](https://github.com/NandhaKishorM/laya/issues) |
| 💻 **Languages** | Python 52% · Java 11% · Go 8% · Rust 7% · C# 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `calibration` `classification` `decision-model` `huggingface` `jev` `modernbert` `multilingual` `nlp` `python` `pytorch` `routing` `typed-decisions` `zero-shot` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-09-18 |
| 📦 **Latest release** | [v0.5.2](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.2) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.2 MB |
| 🌐 **Website** | https://huggingface.co/convaiinnovations/laya |

## 📦 Recent releases

### [v0.5.2](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.2)
<sub>2026-11-21 · today</sub>

> **What's Changed**
> * learn: laya.Escalator and laya.vllm_teacher, a teacher for what the learner is unsure of (0.5.2) by @NandhaKishorM in https://github.com/NandhaKishorM/laya/pull/1518
> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.5.1...v0.5.2

### [v0.5.1](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.1)
<sub>2026-11-21 · yesterday</sub>

> **What's Changed**
> * Sponsor link at the top of the README and a Sponsor button by @NandhaKishorM in https://github.com/NandhaKishorM/laya/pull/1513
> * feat(rust): make ort download-binaries optional by @sathariels in https://github.com/NandhaKishorM/laya/pull/1508
> * fix(policy): require questions.json in manifest hashes and validate manifest/provenance shapes by @aoright in https://github.com/NandhaKishorM/laya/pull/1510
> * fix(serve): correct uvicorn log-level case sensitivity expectation in test by @Aniketchavan7 in https://github.com/NandhaKishorM/laya/pull/1515
> **New Contributors**
> …

### [v0.5.0](https://github.com/NandhaKishorM/laya/releases/tag/v0.5.0)
<sub>2026-11-19 · 2d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.38...v0.5.0

### [v0.4.38](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.38)
<sub>2026-11-19 · 3d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.37...v0.4.38

### [v0.4.37](https://github.com/NandhaKishorM/laya/releases/tag/v0.4.37)
<sub>2026-11-18 · 3d ago</sub>

> **Full Changelog**: https://github.com/NandhaKishorM/laya/compare/v0.4.36...v0.4.37

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [release: 0.5.2, laya.vllm_teacher (a teacher you run yourself) and la…](https://github.com/NandhaKishorM/laya/commit/e150aa92a0d4059ac621875b39b620847cf1b88a) | NandhaKishorM |
| 2026-11-21 | [docs: the teacher line is measured, as in vegaml 0.18](https://github.com/NandhaKishorM/laya/commit/b5ed2fdc91a2233eef79c757554dafeb720b69b3) | NandhaKishorM |
| 2026-11-21 | [learn: laya.Escalator, a teacher for what the learner is unsure of](https://github.com/NandhaKishorM/laya/commit/7e5279fecc1a2d7e28acfd557fc78d168f25ad8e) | NandhaKishorM |
| 2026-11-21 | [test(policy): nest the JSON deep enough to raise RecursionError on ev…](https://github.com/NandhaKishorM/laya/commit/19ccbf2fff0024f1dda11da735881be044bacc0a) | NandhaKishorM |
| 2026-11-21 | [release: 0.5.1, questions.json must be in a policy's manifest, laya-o…](https://github.com/NandhaKishorM/laya/commit/090c540ec4cd0e5c71d539d952f0250e97399fcb) | NandhaKishorM |
| 2026-11-21 | [test(serve): the uppercase log-level witness follows the installed uv…](https://github.com/NandhaKishorM/laya/commit/411e6a31afa8cd28febd05bb429eabb2cc41bc0b) | NandhaKishorM |
| 2026-11-21 | [Merge pull request #1515 from Aniketchavan7: fix(serve): correct uvic…](https://github.com/NandhaKishorM/laya/commit/05948e3747209c8c826f9538c1d3c46af77fdf88) | NandhaKishorM |
| 2026-11-21 | [Merge pull request #1510 from aoright: fix(policy): require questions…](https://github.com/NandhaKishorM/laya/commit/66632aef4b3a40aeb5042038fe96bc418b7d7ab2) | NandhaKishorM |
| 2026-11-21 | [Merge pull request #1508 from sathariels: feat(rust): make ort downlo…](https://github.com/NandhaKishorM/laya/commit/1bf3003bf8a105b1a0aae585958ac7022bc3deb5) | NandhaKishorM |
| 2026-11-20 | [fix(serve): correct uvicorn log-level case sensitivity expectation in…](https://github.com/NandhaKishorM/laya/commit/ec54c20c80daa0f156ed066c2260fa32c2667150) | Aniketchavan7 |

[See all commits ↗](https://github.com/NandhaKishorM/laya/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NandhaKishorM/laya.git
```

# ranxianglei/billion-context

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ranxianglei/billion-context)

> A context-compression plugin for month-long single sessions (billions of tokens)  and small context windows (a 100K context is enough), billion-context is all you need .

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Context-compression plugin for long coding-agent sessions |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 8.3k |
| 🍴 **Forks** | 673 |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/ranxianglei/billion-context/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-08-06 |
| 📦 **Latest release** | [v0.1.216](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.216) — 2026-11-17 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 92.2 MB |

## 📦 Recent releases

### [v0.1.216](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.216)
<sub>2026-11-17 · 7d ago</sub>

> **What's Changed**
> * [PR] gate: two fixes — evidence file is now readable after the run completes + one retry added for the small-window round in  | gate 两个修复:跑完后证据文件能读了 + R 车道小窗口轮次加一次重试 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6808
> * [PR] Gate performance overhaul: P/R lanes parallelized, wall clock 45 min → ~18 min | gate 性能改造:P/R 车道并行,墙钟 45min→~18min by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6810
> * [PR] chore(branch): land 20 single-purpose fixes as one history-preserving batch (wave 10) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6765
> * [PR] fix: pass Claude Code's MCP config as --mcp-config=<file> so it cannot eat the prompt by @MohammadErfan-Jabbari in https://github.com/ranxianglei/billion-context/pull/6524
> * [PR] fix: retry context overflow with measured output headroom by @zouzh22 in https://github.com/ranxianglei/billion-context/pull/6529
> …

### [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215)
<sub>2026-11-15 · 9d ago</sub>

> **What's Changed**
> * [PR] gate: fix upstream recorder leak causing real model gate deadlock (pipe inheritance) | gate: 修上游 recorder 泄漏导致真模型门禁卡死（管道继承） by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6671
> * [PR] chore(branch): land 40 single-purpose fixes as one history-preserving batch (wave 5) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6677
> * [PR] fix: map search evidence offsets back to original Unicode text by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6494
> * [PR] fix: interpret cache-diff byte offsets in original text coordinates by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6496
> * [PR] fix: preserve null response bodies in the inline HTTP engine by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6502
> …

### [v0.1.214](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.214)
<sub>2026-11-14 · 10d ago</sub>

> **What's Changed**
> * [PR] docs: clarify that top-level modelContextLimit / ACP_MODEL_CONTEXT_LIMIT are a last-resort window fallback (#5908) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5909
> * [PR] docs: How-it-works SVG diagrams (en/zh) replacing the ASCII box by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5916
> * [PR] Review follow-ups: 429 throttle saturation/scope guardrails, media-refs carry-forward filter, oversize-refusal messages that say what to do, doc typo by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5905
> * [PR] docs: Minor Documentation Fixes, Part 4 — 6 pure documentation/disclosure fixes bundled for review | docs: 文档小修合集第四辑 —— 6 件纯文档/披露类小修合并送审 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5918
> * [PR] fix(dsh): dsh lane minor fixes batch #5 — activation & other tool registration + liveness log wording | fix(dsh): dsh 车道小修合集第五辑 —— 激活等工具注册 + 存活日志措辞 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5921
> …

### [v0.1.213](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.213)
<sub>2026-11-07 · 16d ago</sub>

> **What's Changed**
> * [PR] fix: revert self-contradictory inclusive billing stamp to split (#5515) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5518
> * [PR] docs(website): add blog post 'What to Do When the Model Keeps Treating Old Compressed Content as New User Instructions?' | docs(website): add blog post '模型总是把压缩老内容当成用户新指令咋办?' (EN+ZH) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5549
> * [PR] fix: read Responses additional_tools preamble in tool reachability observation by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5528
> * [PR] fix: replay unsigned thinking when the upstream does not sign it (#5495) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5496
> * [PR] fix(copy): false-advertising sweep of ACP tool surfaces (host-side) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5556
> …

### [v0.1.212](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.212)
<sub>2026-11-02 · 22d ago</sub>

> **What's Changed**
> * [PR] (ai: anthropic/claude-opus-4-6) fix(release): nuclear box = deps download + build + publish, zero checks; add local zero-install publish script by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5436
> * [PR] Manually remove the fucking AI restrictions | 手动取消傻逼ai限制 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5444
> * [PR] Restore the old CI release manual. | 恢复老的ci release manal by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5446
> * [PR] Restore the emergency channel (raw_publish/skip_ci_gate) + fix the four feature regressions introduced by this revert (A | 恢复紧急通道(raw_publish/skip_ci_gate)+修掉这次回退带回来的四处功能损失(A–E) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5447
> * [PR] fix(release): land the raw-publish bump as a commit before tagging/syncing (empty sync PR 422 + stale-version tag) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5457
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Merge pull request #7659 from ranxianglei/2026-11-24_eg-ga-docs-wrapup](https://github.com/ranxianglei/billion-context/commit/256df56f15348e6597a1347b07a36e4e19ff862d) | ranxianglei |
| 2026-11-24 | [fix(egress diagrams): pointer arrow was a self-loop; remove double ar…](https://github.com/ranxianglei/billion-context/commit/3aee42c3fabda496a88fd121023cac6d2a53660d) | ranxianglei |
| 2026-11-24 | [fix(egress diagrams): the six new arrows had no arrowheads (review m0…](https://github.com/ranxianglei/billion-context/commit/d4ff7ee8a1d53cd23c47e3bfe6d8727a5828a3da) | ranxianglei |
| 2026-11-24 | [regenerate config docs from the rebased seed (egressPlane back to 0 o…](https://github.com/ranxianglei/billion-context/commit/5911beb31392eb81a135b6ff90ca521ae0e1bb99) | ranxianglei |
| 2026-11-24 | [revert: egressPlane config-docs seed back to 0 (off) — the GA flip wa…](https://github.com/ranxianglei/billion-context/commit/c1531f5f0913d154b08f42ea552c3da3ec38fcfd) | ranxianglei |
| 2026-11-24 | [revert: egressPlane default stays 0 (owner ruling) — the PR is docs-o…](https://github.com/ranxianglei/billion-context/commit/21adc8eab4c7fab981b32c5b0bea90268b72dc10) | ranxianglei |
| 2026-11-24 | [test: scope 3 egress-fork/lane suites to egressPlane off after the GA…](https://github.com/ranxianglei/billion-context/commit/b1a3d2cbebb6a690df3eb30fd25ee4fc0b25e631) | ci-check |
| 2026-11-24 | [test: scope 6 legacy-path suites to egressPlane off after the GA defa…](https://github.com/ranxianglei/billion-context/commit/a7fda78087078f73c5ed8426234eb91919f88cb2) | ci-check |
| 2026-11-24 | [fix(docs): sync egressPlane GA wording into the config-docs seed](https://github.com/ranxianglei/billion-context/commit/68a0131a7f5e0685230517572d915e18a2806be7) | ci-check |
| 2026-11-24 | [docs(egress): full doc wrap-up per owner review — dedicated egress-pl…](https://github.com/ranxianglei/billion-context/commit/689cb8d8ef304ce86247c9f80590c3e4124717ac) | ranxianglei |

[See all commits ↗](https://github.com/ranxianglei/billion-context/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ranxianglei/billion-context.git
```

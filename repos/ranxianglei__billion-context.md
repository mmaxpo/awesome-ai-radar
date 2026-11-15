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
| ⭐ **Stars** | 7.5k |
| 🍴 **Forks** | 615 |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/ranxianglei/billion-context/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-08-06 |
| 📦 **Latest release** | [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215) — 2026-11-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 80.5 MB |

## 📦 Recent releases

### [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215)
<sub>2026-11-15 · today</sub>

> **What's Changed**
> * [PR] gate: fix upstream recorder leak causing real model gate deadlock (pipe inheritance) | gate: 修上游 recorder 泄漏导致真模型门禁卡死（管道继承） by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6671
> * [PR] chore(branch): land 40 single-purpose fixes as one history-preserving batch (wave 5) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6677
> * [PR] fix: map search evidence offsets back to original Unicode text by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6494
> * [PR] fix: interpret cache-diff byte offsets in original text coordinates by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6496
> * [PR] fix: preserve null response bodies in the inline HTTP engine by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6502
> …

### [v0.1.214](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.214)
<sub>2026-11-14 · yesterday</sub>

> **What's Changed**
> * [PR] docs: clarify that top-level modelContextLimit / ACP_MODEL_CONTEXT_LIMIT are a last-resort window fallback (#5908) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5909
> * [PR] docs: How-it-works SVG diagrams (en/zh) replacing the ASCII box by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5916
> * [PR] Review follow-ups: 429 throttle saturation/scope guardrails, media-refs carry-forward filter, oversize-refusal messages that say what to do, doc typo by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5905
> * [PR] docs: Minor Documentation Fixes, Part 4 — 6 pure documentation/disclosure fixes bundled for review | docs: 文档小修合集第四辑 —— 6 件纯文档/披露类小修合并送审 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5918
> * [PR] fix(dsh): dsh lane minor fixes batch #5 — activation & other tool registration + liveness log wording | fix(dsh): dsh 车道小修合集第五辑 —— 激活等工具注册 + 存活日志措辞 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5921
> …

### [v0.1.213](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.213)
<sub>2026-11-07 · 7d ago</sub>

> **What's Changed**
> * [PR] fix: revert self-contradictory inclusive billing stamp to split (#5515) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5518
> * [PR] docs(website): add blog post 'What to Do When the Model Keeps Treating Old Compressed Content as New User Instructions?' | docs(website): add blog post '模型总是把压缩老内容当成用户新指令咋办?' (EN+ZH) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5549
> * [PR] fix: read Responses additional_tools preamble in tool reachability observation by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5528
> * [PR] fix: replay unsigned thinking when the upstream does not sign it (#5495) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5496
> * [PR] fix(copy): false-advertising sweep of ACP tool surfaces (host-side) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5556
> …

### [v0.1.212](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.212)
<sub>2026-11-02 · 12d ago</sub>

> **What's Changed**
> * [PR] (ai: anthropic/claude-opus-4-6) fix(release): nuclear box = deps download + build + publish, zero checks; add local zero-install publish script by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5436
> * [PR] Manually remove the fucking AI restrictions | 手动取消傻逼ai限制 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5444
> * [PR] Restore the old CI release manual. | 恢复老的ci release manal by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5446
> * [PR] Restore the emergency channel (raw_publish/skip_ci_gate) + fix the four feature regressions introduced by this revert (A | 恢复紧急通道(raw_publish/skip_ci_gate)+修掉这次回退带回来的四处功能损失(A–E) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5447
> * [PR] fix(release): land the raw-publish bump as a commit before tagging/syncing (empty sync PR 422 + stale-version tag) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5457
> …

### [v0.1.211](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.211)
<sub>2026-11-01 · 14d ago</sub>

> **What's Changed**
> * [PR] test(e2e): fork-adoption relay echoes plain text, not rendered ref tags — unblocks v0.1.210 release by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5377
> * [PR] docs: New blog post — What to do when billion-context is frequently compressed? | docs: 新博客文章——billion-context频繁压缩该怎么办? by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5389
> * [PR] fix: frozen compression state becomes visible, diagnosable, and healable (#5408) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5409
> * [PR] Session compression reminders no longer starve under frequent interruptions: absorption debt is paid in steps starting f | 中断频繁的会话压缩提醒不再饿死:吸收欠账从第 2 次中断起付台阶(#5415) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5416
> * [PR] fix(storage): async ingest twin sweeps foreign rows while drift-latched (#5412) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5420
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Merge pull request #6824 from ranxianglei/ranxianglei-patch-4](https://github.com/ranxianglei/billion-context/commit/2e3cfc973b8620b1f7bc8a415ddcbd31e7f4aaee) | ranxianglei |
| 2026-11-15 | [Improve cache health metrics in README.ja.md](https://github.com/ranxianglei/billion-context/commit/11b5fbeb28a56ffccd0c45cfcb64f9175018da9c) | ranxianglei |
| 2026-11-15 | [Update cache health overview statistics in README](https://github.com/ranxianglei/billion-context/commit/dbc81ce6225e4f550ccde951f953da9f87bdf814) | ranxianglei |
| 2026-11-15 | [Update cache health statistics in README](https://github.com/ranxianglei/billion-context/commit/3c4acf66834cb08bc969b082d1843faca3bdb923) | ranxianglei |
| 2026-11-15 | [Merge pull request #6765 from ranxianglei/batch10-wave10](https://github.com/ranxianglei/billion-context/commit/912aa67292055fb0fda342c3559cd55385701d12) | ranxianglei |
| 2026-11-15 | [Merge pull request #6810 from ranxianglei/2026-11-15_gate-concurrent](https://github.com/ranxianglei/billion-context/commit/3e42aae8bfa6d2f3bf48d376eaaaac27afbcf806) | ranxianglei |
| 2026-11-15 | [fix(gate): default restart-lane agents to dsh,pi in the launcher](https://github.com/ranxianglei/billion-context/commit/2c6c51ef38caa51fe3ce9f574c3a8128faf1c21a) | ework-agent |
| 2026-11-15 | [fix(gate): pass concurrency knobs through bili-gate.sh + document them](https://github.com/ranxianglei/billion-context/commit/db25b227377f864e0388ba90cfd3b372e736c89c) | ci-check |
| 2026-11-15 | [perf(gate): run plugin (P) + restart (R) lanes concurrently](https://github.com/ranxianglei/billion-context/commit/57e75a9b9402b9a7b730adf41cf31b91f27405c9) | ework-agent |
| 2026-11-15 | [Merge pull request #6808 from ranxianglei/2026-11-15_gate-evidence-uid](https://github.com/ranxianglei/billion-context/commit/26d9bcc649a801ff99f31847d51cbad17893d496) | ranxianglei |

[See all commits ↗](https://github.com/ranxianglei/billion-context/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ranxianglei/billion-context.git
```

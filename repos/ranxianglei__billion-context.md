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
| ⭐ **Stars** | 7.7k |
| 🍴 **Forks** | 627 |
| 🐞 **Open issues + PRs** | [1.2k](https://github.com/ranxianglei/billion-context/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-08-06 |
| 📦 **Latest release** | [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215) — 2026-11-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 84.1 MB |

## 📦 Recent releases

### [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215)
<sub>2026-11-15 · yesterday</sub>

> **What's Changed**
> * [PR] gate: fix upstream recorder leak causing real model gate deadlock (pipe inheritance) | gate: 修上游 recorder 泄漏导致真模型门禁卡死（管道继承） by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6671
> * [PR] chore(branch): land 40 single-purpose fixes as one history-preserving batch (wave 5) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6677
> * [PR] fix: map search evidence offsets back to original Unicode text by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6494
> * [PR] fix: interpret cache-diff byte offsets in original text coordinates by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6496
> * [PR] fix: preserve null response bodies in the inline HTTP engine by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6502
> …

### [v0.1.214](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.214)
<sub>2026-11-14 · 2d ago</sub>

> **What's Changed**
> * [PR] docs: clarify that top-level modelContextLimit / ACP_MODEL_CONTEXT_LIMIT are a last-resort window fallback (#5908) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5909
> * [PR] docs: How-it-works SVG diagrams (en/zh) replacing the ASCII box by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5916
> * [PR] Review follow-ups: 429 throttle saturation/scope guardrails, media-refs carry-forward filter, oversize-refusal messages that say what to do, doc typo by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5905
> * [PR] docs: Minor Documentation Fixes, Part 4 — 6 pure documentation/disclosure fixes bundled for review | docs: 文档小修合集第四辑 —— 6 件纯文档/披露类小修合并送审 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5918
> * [PR] fix(dsh): dsh lane minor fixes batch #5 — activation & other tool registration + liveness log wording | fix(dsh): dsh 车道小修合集第五辑 —— 激活等工具注册 + 存活日志措辞 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5921
> …

### [v0.1.213](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.213)
<sub>2026-11-07 · 8d ago</sub>

> **What's Changed**
> * [PR] fix: revert self-contradictory inclusive billing stamp to split (#5515) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5518
> * [PR] docs(website): add blog post 'What to Do When the Model Keeps Treating Old Compressed Content as New User Instructions?' | docs(website): add blog post '模型总是把压缩老内容当成用户新指令咋办?' (EN+ZH) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5549
> * [PR] fix: read Responses additional_tools preamble in tool reachability observation by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5528
> * [PR] fix: replay unsigned thinking when the upstream does not sign it (#5495) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5496
> * [PR] fix(copy): false-advertising sweep of ACP tool surfaces (host-side) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5556
> …

### [v0.1.212](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.212)
<sub>2026-11-02 · 13d ago</sub>

> **What's Changed**
> * [PR] (ai: anthropic/claude-opus-4-6) fix(release): nuclear box = deps download + build + publish, zero checks; add local zero-install publish script by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5436
> * [PR] Manually remove the fucking AI restrictions | 手动取消傻逼ai限制 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5444
> * [PR] Restore the old CI release manual. | 恢复老的ci release manal by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5446
> * [PR] Restore the emergency channel (raw_publish/skip_ci_gate) + fix the four feature regressions introduced by this revert (A | 恢复紧急通道(raw_publish/skip_ci_gate)+修掉这次回退带回来的四处功能损失(A–E) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5447
> * [PR] fix(release): land the raw-publish bump as a commit before tagging/syncing (empty sync PR 422 + stale-version tag) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5457
> …

### [v0.1.211](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.211)
<sub>2026-11-01 · 15d ago</sub>

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
| 2026-11-16 | [Merge pull request #6151 from ranxianglei/nudge-debug-pi](https://github.com/ranxianglei/billion-context/commit/301e1a5459a77d5578206927c8062a58381af642) | ranxianglei |
| 2026-11-16 | [Merge pull request #6944 from ranxianglei/fix/responses-section-helper](https://github.com/ranxianglei/billion-context/commit/4a24c2635e478cfbaa54e73966552f1713a55345) | ranxianglei |
| 2026-11-16 | [fix(responses): shared developer-section joiner kills the round-2 pre…](https://github.com/ranxianglei/billion-context/commit/1494b551500d107c9b5c4e896ff573bda3030930) | ranxianglei |
| 2026-11-16 | [Merge pull request #6745 from ranxianglei/2026-11-14_recovery-visibility](https://github.com/ranxianglei/billion-context/commit/0821a8154428a7593e61e22af06160db78bfb19b) | ranxianglei |
| 2026-11-16 | [Merge pull request #6913 from ranxianglei/2026-11-16_gate-render-knobs](https://github.com/ranxianglei/billion-context/commit/642000e7a3f3124628ddf1a3d80c4b6d76f8ef1e) | ranxianglei |
| 2026-11-16 | [Merge pull request #6929 from ranxianglei/2026-11-16_remove-4521-stat…](https://github.com/ranxianglei/billion-context/commit/662f4b060290ac15c11160f0f876dc991c6589f2) | ranxianglei |
| 2026-11-16 | [fix(gate): t1 prompt quoted the corpus line count dynamically](https://github.com/ranxianglei/billion-context/commit/aa9249411516b569c536640b8477bbb3947c035f) | ework-agent |
| 2026-11-16 | [Merge remote-tracking branch 'origin/ci-fixes' into 2026-11-16_gate-r…](https://github.com/ranxianglei/billion-context/commit/9ed43c2b39fa6dd71e5bb3614c0902ae488d123a) | ci-check |
| 2026-11-16 | [kernel+host: remove the #4521 armed-but-silent '[ACP status: …]' refr…](https://github.com/ranxianglei/billion-context/commit/4ccccab15f722f505c43d977be69095740f08c5a) | ranxianglei |
| 2026-11-16 | [Merge pull request #6883 from ranxianglei/design/6880-dsh-purpose-signal](https://github.com/ranxianglei/billion-context/commit/d1ff6eaab38ea2358f12dac5128550b205edd385) | ranxianglei |

[See all commits ↗](https://github.com/ranxianglei/billion-context/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ranxianglei/billion-context.git
```

# snownico0722/PaperTodo

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/snownico0722/PaperTodo)

> A minimalist Windows desktop sticky note tool. It puts a few quiet, usable, and unobtrusive sheets of paper on your desktop. Native WPF, with support for to-dos and Markdown.——极简 Windows 桌面便签工具。让桌面上有几张安静、可用、不会打扰人的纸。WPF 原生，支持待办与 Markdown。

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Edge-collapsing sticky notes for Windows |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 2.8k |
| 🍴 **Forks** | 146 |
| 🐞 **Open issues + PRs** | [30](https://github.com/snownico0722/PaperTodo/issues) |
| 💻 **Languages** | C# 92% · C 6% · JavaScript 1% · HTML 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `avalonedit` `csharp` `markdown` `minimalist` `notes` `todo` `windows` `wpf` `desktop` `note-taking` `productivity` `sticky-notes` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2026-05-27 |
| 📦 **Latest release** | [v3.40](https://github.com/snownico0722/PaperTodo/releases/tag/v3.40) — 2026-10-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 103.3 MB |

## 📦 Recent releases

### [v3.40](https://github.com/snownico0722/PaperTodo/releases/tag/v3.40) — PaperTodo v3.40
<sub>2026-10-20 · 25d ago</sub>

> **纸片与胶囊**
> - **快捷关闭纸片**：展开的纸片支持 Ctrl+W 或标题栏中键关闭。
> - **「主胶囊缩短」选项**：高级设置新增该选项（默认关闭），开启后主胶囊仅显示展开/收起箭头并缩窄宽度。
> - 开启“再次点击收回”后，关联待办的纸片也可通过再次点击关联的图标再次点击隐藏。
> - 关闭普通胶囊、贴边胶囊或主胶囊后，仍保留各队列已调好的高度，仅在恢复默认设置时重置。
> - 从胶囊展开纸片时先激活窗口；若展开途中切到其他程序，动画结束不再抢回焦点，原最大化纸片会在下次激活时恢复。
> …

### [v4.0.0-beta1](https://github.com/snownico0722/PaperTodo/releases/tag/v4.0.0-beta1) — PaperTodo v4.0.0-beta1 _(pre-release)_
<sub>2026-09-15 · 1mo ago</sub>

> 这是一个测试版，可能存在很多问题、bug。
> This is a beta version; it may contain many issues and bugs.
> <details>
> <summary>简体中文更新日志</summary>
> **边缘预览与胶囊**
> - **边缘实时预览**：鼠标悬停在边缘胶囊即可浏览和操作内容，无需打开完整纸片即可即时浏览内容。
> …

### [v3.31](https://github.com/snownico0722/PaperTodo/releases/tag/v3.31) — PaperTodo v3.31
<sub>2026-08-30 · 2mo ago</sub>

> <details>
> <summary>简体中文更新日志</summary>
> **bug修复和优化**
> - **修复快捷键页恢复默认设置**：点击“恢复本页默认”后，“区分小键盘数字键”会正确恢复为默认关闭，主键盘数字与小键盘数字继续混合响应。
> - **修复 Markdown 标题内行内样式字形**：标题中的斜体、删除线和下划线会保留标题原有的粗体与自定义粗体字形，不再只保留标题字号。
> - **高级设置视觉区分**：开启高级设置后，高级选项会以轻微染色背景与边框分组显示，更容易与常用设置区分。
> …

### [v3.3](https://github.com/snownico0722/PaperTodo/releases/tag/v3.3) — PaperTodo v3.3
<sub>2026-08-23 · 2mo ago</sub>

> <details>
> <summary>简体中文更新日志</summary>
> **待办与快启**
> - **文件/文件夹快启**：待办项支持直接拖入本地文件或文件夹作为快启路径，可直接打开、打开所在位置或解除关联，路径失效时会有明显提示；快启路径与纸片关联互斥。
> - **关联任意纸片**：待办关联由仅支持笔记扩展为支持关联任意纸片（待办纸或笔记纸），无缝兼容已有笔记关联数据。
> - **已完成自动置底**：待办新增“已完成自动置底”选项，勾选完成后自动移到已完成区域末尾，取消完成时移回未完成区域末尾（开启自动清除时暂不触发）。
> …

### [v3.2.1](https://github.com/snownico0722/PaperTodo/releases/tag/v3.2.1) — PaperTodo v3.2.1
<sub>2026-08-05 · 3mo ago</sub>

> <details>
> <summary>简体中文更新日志</summary>
> PaperTodo v3.2.1-额外bug修正
> **bug修复和边界修正**
> - 优化全屏避让：取消边缘胶囊的高频置顶保护，改为前台窗口事件触发、1 秒轻量检查和 5 秒全局兜底；关闭避让后不再保留相关监听与定时检查。
> - 修复程序重启后，直接从未展开的贴边胶囊右键删除非空纸片时，删除确认框可能导致异常退出的问题。
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [修复主胶囊回飞末帧在 WPF 布局期间交接导致的崩溃 [ci] (#457)](https://github.com/snownico0722/PaperTodo/commit/9d5f005d908aad639b656b48993a9524d6e081f9) | snownico0722 |
| 2026-11-12 | [docs: 在中英文 README 添加贡献指南入口](https://github.com/snownico0722/PaperTodo/commit/7506e9265c7cf766671463a85cf3c696390c51fb) | snownico0722 |
| 2026-11-12 | [Add files via upload](https://github.com/snownico0722/PaperTodo/commit/1ec518314c1cb7a86734862fa76096baec08a5e1) | snownico0722 |
| 2026-11-09 | [修正工作区菜单与托盘入口，并明确架构文档维护边界 (#448)](https://github.com/snownico0722/PaperTodo/commit/32bfe9e0533c704d07691a50a00f8b5345dc9a2e) | snownico0722 |
| 2026-11-09 | [校准中英文设置指南，补齐决策索引并精简 Agent 规则 (#447)](https://github.com/snownico0722/PaperTodo/commit/baf3312478298050d061c56e82779b9936cfee21) | snownico0722 |
| 2026-11-09 | [补充按功能组织文件、合并规则与退役入口的判断依据 (#446)](https://github.com/snownico0722/PaperTodo/commit/8cf42e686ba160f29970162d29d757d21a176a2b) | snownico0722 |
| 2026-11-09 | [精简遗留实现，统一待办规则、提示对话框和设置生效逻辑 (#445)](https://github.com/snownico0722/PaperTodo/commit/a32051cd573fb45c0f0915777ef592b8349b3eed) | snownico0722 |
| 2026-11-09 | [修正三方合并的待办关联和写入时序，保护健康备份 (#442)](https://github.com/snownico0722/PaperTodo/commit/bf7d0baaf434737f4dfacee40070de8017fd3de7) | snownico0722 |
| 2026-11-09 | [修复默认纸片隐藏外轮廓时失焦标题栏残留底色 [ci] (#444)](https://github.com/snownico0722/PaperTodo/commit/3934bcea63ebf07c9e64f2027f9090f657e8c4c2) | snownico0722 |
| 2026-11-09 | [优化胶囊队列拖动计算，修复折叠队列落点预览 (#443)](https://github.com/snownico0722/PaperTodo/commit/10eb6b55032e1376a8456e16419dbee68e993937) | snownico0722 |

[See all commits ↗](https://github.com/snownico0722/PaperTodo/commits)

## ⬇️ Get it

```bash
git clone https://github.com/snownico0722/PaperTodo.git
```

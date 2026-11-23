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
| 🍴 **Forks** | 150 |
| 🐞 **Open issues + PRs** | [34](https://github.com/snownico0722/PaperTodo/issues) |
| 💻 **Languages** | C# 92% · C 6% · JavaScript 1% · HTML 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `avalonedit` `csharp` `markdown` `minimalist` `notes` `todo` `windows` `wpf` `desktop` `note-taking` `productivity` `sticky-notes` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-05-27 |
| 📦 **Latest release** | [v3.40](https://github.com/snownico0722/PaperTodo/releases/tag/v3.40) — 2026-10-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 103.7 MB |

## 📦 Recent releases

### [v4.0.0-beta2](https://github.com/snownico0722/PaperTodo/releases/tag/v4.0.0-beta2) — PaperTodo v4.0.0-beta2 _(pre-release)_
<sub>2026-11-18 · 5d ago</sub>

> 这是一个测试版，可能存在很多问题、bug。
> This is a beta version; it may contain many issues and bugs.
> <details>
> <summary>简体中文更新日志</summary>
> **多工作区**
> - **多工作区管理与切换**：支持最多创建 5 个独立工作区，各工作区的纸片、图片与插件状态独立存储。
> …

### [v3.40](https://github.com/snownico0722/PaperTodo/releases/tag/v3.40) — PaperTodo v3.40
<sub>2026-10-20 · 1mo ago</sub>

> **纸片与胶囊**
> - **快捷关闭纸片**：展开的纸片支持 Ctrl+W 或标题栏中键关闭。
> - **「主胶囊缩短」选项**：高级设置新增该选项（默认关闭），开启后主胶囊仅显示展开/收起箭头并缩窄宽度。
> - 开启“再次点击收回”后，关联待办的纸片也可通过再次点击关联的图标再次点击隐藏。
> - 关闭普通胶囊、贴边胶囊或主胶囊后，仍保留各队列已调好的高度，仅在恢复默认设置时重置。
> - 从胶囊展开纸片时先激活窗口；若展开途中切到其他程序，动画结束不再抢回焦点，原最大化纸片会在下次激活时恢复。
> …

### [v4.0.0-beta1](https://github.com/snownico0722/PaperTodo/releases/tag/v4.0.0-beta1) — PaperTodo v4.0.0-beta1 _(pre-release)_
<sub>2026-09-15 · 2mo ago</sub>

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
<sub>2026-08-23 · 3mo ago</sub>

> <details>
> <summary>简体中文更新日志</summary>
> **待办与快启**
> - **文件/文件夹快启**：待办项支持直接拖入本地文件或文件夹作为快启路径，可直接打开、打开所在位置或解除关联，路径失效时会有明显提示；快启路径与纸片关联互斥。
> - **关联任意纸片**：待办关联由仅支持笔记扩展为支持关联任意纸片（待办纸或笔记纸），无缝兼容已有笔记关联数据。
> - **已完成自动置底**：待办新增“已完成自动置底”选项，勾选完成后自动移到已完成区域末尾，取消完成时移回未完成区域末尾（开启自动清除时暂不触发）。
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [支持插件追加笔记图片并保留手动置顶 (#477)](https://github.com/snownico0722/PaperTodo/commit/631f860404ae1560c9a5200eb67a764fb582cce0) | snownico0722 |
| 2026-11-19 | [修复纸片背景设置显示并调整正文间距高级模式可见性 (#474)](https://github.com/snownico0722/PaperTodo/commit/2fd2b580d978f810d4b29065341e6ed890060c29) | snownico0722 |
| 2026-11-19 | [Merge pull request #473 from snownico0722/feature/paper-content-spacing](https://github.com/snownico0722/PaperTodo/commit/6a720ed7bf55265b3d686dd795a2706f669cdc56) | snownico0722 |
| 2026-11-19 | [让两组正文间距支持键盘选择并保留焦点 [ci]](https://github.com/snownico0722/PaperTodo/commit/644caa33f89471397a71ecca12e8ca90a158a3fe) | snownico0722 |
| 2026-11-19 | [修复笔记调整行距后丢失本地正体和粗体字形](https://github.com/snownico0722/PaperTodo/commit/b4653d334145245e995eec74aa50bb9a5d0e2875) | snownico0722 |
| 2026-11-19 | [在已加载的纸片窗口上验证换行与字体继承 [ci]](https://github.com/snownico0722/PaperTodo/commit/51d4925e168a722c452c6e7f0c7750bcd28d995d) | snownico0722 |
| 2026-11-19 | [支持独立设置笔记行距与待办条目间距 [ci]](https://github.com/snownico0722/PaperTodo/commit/c17a0d5722aece7917ffbc2fba6f949bb4af1d02) | snownico0722 |
| 2026-11-19 | [Place capture exclusion in unreleased notes](https://github.com/snownico0722/PaperTodo/commit/b0dd147759377687ae5ba30e5815395b7854947b) | snownico0722 |
| 2026-11-19 | [Complete unreleased notes for PRs 454, 468 and 470](https://github.com/snownico0722/PaperTodo/commit/c21f517c4476f0ec962d13ab3b26a649d8034be1) | snownico0722 |
| 2026-11-19 | [Complete unreleased notes for PRs 454, 468 and 470](https://github.com/snownico0722/PaperTodo/commit/5d9ffc7e60199a01edb421d57a80891fe541eaba) | snownico0722 |

[See all commits ↗](https://github.com/snownico0722/PaperTodo/commits)

## ⬇️ Get it

```bash
git clone https://github.com/snownico0722/PaperTodo.git
```

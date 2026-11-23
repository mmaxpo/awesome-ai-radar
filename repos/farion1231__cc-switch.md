# farion1231/cc-switch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/farion1231/cc-switch)

> A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Desktop switcher for Claude Code, Codex, OpenCode providers & configs |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 156.6k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [736](https://github.com/farion1231/cc-switch/issues) |
| 💻 **Languages** | Rust 63% · TypeScript 36% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-tools` `claude-code` `desktop-app` `open-source` `rust` `tauri` `codex` `mcp` `provider-management` `wsl-support` `opencode` `skills` `skills-management` `hermes` `grok` `grokbuild` `pi` `deepseek-harness` `kimi-code` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2025-08-04 |
| 📦 **Latest release** | [v4.0.40](https://github.com/farion1231/cc-switch/releases/tag/v4.0.40) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 119.5 MB |
| 🌐 **Website** | https://ccswitch.io |

## 📦 Recent releases

### [v4.0.40](https://github.com/farion1231/cc-switch/releases/tag/v4.0.40) — CC Switch v4.0.40
<sub>2026-11-23 · today</sub>

> **CC Switch v4.0.40**
> 本版本让 **Grok Build 的官方卡可以绑定授权中心里的 xAI 账号**，像 Claude、Codex 官方卡一样在多个 Grok 账号之间切换。**插件页**支持 Antigravity CLI；**用量统计**的供应商和模型列表加了缓存命中率；**小米 MiMo** 内置余额和 Token Plan 额度查询；授权中心的账号卡片跟随侧栏应用的顺序和隐藏设置。
> 本版本还加固了深链接导入 MCP、用量脚本、SQL 导入和非本机监听地址的安全检查，并提升了数据库、本地路由、用量同步、会话搜索和「应用」页的速度。另外修复了 Kimi Code Desktop 主 agent 的用量没统计；Antigravity 输出速度从 4.0.38 起虚高；T3 Code 和单独运行的 ACP 里的 Antigravity 会话看不到；Mistral 官方 API 开思考后回复为空；Kimi 原生 Responses 在并行看图工具调用后一直报 400；WorkBuddy 企业账号积分显示为已用完；托盘里看不到 xAI 额度、官方账号显示成网站域名；Skills 页的「发现」里出现重复的技能；「应用」页要等版本检查完才显示安装状态等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-ja.md)**
> ---
> **新增**
> …

### [v4.0.39](https://github.com/farion1231/cc-switch/releases/tag/v4.0.39) — CC Switch v4.0.39
<sub>2026-11-22 · yesterday</sub>

> **CC Switch v4.0.39**
> 本版本以修复为主。**API Key 输入框**加了复制按钮；**备份**可以设置总大小上限，超过时从最旧的开始删；Claude Code 经 Codex OAuth 使用 **GPT-6.2 Sol / Astra** 时，系统提示的缓存命中率大幅提高。
> 另外修复了 Claude Code 和 Claude Desktop 的原生供应商卡住不出字时，要等最长 600 秒才故障转移；很长的流式响应让用量和日志收集占用的内存一直增长；一键导入链接合并配置失败后仍弹出确认框；只装了 Codex 桌面版时，插件页显示「未安装 Codex」；插件页给没装的应用建了空配置文件夹；OpenCode Go 的 DeepSeek V4.1 Flash 缺少 `max` 思考档位；快速点击时弹出层和下拉菜单闪烁等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-ja.md)**
> ---
> **新增**
> …

### [v4.0.38](https://github.com/farion1231/cc-switch/releases/tag/v4.0.38) — CC Switch v4.0.38
<sub>2026-11-21 · 2d ago</sub>

> **CC Switch v4.0.38**
> 本版本以修复为主。一键导入链接现在可以导入 **WorkBuddy** 供应商；Linux 上也能在授权中心切换 **Antigravity** 账号；Antigravity 的会话列表不再混进空会话和内部子会话，会话阅读器能看到思考、工具调用和结果。
> 另外修复了 DeepSeek Harness 的配置文件经过某些 YAML 工具后，所有第三方供应商都消失；从访达打开 CC Switch 时，「应用」页把能正常用的 npm 安装标成「无法运行」；技能仓库不是 GitHub / GitLab / Gitea 时只提示「0 个技能」而不报错；Codex 给模型选的思考等级有时没生效；Codex 经路由的几处格式转换错误；用量重复计算；会话正文搜索失败时显示「没有会话包含这个词」；主界面变成一条白条或被 macOS 菜单栏遮住；Linux AppImage 里点链接没反应等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-ja.md)**
> ---
> **新增**
> …

### [v4.0.37](https://github.com/farion1231/cc-switch/releases/tag/v4.0.37) — CC Switch v4.0.37
<sub>2026-11-20 · 3d ago</sub>

> **CC Switch v4.0.37**
> 本版本以修复为主。读不出来的供应商和 MCP 条目（比如由更新版本写入、经 WebDAV / S3 同步过来的）不再被当成空配置、下次保存时被默认值覆盖，而是单独列出来，可以删除；Pi 新增 **Mistral AI** 预设；韩语界面翻译整体改进。
> 另外修复了本地路由监听地址填 IPv6 时启动不了；「应用到 Claude Code 插件」会把损坏的 `~/.claude/config.json` 整个清空；网速慢时大的技能仓库下载到一半被中断；从访达打开 CC Switch 时 Codex 模型目录探测找不到 Node；工具调用参数里 `_` 开头的字段被删掉后才发给上游；移出又加回故障转移队列的供应商仍被跳过；插件页点「重试」看起来没反应等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.37-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.37-ja.md)**
> ---
> **新增**
> …

### [v4.0.36](https://github.com/farion1231/cc-switch/releases/tag/v4.0.36) — CC Switch v4.0.36
<sub>2026-11-19 · 4d ago</sub>

> **CC Switch v4.0.36**
> 本版本新增**插件**页面，可以在 CC Switch 里安装、启用、更新、卸载 Claude Code、Codex、Grok Build、MiniMax Code、OpenClaw、Pi 的插件，并管理 Claude Code、Codex、Grok Build 的插件市场。技能仓库现在可以用**访问令牌读取私有仓库**；经本地路由的供应商可以设置**费用倍率**；会话管理里能看到 Claude Code 桌面版的**章节**。
> 另外修复了 Codex 开了官方额度保护后自动审批也被拦下；Codex 聚合模式下新发布的官方模型要很久才出现；OpenCode 升级到 2.x 后 1.x 会话的用量不再统计；用量页自定义日期一输入年份就变成 1905；Antigravity 多个模型显示未定价等问题。用量统计里价格相同的推理档位现在合并成一行。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.36-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.36-ja.md)**
> ---
> **新增**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(settings): avoid flashing the loading indicator when reopening se…](https://github.com/farion1231/cc-switch/commit/721ca8e08c5233f41e9a79cc367d581ac1ec4bcd) | fuyundev |
| 2026-11-23 | [docs(release): add v4.0.40 release notes](https://github.com/farion1231/cc-switch/commit/f19a9d4f4f08bda03106a7be87c77cbcdf55b019) | farion1231 |
| 2026-11-23 | [chore(release): v4.0.40](https://github.com/farion1231/cc-switch/commit/08f505b1d28bc2dbe091491030456bee678a4f76) | farion1231 |
| 2026-11-23 | [feat(presets): add StringAI as a full sponsor](https://github.com/farion1231/cc-switch/commit/f81715e5d52ddf746566a7d16b56e515b3c1240c) | farion1231 |
| 2026-11-23 | [fix(proxy): parse chunked thinking/text content from Chat upstreams](https://github.com/farion1231/cc-switch/commit/0c1121ce377722e2cd4ac0897b3780cea3f419e4) | farion1231 |
| 2026-11-23 | [fix(tray): show xAI OAuth quota in the tray, including Codex stack me…](https://github.com/farion1231/cc-switch/commit/0e8a584b601f960309e64b4cbc019a18d0070fee) | farion1231 |
| 2026-11-23 | [fix(kimi): support protocol 1.5 usage accounting (#9505)](https://github.com/farion1231/cc-switch/commit/f08abf96f038330e61052cbc14674db19ff55b9d) | Chenning-Tao |
| 2026-11-23 | [fix(security): enforce per-connection Host check on non-loopback prox…](https://github.com/farion1231/cc-switch/commit/9f1c1bb54cf483e5bf489835af32c95aec322a03) | YUZHEthefool |
| 2026-11-23 | [perf(sessions): cancel obsolete content searches across IPC (#9896)](https://github.com/farion1231/cc-switch/commit/2372b1134e88ce0656003307c970f00b3b073b98) | YUZHEthefool |
| 2026-11-23 | [fix(tests): compile sync_agy_usage helper on all platforms](https://github.com/farion1231/cc-switch/commit/a09a99d7abbb2b7f57c31db8e8a2ce2aa5221635) | farion1231 |

[See all commits ↗](https://github.com/farion1231/cc-switch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/farion1231/cc-switch.git
```

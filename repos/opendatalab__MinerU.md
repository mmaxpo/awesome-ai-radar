# opendatalab/MinerU

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/opendatalab/MinerU)

> Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📄 Documents, OCR & web data |
| **Project** | — |
| **Why it's worth a look** | PDF & Office to LLM-ready Markdown/JSON |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 84.2k |
| 🍴 **Forks** | 7.0k |
| 🐞 **Open issues + PRs** | [16](https://github.com/opendatalab/MinerU/issues) |
| 💻 **Languages** | Python 98% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `extract-data` `layout-analysis` `ocr` `parser` `pdf` `pdf-converter` `python` `document-analysis` `pdf-parser` `pdf-extractor-llm` `pdf-extractor-pretrain` `pdf-extractor-rag` `ai4science` `docx` `pptx` `xlsx` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2024-02-29 |
| 📦 **Latest release** | [mineru-4.2.3-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.3-released) — 2026-11-16 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 186.5 MB |
| 🌐 **Website** | https://opendatalab.github.io/MinerU/ |

## 📦 Recent releases

### [mineru-4.2.3-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.3-released) — MinerU 4.2.3
<sub>2026-11-16 · 6d ago</sub>

> **4.2.3**
> - **新增单文件执行超时与托管恢复**。WebUI、Router 和 API Server 支持 `--task-timeout`，默认 `3600` 秒，从取得解析名额开始计时，覆盖解析和服务端产物打包。超时任务返回 `task_timeout`，独立 API 停止接收新任务，由部署方重建服务。Router 通过父进程监督回收超时 worker 及模型子进程，并重新启动服务，即使执行线程、事件循环或取消清理挂起也能触发恢复。
> - **改善 WebUI 恢复体验与进程清理**。本地 WebUI 由 Router 托管唯一 worker，恢复期间显示状态，尚未提交的排队请求在服务就绪后继续。旧 worker 上其他未完成请求返回 `worker_restarted`，问题文件可手动重试。完善 Windows 进程树、临时目录与控制通道回收，明确报告模型预加载失败，并在连续三次启动恢复失败后停止自动重试。
> - **修复 Doclib 全文检索被图片载荷挤占**。构造检索文本时提取正文、公式和图表说明，再应用字符预算，避免内嵌图片的 base64 内容占满索引而遗漏正文。升级后从解析缓存重建已有索引，并保留跨页内容续接。缓存不完整的文档会记录迁移原因，补齐缓存或重新解析后重启 Doclib 可继续迁移。
> - **提前检查 vLLM 与 Transformers 兼容性**。启动引擎前识别 `vllm<0.29.0` 与 `transformers>=5.23.0` 的不兼容组合，并给出升级 vLLM 或调整 Transformers 版本范围的明确提示，减少模型加载阶段难以定位的失败。
> - **更新 DocVortex 依赖**。最低版本提升至 `0.6.24`，同步原生文档解析与共享渲染能力的改进。
> …

### [mineru-4.2.2-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.2-released) — MinerU 4.2.2
<sub>2026-11-13 · 10d ago</sub>

> **4.2.2**
> - **完善本地 VLM 引擎的故障传播与生命周期管理**。统一消费 LMDeploy、vLLM、llama.cpp 和 MLX 的公共健康与失效契约；确认引擎失效后停止复用缓存实例，并通知关联宿主，避免把全局故障当作普通识别失败而静默降级。普通单片识别失败仍保留既有回退。
> - **增强解析服务的健康检查与任务清理**。周期探测已加载且支持健康检查的运行时；暂时不可用时拒绝新推理，恢复健康后重新开放。确认引擎死亡时，健康与能力接口返回明确错误，运行及排队任务按既有边界清理，恢复由宿主管理。完善关闭期间的在途探测、取消和资源释放顺序。
> - **修复批量解析的输入与错误处理**。使用内容签名和容器识别验证文件，避免 Office 锁文件阻断后续文档，同时保留名称以 `~$` 开头的合法文档。明确的损坏、加密、资源限制、输入缺失及权限错误记录为单项失败并继续；引擎、服务或输出故障停止后续处理。摘要分别报告成功、跳过、失败和未处理数量，部分失败返回非零退出码。
> - **修复批量输出路径判断**。目录和多文件输入始终采用目录输出，只有一个文档时也保持相同语义。支持已有或新建的 `results.v1`、`results.md` 等带点目录，拒绝将批量结果写入已有普通文件；显式单文件输出继续支持覆盖目标文件。
> - **明确阅读与导出的职责**。`mineru read` 的 Markdown 输出用于渐进阅读，保留 stdout、JSON 和续读提示；`--output PATH` 仅用于图片。保存当前文本片段可使用重定向或 SDK，完整导出指定页范围使用 `mineru parse ... -o ...`，避免把受阅读预算限制的片段误当成完整产物。
> …

### [mineru-4.2.1-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.1-released) — MinerU 4.2.1
<sub>2026-11-11 · 12d ago</sub>

> **4.2.1**
> - **修复 Doclib 截断续读遗漏内容**。Markdown 文档或单页读取在 `context=0` 时，达到长度限制后通过 `next_request.locator` 与 `next_request.after` 继续读取当前页的剩余内容，读完后再建议下一页。CLI 续读标记和 SDK 文档同步更新。
> - **完善托管解析服务的故障恢复**。连续启动或重启失败达到上限后停止自动重试，并清理残留进程。重新设置托管模式或档位、重启文档库服务后可再次尝试恢复。切换模式、档位及关闭服务时，完善旧进程和控制通道的回收。
> - **修复 Windows 托管服务端口探测**。按照服务实际绑定行为检查端口，在非严格端口模式下跳过已占用或被系统保留的端口，减少探测成功后仍无法启动的问题。
> - **改善文档库服务的优雅退出**。通过宿主停机回调执行生命周期清理，使 Windows 关闭流程也能回收后台任务、托管解析进程和数据库资源。
> - **修复 Windows GPU 显存信息缺失**。完善 DXGI 与硬件库存的 PCI 地址匹配，在同型号设备条目存在歧义时保留一致的显存和设备属性，提高硬件诊断信息的完整性。
> …

### [mineru-4.2.0-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.0-released) — MinerU 4.2.0
<sub>2026-11-10 · 13d ago</sub>

> **4.2.0**
> MinerU 4.2.0 重点升级 WebUI 交互与结果溯源，改善复杂 PDF、公式和表格的解析质量，并完善设备选择、模型缓存、服务管理与输入安全。以下为相对 4.1.0 的累计更新，包含 4.1.x 期间已发布的改进。
> **WebUI 交互与结果溯源**
> - **新增原文与结果双向定位**：点击 PDF 或图片中的区域，即可定位并高亮对应的解析内容；点击结果中的段落、标题、公式或图表，也可返回原文位置。跨页合并内容支持切换来源页。
> - **增强布局可视化**：合并后的段落、列表和表格可关联多个原文区域，并通过连线展示合并关系，方便检查阅读顺序、内容归属和跨页合并结果。
> - **新增结果目录导航**：根据标题生成可折叠目录，支持快速跳转到对应内容。
> …

### [mineru-4.1.7-released](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.1.7-released) — MinerU 4.1.7
<sub>2026-11-04 · 19d ago</sub>

> MinerU 4.1.7 adds persistent authentication for the local document library and improves layout detection.
> - Require a persistent bearer token for Doclib HTTP endpoints. The SDK reads local credentials automatically; direct HTTP integrations must send the token.
> - Protect credential files with private POSIX permissions and native macOS/Windows ACLs.
> - Restore per-class layout output thresholds consistently across the ONNX and Torch backends.
> - Place absorbed image regions according to their geometry in the reading order.
> - Upgrade the DocVortex dependency to `>=0.6.13,<0.7`.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Merge pull request #5782 from opendatalab/dev](https://github.com/opendatalab/MinerU/commit/097de7f63f54722c9b805ee1c9a14a0c5b02e078) | myhloli |
| 2026-11-18 | [Merge pull request #5781 from myhloli/dev](https://github.com/opendatalab/MinerU/commit/d3e049f2ba2966581785ffcdcd0791c8d5844563) | myhloli |
| 2026-11-18 | [docs: reorganize bilingual MkDocs guides by workflow](https://github.com/opendatalab/MinerU/commit/1f038d16f32260acb0017ea83dd61701976b872f) | myhloli |
| 2026-11-16 | [chore: sync recent releases in issue templates](https://github.com/opendatalab/MinerU/commit/b4efa4b2b76ebb012c476b79bdfc6f18a95aacd6) | github-actions[bot] |
| 2026-11-16 | [Merge pull request #5779 from myhloli/codex/release-4.2.3](https://github.com/opendatalab/MinerU/commit/cba4f4dad1c386f13065be832e3321cb0d1ae095) | myhloli |
| 2026-11-16 | [chore(release): prepare MinerU 4.2.3](https://github.com/opendatalab/MinerU/commit/be3047a49a993808502998d4bec3da9b261ff170) | myhloli |
| 2026-11-16 | [Merge pull request #5778 from opendatalab/dev](https://github.com/opendatalab/MinerU/commit/1fde29e73493bad2f4f71a3d0475e65ea999d56f) | myhloli |
| 2026-11-16 | [Merge pull request #5777 from myhloli/dev](https://github.com/opendatalab/MinerU/commit/1a5c8737963b5e1e586868820f6df79842981346) | myhloli |
| 2026-11-16 | [fix(doclib): keep image payloads out of search indexes](https://github.com/opendatalab/MinerU/commit/97178455c9955c3b225d65b32d9f60322887f372) | myhloli |
| 2026-11-16 | [Merge pull request #5775 from myhloli/dev](https://github.com/opendatalab/MinerU/commit/87298aad62b03f138cf72b2e7b944731b6a47c16) | myhloli |

[See all commits ↗](https://github.com/opendatalab/MinerU/commits)

## ⬇️ Get it

```bash
git clone https://github.com/opendatalab/MinerU.git
```

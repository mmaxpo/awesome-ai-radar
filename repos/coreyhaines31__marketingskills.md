# coreyhaines31/marketingskills

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/coreyhaines31/marketingskills)

> Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | agency |
| **Why it's worth a look** | Marketing skills for agents: CRO, copywriting, SEO, analytics |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 63.0k |
| 🍴 **Forks** | 9.2k |
| 🐞 **Open issues + PRs** | [82](https://github.com/coreyhaines31/marketingskills/issues) |
| 💻 **Languages** | JavaScript 94% · Python 3% · HTML 2% · Shell 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `claude` `codex` `marketing` `agent-skills` `ai-agents` `ai-seo` `claude-code` `claude-code-plugin` `claude-skills` `content-marketing` `conversion-rate-optimization` `copywriting` `cursor` `email-marketing` `generative-engine-optimization` `growth-marketing` `marketing-automation` `saas-marketing` `seo` `skill-md` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-01-15 |
| 📦 **Latest release** | [v2.14.29](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.29) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 7.4 MB |
| 🌐 **Website** | https://marketing-skills.com |

## 📦 Recent releases

### [v2.14.29](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.29) — v2.14.29 — Updated the AIsa integration and quick start for schema discovery, fr…
<sub>2026-11-26 · today</sub>

> - Updated the AIsa integration and quick start for schema discovery, free `batch_quote`, and execution through `batch_use`.
> - Aligned account verification and five evaluation scenarios with the current MCP interface. Repaired documentation links and clarified the referring-domain comparison.
> **Skill ZIP assets**
> Complete source catalog: 53 skills.
> Claude web target: 53 skills with reviewed short descriptions.
> Perplexity Computer target: 53 skills.
> …

### [v2.14.28](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.28) — v2.14.28 — Three methods added to existing skills (#1048).
<sub>2026-11-23 · 3d ago</sub>

> Three methods added to existing skills (#1048).
> - **prospecting** (1.7.0 → 1.8.0): podcast appearances as a lead source. Episodes are indexed with speaker-labelled transcripts, so a search finds a named guest describing the problem you solve, in their own words. `references/signal-plays.md` covers three uses (find people describing the problem, research an account's leader, find the shows your buyers appear on) and five rules: check the air date, confirm who said it on the episode page, apply ICP fit, name the episode openly because they published it, and keep the reference to one line. A 90-day freshness window and a tools row are added. Eval 15 added.
> - **social** (2.6.0 → 2.6.1), **marketing-loops** (1.9.0 → 1.9.1): outlier posts are scored against the account's own median, split by platform and format, as a multiple of the baseline (1.5–2× mild, 2–5× strong, 5× or more huge), from at least 20 posts, with low confidence under 10. This replaces "for example 100K+ views" in the listening reference and the niche-outlier loop. Method adapted from ScrapeCreators' outlier-post-finder skill (MIT).
> - **customer-research** (2.0.8 → 2.0.9): a table for sorting a comment thread into questions, objections, complaints, confusion, requests, buying intent, debate, and praise before clustering, with two cautions: the top comments are not the representative ones, and commenters are an audience, not a list.
> **Skill ZIP assets**
> Complete source catalog: 53 skills.
> …

### [v2.14.27](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.27) — v2.14.27 — New tool access for app store, SEO audit, comment, and podcast data (…
<sub>2026-11-23 · 3d ago</sub>

> New tool access for app store, SEO audit, comment, and podcast data (#1048).
> - **aso** (2.0.6 → 2.1.0): a new section, With App Store Connect Access. For the user's own Apple app, an agent with the open-source App Store Connect CLI reads reviews by rating and country, the rating breakdown, Apple's review summaries, week-over-week numbers, and the exact listing text, always in read-only mode, in place of asking for an export. Review responses and metadata changes are drafted and sent only on approval. New guide: `tools/integrations/app-store-connect-cli.md`, plus an App Store category in the registry.
> - **seo-audit** (2.2.9 → 2.2.10): SEOmator joins Tools Referenced, an open-source audit CLI and local MCP server an agent or CI job can run free. Checks it couldn't run stay "not measured" in the report. New guide: `tools/integrations/seomator.md`. Its repository ships a skill also named `seo-audit`; the guide covers the CLI and MCP server only.
> - **ScrapeCreators guide**: comment and transcript endpoints, for mining what an audience asks and objects to. The wording is kept; lists of commenters are not.
> - **Firecrawl guide**: podcast transcripts through Alexandria (speaker-labelled, quotes with timestamps), with the documented request, credit costs, and the third-party terms step that needs the user.
> **Skill ZIP assets**
> …

### [v2.14.26](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.26) — v2.14.26 — prospecting (1.6.3 → 1.7.0): subprocessor and DPA pages as a prospect…
<sub>2026-11-23 · 3d ago</sub>

> - **prospecting** (1.6.3 → 1.7.0): subprocessor and DPA pages as a prospecting source (#1046). Companies publish the vendors that process their customers' data, so the page is a free, first-party record of part of the stack. `references/signal-plays.md` gains a section on three uses: finding accounts that name a given vendor (`"subprocessors" "<vendor>"`), qualifying an account before writing, and catching a vendor being added or dropped. It says where the pages live, and gives rules for the weak points: the list covers only vendors that touch customer data, absence proves nothing, names may be legal entities, and the lookup is never the opening line. The tools table, the tech-stack signal row, and `references/data-sources.md` list it. Eval 14 added.
> **Skill ZIP assets**
> Complete source catalog: 53 skills.
> Claude web target: 53 skills with reviewed short descriptions.
> Perplexity Computer target: 53 skills.
> Choose `<name>-claude-web.zip` for the documented single-folder web upload format.
> …

### [v2.14.25](https://github.com/coreyhaines31/marketingskills/releases/tag/v2.14.25) — v2.14.25 — Community batch: fourteen new tool guides, three guide updates, and t…
<sub>2026-11-20 · 7d ago</sub>

> Community batch: fourteen new tool guides, three guide updates, and three skill contributions.
> - **New integration guides**, each reviewed against the usefulness and neutrality rules in `tools/PARTNERS.md`: Hermoso (#1014), Calven (#980), PostOnce (#979), GetYouTubeTranscript (#975), Hyper Elements (#974), ScrapeWhale (#972), Adspy (#965), Adeli (#964), SignalShelf (#959), GoAnyAPI with a CLI and tests (#946), Parallel with a CLI and tests (#943), Marcora (#939), Adlicio (#898), and SocialToAI (#917). Updated guides: Precleared (#957) and Coupler (#904). Edits made on the way in: tracking links, in-guide disclosure lines, pointers to vendors' own skill packs, comparison framing, and price pitches were removed; Adlicio no longer documents Google Maps or logged-in Facebook group scraping; GetYouTubeTranscript and ScrapeWhale carry a platform-terms note.
> - **social** (2.5.4 → 2.6.0): a new `references/chinese-platforms.md` on Xiaohongshu, Douyin, Weibo, Bilibili, and WeChat (how search works, what the metrics mean, creator and ad marketplaces, disclosure rules, data limits), and a Social Data & Listening category in the registry (#917 by the SocialToAI team; the reference names no tool).
> - **Outdated facts corrected** (#892 by @canermoral5-sys), after a check against primary sources. **ai-seo** (2.12.6 → 2.12.7): the GEO study table now carries the figures derived from the paper's Table 1 (quotations +41%, statistics +31%, fluency +28%, citing sources +27%, keyword stuffing -8%), with the rank effect (citing sources helped a fifth-ranked site and hurt the top one); Search Console's Generative AI performance report replaces "no AI-specific reporting"; Claude's use of Brave is described as reported, not documented. **ads** (2.7.8 → 2.7.9): Meta's 20% text limit is gone since September 2020, and the event-prioritization checklist items are replaced. **seo-audit** (2.2.8 → 2.2.9): a caveat on Search Console impressions between May 13, 2025 and April 27, 2026. **prospecting** (1.6.2 → 1.6.3), **cold-email** (2.2.6 → 2.2.7): Austria joins Germany and Italy in requiring prior consent for cold email. **emails** (2.1.8 → 2.1.9): open rate is a trend within one list, not a benchmark. **paywalls** (2.1.4 → 2.1.5): the escape hatch wording covers paid-only products. One of the PR's corrections, on ChatGPT's search providers, was not confirmed and is not included.
> - **ai-seo**: the agent-readiness reference gains checks for stores: machine-readable price and availability, whether cart and checkout answer an agent's user agent, and structured returns and shipping terms (#859 by @vlloic).
> - **public-relations** (1.3.0 → 1.3.1), **referrals** (2.2.6 → 2.2.7): two tool mentions that makers added to skill files in 2.14.24 are removed, under the rule that a maker's PR does not add its own tool to a skill. Both tools keep their guides and registry rows.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Merge pull request #1065 from lhymmEU/docs/aisa-mcp-quoting](https://github.com/coreyhaines31/marketingskills/commit/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64) | coreyhaines31 |
| 2026-11-25 | [docs: fix AIsa MCP quoting and execution guidance](https://github.com/coreyhaines31/marketingskills/commit/f97ae59325a90e7f5e006c97f568f51c63c38e9e) | lhymmEU |
| 2026-11-23 | [Merge pull request #1050 from coreyhaines31/feature/1048-methods](https://github.com/coreyhaines31/marketingskills/commit/8fd2fcade2fd6629026e9dfe6d133b55b36968b9) | coreyhaines31 |
| 2026-11-23 | [Merge branch 'main' into feature/1048-methods](https://github.com/coreyhaines31/marketingskills/commit/3436288411ad04572058fe7776e617ffec74e1af) | coreyhaines31 |
| 2026-11-23 | [Merge pull request #1049 from coreyhaines31/feature/1048-tool-access](https://github.com/coreyhaines31/marketingskills/commit/1a6f91eeb23fa049427187690522e1acd328f019) | coreyhaines31 |
| 2026-11-23 | [chore: release 2.14.28](https://github.com/coreyhaines31/marketingskills/commit/4f053d928385449457721fed537af9fd5671f828) | coreyhaines31 |
| 2026-11-23 | [feat: add outlier scoring, comment sorting, and podcasts as a lead so…](https://github.com/coreyhaines31/marketingskills/commit/be85be135de750813a48f7eb6bd1c9cde48ca63d) | coreyhaines31 |
| 2026-11-23 | [chore: release 2.14.27](https://github.com/coreyhaines31/marketingskills/commit/fe0678517ee73d4a4876ddbe57e43b252e87a384) | coreyhaines31 |
| 2026-11-23 | [feat(aso, seo-audit): use App Store Connect and a local audit engine …](https://github.com/coreyhaines31/marketingskills/commit/bc44169abcca53847f5cef6207bbc009ef3b15b3) | coreyhaines31 |
| 2026-11-23 | [feat(tools): add App Store Connect CLI and SEOmator guides; extend Sc…](https://github.com/coreyhaines31/marketingskills/commit/0f668c2bad3969b5eb8c3df3c9e82fe22bcd61cf) | coreyhaines31 |

[See all commits ↗](https://github.com/coreyhaines31/marketingskills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
```

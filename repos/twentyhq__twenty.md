# twentyhq/twenty

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/twentyhq/twenty)

> The open alternative to Salesforce, designed for AI.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Open-source Salesforce alternative built for AI |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 61.4k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [173](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3092.0 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0)
<sub>2026-11-23 · today</sub>

> This release fixes a sidebar regression that left non-admin members without the Applications permission unable to see standard navigation items. Companies, People, Opportunities, Tasks, Notes, Dashboards, and folders all disappeared when the customizable sidebar flag was disabled.
> No SDK exports, types, or CLI commands changed. Package consumers do not need to update their code.
> **🌟 Highlights**
> - Sidebar navigation items (Companies, People, Opportunities, Tasks, Notes, Dashboards) are now visible to members without the Applications permission when the customizable sidebar flag is off. ([#31179](https://github.com/twentyhq/twenty/pull/31179))
> **🐛 Bug fixes**
> - Fixes a bug where sidebar items (Companies, People, Opportunities, Tasks, Notes, Dashboards) were hidden for members lacking the Applications permission when the customizable sidebar flag is off — no SDK changes required. ([#31179](https://github.com/twentyhq/twenty/pull/31179)) by @thomtrp
> …

### [twenty/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.62.0)
<sub>2026-11-23 · today</sub>

> The `NOT_STARTED` workflow run status is removed in this release. The upgrade command converts any runs in that state to `ENQUEUED` automatically. Update any custom integrations, filters, or views that reference `NOT_STARTED` before upgrading.
> A regression from 2.61 is fixed for team members without the Applications permission. Those members were seeing an empty sidebar — Companies, People, Opportunities, Tasks, Notes, and Dashboards all gone. Navigation is restored for those roles.
> Emoji reactions now work in direct messages. Email thread panels no longer break when channel visibility is enabled. Internally, workflow privacy moves from a visibility enum to a boolean flag; the old column stays this release and is dropped in 2.63.
> **⚠️ Breaking changes**
> - The NOT_STARTED workflow run status is removed. The upgrade converts existing NOT_STARTED runs to ENQUEUED. Update any integrations, filters, or views that reference NOT_STARTED before upgrading. ([#31154](https://github.com/twentyhq/twenty/pull/31154)) by @charlesBochet
> **🌟 Highlights**
> …

### [twenty/v2.61.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.61.0)
<sub>2026-11-22 · today</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Show member health checks in Apps preferences ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - [BREAKING_CHANGE] Upsert row-level permission rules instead of a predicate tree ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> - Import recurring Google Calendar meetings only up to 90 days ahead ([#30335](https://github.com/twentyhq/twenty/pull/30335)) by @neo773
> - [BREAKING_CHANGE] Add a 2.60 command that drops the workspace workflowVersion object ([#30500](https://github.com/twentyhq/twenty/pull/30500)) by @thomtrp
> - [BREAKING_CHANGE] Add generic date functions to validation rules ([#30527](https://github.com/twentyhq/twenty/pull/30527)) by @FelixMalfait
> …

### [sdk/v2.61.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.61.0)
<sub>2026-11-22 · today</sub>

> Nine breaking changes ship here. Billing types are the main target: `planKey` on `BillingSubscriptionItem` is now nullable, the metered API is removed, and `... on BillingLicensedProduct` fragments need updating. `navigationMenuItem.folderId` renames to `parentId` and `upsertRowLevelPermissionPredicates` moves to a rules array. `recordShare` and `accessGroup` are removed as standard workspace objects.
> App manifests gain `billing.prices` for real-currency per-member pricing. Agents support `isPrivate` and `createdByUserWorkspaceId`. Three new APIs — `connectedAccount`, `READ_PRIVATE_CHANNELS`, and `calendarChannels` — let an app map calendar channels to their owners without user context.
> `twenty app pull` now restores both frontend dependencies and logic-function sources. `twenty app dev --verbose` shows the full watch scope.
> **⚠️ Breaking changes**
> - `defineHealthCheck` now accepts `runOnUserPreferences: true` to show the check in member preferences; without it, checks only run in workspace settings. ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - `upsertRowLevelPermissionPredicates` is removed; replace calls with the rules-based API, passing each rule as an object with its own `operations` array and predicate groups. ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> …

### [sdk/v2.60.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.60.0)
<sub>2026-11-22 · today</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Show member health checks in Apps preferences ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - [BREAKING_CHANGE] Upsert row-level permission rules instead of a predicate tree ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> - Import recurring Google Calendar meetings only up to 90 days ahead ([#30335](https://github.com/twentyhq/twenty/pull/30335)) by @neo773
> - [BREAKING_CHANGE] Add a 2.60 command that drops the workspace workflowVersion object ([#30500](https://github.com/twentyhq/twenty/pull/30500)) by @thomtrp
> - [BREAKING_CHANGE] Add generic date functions to validation rules ([#30527](https://github.com/twentyhq/twenty/pull/30527)) by @FelixMalfait
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Fix CLI manifest mock so named UI imports resolve at load time (#30933)](https://github.com/twentyhq/twenty/commit/73cf770ecf565b82e6f2eb8adf24eadd7216288c) | BOHEUS |
| 2026-11-23 | [Refuse links to records the role cannot read (#31198)](https://github.com/twentyhq/twenty/commit/79b780c867a18fd07e984a25932dfabec4b2e23a) | charlesBochet |
| 2026-11-23 | [Exempt API keys from channel visibility behind a feature flag (#31215)](https://github.com/twentyhq/twenty/commit/67076baf6df464c9c8c6e453115018873839b7d8) | charlesBochet |
| 2026-11-23 | [chore: remove the unused entities dependency from twenty-shared (#31230)](https://github.com/twentyhq/twenty/commit/315f315403bd628d3892bbc5a187f88389b698e5) | mabdullahabaid |
| 2026-11-23 | [Compute access groups on writes made in the lite workspace context (#…](https://github.com/twentyhq/twenty/commit/c4ccdfcd258762b0d4ecfe01c7410c8175628bfe) | charlesBochet |
| 2026-11-23 | [chore: remove unused dependencies from twenty-zapier (#31232)](https://github.com/twentyhq/twenty/commit/f938ee43cdf8c31c7493a2f28c99497285e30648) | mabdullahabaid |
| 2026-11-23 | [i18n - translations (#31246)](https://github.com/twentyhq/twenty/commit/d0257d16a81f18a00a6d3389b94cc308bdb154d5) | twenty-pr[bot] |
| 2026-11-23 | [i18n - translations (#31241)](https://github.com/twentyhq/twenty/commit/5722ff75a6475bf4d2cf6c8a659acf5281489389) | twenty-pr[bot] |
| 2026-11-23 | [Move a built-in section to a tab that already holds one (#31030)](https://github.com/twentyhq/twenty/commit/554aa20418073dbb9457556afa620230add04f6d) | thomtrp |
| 2026-11-23 | [feat(ai-chat): refuse attachments over 50 MB with an error toast (#31…](https://github.com/twentyhq/twenty/commit/5511cff1f8459edc6b8245679d2b9f11bb0f3b10) | etiennejouan |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```

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
| 🐞 **Open issues + PRs** | [133](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3135.4 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0)
<sub>2026-11-23 · yesterday</sub>

> This release fixes a sidebar regression that left non-admin members without the Applications permission unable to see standard navigation items. Companies, People, Opportunities, Tasks, Notes, Dashboards, and folders all disappeared when the customizable sidebar flag was disabled.
> No SDK exports, types, or CLI commands changed. Package consumers do not need to update their code.
> **🌟 Highlights**
> - Sidebar navigation items (Companies, People, Opportunities, Tasks, Notes, Dashboards) are now visible to members without the Applications permission when the customizable sidebar flag is off. ([#31179](https://github.com/twentyhq/twenty/pull/31179))
> **🐛 Bug fixes**
> - Fixes a bug where sidebar items (Companies, People, Opportunities, Tasks, Notes, Dashboards) were hidden for members lacking the Applications permission when the customizable sidebar flag is off — no SDK changes required. ([#31179](https://github.com/twentyhq/twenty/pull/31179)) by @thomtrp
> …

### [twenty/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.62.0)
<sub>2026-11-23 · yesterday</sub>

> The `NOT_STARTED` workflow run status is removed in this release. The upgrade command converts any runs in that state to `ENQUEUED` automatically. Update any custom integrations, filters, or views that reference `NOT_STARTED` before upgrading.
> A regression from 2.61 is fixed for team members without the Applications permission. Those members were seeing an empty sidebar — Companies, People, Opportunities, Tasks, Notes, and Dashboards all gone. Navigation is restored for those roles.
> Emoji reactions now work in direct messages. Email thread panels no longer break when channel visibility is enabled. Internally, workflow privacy moves from a visibility enum to a boolean flag; the old column stays this release and is dropped in 2.63.
> **⚠️ Breaking changes**
> - The NOT_STARTED workflow run status is removed. The upgrade converts existing NOT_STARTED runs to ENQUEUED. Update any integrations, filters, or views that reference NOT_STARTED before upgrading. ([#31154](https://github.com/twentyhq/twenty/pull/31154)) by @charlesBochet
> **🌟 Highlights**
> …

### [twenty/v2.61.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.61.0)
<sub>2026-11-22 · yesterday</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Show member health checks in Apps preferences ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - [BREAKING_CHANGE] Upsert row-level permission rules instead of a predicate tree ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> - Import recurring Google Calendar meetings only up to 90 days ahead ([#30335](https://github.com/twentyhq/twenty/pull/30335)) by @neo773
> - [BREAKING_CHANGE] Add a 2.60 command that drops the workspace workflowVersion object ([#30500](https://github.com/twentyhq/twenty/pull/30500)) by @thomtrp
> - [BREAKING_CHANGE] Add generic date functions to validation rules ([#30527](https://github.com/twentyhq/twenty/pull/30527)) by @FelixMalfait
> …

### [sdk/v2.61.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.61.0)
<sub>2026-11-22 · yesterday</sub>

> Nine breaking changes ship here. Billing types are the main target: `planKey` on `BillingSubscriptionItem` is now nullable, the metered API is removed, and `... on BillingLicensedProduct` fragments need updating. `navigationMenuItem.folderId` renames to `parentId` and `upsertRowLevelPermissionPredicates` moves to a rules array. `recordShare` and `accessGroup` are removed as standard workspace objects.
> App manifests gain `billing.prices` for real-currency per-member pricing. Agents support `isPrivate` and `createdByUserWorkspaceId`. Three new APIs — `connectedAccount`, `READ_PRIVATE_CHANNELS`, and `calendarChannels` — let an app map calendar channels to their owners without user context.
> `twenty app pull` now restores both frontend dependencies and logic-function sources. `twenty app dev --verbose` shows the full watch scope.
> **⚠️ Breaking changes**
> - `defineHealthCheck` now accepts `runOnUserPreferences: true` to show the check in member preferences; without it, checks only run in workspace settings. ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - `upsertRowLevelPermissionPredicates` is removed; replace calls with the rules-based API, passing each rule as an object with its own `operations` array and predicate groups. ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> …

### [sdk/v2.60.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.60.0)
<sub>2026-11-22 · yesterday</sub>

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
| 2026-11-24 | [Make personal Favorites a Home section admins can move, rename or rem…](https://github.com/twentyhq/twenty/commit/e51a65558f09e2cd2aa351f06953706020f0a196) | thomtrp |
| 2026-11-24 | [fix(ai-chat): show the picked record in AI chat form fields (#31367)](https://github.com/twentyhq/twenty/commit/2b5775b06a53d6af64c787c0ab2ced3487530894) | etiennejouan |
| 2026-11-24 | [Hint how a triggered agent runs in its Test form, and fix the stale A…](https://github.com/twentyhq/twenty/commit/4c16fc15872166a4a0282229c1d6b47eecd63733) | FelixMalfait |
| 2026-11-24 | [i18n - translations (#31370)](https://github.com/twentyhq/twenty/commit/784b65f48b81e0af8a2be9e21bb4b42067724390) | twenty-pr[bot] |
| 2026-11-24 | [Download integration test timings once per CI Server run (#31368)](https://github.com/twentyhq/twenty/commit/0f73aa49600000a347da3573d640062d832b972f) | charlesBochet |
| 2026-11-24 | [i18n - translations (#31366)](https://github.com/twentyhq/twenty/commit/ffdb81839be47083d35f51e186dbfb35c528289f) | twenty-pr[bot] |
| 2026-11-24 | [Remove the type-check suppressions in format-result.util.ts (#31171)](https://github.com/twentyhq/twenty/commit/497725c2ec07c1ba4f11ee143d8402a91d957647) | twenty-pr-author[bot] |
| 2026-11-24 | [Default the CI runner picker fallback to the standard runner (#31364)](https://github.com/twentyhq/twenty/commit/0554c86c05eabf3cfd1b95a633cd589d87d3e9b8) | charlesBochet |
| 2026-11-24 | [Let users create recurring calendar events (#31248)](https://github.com/twentyhq/twenty/commit/0d37d5d126bb02067a76bc68ebd0fdfde505f056) | neo773 |
| 2026-11-24 | [fix(inbox): give the Open status its own translation string (#31353)](https://github.com/twentyhq/twenty/commit/2eeeab429e9c33d7a77cc3afca7036465904df4b) | etiennejouan |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```

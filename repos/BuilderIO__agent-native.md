# BuilderIO/agent-native

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/BuilderIO/agent-native)

> A framework for building agentic apps

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Apps that mix agent chat with traditional UI |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 7.7k |
| 🍴 **Forks** | 710 |
| 🐞 **Open issues + PRs** | [261](https://github.com/BuilderIO/agent-native/issues) |
| 💻 **Languages** | TypeScript 87% · MDX 10% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `react` `agent-native` `typescript` `agent-framework` `agentic-ai` `ai-agents` `framework` `generative-ui` `mcp` `open-source` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [@agent-native/skills@0.4.8](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/skills%400.4.8) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 594.5 MB |
| 🌐 **Website** | https://www.agent-native.com |

## 📦 Recent releases

### [@agent-native/skills@0.4.8](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/skills%400.4.8)
<sub>2026-11-16 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.
> - Updated dependencies [e04e57c]
> - Updated dependencies [cdf52f4]
> - Updated dependencies [a4a4f9e]
> - Updated dependencies [9af0433]
> …

### [@agent-native/core@0.229.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.229.0)
<sub>2026-11-16 · today</sub>

> **Minor Changes**
> - 9af0433: Add `defineAppConfigSection(key, schema)` so an app can register its own typed server config section. Its fields resolve like the framework's (declared default, `.meta({ env })` aliases, then `defineAppConfig()`), and `getAppConfig()[key]` or the returned `read()` reads it. Declare the section's type by augmenting `AppConfigSections`. Keys that collide with framework sections and env aliases another field already reads are refused at registration.
> - 62bbf91: Two files created under one name at the same moment no longer collide. Core adds `nextFreeName` in `@agent-native/core/free-name`, which gives `name.html`, then `name-2.html`, `name-3.html` and so on, and `nameTaken` in `@agent-native/core/free-name/server`, one typed `name_taken` refusal that carries a free name to use instead. Design uses them first: copies made at once each save under their own name, a rename onto a taken name says so and suggests a free one, and older files that already share a name are given free names so Design's unique filename index can hold.
> - f152dfe: Framework reliability improvements: agent runs, run recovery and tool approvals report failures instead of settling as empty successes; actions, the action query cache and session hooks handle cold starts, retries and mounted base paths; sign-in, organization context and workspace connections resolve the right org and credential; provider API calls are metered per app and operation; deploy builds bundle the installed optional ingestion parsers; and MCP `tool-search` can recommend tools for a short task summary.
> - dd24195: Add `agent-native netlify-deploy`, which zips workspace functions deterministically with the installed Netlify CLI's bundler and runs `netlify deploy` in the same command, so unchanged functions keep their digest and are not re-uploaded. It fails with a `manifest-expired` line instead of silently deploying unstable ZIPs.
> - e79c1ae: Comments & Review Kit: the comment box formats. Select text for a bar with bold, italic, strikethrough, code and links, use their shortcuts, or type Markdown as you go, including lists, quotes and code blocks. The box saves Markdown that shows the way it looked, opens a saved comment the way it shows, and reads pasted text as Markdown. `@agent-native/core/review/markdown` converts between a comment's Markdown and the box's document, and `findCommentMentions` in `@agent-native/core/review/plain-text` finds a comment's mentions the way the renderer chips them. Cmd/Ctrl+K in the box opens its link field even in apps whose command menu takes the shortcut from editable text: the command menu now leaves it to any field inside `data-command-menu-shortcut="own"`. The box shows its placeholder again once a comment is sent.
> …

### [@agent-native/dispatch@0.42.8](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/dispatch%400.42.8)
<sub>2026-11-16 · today</sub>

> **Patch Changes**
> - c28f853: A fresh Dispatch install no longer creates the retired, unused `vault_secrets` table. Databases that already have it keep it untouched, and the Vault keeps its keys in `app_secrets`.
> - d9515da: Scope app creation settings writes to their owner.
> - f152dfe: The MCP gateway and workspace app chat proxy forward app context and errors more reliably, and workspace app routes and cards handle mounted app paths.
> - Release all public npm packages with a patch version bump.
> - Updated dependencies [a4a4f9e]
> …

### [@agent-native/recap-cli@0.5.104](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/recap-cli%400.5.104)
<sub>2026-11-16 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

### [@agent-native/scheduling@0.3.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/scheduling%400.3.0)
<sub>2026-11-16 · today</sub>

> **Minor Changes**
> - f152dfe: Booking attendees keep the order they were added in through a new nullable `booking_attendees.position` column (add it in your app's migrations), and calendar and video providers can read credentials and account identity through workspace connections, including a Google Calendar workspace provider and calendar reminders.
> **Patch Changes**
> - Release all public npm packages with a patch version bump.
> - Updated dependencies [a4a4f9e]
> - Updated dependencies [988cdee]
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Add pnpm bench:create to measure a cold create, add-app, and install …](https://github.com/BuilderIO/agent-native/commit/6531e3edd264a06d013d8ebe3f8a1c8bbef08966) | rjcortese |
| 2026-11-17 | [Retry convergence job-list reads on GitHub 5xx errors (#9303)](https://github.com/BuilderIO/agent-native/commit/4e974812a0c1ba4ab1b9c92aa601cd8e58a40491) | builder-io-integration[bot] |
| 2026-11-17 | [Keep the dialog a valid workspace UI leaf (#9304)](https://github.com/BuilderIO/agent-native/commit/0741e053b2fc01ef03857bad11d6e855d286375e) | builder-io-integration[bot] |
| 2026-11-17 | [Core, Toolkit, Dispatch: dialog focus return, popover anchor fix, dur…](https://github.com/BuilderIO/agent-native/commit/3fc244010853a993e79019420ce96e46fb695df8) | steve8708 |
| 2026-11-17 | [Forms: respect text direction in editor and shared forms (#9142)](https://github.com/BuilderIO/agent-native/commit/29757b8de50485897eedca3fb72c1dccfa868f5c) | builder-factory |
| 2026-11-17 | [MCP: open embed tools as full apps in the host side panel (#9213)](https://github.com/BuilderIO/agent-native/commit/2f65a0665d3be97beee63be17bd3577f2c57e1a7) | steve8708 |
| 2026-11-17 | [Keep an Analytics panel's chart in a Content page (#8937)](https://github.com/BuilderIO/agent-native/commit/f6464e106dd585674a71a001f824901ec8946523) | 3mdistal |
| 2026-11-17 | [Draw Analytics' dashboard charts from the toolkit (#9172)](https://github.com/BuilderIO/agent-native/commit/5c2d0ab562b1ac119c9fff2e7ad6a02661cba851) | 3mdistal |
| 2026-11-17 | [Keep approval questions through the action registry, and keep shared …](https://github.com/BuilderIO/agent-native/commit/98fe7e4de26e158602ad7b737394c2f5d050f5ec) | 3mdistal |
| 2026-11-17 | [Make a public Content page's sub-pages public with it, and keep publi…](https://github.com/BuilderIO/agent-native/commit/f53f27f9c5f43563016015970afe7b29dbe4f786) | 3mdistal |

[See all commits ↗](https://github.com/BuilderIO/agent-native/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BuilderIO/agent-native.git
```

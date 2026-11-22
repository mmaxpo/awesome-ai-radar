# shadcn-ui/ui

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/shadcn-ui/ui)

> Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make your own.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why it's worth a look** | shadcn/ui components, CLI, registry and MCP |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 128.7k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/shadcn-ui/ui/issues) |
| 💻 **Languages** | TypeScript 86% · MDX 10% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `components` `nextjs` `radix-ui` `react` `tailwindcss` `ui` `shadcn` `base-ui` `laravel` `tanstack` `vite` `react-aria` `react-aria-components` `ai` `gen-ui` `generative-ai` `generative-ui` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [shadcn@4.23.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.23.0) — 2026-10-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 73.4 MB |
| 🌐 **Website** | https://ui.shadcn.com |

## 📦 Recent releases

### [shadcn@4.23.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.23.0)
<sub>2026-10-27 · 26d ago</sub>

> **Minor Changes**
> - [#12296](https://github.com/shadcn-ui/ui/pull/12296) [`15f59b4`](https://github.com/shadcn-ui/ui/commit/15f59b41750542ef5d41ee34601a85a4e7c1be17) Thanks [@mattzcarey](https://github.com/mattzcarey)! - Upgrade the MCP server to MCP TypeScript SDK v2 (`@modelcontextprotocol/server`). `shadcn mcp` now serves MCP protocol 2026-07-28 as well as earlier versions. The `shadcn/mcp` export is now an `McpServer`, and a new `createServer()` export returns a fresh instance per connection. Code that called `server.setRequestHandler(...)` on the old `Server` export should use `server.registerTool(...)` or `server.server.setRequestHandler(...)` instead.

### [shadcn@4.22.2](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.2)
<sub>2026-10-27 · 26d ago</sub>

> **Patch Changes**
> - [#12479](https://github.com/shadcn-ui/ui/pull/12479) [`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf) Thanks [@dependabot](https://github.com/apps/dependabot)! - Update `undici` to 7.30.1.
> - Updated dependencies [[`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf)]:
>   - @shadcn/registry@0.2.1

### [@shadcn/registry@0.2.1](https://github.com/shadcn-ui/ui/releases/tag/%40shadcn/registry%400.2.1)
<sub>2026-10-27 · 26d ago</sub>

> **Patch Changes**
> - [#12479](https://github.com/shadcn-ui/ui/pull/12479) [`8f04138`](https://github.com/shadcn-ui/ui/commit/8f04138777c1b6996e709993362a7b0a12888ecf) Thanks [@dependabot](https://github.com/apps/dependabot)! - Update `undici` to 7.30.1.

### [shadcn@4.22.1](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.1)
<sub>2026-10-18 · 1mo ago</sub>

> **Patch Changes**
> - [#12360](https://github.com/shadcn-ui/ui/pull/12360) [`4381eeb`](https://github.com/shadcn-ui/ui/commit/4381eeb3fe421af7d25b780f85ff9cbc8d50c51a) Thanks [@shadcn](https://github.com/shadcn)! - Fix `shadcn add --all` and the component picker to only include components available for the project's style.

### [shadcn@4.22.0](https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.0)
<sub>2026-10-16 · 1mo ago</sub>

> **Minor Changes**
> - [#12298](https://github.com/shadcn-ui/ui/pull/12298) [`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115) Thanks [@shadcn](https://github.com/shadcn)! - Upgrade to Zod 4. `shadcn/schema` and `@shadcn/registry/schema` now export Zod 4 schemas, so passing them to Zod 3's `z` no longer typechecks. On Zod 3, use the exported types (`RegistryItem`, `RegistryItemFile`, `Config`) and the schema's own methods (`registryItemSchema.array()`) instead of `z.infer` and `z.array`. Zod errors expose `issues`, not `errors`. Validation messages now use Zod 4's wording.
> **Patch Changes**
> - Updated dependencies [[`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115)]:
>   - @shadcn/registry@0.2.0

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [chore(deps-dev): bump the deps group in /templates/vite-app with 2 up…](https://github.com/shadcn-ui/ui/commit/bfa64ff4d1cb7317d2403ecb176df6826d4caffc) | dependabot[bot] |
| 2026-11-21 | [chore(deps-dev): bump the deps group in /templates/start-app with 2 u…](https://github.com/shadcn-ui/ui/commit/654a6d78ea6754b9c98444cf7bbf5dfe2bf546ce) | dependabot[bot] |
| 2026-11-20 | [chore(deps-dev): bump the deps group (#12775)](https://github.com/shadcn-ui/ui/commit/45bbf9ba23c9c0f63d38887947e5fb06f59c7da3) | dependabot[bot] |
| 2026-11-20 | [chore(deps): bump the deps group (#12779)](https://github.com/shadcn-ui/ui/commit/4e36f8731103654574f02afdcd8543c4a8a9b916) | dependabot[bot] |
| 2026-11-20 | [chore(deps): bump the deps group (#12778)](https://github.com/shadcn-ui/ui/commit/1e6e0ab0d03a48c4b362b0bba6d81934044f30e2) | dependabot[bot] |
| 2026-11-20 | [chore(deps-dev): bump the deps group (#12772)](https://github.com/shadcn-ui/ui/commit/ebc1b168a49ce5c80ff400184ba23ee3395c6b56) | dependabot[bot] |
| 2026-11-20 | [chore(deps-dev): bump the deps group (#12771)](https://github.com/shadcn-ui/ui/commit/4e3495f9a3a8e3c6be1a7cdd19746dd225f15cb0) | dependabot[bot] |
| 2026-11-20 | [chore(deps-dev): bump the deps group (#12769)](https://github.com/shadcn-ui/ui/commit/c02800d2e37757039bacfc3483ef8e6415226265) | dependabot[bot] |
| 2026-11-20 | [chore(deps): bump the deps group in /templates/next-app with 3 update…](https://github.com/shadcn-ui/ui/commit/ad730ab0c3ed38bed560500e575440760db60f5c) | dependabot[bot] |
| 2026-11-19 | [feat(registry): add community registries (#12763)](https://github.com/shadcn-ui/ui/commit/f50887ae68d0fdcbfbe86b57be08af94a4c88a68) | shadcn |

[See all commits ↗](https://github.com/shadcn-ui/ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/shadcn-ui/ui.git
```

# bilawalsidhu/gods-eye-view

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/bilawalsidhu/gods-eye-view)

> A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Live 3D globe of public data feeds |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 65.0k |
| 🍴 **Forks** | 12.8k |
| 🐞 **Open issues + PRs** | [432](https://github.com/bilawalsidhu/gods-eye-view/issues) |
| 💻 **Languages** | JavaScript 96% · CSS 2% · Vue 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `3d-globe` `cesium` `flight-tracking` `geospatial` `geospatial-intelligence` `gis` `osint` `photogrammetry` `satellite-tracking` `spatial-intelligence` `webgl` `worldview` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-06-22 |
| 📦 **Latest release** | [v0.3.0](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.3.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 206.9 MB |
| 🌐 **Website** | https://godseyeview.ai/ |

## 📦 Recent releases

### [v0.3.0](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.3.0) — v0.3.0 — Street Level, On Your Phone, in Your Language
<sub>2026-10-28 · 18d ago</sub>

> v0.3.0 brings God's Eye View down to the street, into your pocket and into three new languages. Open street-level photos from four providers without leaving the globe, use the app on a phone with a layout built for it, and read the interface in Spanish, Russian or Simplified Chinese. Short share links, a rebuilt voice assistant, your own map files, GNSS interference and aircraft emergencies, ten new camera packs and about thirty new bikeshare systems come with it.
> **Street Level**
> <img width="1600"  alt="street-level-panoramax-photo-paris" src="https://github.com/user-attachments/assets/af9d1bc3-ecba-4493-8a09-8d8c1b83a087" />
> See the street from the globe (Cameras ▸ Street Level). Coverage lines drape on the terrain and Google 3D tiles; click a street and the nearest photo opens in the panel, flat or 360°, with view cones along its sequence and ‹ › to step through it.
> - **Four providers, one at a time**: **Panoramax** and **KartaView**, which need no key at all, **Mapillary** with a free client token, and **Google Street View** on the Google 3D map with your Google Maps key.
> - Every caption names the photo's author and licence and links to the original.
> …

### [v0.2.1](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.2.1) — v0.2.1 — God's Eye View through Your Agent (with security fixes and other featur…
<sub>2026-10-03 · 1mo ago</sub>

> v0.2.1 hardens the local server and the MCP panel, shrinks the build, and refines the Cyber HUD. It also catches up on everything new since v0.1.1 that the first v0.2.0 notes left out.
> **Security**
> - **Cross-site requests refused** for the endpoints that cost money or write logs (OpenAI realtime and HUD summary, Google Places, the voice debug log), and the dev and preview servers send one full Content-Security-Policy.
> - **Cost-bearing proxies throttled by default**: 30 requests a minute for OpenAI and 120 for Google per client, the caps Pinokio already ships. `0` opts out, and an unreadable value falls back to the default instead of unlimited.
> - **Host checks everywhere**: the Host check now runs before the app's own routes (they used to answer any Host, including DNS-rebinding names), and binding to all interfaces keeps the check, accepting IP addresses, `localhost` and the LAN names you list.
> - **The MCP server and panel**: the panel's requests need a key from its own page and refuse settings, credential and model routes in any spelling; panels share six requests in flight; `/mcp` applies the same proxy and origin checks as Provider Settings and times out request bodies; embed mode can no longer be framed unless you allow the framing page. [SECURITY.md](https://github.com/bilawalsidhu/gods-eye-view/blob/main/SECURITY.md) describes the MCP surface.
> …

### [v0.2.0](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.2.0) — v0.2.0 — God's Eye View through Your Agent
<sub>2026-10-03 · 1mo ago</sub>

> v0.2.0 brings God's Eye View to your agent: ask Claude, Codex or ChatGPT to show a place, and the live globe opens right in the conversation. It also adds Recent Imagery, drawing and directions, transit, local radio receivers, live weather, thousands more cameras and much more.
> **God's Eye View through your agent**
> - **MCP server and shared tool catalog.** About 40 tools — aircraft, ships, satellites, earthquakes, fires and fire perimeters, launches, CCTV and ALPR cameras, radio, places, routing, transit, traffic, weather, wind, cyclones, recent imagery, infrastructure, military awareness and situation briefs — defined once and used by MCP clients and by voice.
> - **The live globe in the conversation.** In Claude Desktop and the Codex and ChatGPT desktop apps, answers open as an interactive God's Eye View panel at the right place, with the right layers and style, following an aircraft or riding in its cockpit. Every answer also carries a link that opens the full app there.
> - **Works locally, with no HTTPS or tunnel.** The panel loads through the MCP server itself. Setup takes a minute: [docs/MCP_SETUP.md](https://github.com/bilawalsidhu/gods-eye-view/blob/main/docs/MCP_SETUP.md).
> - **Embed mode.** `?embed=1` shows the globe alone for pages that frame the app.
> …

### [v0.1.1](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.1.1) — v0.1.1 — Installation and live-data fixes
<sub>2026-09-01 · 2mo ago</sub>

> v0.1.1 is a reliability patch for one-click setup and live-data ingestion.
> **Fixed**
> - **Pinokio setup:** Completed clean installs now expose **Start** instead of returning to **Install**.
> - **macOS keyless launch:** `./scripts/dev-fresh.sh` no longer crashes under the stock Bash 3.2 runtime when no provider keys are exported.
> - **Active Fires:** All three VIIRS source batches are retained when global record counts exceed the JavaScript engine's argument limit.
> - **GBFS safety:** Response-size limits are now measured in bytes, including multi-byte upstream payloads.
> …

### [v0.1.0](https://github.com/bilawalsidhu/gods-eye-view/releases/tag/v0.1.0) — v0.1.0 — One-click install, keyless boot, Provider Settings
<sub>2026-08-31 · 2mo ago</sub>

> The first formal release: one-click install, a keyless boot that lands on a real satellite globe, and in-app key management.
> **Get started in one click → [Quick Start](https://github.com/bilawalsidhu/gods-eye-view#-quick-start)** — no keys, no signup, no config file.
> **Highlights**
> - **One-click install** via Pinokio. Keyless boot lands on live Esri World Imagery with keyless terrain; OSM takes over automatically if Esri is unreachable, and the globe continues without terrain if its source is unavailable.
> - **Provider Settings** (the POWER UP panel): add, replace, or remove API keys inside the app. Credential files are made owner-only before any secret is written — verified on macOS and Windows — and keys configured outside the panel are shown read-only. The panel answers only local, unproxied requests and disables itself whenever the server is shared.
> - **Keyless capability responses**: the optional HUD summary and place-search endpoints return a deliberate "not configured" success instead of errors, without consuming rate-limit quota.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Merge pull request #1747 from bilawalsidhu/motion/vessels-frame-cadence](https://github.com/bilawalsidhu/gods-eye-view/commit/3d25a284f9186dcc936c26e0c4f745337b402e37) | samehkhamis |
| 2026-11-15 | [Merge branch 'main' into motion/vessels-frame-cadence](https://github.com/bilawalsidhu/gods-eye-view/commit/c2fa15b205107a011e57650f3b150e3ec52f4831) | samehkhamis |
| 2026-11-15 | [Merge pull request #1746 from bilawalsidhu/motion/satellites-dead-reckon](https://github.com/bilawalsidhu/gods-eye-view/commit/ec63345b3b2e4dbd2ec4b6f8eccfb93ff0d04adc) | samehkhamis |
| 2026-11-15 | [fix(vessels): world-clock motion moves only drawn vessels, once per w…](https://github.com/bilawalsidhu/gods-eye-view/commit/52695daf5c8dd97162eb58c0ddc0d2bfecc23a68) | samehkhamis |
| 2026-11-15 | [Add the changelog fragment for #1747](https://github.com/bilawalsidhu/gods-eye-view/commit/7bea88b395b1a606c761b25bb0c9586cf748cdbc) | samehkhamis |
| 2026-11-15 | [Add the changelog fragment for #1746](https://github.com/bilawalsidhu/gods-eye-view/commit/e4afde3317a9a8d58e76787ca9ffee267b24a027) | samehkhamis |
| 2026-11-15 | [Move vessels every frame and ask for frames as they move](https://github.com/bilawalsidhu/gods-eye-view/commit/57bacd98a803ca756b13af0c6aab729889746152) | samehkhamis |
| 2026-11-15 | [Move satellites every frame between SGP4 samples](https://github.com/bilawalsidhu/gods-eye-view/commit/e31de29cccb5a4fe89fa79089ccbafc3d0fa17fc) | samehkhamis |
| 2026-11-15 | [Merge pull request #1745 from bilawalsidhu/timeline/one-control-and-m…](https://github.com/bilawalsidhu/gods-eye-view/commit/e4708a815d012505a60e2f9c7fa57672820dfdd0) | samehkhamis |
| 2026-11-15 | [A row plays only with a timeline to play; the speed shown follows the…](https://github.com/bilawalsidhu/gods-eye-view/commit/ac04812db200f58278eb86bd5f2d6dd6e82863a0) | samehkhamis |

[See all commits ↗](https://github.com/bilawalsidhu/gods-eye-view/commits)

## ⬇️ Get it

```bash
git clone https://github.com/bilawalsidhu/gods-eye-view.git
```

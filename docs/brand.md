# The brand layer

Atelier Podium is DeckCraft with a different name on the door. We keep the change small on purpose:
upstream lands many changes a day, and every file we touch is a file that can conflict when we pull
them in. So:

**Renamed (what a person sees):** the window title and Presenter View title, the Help menu and
About (where Podium comes from, the Nation, this repository), the start screen's name, logo and
Nation link, messages in the UI crate and the apps, the sample deck's notes and closing slide, the
PDF Creator and Producer, Windows file properties, the MCP server title and links, the CLI `links`
output, installer and package names, vendor, links and "Open with" name, the browser page, the app
icon (and the logo the app draws in About and on the start screen), and where settings and recovery
files live (`~/Library/Application Support/Atelier Podium`, `%APPDATA%\Atelier Podium`).

**Not renamed (machine names):** crate names (`deckcraft-*`), the binaries (`deckcraft`,
`deckcraft-cli`), command ids and the `app.links` keys (`discord` is the Nation), the
`ai.storyteller.deckcraft` app id and icon file names in packaging, the `.deckcraft` format, the
default theme named "DeckCraft" (presentations name it), the Application tag in exported .pptx, the
Windows ProgId (`DeckCraft.Presentation`) and upgrade code, environment variables (`DECKCRAFT_*`),
the Linux settings folder, and the docs under `docs/`.

## Where the name lives

| Place | File |
|---|---|
| Links | `crates/engine/src/links.rs` |
| English UI strings | literal `"Atelier Podium"` in `crates/ui-egui/src` and `apps/` |
| About, start screen, in-app logo | `crates/ui-egui/src/dialogs.rs` (`about`, `start_screen`, `paint_logo`) |
| Sample deck | `crates/engine/src/sample.rs` |
| Settings and recovery folders | `apps/deckcraft/src/main.rs`, `crates/engine/src/recovery.rs` |
| PDF Creator and Producer | `crates/pdf/src/lib.rs` |
| MCP and CLI | `crates/mcp/src/{server,backend}.rs`, `apps/deckcraft-cli/src/main.rs` |
| Windows file properties | `apps/deckcraft/build.rs` |
| macOS bundle | `packaging/macos/Info.plist.in` (display name, copyright, document type; identifier unchanged) |
| Windows installer | `packaging/windows/deckcraft.wxs` (names, manufacturer, links, install folder, Open With name; ProgId and upgrade code unchanged) |
| Linux desktop entry, AppStream, nfpm | `packaging/linux/ai.storyteller.deckcraft.*`, `nfpm.yaml` |
| Browser build | `apps/deckcraft-web/index.html` |
| README and NOTICE | README: our header above upstream's feature sections; NOTICE: ours on top of theirs, kept on merge by `.gitattributes` |
| App icon | `assets/app-icon/` (ours: `deckcraft.svg` is the master; rows in `ATTRIBUTION.md`) |

Still upstream's name, for later passes: messages from the engine crates, and the `docs/` manuals.
For the packaging pass (real installers): the macOS `.app` bundle and DMG names
(`packaging/macos/package.sh`), the DMG background, and the package scripts' file names.

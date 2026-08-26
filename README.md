# Rain's Better SMP Modpack

NeoForge-Modpack für Minecraft 1.21.1: Erkundung (Biomes O' Plenty, die YUNG's-Serie,
Towns and Towers, Trek, Terralith, Repurposed Structures), die komplette Farmer's-Delight-
Familie, Performance-Mods (Embeddium, ModernFix, FerriteCore, Distant Horizons, ...) sowie
Karten/QoL (Xaero's Minimap/Worldmap, Waystones, Simple Voice Chat, Sophisticated
Backpacks/Storage, VeinMiner, ...).

Die vollständige Modliste steht in [`modlist.json`](modlist.json). Konkrete Versionen werden
**nicht** eingecheckt, sondern bei jedem CI-Lauf frisch gegen die Modrinth-API aufgelöst
(neueste NeoForge-1.21.1-kompatible Version pro Mod, inkl. automatisch nachgezogener
Pflicht-Abhängigkeiten wie Kotlin for Forge oder Cloth Config).

## Installation

Die neuesten Builds gibt es unter [Releases](../../releases) (wird automatisch bei jedem
Push auf `main`, wöchentlich und manuell per `workflow_dispatch` neu gebaut):

- **`rains-better-smp-modpack.mrpack`** — Modrinth-Pack-Format. Import über die
  [Modrinth App](https://modrinth.com/app), Prism Launcher oder ATLauncher
  (Datei → Modpack importieren).
- **`rains-better-smp-modpack-client.zip`** — Dropin-ZIP für einen bestehenden
  NeoForge-1.21.1-Client: Inhalt in den `mods/`-Ordner des Instanzprofils entpacken.
- **`rains-better-smp-modpack-server.zip`** — Dropin-ZIP für den Server: Inhalt in den
  `mods/`-Ordner eines laufenden NeoForge-1.21.1-Servers entpacken. Enthält nur Mods, die
  serverseitig tatsächlich gebraucht werden (rein clientseitige Mods wie Xaero's Minimap
  werden ausgelassen).

Die passende NeoForge-Loader-Version steht im Build-Log bzw. in `dist/resolved-versions.json`
des jeweiligen Runs.

## Modliste ändern

`modlist.json` bearbeiten (Modrinth-Slug hinzufügen/entfernen) und pushen — die Pipeline
löst Versionen, Dateien und Pflicht-Abhängigkeiten beim nächsten Lauf automatisch neu auf.

## Lokal bauen

```bash
pip install -r requirements.txt
python scripts/build_pack.py
# Ergebnis liegt in dist/
```

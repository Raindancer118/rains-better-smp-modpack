# Rain's Better SMP Modpack

A NeoForge modpack for Minecraft 1.21.1: exploration and world generation (Biomes O'
Plenty, Terralith, the YUNG's series, Towns and Towers, Trek), the full Farmer's Delight
family, performance mods (Embeddium, ModernFix, FerriteCore, Distant Horizons, ...) and a
big pile of navigation/QoL/visual mods (Xaero's Minimap & World Map, Waystones,
Sophisticated Backpacks/Storage, Simple Voice Chat, VeinMiner, ...).

Mod versions are never checked into git — `scripts/build_pack.py` resolves the newest
NeoForge/1.21.1-compatible version of every mod straight from the Modrinth API on every
CI run, and automatically pulls in required dependencies (shared libraries etc.) that
aren't listed explicitly.

## Modlist
<!-- MODLIST:START -->

### Exploration & Structures

| Mod | Version |
|---|---|
| [Biomes O' Plenty](https://modrinth.com/mod/biomes-o-plenty) | `21.1.0.14` |
| [Terralith](https://modrinth.com/mod/terralith) | `2.6.2` |
| [Repurposed Structures - Neoforge/Forge](https://modrinth.com/mod/repurposed-structures-forge) | `7.5.22+1.21.1-neoforge` |
| [YUNG's API](https://modrinth.com/mod/yungs-api) | `1.21.1-NeoForge-5.1.8` |
| [YUNG's Better Nether Fortresses](https://modrinth.com/mod/yungs-better-nether-fortresses) | `1.21.1-NeoForge-3.1.5` |
| [YUNG's Better Ocean Monuments](https://modrinth.com/mod/yungs-better-ocean-monuments) | `1.21.1-NeoForge-4.1.2` |
| [YUNG's Better Dungeons](https://modrinth.com/mod/yungs-better-dungeons) | `1.21.1-NeoForge-5.1.4` |
| [YUNG's Better Mineshafts](https://modrinth.com/mod/yungs-better-mineshafts) | `1.21.1-NeoForge-5.1.1` |
| [YUNG's Better Jungle Temples](https://modrinth.com/mod/yungs-better-jungle-temples) | `1.21.1-NeoForge-3.1.2` |
| [YUNG's Better End Island](https://modrinth.com/mod/yungs-better-end-island) | `1.21.1-NeoForge-3.1.2` |
| [YUNG's Better Strongholds](https://modrinth.com/mod/yungs-better-strongholds) | `1.21.1-NeoForge-5.1.3` |
| [YUNG's Better Witch Huts](https://modrinth.com/mod/yungs-better-witch-huts) | `1.21.1-NeoForge-4.1.1` |
| [YUNG's Better Desert Temples](https://modrinth.com/mod/yungs-better-desert-temples) | `1.21.1-NeoForge-4.1.5` |
| [YUNG's Bridges](https://modrinth.com/mod/yungs-bridges) | `1.21.1-NeoForge-5.1.1` |
| [YUNG's Extras](https://modrinth.com/mod/yungs-extras) | `1.21.1-NeoForge-5.1.1` |
| [Dungeons and Taverns](https://modrinth.com/mod/dungeons-and-taverns) | `v4.4.4+mod` |
| [Towns and Towers](https://modrinth.com/mod/towns-and-towers) | `1.13.11` |
| [Trek](https://modrinth.com/mod/trek) | `B0.6.2+mod` |

### Farmer's Delight Family

| Mod | Version |
|---|---|
| [Farmer's Delight](https://modrinth.com/mod/farmers-delight) | `1.21.1-1.3.4` |
| [Chef's Delight - Farmer's Delight Villagers](https://modrinth.com/mod/chefs-delight) | `1.0.5` |
| [Veggies Delight (A Farmer's Delight Add-on)](https://modrinth.com/mod/veggies-delight) | `1.9.3` |
| [End's Delight](https://modrinth.com/mod/ends-delight) | `2.6.1+neoforge.1.21.1` |
| [Expanded Delight](https://modrinth.com/mod/expanded-delight) | `0.1.4-neoforge` |
| [My Nether's Delight](https://modrinth.com/mod/my-nethers-delight) | `1.10.4.1` |
| [Rustic Delight](https://modrinth.com/mod/rustic-delight) | `1.7.1` |
| [Fruits Delight](https://modrinth.com/mod/fruits-delight) | `1.2.14` |
| [ExtraDelight](https://modrinth.com/mod/extradelight) | `2.6.6` |
| [More Delight (for Farmer's Delight)](https://modrinth.com/mod/more-delight) | `26.05.20a-1.21-neoforge` |
| [The Lost Castle](https://modrinth.com/mod/the-lost-castle) | `2.1.0` |
| [Ocean's Delight](https://modrinth.com/mod/oceans-delight) | `1.0.4` |

### Ocean & Creatures

| Mod | Version |
|---|---|
| [Hybrid Aquatic](https://modrinth.com/mod/hybrid-aquatic) | `mc1.21.1-1.7.0-neoforge` |
| [Ecologics](https://modrinth.com/mod/ecologics) | `2.3.7-NeoForge` |

### Performance

| Mod | Version |
|---|---|
| [Embeddium](https://modrinth.com/mod/embeddium) | `1.0.15+mc1.21.1` |
| [ModernFix](https://modrinth.com/mod/modernfix) | `5.27.24+mc1.21.1` |
| [FerriteCore](https://modrinth.com/mod/ferrite-core) | `7.0.3-neoforge` |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) | `1.6.14+1.21.1-neoforge` |
| [Entity Culling](https://modrinth.com/mod/entityculling) | `1.10.5` |
| [Cull Leaves](https://modrinth.com/mod/cull-leaves) | `4.1.1+1.21.1-neoforge` |
| [Dynamic FPS](https://modrinth.com/mod/dynamic-fps) | `3.11.4` |
| [Distant Horizons](https://modrinth.com/mod/distanthorizons) | `3.2.0-b-1.21.1` |

### Storage & Inventory

| Mod | Version |
|---|---|
| [Sophisticated Backpacks](https://modrinth.com/mod/sophisticated-backpacks) | `1.21.1-3.26.3.2158` |
| [Sophisticated Storage](https://modrinth.com/mod/sophisticated-storage) | `1.21.1-1.5.91.2127` |
| [Inventory Profiles Next](https://modrinth.com/mod/inventory-profiles-next) | `neoforge-1.21.1-2.2.5` |
| [Mouse Tweaks](https://modrinth.com/mod/mouse-tweaks) | `1.21-2.26.1-neoforge` |
| [VeinMiner](https://modrinth.com/mod/veinminer) | `2.11.2` |

### Navigation & Travel

| Mod | Version |
|---|---|
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | `neoforge-1.21.1-26.5.0` |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | `neoforge-1.21.1-1.46.0` |
| [Xaero's Minimap & World Map - Waystones Compatibility](https://modrinth.com/mod/xaeros-minimap-world-map-waystones-compatibility-forge) | `2.1.0` |
| [Waystones](https://modrinth.com/mod/waystones) | `21.1.45+neoforge-1.21.1` |
| [Paragliders](https://modrinth.com/mod/paragliders) | `21.1.5` |
| [Elytra Slot](https://modrinth.com/mod/elytra-slot) | `9.0.2+1.21.1` |
| [Elytra Trims](https://modrinth.com/mod/elytra-trims) | `3.10.0` |
| [Elytra Trims Extensions](https://modrinth.com/mod/elytra-trims-extensions) | `2.2.2` |
| [Boat Item View](https://modrinth.com/mod/boat-item-view) | `1.21-1.21.1-0.0.6-neoforge` |
| [Just Zoom](https://modrinth.com/mod/just-zoom) | `2.1.0-1.21.1-neoforge` |

### Visuals & Social

| Mod | Version |
|---|---|
| [3D Skin Layers](https://modrinth.com/mod/3dskinlayers) | `1.11.2` |
| [[ETF] Entity Texture Features](https://modrinth.com/mod/entitytexturefeatures) | `7.2.1-neoforge-1.21` |
| [[EMF] Entity Model Features](https://modrinth.com/mod/entity-model-features) | `3.3.5-neoforge-1.21` |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations) | `1.12.4` |
| [Chat Heads](https://modrinth.com/mod/chat-heads) | `0.15.7` |
| [Handcrafted](https://modrinth.com/mod/handcrafted) | `4.0.3` |
| [MmmMmmMmmMmm](https://modrinth.com/mod/mmmmmmmmmmmm) | `1.21-2.1.1` |
| [Continuity](https://modrinth.com/mod/continuity) | `3.0.0+1.21.neoforge` |
| [Sound Physics Remastered](https://modrinth.com/mod/sound-physics-remastered) | `neoforge-1.21.1-1.5.1` |
| [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat) | `neoforge-1.21.1-2.6.23` |

### Building & Decoration

| Mod | Version |
|---|---|
| [Macaw's Bridges](https://modrinth.com/mod/macaws-bridges) | `3.1.2` |
| [Chipped](https://modrinth.com/mod/chipped) | `4.0.2` |

### Utility

| Mod | Version |
|---|---|
| [Just Enough Items (JEI)](https://modrinth.com/mod/jei) | `19.56.0.438` |
| [Open Parties and Claims](https://modrinth.com/mod/open-parties-and-claims) | `neoforge-1.21.1-0.31.6` |
| [Comforts](https://modrinth.com/mod/comforts) | `9.0.5+1.21.1` |
| [AppleSkin](https://modrinth.com/mod/appleskin) | `3.0.9+mc1.21` |

### Libraries (required dependencies)

| Mod | Version |
|---|---|
| [Balm](https://modrinth.com/mod/balm) | `21.0.65+neoforge-1.21.1` |
| [Athena](https://modrinth.com/mod/athena-ctm) | `4.0.6` |
| [Biolith](https://modrinth.com/mod/biolith) | `3.0.14` |
| [Cloth Config API](https://modrinth.com/mod/cloth-config) | `15.0.140+neoforge` |
| [Sinytra Connector](https://modrinth.com/mod/connector) | `2.0.0-beta.17+1.21.1` |
| [Cristel Lib](https://modrinth.com/mod/cristel-lib) | `neoforge-1.21.1-3.1.7` |
| [Curios API](https://modrinth.com/mod/curios) | `9.5.1+1.21.1` |
| [Delight Lib](https://modrinth.com/mod/delight-lib) | `26.05.18-1.21-neoforge` |
| [Forgified Fabric API](https://modrinth.com/mod/forgified-fabric-api) | `0.116.15+2.3.5+1.21.1` |
| [Geckolib](https://modrinth.com/mod/geckolib) | `4.9.2` |
| [GlitchCore](https://modrinth.com/mod/glitchcore) | `2.1.0.2` |
| [Konkrete](https://modrinth.com/mod/konkrete) | `1.9.9-1.21-neoforge` |
| [Kotlin for Forge](https://modrinth.com/mod/kotlin-for-forge) | `5.12.0` |
| [KotlinLangForge](https://modrinth.com/mod/kotlin-lang-forge) | `2.13.0-k2.4.20-3.0+neoforge` |
| [libIPN](https://modrinth.com/mod/libipn) | `neoforge-1.21.1-6.6.3` |
| [Lithostitched](https://modrinth.com/mod/lithostitched) | `1.8.0+beta6-neoforge-21.1` |
| [MidnightLib](https://modrinth.com/mod/midnightlib) | `1.9.3+1.21.1-neoforge` |
| [Moonlight Lib](https://modrinth.com/mod/moonlight) | `1.21.1-3.6.4` |
| [Resourceful Lib](https://modrinth.com/mod/resourceful-lib) | `3.0.12` |
| [Sophisticated Core](https://modrinth.com/mod/sophisticated-core) | `1.21.1-1.5.1.2341` |
| [TerraBlender](https://modrinth.com/mod/terrablender) | `4.1.0.8` |

### Other

| Mod | Version |
|---|---|
| [Caelus API](https://modrinth.com/mod/caelus) | `7.0.1+1.21.1` |
| [Hybrid API](https://modrinth.com/mod/hybrid-api) | `mc1.21.1-1.1.0-neoforge` |
| [MezzConfig](https://modrinth.com/mod/mezzconfig) | `0.5.7` |
<!-- MODLIST:END -->

## Installation

The latest build is always available under [Releases](../../releases) (rebuilt
automatically on every push, weekly, and on demand via `workflow_dispatch`):

- **`rains-better-smp-modpack.mrpack`** — Modrinth pack format. Import via the
  [Modrinth App](https://modrinth.com/app), Prism Launcher or ATLauncher
  (File → Import modpack).
- **`rains-better-smp-modpack-client.zip`** — dropin zip for an existing NeoForge
  1.21.1 client: extract into the instance's `mods/` folder.
- **`rains-better-smp-modpack-server.zip`** — dropin zip for the server: extract into the
  `mods/` folder of a running NeoForge 1.21.1 server. Only contains mods that are actually
  needed server-side (purely client-side mods like Xaero's Minimap are left out).
- **`resolved-versions.json`** — exact version/filename of every mod in that build, for
  traceability.

The matching NeoForge loader version is printed in the build log.

## Changing the modlist

Edit `modlist.json` (add/remove a Modrinth slug) and push — the pipeline re-resolves
versions, files and required dependencies on the next run, and updates the modlist table
above automatically.

## Building locally

```bash
pip install -r requirements.txt
python scripts/build_pack.py
# output lands in dist/
```

## License / Credits

All mods belong to their respective authors (see the Modrinth links above). This repo
does not check in any mod jars — only the generated release assets (`.mrpack`/`.zip`).

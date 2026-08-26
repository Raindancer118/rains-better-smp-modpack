#!/usr/bin/env python3
"""Resolves the mod list against the Modrinth API and builds:
- a .mrpack (Modrinth modpack format) for the Modrinth App / Prism / MultiMC
- a client dropin zip (mods/ folder to copy into an existing instance)
- a server dropin zip (mods/ folder to copy onto a NeoForge server)

Mod versions are always resolved fresh against the live Modrinth API, so the
pack automatically tracks the newest compatible build of every mod at build
time. Required dependencies that aren't already in modlist.json are pulled in
transitively (e.g. shared library mods).
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

import requests

API = "https://api.modrinth.com/v2"
NEOFORGE_MAVEN = "https://maven.neoforged.net/api/maven/versions/releases/net/neoforged/neoforge"
HEADERS = {"User-Agent": "rains-better-smp-modpack/1.0 (github.com/Raindancer118)"}

ROOT = Path(__file__).resolve().parent.parent
MODLIST_PATH = ROOT / "modlist.json"
README_PATH = ROOT / "README.md"
MODLIST_START = "<!-- MODLIST:START -->"
MODLIST_END = "<!-- MODLIST:END -->"

# Order = order of the headings in the README. Slugs that aren't listed here
# (e.g. a newly pulled-in required dependency) automatically land under "Other".
CATEGORIES = {
    "Exploration & Structures": [
        "biomes-o-plenty", "terralith", "repurposed-structures-forge", "yungs-api",
        "yungs-better-nether-fortresses", "yungs-better-ocean-monuments", "yungs-better-dungeons",
        "yungs-better-mineshafts", "yungs-better-jungle-temples", "yungs-better-end-island",
        "yungs-better-strongholds", "yungs-better-witch-huts", "yungs-better-desert-temples",
        "yungs-bridges", "yungs-extras", "dungeons-and-taverns", "towns-and-towers", "trek",
    ],
    "Farmer's Delight Family": [
        "farmers-delight", "chefs-delight", "veggies-delight", "ends-delight", "expanded-delight",
        "my-nethers-delight", "rustic-delight", "fruits-delight", "extradelight", "more-delight",
        "the-lost-castle", "oceans-delight",
    ],
    "Ocean & Creatures": ["hybrid-aquatic", "ecologics"],
    "Performance": [
        "embeddium", "modernfix", "ferrite-core", "immediatelyfast", "entityculling",
        "cull-leaves", "dynamic-fps", "distanthorizons",
    ],
    "Storage & Inventory": [
        "sophisticated-backpacks", "sophisticated-storage", "inventory-profiles-next",
        "mouse-tweaks", "veinminer",
    ],
    "Navigation & Travel": [
        "xaeros-minimap", "xaeros-world-map", "xaeros-minimap-world-map-waystones-compatibility-forge",
        "waystones", "paragliders", "elytra-slot", "elytra-trims", "elytra-trims-extensions",
        "boat-item-view", "just-zoom",
    ],
    "Visuals & Social": [
        "3dskinlayers", "entitytexturefeatures", "entity-model-features", "not-enough-animations",
        "chat-heads", "handcrafted", "mmmmmmmmmmmm", "continuity", "sound-physics-remastered",
        "simple-voice-chat",
    ],
    "Building & Decoration": ["macaws-bridges", "chipped"],
    "Utility": ["jei", "open-parties-and-claims", "comforts", "appleskin"],
    "Libraries (required dependencies)": [
        "balm", "athena-ctm", "biolith", "cloth-config", "connector", "cristel-lib", "curios",
        "delight-lib", "forgified-fabric-api", "geckolib", "glitchcore", "konkrete",
        "kotlin-for-forge", "kotlin-lang-forge", "libipn", "lithostitched", "midnightlib",
        "moonlight", "resourceful-lib", "sophisticated-core", "terrablender",
    ],
}


def api_get(path: str, **params):
    r = requests.get(f"{API}{path}", params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def latest_neoforge_version(mc_version: str) -> str:
    branch = mc_version.removeprefix("1.")  # "21.1" for mc "1.21.1"
    r = requests.get(NEOFORGE_MAVEN, headers=HEADERS, timeout=30)
    r.raise_for_status()
    versions = [v for v in r.json()["versions"] if v.startswith(f"{branch}.")]
    if not versions:
        raise SystemExit(f"No NeoForge release found for Minecraft {mc_version}")

    def sort_key(v: str):
        return [int(p) for p in v.split(".")]

    return sorted(versions, key=sort_key)[-1]


class Resolver:
    def __init__(self, mc_version: str, loader: str):
        self.mc_version = mc_version
        self.loader = loader
        self.projects: dict[str, dict] = {}
        self.versions: dict[str, dict] = {}
        self.missing: list[str] = []

    def project(self, slug_or_id: str) -> dict:
        if slug_or_id not in self.projects:
            self.projects[slug_or_id] = api_get(f"/project/{slug_or_id}")
        return self.projects[slug_or_id]

    def best_version(self, slug_or_id: str) -> dict | None:
        versions = api_get(
            f"/project/{slug_or_id}/version",
            loaders=json.dumps([self.loader]),
            game_versions=json.dumps([self.mc_version]),
        )
        if not versions:
            return None
        versions.sort(key=lambda v: v["date_published"], reverse=True)
        return versions[0]

    def resolve_all(self, seed_slugs: list[str]) -> dict[str, dict]:
        queue = list(dict.fromkeys(seed_slugs))
        seen_projects: set[str] = set()

        while queue:
            slug = queue.pop(0)
            try:
                project = self.project(slug)
            except requests.exceptions.HTTPError:
                self.missing.append(f"{slug} (project not found)")
                continue
            project_id = project["id"]
            if project_id in seen_projects:
                continue
            seen_projects.add(project_id)

            version = self.best_version(slug)
            if version is None:
                self.missing.append(project["title"])
                continue

            self.versions[project_id] = {"project": project, "version": version}

            for dep in version.get("dependencies", []):
                if dep.get("dependency_type") != "required":
                    continue
                dep_project_id = dep.get("project_id")
                if not dep_project_id or dep_project_id in seen_projects:
                    continue
                queue.append(dep_project_id)

        return self.versions


def env_side(value: str) -> str:
    # Modrinth project fields ("required"/"optional"/"unsupported") map 1:1
    # onto mrpack's env values.
    return value if value in ("required", "optional", "unsupported") else "unsupported"


def build_mrpack(resolved: dict[str, dict], mc_version: str, loader: str, loader_version: str,
                  pack_name: str, pack_summary: str, pack_version: str, out_path: Path) -> None:
    files = []
    for entry in resolved.values():
        project, version = entry["project"], entry["version"]
        primary = next((f for f in version["files"] if f["primary"]), version["files"][0])
        files.append({
            "path": f"mods/{primary['filename']}",
            "hashes": {
                "sha1": primary["hashes"]["sha1"],
                "sha512": primary["hashes"]["sha512"],
            },
            "env": {
                "client": env_side(project.get("client_side", "required")),
                "server": env_side(project.get("server_side", "required")),
            },
            "downloads": [primary["url"]],
            "fileSize": primary["size"],
        })

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": pack_version,
        "name": pack_name,
        "summary": pack_summary,
        "files": sorted(files, key=lambda f: f["path"]),
        "dependencies": {
            "minecraft": mc_version,
            loader: loader_version,
        },
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("modrinth.index.json", json.dumps(index, indent=2))
        z.writestr("overrides/README.txt", "No config overrides shipped with this pack.\n")


def build_dropin_zip(resolved: dict[str, dict], side: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for entry in resolved.values():
            project, version = entry["project"], entry["version"]
            side_value = project.get(f"{side}_side", "required")
            if side_value == "unsupported":
                continue
            primary = next((f for f in version["files"] if f["primary"]), version["files"][0])
            jar_bytes = requests.get(primary["url"], headers=HEADERS, timeout=60).content
            z.writestr(f"mods/{primary['filename']}", jar_bytes)


def build_categorized_modlist_markdown(resolved: dict[str, dict]) -> str:
    by_slug = {entry["project"]["slug"]: entry for entry in resolved.values()}
    seen: set[str] = set()
    lines = []

    for category, slugs in CATEGORIES.items():
        cat_slugs = [s for s in slugs if s in by_slug]
        if not cat_slugs:
            continue
        seen.update(cat_slugs)
        lines.append(f"\n### {category}\n")
        lines.append("| Mod | Version |")
        lines.append("|---|---|")
        for slug in cat_slugs:
            entry = by_slug[slug]
            title = entry["project"]["title"]
            version_number = entry["version"]["version_number"]
            lines.append(f"| [{title}](https://modrinth.com/mod/{slug}) | `{version_number}` |")

    leftover = sorted(set(by_slug) - seen)
    if leftover:
        lines.append("\n### Other\n")
        lines.append("| Mod | Version |")
        lines.append("|---|---|")
        for slug in leftover:
            entry = by_slug[slug]
            lines.append(f"| [{entry['project']['title']}](https://modrinth.com/mod/{slug}) | `{entry['version']['version_number']}` |")

    return "\n".join(lines) + "\n"


def update_readme_modlist(resolved: dict[str, dict]) -> None:
    content = README_PATH.read_text()
    start = content.index(MODLIST_START) + len(MODLIST_START)
    end = content.index(MODLIST_END)
    modlist_md = build_categorized_modlist_markdown(resolved)
    README_PATH.write_text(content[:start] + "\n" + modlist_md + content[end:])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--pack-version", default="dev")
    args = parser.parse_args()

    modlist = json.loads(MODLIST_PATH.read_text())
    mc_version = modlist["minecraft_version"]
    loader = modlist["loader"]

    print(f"Resolving {len(modlist['mods'])} seed mods for {loader} {mc_version} ...")
    resolver = Resolver(mc_version, loader)
    resolved = resolver.resolve_all(modlist["mods"])

    if resolver.missing:
        print("ERROR: no compatible version found for:", file=sys.stderr)
        for name in resolver.missing:
            print(f"  - {name}", file=sys.stderr)
        sys.exit(1)

    print(f"Resolved {len(resolved)} mods (including transitive dependencies).")
    loader_version = latest_neoforge_version(mc_version)
    print(f"Using NeoForge {loader_version}.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output_dir / "resolved-versions.json"
    manifest_path.write_text(json.dumps(
        {
            pid: {
                "title": e["project"]["title"],
                "version_number": e["version"]["version_number"],
                "filename": next((f for f in e["version"]["files"] if f["primary"]), e["version"]["files"][0])["filename"],
            }
            for pid, e in resolved.items()
        },
        indent=2,
    ))

    build_mrpack(
        resolved, mc_version, loader, loader_version,
        pack_name=modlist["name"],
        pack_summary=modlist["summary"],
        pack_version=args.pack_version,
        out_path=args.output_dir / "rains-better-smp-modpack.mrpack",
    )
    print("Built .mrpack")

    build_dropin_zip(resolved, "client", args.output_dir / "rains-better-smp-modpack-client.zip")
    print("Built client dropin zip")

    build_dropin_zip(resolved, "server", args.output_dir / "rains-better-smp-modpack-server.zip")
    print("Built server dropin zip")

    update_readme_modlist(resolved)
    print("Updated README.md modlist section")


if __name__ == "__main__":
    main()

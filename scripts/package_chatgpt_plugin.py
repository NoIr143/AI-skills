#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
SKILLS_DIR = ROOT / "skills"
IGNORED_NAMES = {".DS_Store", ".gitkeep"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}


def included_files() -> list[Path]:
    files = [MANIFEST]
    files.extend(
        path
        for path in SKILLS_DIR.rglob("*")
        if path.is_file()
        and path.name not in IGNORED_NAMES
        and path.suffix not in IGNORED_SUFFIXES
        and "__pycache__" not in path.parts
    )
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def add_deterministic(archive: zipfile.ZipFile, path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, path.read_bytes())


def package(output: Path) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("skills") != "./skills/":
        raise ValueError("plugin manifest must point skills to ./skills/")

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        raise ValueError("plugin archive requires at least one skills/<name>/SKILL.md")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as archive:
        for path in included_files():
            add_deterministic(archive, path)

    with zipfile.ZipFile(output) as archive:
        names = set(archive.namelist())
    if ".codex-plugin/plugin.json" not in names:
        raise ValueError("archive is missing .codex-plugin/plugin.json")
    if not all(path.relative_to(ROOT).as_posix() in names for path in skill_files):
        raise ValueError("archive is missing one or more skill entry points")

    print(f"Created {output} with {len(names)} files")


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    default_output = ROOT / "dist" / f"ai-skills-{manifest['version']}.zip"
    parser = argparse.ArgumentParser(
        description="Create a skills-only ZIP for the ChatGPT plugin submission portal."
    )
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()
    package(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

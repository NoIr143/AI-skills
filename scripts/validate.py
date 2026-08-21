#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_platform_manifests() -> list[str]:
    errors: list[str] = []
    codex = read_json(ROOT / ".codex-plugin" / "plugin.json")
    claude = read_json(ROOT / ".claude-plugin" / "plugin.json")
    claude_marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")

    if codex.get("name") != claude.get("name"):
        errors.append("Codex and Claude Code plugin names must match")
    if codex.get("version") != claude.get("version"):
        errors.append("Codex and Claude Code plugin versions must match")
    if codex.get("skills") != "./skills/":
        errors.append("Codex plugin must load the shared ./skills/ directory")

    plugins = claude_marketplace.get("plugins", [])
    matching_plugins = [plugin for plugin in plugins if plugin.get("name") == claude.get("name")]
    if len(matching_plugins) != 1 or matching_plugins[0].get("source") != "./":
        errors.append("Claude Code marketplace must expose the repository-root plugin")

    return errors


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["frontmatter must start with ---"]

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, ["frontmatter is missing its closing ---"]

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")

    return metadata, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not NAME_PATTERN.fullmatch(skill_dir.name):
        errors.append("directory name must use lowercase kebab-case")
    if not skill_file.is_file():
        return errors + ["missing SKILL.md"]

    metadata, parse_errors = parse_frontmatter(skill_file)
    errors.extend(parse_errors)
    extra_keys = sorted(set(metadata) - {"name", "description"})

    if metadata.get("name") != skill_dir.name:
        errors.append("frontmatter name must match the directory name")
    if not metadata.get("description"):
        errors.append("frontmatter description is required")
    if extra_keys:
        errors.append(f"unsupported frontmatter keys: {', '.join(extra_keys)}")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("skills directory does not exist", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    failures = 0

    for error in validate_platform_manifests():
        failures += 1
        print(f"ERROR platforms: {error}", file=sys.stderr)

    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            for error in errors:
                print(f"ERROR {skill_dir.name}: {error}", file=sys.stderr)
        else:
            print(f"OK {skill_dir.name}")

    if failures:
        print(f"Validation failed with {failures} error group(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

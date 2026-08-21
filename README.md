# AI Skills

Personal, reusable skills for AI coding agents. Each skill lives in `skills/<skill-name>/` and must contain a `SKILL.md` file.

## Repository layout

```text
skills/                 Reusable skill folders
scripts/install.sh      Install one or all skills
scripts/validate.py     Validate every skill
manifest.json           Repository metadata
```

Do not store passwords, API keys, access tokens, production data, or private customer information in a skill.

## Add a skill

Create `skills/<skill-name>/SKILL.md` with only `name` and `description` in its YAML frontmatter:

```markdown
---
name: review-code-changes
description: Review commits and code changes for correctness, security, regressions, and missing tests. Use when asked to review a diff, commit, branch, or pull request.
---

# Review code changes

1. Inspect repository instructions and the requested diff.
2. Verify each finding against surrounding code.
3. Report actionable findings in severity order.
```

Optional folders are `agents/`, `scripts/`, `references/`, and `assets/`.

## Validate

```bash
python3 scripts/validate.py
```

## Install

Install all skills for Codex:

```bash
bash scripts/install.sh codex
```

Install selected skills:

```bash
bash scripts/install.sh codex review-code-changes understand-ticket
```

Codex uses `$HOME/.agents/skills` for user-level skills. The installer creates symbolic links, so pulling repository updates also updates installed skills.

Claude Code can use the same skill source through an adapter target:

```bash
bash scripts/install.sh claude
```

Override either destination when necessary:

```bash
AI_SKILLS_TARGET_DIR=/custom/path bash scripts/install.sh codex
```


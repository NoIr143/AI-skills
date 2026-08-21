# AI Skills

Personal, reusable skills for AI coding agents. Each skill lives in `skills/<skill-name>/` and must contain a `SKILL.md` file.

## Repository layout

```text
.agents/plugins/        Codex marketplace catalog
.claude-plugin/         Claude Code marketplace metadata
.codex-plugin/          Codex plugin metadata
skills/                 Reusable skill folders
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

## Install over the network

No installer script or local repository checkout is required. The plugin host downloads this private repository from GitHub and installs every skill in `skills/`.

Your Git credentials must have access to `NoIr143/AI-skills` because the repository is private.

### Codex CLI

Add this repository as a marketplace:

```bash
codex plugin marketplace add NoIr143/AI-skills --ref main
```

Install the skill bundle:

```bash
codex plugin add ai-skills@noir143-ai-skills
```

Refresh after repository updates:

```bash
codex plugin marketplace upgrade noir143-ai-skills
```

You can also run `/plugins` inside Codex and install `AI Skills` from the `NoIr143 AI Skills` marketplace.

### Claude Code

Add the same GitHub repository as a marketplace:

```bash
/plugin marketplace add NoIr143/AI-skills
```

Install the bundle:

```bash
/plugin install ai-skills@noir143-ai-skills
```

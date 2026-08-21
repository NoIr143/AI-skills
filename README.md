# AI Skills

One private, network-installable skill collection for both Codex and Claude Code. Each portable skill lives in `skills/<skill-name>/` and has a single `SKILL.md` source of truth.

## Cross-platform model

- `skills/` contains the shared Agent Skills used by both platforms. Do not duplicate skill instructions in platform-specific folders.
- `.codex-plugin/` and `.agents/plugins/` expose the shared skills to Codex.
- `.claude-plugin/` exposes the same shared skills to Claude Code.
- `skills/*/agents/openai.yaml` is optional Codex interface metadata. Claude Code ignores it and reads the shared `SKILL.md`.
- Keep `SKILL.md` frontmatter portable: use only `name` and `description`. Put workflow and tool constraints in the Markdown body.

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

When publishing a change, bump the version in both `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`. The validator rejects version drift and confirms that both platforms resolve the shared `skills/` directory.

## Validate

```bash
python3 scripts/validate.py
```

## Available skills

| Skill | Codex | Claude Code | Purpose |
|---|---|---|---|
| Generate PR Description | `$generate-pr-description` | `/ai-skills:generate-pr-description` | Produce a verified PR description from a diff. |
| SDLC Planning | `$sdlc-planning` | `/ai-skills:sdlc-planning` | Define scope, goals, roles, estimates, risks, governance, and project readiness. |
| SDLC Analysis | `$sdlc-analysis` | `/ai-skills:sdlc-analysis` | Gather detailed requirements and produce a traceable, verifiable SRS. |

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

Invoke the included PR description skill:

```text
$generate-pr-description HEAD~1
```

### Claude Code

Add the same GitHub repository as a marketplace:

```bash
/plugin marketplace add NoIr143/AI-skills
```

Install the bundle:

```bash
/plugin install ai-skills@noir143-ai-skills
```

Reload updated plugins when Claude Code asks you to, then invoke the namespaced skill:

```text
/ai-skills:generate-pr-description HEAD~1
```

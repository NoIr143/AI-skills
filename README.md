# AI Skills

One private, installable skill collection for ChatGPT Work, Codex, and Claude Code. Each portable skill lives in `skills/<skill-name>/` and has a single `SKILL.md` source of truth.

## Cross-platform model

- `skills/` contains the shared Agent Skills used by both platforms. Do not duplicate skill instructions in platform-specific folders.
- `.codex-plugin/` and `.agents/plugins/` package the shared skills for ChatGPT Work and Codex.
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
scripts/package_chatgpt_plugin.py  Build a skills-only ChatGPT upload ZIP
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

| Skill | ChatGPT Work | Codex | Claude Code | Purpose |
|---|---|---|---|---|
| Generate PR Description | `@generate-pr-description` | `$generate-pr-description` | `/ai-skills:generate-pr-description` | Produce a verified PR description from a diff. |
| SDLC Planning | `@sdlc-planning` | `$sdlc-planning` | `/ai-skills:sdlc-planning` | Define scope, goals, roles, estimates, risks, governance, and project readiness. |
| SDLC Analysis | `@sdlc-analysis` | `$sdlc-analysis` | `/ai-skills:sdlc-analysis` | Gather detailed requirements and produce a traceable, verifiable SRS. |
| SDLC Design | `@sdlc-design` | `$sdlc-design` | `/ai-skills:sdlc-design` | Map architecture, UI, interfaces, and database models from an approved SRS. |
| SDLC Coding | `@sdlc-coding` | `$sdlc-coding` | `/ai-skills:sdlc-coding` | Implement approved requirements and design as secure, tested, traceable production code. |
| SDLC Testing | `@sdlc-testing` | `$sdlc-testing` | `/ai-skills:sdlc-testing` | Find functional, security, performance, and quality problems with reproducible evidence. |

## Install and use in ChatGPT Web — Work mode

ChatGPT Web loads these skills through an installed plugin. It does not install a private GitHub repository URL directly from the Work composer.

### Private workspace distribution

1. On a computer whose Git credentials can access this private repository, add the marketplace and install the plugin through Codex CLI or the ChatGPT desktop plugin browser:

```bash
codex plugin marketplace add NoIr143/AI-skills --ref main
codex plugin add ai-skills@noir143-ai-skills
```

2. As a ChatGPT workspace admin, open [ChatGPT Plugins](https://chatgpt.com/plugins), select **Personal**, open the **AI Skills** menu, choose **Publish**, and select the workspace roles that may use it.
3. Start a new ChatGPT Web **Work** chat, type `@`, and choose a bundled skill such as `@sdlc-planning`.

Publishing this way keeps the plugin inside the selected ChatGPT workspace. It does not publish the private repository to the public Plugins Directory. Workspace publishing requires admin permission and may be disabled by workspace policy.

### Skills-only upload package

Build the deterministic ZIP accepted by the OpenAI plugin submission portal:

```bash
python3 scripts/package_chatgpt_plugin.py
```

The output is `dist/ai-skills-<version>.zip`. GitHub Actions also attaches the same package to every validation run. In the submission portal, choose **Create plugin → Skills only**, upload the ZIP, review the normalized manifest, test every skill, and complete the required listing and review fields.

Public submission requires the appropriate OpenAI Platform permission and verified developer or business identity. It is not required for private workspace publishing.

## Install over the network for developer clients

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

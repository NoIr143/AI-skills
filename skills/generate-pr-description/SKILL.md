---
name: generate-pr-description
description: Generate a concise, copy-paste-ready pull request description with Description, Key changes, and Impacts sections from a commit, commit range, or current branch diff. Use when asked to draft or update a PR description, summarize code changes for reviewers, trace changed API values to user-visible screens, or identify compatibility and working-tree warnings before opening a pull request.
---

# Generate PR Description

Generate a pull request description for the requested change and return it as one copy-paste-ready Markdown block.

Use only shell commands, file reads, grep, and glob-style file discovery. Do not modify project source files.

## Input

Treat the text supplied with the skill invocation as the target:

- A commit SHA, tag, `HEAD~1`, or other commit-ish: describe that single commit.
- A range such as `base..head`: describe the complete range.
- No target: describe the current branch against `master`, using `git merge-base HEAD master` to find the base.

## Inspect the actual change

Do not infer behavior from the commit message alone.

1. Run `git log --format='%H%n%an%n%ad%n%s%n%b' <target>` to obtain commit metadata and the ticket ID.
2. Run `git show --stat <target>`, then inspect the full diff of every changed file. For a range or branch comparison, use the equivalent `git diff` commands.
3. Read enough surrounding source to explain why the change is correct:
   - Find callers for every changed symbol.
   - Find where changed fields and values are produced and consumed.
   - Follow data one hop beyond the diff into views, API responses, or database columns.
   - Check whether other code paths already behave as the change now makes this path behave.
4. When a changed value reaches an API response, enumerate the endpoint's consumers before writing:
   - Search the endpoint path across front-end sources, view templates, and built bundles.
   - Follow store constants and component props to every page that mounts the consumer.
   - Verify that the changed value is actually rendered.
5. Resolve user-facing URIs from routing configuration, such as `apps/*/application/config/routes.php`, rather than deriving them from controller names.
6. Run `git status`, `git diff`, and `git diff --cached`. If uncommitted changes revert or alter the target, report a warning after the generated description.

## Write the description

Use exactly the following three sections. Keep the result short enough to read in under one minute.

```markdown
## Description

<Write 2-4 plain sentences with no code. Explain what the user saw wrong, or what is now possible,
and what happens now. Make it understandable without opening the diff.>

## Key changes

- `path/to/file.ext` (`function_name()`, line N): <Explain what changed and briefly name the cause it addresses. Put every technical detail here. Use one line per file.>

## Impacts

| Screen | Change |
|---|---|
| <Screen name (`/uri/path`)> | <What the user now sees> |

<Add the API table only when a changed API value is actually displayed on a screen. Omit it otherwise.>

| API | Change | Used by |
|---|---|---|
| `GET /api/...` | <What the payload now returns and where it appears> | <Screen name (`/uri`), Screen name (`/uri`)> |

<Close with one line covering data migration, compatibility, and relevant non-changes such as DB schema, API contract, front-end build, or forced re-login.>
```

## Apply content rules

### Description

- Write at most four sentences and no bullets.
- Do not include code, identifiers, function or class names, file paths, variables, columns, backticks, root-cause details, call chains, or unchanged code paths.
- Use plain user-facing wording, such as "the account name shown in the logs."
- Move all technical detail to Key changes.

### Key changes

- Reference files as plain backticked paths, never Markdown links.
- Use one line per changed file.
- Include the changed symbol and a useful line number when the source provides one.
- Explain both the change and the cause it addresses.
- Obtain ticket IDs such as `EDT-1234` from commit messages only. Never invent one.

### Impacts

- List only screens and user-visible entry points, not internal call sites or refactoring notes.
- Format every screen as `<screen name> (<URI>)`, using the name a QA tester would recognize and the browser URI from routing configuration.
- Keep route placeholders readable, for example `/stream/{id}/logs` or `/event/{show_id}`.
- Group screens that share the same change into one Screen table row.
- If an endpoint feeds one screen, prefer a Screen row. Use an API row only when naming a shared endpoint clarifies a change used by multiple screens.
- Include an API only when its changed value is verified as rendered on a screen.
- Do not list an API whose changed field is only used for matching, filtering, or lookup. Mention external or unknown consumer risk in the closing note instead.
- For every listed API, enumerate all consuming screens in one `Used by` cell. Follow endpoint paths, store constants, `url` or `urlSearch` props, parent components, view templates, and built bundles. Never write "and others."
- If a consumer is outside the repository, say so explicitly.
- If there is no user-visible screen impact, replace the table with one direct sentence instead of forcing rows.

Write in the language used by the repository's existing commit messages. Default to English unless the repository primarily uses Japanese.

## Save and return the result

1. Derive the ticket ID from the commit message. Use `NO-TICKET` when no ticket ID exists.
2. Save the description as `pr-<TICKET-ID>.md` in the environment's designated scratchpad directory. If no scratchpad directory is configured, use `.scratchpad` at the repository root and create it when needed.
3. Print the description in chat inside a four-backtick fenced block so its inner Markdown remains copyable.
4. Add nothing after the block except working-tree warnings found during inspection.


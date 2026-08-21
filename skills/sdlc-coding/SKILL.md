---
name: sdlc-coding
description: Implement production-quality software functions from an approved SRS and system design. Use when writing, changing, integrating, or completing application code, APIs, user interfaces, database migrations, background jobs, infrastructure configuration, or automated tests while preserving requirement and design traceability, repository conventions, security, compatibility, and verifiable implementation evidence before independent testing or release.
---

# SDLC Coding

Convert approved requirements and design into the smallest complete, working implementation. Produce actual repository changes and verification evidence, not a prose-only coding plan.

Read [references/standards.md](references/standards.md) before implementation. Read [references/implementation-checklist.md](references/implementation-checklist.md) before declaring completion. Treat standards as guidance; do not claim certification or formal compliance.

## Establish the implementation baseline

Read repository instructions and inspect the current working tree before editing. Preserve unrelated user changes and never overwrite, revert, reformat, stage, or commit them.

Use the latest approved SRS, system design, ADRs, interface contracts, data model, UI specifications, acceptance criteria, and delivery task. Inspect the surrounding source, tests, dependency manifests, build configuration, migrations, schemas, routes, generated clients, CI workflows, and similar existing implementations.

Classify inputs as:

- **Approved**: baselined requirement, design, contract, or decision.
- **Constraint**: repository, platform, compatibility, policy, or operational limit.
- **Assumption**: temporary proposition requiring validation.
- **Open**: unresolved issue capable of changing behavior or public contracts.

Do not silently design missing behavior. Return requirement gaps to `sdlc-analysis` and architecture, UI, data, or interface gaps to `sdlc-design`. Return scope, schedule, staffing, or cost changes to `sdlc-planning`.

Ask at most five grouped questions when missing information materially changes behavior, security, data integrity, compatibility, or acceptance. Otherwise implement the safe, well-defined subset and report the blocked remainder.

## Pass the coding entry gate

Start implementation only when the selected slice has:

- requirement and design identifiers or clearly labeled non-normative source anchors;
- observable acceptance criteria;
- defined inputs, outputs, errors, permissions, state changes, and side effects;
- stable interface, persisted-record, event, audit, and data contracts where applicable;
- resolved consequential ADRs;
- a known verification method and runnable environment, or an explicit limitation.

Mark the task `BLOCKED` when a missing decision could cause an incompatible API, unsafe authorization, destructive migration, data loss, privacy violation, or incorrect critical behavior. Do not invent credentials, production data, endpoints, schemas, or business rules to bypass the gate.

Do not infer fields or semantics for public DTOs, persisted records, audit entries, events, outbox messages, migrations, or third-party payloads. If the selected acceptance criteria require an undefined contract, mark that portion `BLOCKED` and identify the exact decision needed from `sdlc-analysis` or `sdlc-design`. Infer an internal representation only when it is fully encapsulated, existing repository conventions provide clear precedent, and it cannot affect persistence, interoperability, security, observability, or compatibility; report the inference as an assumption.

## Select an implementation slice

Implement one coherent vertical slice at a time. Trace it as:

`requirement → acceptance criterion → design element → code change → automated check → result`

Define the slice boundary, impacted components, compatibility constraints, risks, and verification commands before editing. Prefer the smallest end-to-end change that delivers observable behavior over many partially connected layers.

Keep identifiers such as `FR-###`, `ARC-###`, `UI-###`, `DATA-###`, `INT-###`, and `ADR-###` in the implementation report, tests, or existing traceability mechanism. Do not scatter requirement IDs through production code unless repository convention requires it.

## Implement in the repository

### Follow existing engineering conventions

Match the repository's language version, architecture, module boundaries, naming, formatting, dependency injection, error handling, logging, configuration, test style, and tooling. Reuse established abstractions only when they fit the required behavior. Do not add a new framework, dependency, service, or pattern without documented need and compatibility review.

Make focused changes. Avoid unrelated refactors, speculative abstractions, premature optimization, generated-file edits without their source, and mass formatting. Remove temporary debug code and dead branches created by the change.

### Implement behavior completely

Cover the approved success, alternate, validation, authorization, failure, timeout, retry, cancellation, recovery, concurrency, and idempotency paths that apply to the slice. Preserve invariants across layers and ensure side effects occur exactly under the specified conditions.

Use precise domain types and explicit boundaries. Validate untrusted input at a trusted boundary, canonicalize before comparison where required, encode output for its destination, and avoid leaking internal or sensitive details through errors or logs.

Handle resources deliberately: transactions, connections, files, streams, locks, memory, timeouts, cancellation, and cleanup. Avoid unbounded reads, loops, retries, queues, payloads, or concurrency. Make retry policies bounded and compatible with idempotency.

### Implement interfaces and integrations

Keep implementations aligned with approved API, event, file, and third-party contracts. Preserve versioning and backward compatibility for known consumers. Define consistent validation and error mapping; do not expose implementation exceptions as public responses.

For state-changing operations, implement the specified duplicate-request and stale-state behavior. For asynchronous work, preserve delivery semantics, ordering assumptions, deduplication, retry, dead-letter, replay, observability, and user-visible side-effect rules.

Regenerate contract-derived artifacts using repository commands and review the generated diff. Never hand-edit generated output when an authoritative schema or generator exists.

### Implement data changes safely

Enforce required identifiers, relationships, uniqueness, nullability, checks, and referential behavior in the correct layer. Use explicit transactions and the designed isolation or concurrency control. Derive queries and indexes from approved access patterns, and inspect their plans when performance is material.

For zero-downtime schema changes, follow expand, migrate, verify, and contract phases. Maintain mixed-version compatibility for the approved window. Make backfills restartable and bounded, provide reconciliation evidence, and keep destructive changes behind the approved retirement and rollback gate.

Never execute destructive production data operations, deploy, rotate secrets, or modify live infrastructure unless the user explicitly requests and authorizes the exact action.

### Implement user interfaces faithfully

Map code to the approved `UI-###` screens, routes, component states, content, responsive behavior, and design-system tokens. Implement applicable loading, empty, partial, success, validation-error, system-error, offline or degraded, permission-denied, session-expiry, stale-data, and destructive-confirmation states.

Use semantic elements and accessible names, keyboard operation, visible focus, announced status and validation, adequate contrast, non-color cues, reflow, and motion preferences according to the approved WCAG level. Do not replace the approved design with generic UI or hard-coded styling that bypasses the project system.

## Build security into the code

Apply the approved threat model, data classification, authorization matrix, and security requirements. At minimum, inspect applicable authentication and session handling, access control, input validation, output encoding, injection defenses, secrets, cryptography, sensitive-data storage, log redaction, audit integrity, file handling, outbound requests, dependency risk, abuse controls, and error disclosure.

Use maintained platform security primitives rather than custom cryptography or authentication. Use parameterized data access, least privilege, secure defaults, explicit allowlists where appropriate, and constant-time comparisons for secrets when supported. Never place secrets, tokens, private keys, production records, or sensitive fixtures in source code, tests, logs, or prompts.

Record the applicable NIST SSDF or OWASP ASVS control identifiers when the project already uses them. Do not claim a security control is satisfied without code or verification evidence.

## Add implementation-level tests

Add or update tests in the same slice. Use the repository's test pyramid and include the lowest-cost test that proves each acceptance criterion:

- unit tests for domain rules and edge cases;
- integration or contract tests for boundaries, persistence, APIs, events, and external adapters;
- component or UI tests for important interactions and states;
- regression tests that fail before a bug fix and pass after it;
- migration, concurrency, security, or performance checks when required by risk or acceptance criteria.

Test negative paths and boundary values, not only happy paths. Keep tests deterministic, isolated, readable, and independent of production systems. Mock only external boundaries; avoid tests that merely repeat implementation logic.

Independent system, acceptance, exploratory, penetration, and release testing remain later SDLC activities. Coding tests support them but do not replace them.

## Verify incrementally

Run the narrowest relevant check after each meaningful change, then the broader repository checks before completion. Use documented project commands for formatting, linting, type checking, compilation, unit tests, integration tests, contract validation, migration validation, security scanning, and builds.

Do not report a check as passed unless it ran successfully. If a check cannot run, record the exact command, reason, affected confidence, and safe next action. Distinguish failures caused by the change from pre-existing or environment failures with evidence.

Inspect the final diff, working tree, generated artifacts, and dependency changes. Confirm that no debug output, secret, unrelated edit, accidental lockfile churn, or unsupported compatibility break remains.

## Report the implementation

Return a concise implementation report containing:

- completion status: `DONE`, `PARTIAL`, or `BLOCKED`;
- implemented behavior and user-visible result;
- changed files and their responsibilities;
- traceability from requirements and design to tests;
- commands run and results;
- migrations, compatibility, configuration, rollout, and rollback notes;
- assumptions, unresolved items, residual risks, and follow-up testing.

Do not create an extra implementation document unless the user or repository requires one. Commit, push, open a pull request, deploy, or mutate external systems only when authorized by the request.

## Enforce the coding exit gate

Declare `DONE` only when:

- the selected acceptance criteria are implemented and traceable;
- code follows the approved design or deviations are documented and approved;
- applicable error, authorization, concurrency, recovery, accessibility, and compatibility paths are implemented;
- tests cover the changed behavior and relevant regression risk;
- required formatting, static analysis, compilation, tests, contract checks, and builds pass;
- data changes are reversible or protected by the approved migration gate;
- security-sensitive behavior has implementation and verification evidence;
- the final diff contains only intended changes;
- deployment, configuration, observability, and follow-up testing needs are explicit.

Use `PARTIAL` when a safe subset is complete but identified work remains. Use `BLOCKED` when proceeding would require inventing behavior, weakening controls, breaking a contract, risking data, or bypassing required evidence. Never fabricate completion.

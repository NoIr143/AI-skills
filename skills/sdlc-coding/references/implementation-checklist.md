# Implementation completion checklist

Use this checklist after implementing the selected slice. Mark each item `PASS`, `FAIL`, `BLOCKED`, or `N/A` with evidence; explain every `N/A` that could reasonably apply.

## Baseline and scope

- Repository instructions and working-tree state were inspected.
- Requirement, acceptance, design, interface, and data baselines are identified.
- Public DTO, persisted-record, audit, event, outbox, and third-party payload schemas needed by the slice are defined rather than inferred.
- The diff is limited to the selected vertical slice.
- Assumptions, deviations, and blocked behavior are visible.

## Behavior

- Success and relevant alternate, validation, failure, recovery, timeout, and cancellation paths are implemented.
- Authorization, state transitions, concurrency, idempotency, and side effects match the design.
- Public errors are stable and do not leak internals.
- Resources, bounds, cleanup, and retry behavior are explicit.

## Interfaces, data, and UI

- API, event, file, and external contracts remain compatible or use the approved versioning plan.
- Data invariants, transactions, query patterns, and migrations match the approved model.
- Backfills are bounded, restartable, reconcilable, and compatible with rollback where applicable.
- UI screens, states, responsive behavior, design tokens, content, and accessibility match the approved design.

## Security and privacy

- Authentication, session, and authorization behavior were checked where applicable.
- Untrusted input, output encoding, injection, file, and outbound-request risks were addressed.
- Secrets, cryptography, sensitive storage, logs, errors, audit evidence, and dependencies were checked.
- No credential, private key, production record, or sensitive fixture was introduced.

## Tests and tooling

- Tests prove each selected acceptance criterion and meaningful negative path.
- Relevant formatter, linter, type checker, compiler, unit, integration, contract, migration, security, and build commands ran.
- Failures and skipped checks include commands, causes, confidence impact, and next actions.
- Generated artifacts and lockfile changes were produced intentionally and reviewed.

## Handoff

- Requirement-to-design-to-code-to-test traceability is recorded.
- Configuration, migration, rollout, rollback, observability, and follow-up testing are documented.
- The final diff and working tree were inspected for unrelated changes and debug artifacts.
- Status is honestly reported as `DONE`, `PARTIAL`, or `BLOCKED`.

---
name: sdlc-testing
description: Test implemented software for functional defects, security vulnerabilities, performance regressions, reliability problems, compatibility issues, accessibility failures, and unmet acceptance criteria. Use after coding or when validating a commit, branch, build, release candidate, API, UI, migration, integration, or deployed test environment through risk-based test planning, static and dynamic analysis, reproducible test execution, defect reporting, requirement traceability, and an evidence-based quality decision before deployment.
---

# SDLC Testing

Evaluate implemented software against its approved requirements and design. Run real checks and produce reproducible evidence; do not substitute a checklist or opinion for test execution.

Read [references/standards.md](references/standards.md) before planning. Read [references/test-report-template.md](references/test-report-template.md) before reporting. Treat standards as guidance; do not claim certification or formal compliance.

## Establish the test basis

Read repository instructions and inspect the working tree before acting. Preserve unrelated user changes. Identify the exact test item: commit, diff, branch, build, artifact, release candidate, endpoint, screen, migration, or environment.

Use the approved SRS, system design, ADRs, interface and data contracts, UI specifications, threat model, acceptance criteria, implementation report, changed code, tests, dependency changes, configuration, migrations, CI history, and known defects. Treat observed legacy behavior as a test oracle only when an authoritative baseline confirms it.

Classify each test expectation as:

- **Required**: defined by an approved requirement, contract, design, or acceptance criterion.
- **Regression**: established behavior that the selected change must preserve.
- **Exploratory**: a risk-driven hypothesis without a normative expected result.
- **Open**: missing or contradictory information that prevents a valid verdict.

Do not invent expected behavior. Return requirement gaps to `sdlc-analysis`, design or contract gaps to `sdlc-design`, and incomplete implementation to `sdlc-coding`.

## Pass the testing entry gate

Begin execution when the selected scope has:

- an identifiable build, revision, artifact, and environment;
- testable acceptance criteria or a clearly labeled exploratory objective;
- known interfaces, data shapes, roles, permissions, and critical quality thresholds;
- suitable test data and isolated dependencies;
- commands or safe access paths for the intended test levels;
- authorization for any active security, load, destructive, or external-system testing.

If important inputs are missing, run the safe and meaningful subset and mark the rest `BLOCKED`. Never infer a passing result from unavailable evidence.

## Plan by risk

Build a compact risk matrix using impact, likelihood, change complexity, exposure, reversibility, and detection difficulty. Prioritize safety, security, privacy, financial or data integrity, critical user journeys, public contracts, concurrency, migrations, and high-volume paths.

Trace coverage as:

`requirement/risk → test condition → test case → execution result → evidence → defect`

Assign stable identifiers such as `TC-###` for test cases and `DEF-###` for defects. Preserve existing IDs where the project already has a test-management convention.

Select only useful test levels and types:

- static review, linting, type checking, SAST, dependency and secret scanning;
- unit, component, integration, contract, system, end-to-end, acceptance, and regression;
- exploratory, state-transition, concurrency, recovery, migration, compatibility, accessibility, security, and performance testing.

Use equivalence partitions, boundary values, decision tables, state transitions, use-case scenarios, pairwise combinations, property-based tests, fuzzing, or mutation testing where they increase defect-detection value. Avoid duplicating the same assertion across every level.

Define scope, exclusions, environment, data, preconditions, test order, expected results, evidence, stop conditions, and exit criteria before expensive or high-risk execution.

## Inspect before dynamic execution

Read the changed implementation and one hop of its callers and consumers. Review control flow, data flow, trust boundaries, error handling, transactions, locks, retries, timeouts, idempotency, resource bounds, logging, configuration, generated artifacts, and dependency changes.

Run repository-provided formatter checks, linters, type checkers, compilers, static analyzers, secret scanners, dependency checks, contract validators, and test discovery commands when available. Treat tool output as evidence to investigate, not automatic proof of a defect or absence of defects.

## Test functional behavior

Execute tests for approved success, alternate, validation, authorization, failure, timeout, cancellation, recovery, retry, concurrency, and duplicate-request paths. Cover boundary values, empty and malformed inputs, invalid states, ordering, time zones, precision, encoding, large inputs, partial dependency failures, and repeat execution where relevant.

Verify externally observable results and side effects: responses, UI states, persisted data, events, audit records, notifications, logs, metrics, and cleanup. Confirm failed operations do not leave partial writes or duplicate effects.

For regression testing, select tests from changed behavior, callers, consumers, shared contracts, data migrations, configuration, and previously fixed defects. Do not rely only on new happy-path tests.

## Test security safely

Derive security tests from the threat model, data classification, authorization matrix, security requirements, and applicable OWASP ASVS or WSTG controls. Consider:

- identity, authentication, session, authorization, object and function access;
- input validation, injection, output encoding, deserialization, file handling, and path traversal;
- SSRF and outbound requests, redirects, cross-origin behavior, CSRF, and browser controls;
- secrets, cryptography, sensitive storage and transport, log redaction, and error disclosure;
- rate limits, resource exhaustion, replay, race conditions, abuse cases, audit integrity, and dependency risk.

Confirm scanner findings against source, configuration, or a minimal reproducible test before reporting them as vulnerabilities. Distinguish exploitable defects, defense-in-depth gaps, configuration risks, and unverified hypotheses.

Use synthetic, non-sensitive test data. Do not exfiltrate data, persist access, evade monitoring, brute-force accounts, degrade service, or exploit beyond the minimum safe proof. Never run active security tests against production or third-party systems without explicit authorization for the exact target, techniques, time window, and stop conditions. Redact secrets and harmful payload details from shared evidence.

## Test performance scientifically

Start from approved performance, capacity, availability, and resource thresholds. Define the workload model: user journeys or operations, request mix, concurrency or arrival rate, data volume, payload sizes, cache state, test duration, ramp pattern, geography or network assumptions, and dependency behavior.

Record environment and build fingerprints. Warm up runtimes where applicable, keep test conditions comparable, run enough samples to expose variance, and separate client-side limits from system limits.

Measure at least throughput, error rate, latency distribution such as p50/p95/p99, and relevant resource saturation. Include queue depth, connection pools, locks, garbage collection, database plans and waits, network, disk I/O, or downstream latency when they can explain results.

Compare results with explicit thresholds and a valid baseline. Report sample count, duration, variance, outliers, and measurement limitations. Do not claim a regression from a single noisy run or compare unlike environments.

Use a production-like isolated environment for load, stress, soak, spike, and capacity tests. Never load test production without explicit authorization, monitoring, rollback capability, rate ceilings, owner presence, and stop conditions.

## Test data, migrations, resilience, and UX

For data or schema changes, test forward migration, mixed-version operation, backfill restartability, reconciliation, constraints, rollback boundary, retention, and destructive-change gates using disposable copies or synthetic data.

For reliability, test specified dependency failures, retries, timeouts, circuit breaking, failover, restart, replay, backup/restore, and degraded behavior without causing uncontrolled impact.

For user interfaces, test the approved screens, roles, navigation, responsive layouts, keyboard flows, focus, labels, validation announcements, contrast, zoom/reflow, motion preferences, loading, empty, error, offline, permission, session-expiry, stale-data, and destructive-action states. Use automated accessibility checks as a supplement to manual keyboard and assistive-technology testing, not a replacement.

## Record evidence and defects

For every execution, record test ID, timestamp, revision/build, environment, data, command or steps, expected result, actual result, status, and evidence location. Use `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `INCONCLUSIVE`; do not convert blocked or inconclusive tests into passes.

Report each confirmed defect with:

- stable ID and concise title;
- affected requirement, design element, version, and environment;
- severity based on user/business/security impact and likelihood;
- priority kept separate from severity;
- minimal reproducible steps or test;
- expected and actual behavior;
- logs, traces, screenshots, profiles, queries, or other sanitized evidence;
- scope, frequency, workaround, suspected area, and confidence;
- regression status and recommended owner.

Lead with findings ordered by severity. Do not report style preferences as defects, and do not assert a root cause unless evidence supports it. Record duplicate findings once and link affected cases.

Do not change production code while performing a test-only request. Add or adjust test code, fixtures, and test configuration only when authorized by the task and keep those changes separate from defect remediation. Fix defects only when the user explicitly expands the scope.

## Produce the test report

Follow [references/test-report-template.md](references/test-report-template.md). Write in the user's language unless requested otherwise. Use the requested destination. If no destination is given and the repository requires test artifacts, save to `docs/TEST_REPORT.md`; otherwise return the complete report in chat.

Set the overall decision to:

- `PASS`: required tests and exit criteria pass, with no unresolved release-blocking defect.
- `PASS WITH RISKS`: required evidence passes, but explicitly accepted residual risks or non-blocking gaps remain.
- `FAIL`: a confirmed defect violates a required acceptance or release criterion.
- `BLOCKED`: missing basis, environment, authorization, data, or tooling prevents a defensible decision.

Never equate “tests passed” with proof that no defects exist. State tested scope, excluded scope, confidence, and residual risk.

## Enforce the testing exit gate

Before returning the verdict, verify that:

- the exact revision, build, environment, scope, and test basis are recorded;
- risk-based coverage traces to requirements, design, interfaces, and changed code;
- critical functional, negative, authorization, concurrency, recovery, and regression paths were addressed;
- applicable security findings were safely confirmed and sanitized;
- performance results use a defined workload, stable measurements, thresholds, and environment evidence;
- migrations, compatibility, accessibility, resilience, and data integrity were tested where applicable;
- every result has reproducible evidence and every defect has impact and expected behavior;
- skipped, blocked, inconclusive, flaky, and environment-failed tests remain visible;
- the overall decision follows from explicit exit criteria.

If evidence is incomplete, return the useful results already obtained and lower confidence or mark the decision `BLOCKED`. Never fabricate execution, coverage, or quality.

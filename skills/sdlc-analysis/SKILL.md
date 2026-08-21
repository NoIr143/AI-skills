---
name: sdlc-analysis
description: Elicit, analyze, validate, document, and baseline detailed software requirements in a Software Requirements Specification (SRS). Use after project planning or when converting ideas, planning baselines, briefs, tickets, stakeholder input, existing-system behavior, APIs, data models, or regulations into functional requirements, use cases, non-functional requirements, interface and data requirements, acceptance criteria, verification methods, and end-to-end traceability before architecture, design, or implementation.
---

# SDLC Analysis

Produce an evidence-based Software Requirements Specification that stakeholders can validate and engineering teams can design, estimate, implement, and test.

Read [references/standards.md](references/standards.md) before analyzing requirements. Read [references/srs-template.md](references/srs-template.md) before writing the final document. Treat standards as guidance; do not claim formal compliance or certification.

## Establish the analysis baseline

Start from the latest approved planning baseline when available. Inspect supplied briefs, tickets, interview notes, contracts, policies, diagrams, repository documentation, source code, tests, routes, APIs, schemas, UI flows, logs, and existing SRS files before asking questions.

Classify every important statement as:

- **Confirmed**: directly supported by an authoritative source.
- **Derived**: logically necessary to satisfy another confirmed requirement; record the derivation.
- **Assumed**: a temporary proposition that requires validation.
- **Proposed**: a recommendation that has not been approved.
- **Open**: unresolved and capable of changing requirements or design.

Never convert assumptions or observed legacy behavior into approved requirements without labeling them. Record contradictions with their sources instead of choosing silently.

Ask at most five grouped questions per round. Prioritize questions that affect system boundary, actors, business rules, data ownership, interfaces, security, acceptance, or release scope. If answers are unavailable, continue with explicit `TBD` items, owners, and decision dates.

## Elicit complete behavior

Identify:

- stakeholders, user classes, external systems, administrators, operators, and support roles;
- business goals, user outcomes, scope boundaries, constraints, and success measures inherited from planning;
- normal workflows, alternate flows, failure paths, recovery, cancellation, retry, timeout, and concurrency behavior;
- business rules, state transitions, permissions, approvals, notifications, audit events, and reporting needs;
- data inputs, outputs, ownership, validation, lifecycle, retention, deletion, migration, and sensitivity;
- user interfaces, APIs, events, files, devices, protocols, third-party services, and operational interfaces;
- applicable quality, security, privacy, accessibility, localization, compliance, and operational expectations.

Do not design the solution during requirements analysis. Record mandated technologies or protocols only when they are genuine constraints. Separate what the system must achieve from how it may be implemented.

## Model the requirement set

### Define context and actors

Describe the system of interest, its boundary, external actors, upstream and downstream systems, trust boundaries, and major information flows. Use a small context diagram when it materially clarifies three or more relationships; accompany it with text so the SRS remains understandable without the diagram.

### Define use cases and scenarios

For each meaningful user goal, capture:

- ID and name;
- primary and secondary actors;
- trigger and preconditions;
- main success flow;
- alternate and exception flows;
- postconditions and observable outcome;
- related business rules, data, and requirements.

Use scenarios to discover requirements. Do not treat a scenario as a substitute for atomic requirements.

### Write atomic requirements

Assign stable identifiers:

- `BR-###` for business rules;
- `FR-###` for functional requirements;
- `NFR-<CATEGORY>-###` for quality requirements;
- `IR-<TYPE>-###` for interface requirements;
- `DR-###` for data requirements.

Preserve existing IDs when updating an SRS. Mark removed requirements as retired or superseded rather than renumbering the set.

Write one observable obligation per statement using this form when suitable:

`The <system or component> shall <observable behavior> <condition or trigger> <measurable constraint>.`

Use event, state, optional-feature, or failure conditions where they remove ambiguity. Avoid vague terms such as fast, intuitive, robust, appropriate, normally, and user-friendly unless paired with a measurable definition.

For every requirement, capture:

- statement;
- rationale and source;
- priority and release allocation;
- acceptance criteria;
- verification method and evidence;
- dependencies and trace links;
- status and owner;
- unresolved assumptions or `TBD` values.

### Specify functional behavior

Cover inputs, processing rules, decisions, outputs, state changes, permissions, validation, errors, retries, idempotency, concurrency, auditability, and side effects when relevant. Define externally observable behavior without prescribing internal classes, functions, tables, or services unless the existing system or contract makes them constraints.

### Specify quality requirements

Use the ISO/IEC 25010 product-quality model as a coverage checklist, then retain only relevant and measurable characteristics. Consider:

- functional suitability;
- performance efficiency;
- compatibility;
- interaction capability;
- reliability;
- security;
- maintainability;
- flexibility;
- safety.

Express workloads, environments, thresholds, percentiles, duration, failure conditions, recovery objectives, measurement method, and acceptance evidence. Replace “the system shall be scalable” with a measurable capacity and response requirement under a defined workload.

### Specify interfaces and data

For each interface, define direction, actors, purpose, protocol or format constraints, inputs, outputs, validation, authentication and authorization, error semantics, timeouts, retries, compatibility, rate or volume expectations, and ownership.

For data, define conceptual entities, meaning, source of truth, identifiers, validation, relationships, lifecycle, retention, deletion, privacy classification, residency, audit, migration, reconciliation, and quality rules. Do not invent physical schemas during analysis.

## Validate and baseline

Review each requirement for necessity, singularity, clarity, completeness, consistency, feasibility, verifiability, correctness against its source, and conformity to the chosen format.

Build bidirectional traceability:

`planning goal → stakeholder need/use case → requirement → acceptance criterion → verification method`

Detect and report:

- goals, scenarios, or requirements without downstream coverage;
- requirements without a source, owner, acceptance criterion, or verification method;
- conflicting requirements or business rules;
- undefined terms and inconsistent vocabulary;
- hidden solution decisions;
- missing negative paths and operational behavior;
- `TBD` items without an owner and target decision date;
- scope additions that require planning reapproval or re-estimation.

Set the SRS status to `Draft`, `In review`, `Approved`, or `Changed after baseline` only when supported by evidence. Never mark it approved on behalf of stakeholders.

## Create the SRS

Follow [references/srs-template.md](references/srs-template.md). Write in the user's language unless requested otherwise. Keep normative requirement keywords such as `shall` consistent within the chosen language.

Use the requested destination. If no destination is given and a repository is available, save to `docs/SRS.md`; otherwise return the complete SRS in chat. When updating an existing SRS, preserve its history, IDs, and approved content unless the evidence authorizes a change.

After the document, report separately:

- blocking questions;
- assumptions requiring validation;
- scope changes that must return to `sdlc-planning`;
- readiness for architecture/design: `READY`, `CONDITIONALLY READY`, or `NOT READY`.

Do not implement product code, create architecture, or select technology unless the user explicitly expands the task.

## Enforce the analysis gate

Before returning the SRS, verify that:

- scope matches the planning baseline or deviations are flagged;
- every actor and external system appears in at least one scenario or interface;
- functional requirements cover success, alternate, failure, and recovery behavior;
- relevant quality requirements are measurable;
- security and privacy requirements include verification evidence;
- interfaces and data ownership are explicit;
- every requirement has a stable ID, source, rationale, priority, owner, acceptance criteria, and verification method;
- traceability works in both directions;
- contradictions and unresolved decisions remain visible;
- the readiness decision follows from objective exit criteria.

If the evidence is incomplete, produce a useful draft SRS and mark the affected sections. Do not fabricate completeness.

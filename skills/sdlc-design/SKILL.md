---
name: sdlc-design
description: Design and evaluate software architecture, user interfaces, data models, and integration contracts from an approved SRS. Use after requirements analysis or when converting requirements, constraints, quality attributes, existing-system evidence, and planning baselines into traceable architecture views, UI flows and screen specifications, conceptual/logical/physical data models, APIs and events, ADRs, migration considerations, and a design-readiness decision before implementation.
---

# SDLC Design

Turn an approved requirements baseline into an implementable, testable system design without silently changing scope or inventing requirements.

Read [references/standards.md](references/standards.md) before designing. Read [references/design-template.md](references/design-template.md) before writing the deliverable. Treat standards as guidance; do not claim certification or formal compliance.

## Establish the design baseline

Use the latest approved SRS and planning baseline. Inspect existing architecture documents, ADRs, source code, routes, interfaces, schemas, migrations, infrastructure, design systems, analytics, operational evidence, and deployment constraints when available.

Classify design inputs and decisions as:

- **Constraint**: mandated by an approved requirement, contract, policy, or existing boundary.
- **Decision**: selected after comparing viable alternatives; record it in an ADR.
- **Assumption**: temporarily accepted and requiring validation.
- **Open**: unresolved and capable of changing the design.
- **Deferred**: deliberately postponed with owner, reason, and trigger.

Never treat an assumption as an approved requirement. If the design exposes missing, conflicting, or infeasible requirements, return them to `sdlc-analysis`. If scope, budget, schedule, or staffing must change, return them to `sdlc-planning`.

Ask at most five grouped questions per round. Prioritize questions that change system boundaries, quality-attribute targets, data ownership, trust boundaries, interaction flows, integration contracts, or irreversible technology choices. Continue with explicit assumptions and `TBD` items when answers are unavailable.

## Maintain end-to-end traceability

Assign stable identifiers:

- `ARC-###` for architecture elements;
- `UI-###` for screens or interaction surfaces;
- `DATA-###` for logical data entities or stores;
- `INT-###` for APIs, events, files, or external interfaces;
- `ADR-###` for architecture decisions.

Trace both directions:

`requirement → architecture element → UI/data/interface design → verification evidence`

Every design element must satisfy at least one requirement or documented operational constraint. Every in-scope requirement must map to sufficient design coverage. Preserve existing IDs when revising a design; retire or supersede them rather than renumbering.

If an approved baseline lacks requirement IDs, create document-local anchors such as `BASE-F-001` and `BASE-Q-001` for traceability. Label them as non-normative references to quoted or linked source statements; do not present them as newly approved requirements.

## Design the architecture

### Define concerns and viewpoints

Identify stakeholders, their concerns, and the views needed to address them. Include only views that support a decision or verification activity. Usually consider:

- context and external dependencies;
- logical responsibilities and boundaries;
- runtime interactions for critical scenarios;
- deployment, environments, trust zones, and network boundaries;
- data ownership and movement;
- operations, observability, continuity, and support.

Use C4 context, container, and component views where appropriate. Add dynamic or deployment views when runtime order, failure handling, scaling, or topology matters. Accompany diagrams with responsibilities, interfaces, assumptions, and requirement IDs; a diagram alone is not a design.

### Allocate responsibilities

For each architecture element, define purpose, owned capabilities and data, inbound and outbound interfaces, dependencies, scaling model, failure behavior, security boundary, observability, deployment unit, and mapped requirements. Prefer explicit ownership and low coupling over speculative service decomposition.

Describe critical runtime scenarios end to end, including validation, authorization, state changes, transactions, asynchronous work, timeouts, retries, idempotency, compensation, degraded behavior, and audit evidence. Separate required behavior from optional implementation guidance.

### Design for quality attributes

Translate measurable quality requirements into design tactics and budgets. Cover only relevant attributes, such as performance, availability, reliability, security, privacy, accessibility, interoperability, maintainability, portability, safety, and recoverability.

For each critical quality scenario, state stimulus, environment, affected element, expected response, measurable threshold, design tactic, and verification approach. Allocate end-to-end budgets only when evidence supports the allocation. Do not claim capacity, latency, RTO, or RPO without a source or validation plan.

For availability targets, show the measurement window, allowed unavailability or error budget, planned-maintenance treatment, dependency and single-point-of-failure analysis, backup/restore expectations, and validation method. Leave missing recovery targets or high-availability assumptions open.

### Record architecture decisions

Create an ADR for consequential, costly-to-reverse choices. Record context, decision drivers, viable alternatives, decision, trade-offs, consequences, related requirements, validation evidence, owner, date, and status. Include build-versus-buy and technology choices only when needed for the design.

## Design user interfaces

Derive interaction design from actors, tasks, use cases, business rules, interface requirements, and accessibility needs in the SRS.

Define:

- information architecture, navigation, entry points, and authorization boundaries;
- user flows for primary, alternate, failure, recovery, cancellation, and timeout paths;
- a screen or surface inventory with stable `UI-###` identifiers;
- responsive behavior, localization, content rules, accessibility, and design-system constraints;
- analytics and audit events only when required and with privacy implications recorded.

For each screen or interaction surface, specify purpose, route or entry point, actors, prerequisites, displayed data, actions, validation, permissions, downstream interfaces, and states. Include loading, empty, partial, success, validation error, system error, offline or degraded, permission-denied, and destructive-action confirmation states when applicable.

Create low-fidelity wireframes only when they clarify hierarchy or interaction. Prefer a navigational flow diagram plus structured screen specifications; use the project's design tool and component library when supplied. Check relevant flows and states against WCAG 2.2 and record the intended conformance level from requirements rather than choosing one silently.

Use a compact state-applicability matrix across screens so omitted states are deliberate. Consider session expiry, stale or concurrently changed data, interrupted submission, offline behavior, and partial dependency failure in addition to the common states above.

## Design data models

Keep the following levels distinct:

1. **Conceptual**: business concepts and relationships, independent of storage technology.
2. **Logical**: entities, attributes, identifiers, cardinalities, invariants, and normalization decisions.
3. **Physical**: technology-specific tables, columns, types, keys, constraints, indexes, partitions, and storage settings.

For each `DATA-###` element, define meaning, owner and source of truth, identifiers, relationships, lifecycle, classification, retention, deletion, audit/history, residency, and mapped requirements. Use a Mermaid ER diagram when three or more entities interact.

Derive physical indexes from documented access patterns and query shapes. Define uniqueness, nullability, defaults, check constraints, referential actions, transaction boundaries, isolation or concurrency strategy, and idempotency behavior where relevant. Avoid speculative denormalization, partitioning, caching, or sharding; attach evidence, thresholds, and a validation plan when proposed.

Document migration, backfill, dual-read/write, reconciliation, rollback, compatibility, retention, and secure disposal for changed or existing data. Identify personally identifiable, confidential, regulated, or security-sensitive data and show how protection requirements are realized.

For zero-downtime changes, define the mixed-version compatibility window, deployment order, rollback cutoff, reconciliation evidence, and a gate that prevents destructive schema changes until old application versions and data paths are retired.

## Design interfaces and integrations

For each `INT-###`, specify producer, consumers, purpose, transport and format, contract, versioning, authentication, authorization, validation, error semantics, timeout, retry, idempotency, ordering, rate or volume, compatibility, observability, and ownership.

Use the project-approved OpenAPI version for HTTP APIs when applicable. Use a consistent machine-readable problem format, such as RFC 9457, only when adopted by the project. For events, specify delivery semantics, schema evolution, ordering, duplication, replay, dead-letter handling, and consumer recovery. Explicitly identify external or unknown consumers.

For state-changing interfaces, define duplicate-request outcomes and concurrent or stale-state conflicts. For notifications and other side effects, define deduplication keys, delivery-state ownership, and whether retries may create duplicate user-visible effects.

## Cover security and privacy fundamentals

Where applicable, explicitly address identity and session boundaries, authentication, an authorization matrix, least privilege, trust boundaries, threat modeling, data classification, encryption in transit and at rest, key and secret ownership, log redaction, audit integrity, abuse controls, privacy analysis, retention and deletion, incident evidence, and security verification. Mark each item non-applicable with a rationale or trace it to requirements, design controls, and evidence; do not assume a control exists because a technology commonly provides it.

## Evaluate the design

Evaluate the proposed design against stakeholder concerns and the highest-risk functional and quality scenarios. For each scenario, state the expected behavior, supporting elements and decisions, evidence available, residual risk, and required proof of concept, benchmark, threat model, usability test, or operational exercise.

Report:

- uncovered or weakly covered requirements;
- single points of failure and unsafe trust assumptions;
- ambiguous ownership or contracts;
- irreversible decisions lacking evidence;
- migration, compatibility, accessibility, privacy, security, and operational risks;
- design debt and deliberately deferred work;
- open decisions with owner and decision date.

Set design readiness to `READY`, `CONDITIONALLY READY`, or `NOT READY` from objective exit criteria. Never approve the design on behalf of stakeholders.

Use these minimum decision rules:

- `READY`: all gate items pass; no unresolved item can materially change boundaries, contracts, data integrity, security/privacy, accessibility, deployment, migration, or verification; residual risks are accepted by named owners.
- `CONDITIONALLY READY`: implementation may begin only in unaffected areas; every unresolved item has an owner, target date, containment, and explicit condition that must pass before the affected work or release proceeds.
- `NOT READY`: any blocker affects a critical flow or quality target, requirements are not adequately baselined, a consequential decision lacks viable evidence, or a blocking item has no owner or target date.

## Create the design document

Follow [references/design-template.md](references/design-template.md). Write in the user's language unless requested otherwise. Use the requested destination. If none is given and a repository is available, save to `docs/SYSTEM_DESIGN.md`; otherwise return the complete design in chat.

When updating an existing design, preserve history, identifiers, approved decisions, and compatibility constraints unless evidence authorizes a change. Do not implement product code, migrations, infrastructure, or production UI unless the user explicitly expands the task.

## Enforce the design gate

Before returning the design, verify that:

- the design baseline and requirement version are explicit;
- architecture views address identified stakeholder concerns;
- critical workflows include failure and recovery behavior;
- every in-scope requirement has traceable design coverage;
- UI flows cover applicable roles, permissions, states, accessibility, and responsive behavior;
- conceptual, logical, and physical data models are not conflated;
- interface contracts and compatibility policies are explicit;
- security, privacy, observability, deployment, continuity, and migration are addressed where applicable;
- consequential decisions have ADRs and evidence or a validation plan;
- all assumptions and `TBD` items have owners and target dates;
- readiness follows from recorded evaluation evidence.

If evidence is incomplete, produce a useful draft with marked gaps. Do not fabricate precision or completeness.

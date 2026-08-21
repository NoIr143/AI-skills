---
name: sdlc-planning
description: Define a software project's scope, measurable goals, delivery approach, team roles, milestones, effort, schedule, and cost estimates using recognized SDLC and project-planning standards. Use when starting a project, assessing an idea or feature, preparing a project charter or software development plan, estimating budget and staffing, clarifying ownership, comparing delivery approaches, or deciding whether work is ready to enter requirements and design.
---

# SDLC Planning

Create an evidence-based planning baseline that decision-makers can approve and the delivery team can execute. Cover the complete software life cycle where relevant, not only implementation.

Read [references/standards.md](references/standards.md) before producing the plan. Apply the standards as guidance and tailoring criteria; do not claim certification or formal compliance from this planning exercise.

## Establish the planning basis

Inspect supplied briefs, tickets, repository documentation, architecture notes, contracts, and existing code before asking questions. Separate all planning inputs into:

- **Confirmed facts**: explicitly supported by the supplied material.
- **Assumptions**: reasonable placeholders that require validation.
- **Open decisions**: choices that materially affect scope, architecture, schedule, staffing, or cost.

Ask at most five grouped questions when missing information would materially change the plan. If answers are unavailable, continue with labeled assumptions, ranges, and confidence levels. Never invent stakeholder approval, budget, deadlines, team capacity, rates, compliance obligations, or existing capabilities.

At minimum, determine:

- business problem, target users, expected outcome, sponsor, and key stakeholders;
- required capabilities, excluded capabilities, interfaces, data, environments, and operational boundaries;
- schedule or budget constraints and important external dependencies;
- available roles, allocation, skills, labor rates, and calendar assumptions;
- quality, security, privacy, reliability, accessibility, and regulatory expectations;
- whether the work is predictive, iterative, incremental, agile, DevOps-oriented, or hybrid.

## Build the planning baseline

### 1. Define purpose and measurable goals

State the problem and intended value in user and business terms. Convert goals into measurable outcomes with a baseline, target, measurement method, owner, and target date whenever evidence permits. Distinguish business success metrics from delivery metrics.

### 2. Bound the scope

Define:

- in-scope outcomes and capabilities;
- explicitly out-of-scope items;
- deliverables and acceptance evidence;
- affected users, systems, interfaces, data, and environments;
- constraints, dependencies, and assumptions;
- minimum viable release versus later releases.

Use outcome-oriented scope statements. Do not silently turn uncertain ideas into commitments. Flag ambiguity that can create scope creep.

### 3. Tailor the life cycle

Select a delivery approach based on uncertainty, compliance, release risk, feedback speed, and dependency structure. Define only the phases and controls the project needs. Consider planning for:

- discovery and feasibility;
- stakeholder and system requirements;
- architecture and detailed design;
- implementation and integration;
- verification, validation, security, and acceptance;
- deployment, transition, operations, maintenance, and retirement.

For each applicable phase, identify entry criteria, principal outputs, accountable approver, and exit criteria. Include feedback loops for iterative delivery.

### 4. Decompose work and milestones

Create a deliverable-oriented work breakdown structure. Decompose until work can be estimated and assigned without pretending to know implementation detail that has not been discovered. Include cross-cutting work such as environments, CI/CD, data migration, observability, security, documentation, training, release, and operational handover when applicable.

Identify milestones, dependencies, critical sequencing, and decision gates. Do not present dates as committed when capacity or dependencies are unknown.

### 5. Assign roles and decision rights

Create a lean RACI matrix using project-specific roles. Ensure each major deliverable or decision has exactly one Accountable role and at least one Responsible role. Include business, product, engineering, architecture, quality, security, operations, data, UX, and external parties only when relevant.

Separate role names from named people unless names are supplied. Highlight missing roles, overloaded roles, segregation-of-duty concerns, and approval bottlenecks.

### 6. Estimate effort, schedule, and cost

Estimate from the work breakdown structure, historical evidence, analogous work, parametric data, team estimates, or three-point estimates. State the method and basis for every estimate.

When three-point inputs are available, use:

`expected effort = (optimistic + 4 × most likely + pessimistic) / 6`

Do not convert effort directly to elapsed time without accounting for team capacity, dependencies, reviews, handoffs, leave, operational duties, and parallel work. Show optimistic, most-likely, and conservative scenarios or an equivalent confidence range.

Build the cost model from applicable categories:

- labor by role, effort, allocation, and rate;
- cloud and runtime infrastructure;
- development, test, staging, and production environments;
- licenses, tools, third-party APIs, data, devices, and vendor services;
- security, compliance, testing, migration, training, and rollout;
- contingency for identified uncertainty and risk;
- recurring operating and maintenance cost after launch.

Keep estimate, contingency, and management reserve separate. If rates are unknown, report effort and a formula instead of fabricating currency values. State currency, tax treatment, rounding, estimate date, exclusions, confidence, and expected accuracy range.

### 7. Plan risks, governance, and change control

Record each material risk with cause, event, impact, probability, severity, owner, response, trigger, and contingency. Include delivery, technical, security, privacy, supplier, operational, data, schedule, and cost risks as applicable.

Define how scope, schedule, and budget baselines are approved and changed. Require impact analysis for change requests. Identify status cadence, decision forum, escalation path, evidence repository, and re-estimation triggers.

Integrate security activities into relevant phases. Assign security responsibilities, identify sensitive assets and threat assumptions, define security acceptance evidence, and include security work in effort and cost.

## Produce the plan

Use the following structure. Adapt table size to the project but keep every section. Write in the user's language unless they request another language.

```markdown
# SDLC Planning Baseline — <Project>

## 1. Executive summary
<Problem, intended value, recommended delivery approach, rough duration/cost range, confidence, and go/no-go recommendation.>

## 2. Planning basis
### Confirmed facts
### Assumptions
### Open decisions

## 3. Goals and success measures
| Goal | Metric and baseline | Target | Measurement | Owner | Target date |

## 4. Scope baseline
### In scope
### Out of scope
### Deliverables and acceptance evidence
### Constraints and dependencies

## 5. Life-cycle and delivery approach
| Phase | Entry criteria | Main outputs | Accountable | Exit criteria |

## 6. Work breakdown and milestones
| ID | Deliverable/work package | Dependency | Owner role | Effort range | Milestone |

## 7. Team and RACI
### Staffing assumptions
| Deliverable/decision | A | R | C | I |

## 8. Estimate
### Method and basis
| Scenario | Effort | Elapsed time | One-time cost | Recurring cost | Confidence |
### Cost breakdown
| Category | Basis | Low | Most likely | High | Included/excluded |

## 9. Risks and responses
| Risk | Probability | Impact | Owner | Response | Trigger/contingency |

## 10. Governance and change control

## 11. Readiness decision
### Ready now
### Conditions before requirements/design
### Deferred decisions
### Recommendation: GO / CONDITIONAL GO / NO-GO
```

## Enforce quality gates

Before returning the plan, verify that:

- every goal is measurable or explicitly marked as needing a baseline;
- scope contains both inclusions and exclusions;
- every deliverable has acceptance evidence;
- every major decision has one Accountable role;
- estimates trace to work, capacity, rates, and assumptions;
- labor, non-labor, contingency, and recurring cost are visible;
- uncertainty is expressed as ranges and confidence, not false precision;
- risks have owners and actionable responses;
- security, operations, maintenance, and retirement were considered;
- open decisions have an owner and a deadline or decision gate;
- the final readiness decision follows from the listed evidence.

If evidence is insufficient, produce a preliminary plan and label it clearly. Never hide uncertainty to make the project appear ready.

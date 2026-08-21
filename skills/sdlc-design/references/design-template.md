# System design document template

Use every top-level section. Mark non-applicable sections with a brief rationale instead of deleting them. Keep diagrams readable and link detailed contracts, schemas, prototypes, or ADR files by stable identifier.

```markdown
# System Design — <System>

| Field | Value |
|---|---|
| Document ID | SDD-<PROJECT> |
| Version/status | <version> / Draft, In review, Approved, Changed after baseline |
| Owner | <role or person> |
| Last updated | <YYYY-MM-DD> |
| Requirements baseline | <SRS reference/version> |

## Revision history
| Version | Date | Author | Change | Approver/status |

## 1. Executive design summary
### 1.1 Goals and requirement drivers
### 1.2 Scope, constraints, assumptions, and open decisions
### 1.3 Selected approach and major trade-offs

## 2. Stakeholders, concerns, and viewpoints
| Stakeholder | Concern | Viewpoint/view | Acceptance evidence |

## 3. Architecture
### 3.1 System context and external dependencies
### 3.2 Containers, components, and responsibilities
| ID | Element | Responsibility/data | Interfaces/dependencies | Deployment/scaling | Requirement IDs |
### 3.3 Critical runtime scenarios and failure handling
### 3.4 Deployment, environments, trust zones, and topology
### 3.5 Quality-attribute scenarios and budgets
| Requirement | Stimulus/environment | Response/threshold | Tactic/allocation | Verification |
### 3.6 Security, privacy, observability, continuity, and support

## 4. User experience and interface design
### 4.1 Personas, tasks, information architecture, and navigation
### 4.2 User flows
### 4.3 Screen and interaction inventory
| ID | Screen/route | Actor and purpose | Data/actions | States and errors | Accessibility/responsive | Requirements |
### 4.4 Wireframes, content, design system, and localization

## 5. Data design
### 5.1 Conceptual model
### 5.2 Logical model
| ID | Entity | Meaning/owner | Keys/relationships/invariants | Lifecycle/classification | Requirements |
### 5.3 Physical model and access patterns
| Store/table | Columns/types/constraints | Access patterns/indexes | Transaction/concurrency | Capacity evidence |
### 5.4 Migration, reconciliation, retention, and deletion

## 6. Interfaces and integrations
| ID | Producer/consumer | Contract/version | Auth and validation | Failure/retry/idempotency | Volume/compatibility | Requirements |
### 6.1 HTTP/API contracts
### 6.2 Events, files, devices, and third-party services

## 7. Architecture decision records
| ID | Decision/status | Drivers and alternatives | Trade-offs/consequences | Evidence/owner/date | Requirements |

## 8. Verification and evaluation
| Scenario/requirement | Design coverage | Evidence or planned validation | Residual risk | Owner |

## 9. Traceability matrix
| Requirement ID | Architecture IDs | UI IDs | Data IDs | Interface/ADR IDs | Verification/status |

## 10. Delivery and implementation guidance
### 10.1 Work packages and dependency order
### 10.2 Prototypes, benchmarks, threat models, and usability tests
### 10.3 Rollout, migration, rollback, and compatibility

## 11. Risks, assumptions, open items, and design debt
| ID | Type/item | Impact | Owner | Decision/validation date | Status |

## 12. Design readiness
### Exit-criteria results
### Recommendation: READY / CONDITIONALLY READY / NOT READY

## Appendices
```

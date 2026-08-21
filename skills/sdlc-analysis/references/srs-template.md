# Software Requirements Specification template

Use every top-level section. Mark non-applicable sections with a brief rationale instead of deleting them. Keep requirement tables readable; place lengthy API schemas or data dictionaries in appendices and link them by stable identifiers.

```markdown
# Software Requirements Specification — <System>

| Field | Value |
|---|---|
| Document ID | SRS-<PROJECT> |
| Version | <version> |
| Status | Draft / In review / Approved / Changed after baseline |
| Owner | <role or person> |
| Last updated | <YYYY-MM-DD> |
| Planning baseline | <reference/version> |

## Revision history
| Version | Date | Author | Change | Approver/status |

## 1. Purpose and scope
### 1.1 Purpose
### 1.2 In scope
### 1.3 Out of scope
### 1.4 Intended audience
### 1.5 References
### 1.6 Terms and abbreviations

## 2. Product context
### 2.1 Business goals and success measures
### 2.2 System boundary
### 2.3 Stakeholders and user classes
### 2.4 External systems and dependencies
### 2.5 Assumptions and constraints

## 3. Operational concept
### 3.1 Context and information flows
### 3.2 User journeys and use cases
| ID | Actor and goal | Preconditions/trigger | Main flow | Alternatives/exceptions | Postconditions |
### 3.3 States and transitions
### 3.4 Business rules
| ID | Rule | Source | Priority | Owner | Status |

## 4. Functional requirements
| ID | Requirement | Rationale/source | Priority/release | Acceptance criteria | Verification | Owner/status |

## 5. Interface requirements
### 5.1 User interfaces
### 5.2 Software and API interfaces
### 5.3 Events, files, and communication interfaces
### 5.4 Hardware or device interfaces
| ID | Interface requirement | Contract/format | Errors and recovery | Security | Verification |

## 6. Data requirements
| ID | Data requirement | Source of truth/owner | Validation and lifecycle | Privacy/classification | Verification |
### 6.1 Conceptual data model
### 6.2 Retention, deletion, archival, and audit
### 6.3 Migration and reconciliation

## 7. Quality requirements
| ID | Category | Measurable requirement | Conditions/workload | Acceptance threshold | Verification |

## 8. Security, privacy, and compliance
### 8.1 Protection needs and trust boundaries
### 8.2 Authentication and authorization
### 8.3 Data protection and privacy
### 8.4 Audit, monitoring, and incident evidence
### 8.5 Applicable obligations and control references

## 9. Operational and support requirements
### 9.1 Deployment and environments
### 9.2 Observability and support
### 9.3 Backup, restore, continuity, and recovery
### 9.4 Maintenance, compatibility, and retirement

## 10. Acceptance and verification strategy
| Requirement ID | Acceptance evidence | Method | Environment/data | Responsible role |

## 11. Traceability matrix
| Goal/need | Use case | Requirement IDs | Acceptance/verification | Status |

## 12. Open items and decisions
| ID | Question/TBD/conflict | Impact | Owner | Decision date | Status |

## 13. Requirements baseline and change control

## 14. Analysis readiness
### Exit-criteria results
### Recommendation: READY / CONDITIONALLY READY / NOT READY

## Appendices
```

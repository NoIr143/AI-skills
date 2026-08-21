# Design standards basis

Use these sources as a design framework and tailor the output to project size, risk, domain, contract, and delivery model. Do not reproduce paid standard text or claim formal compliance.

| Source | Apply to this skill |
|---|---|
| [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) | Structure architecture descriptions around stakeholders, concerns, viewpoints, views, model kinds, correspondences, and rationale. |
| [ISO/IEC/IEEE 42020:2019](https://www.iso.org/standard/68982.html) | Connect architecture governance, management, conceptualization, evaluation, elaboration, enablement, and change across the life cycle. |
| [ISO/IEC/IEEE 42030:2019](https://www.iso.org/standard/73436.html) | Evaluate architecture against stakeholder concerns, quality characteristics, risks, and value rather than relying on diagram review alone. |
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Preserve traceability to the approved stakeholder, system, software, interface, and quality requirements baseline. |
| [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Use relevant product-quality characteristics to discover design concerns and measurable quality scenarios. |
| [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) | Apply human-centred design principles to user understanding, iterative interaction design, and evaluation. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Design and evaluate web interaction states against the accessibility conformance level required by the project. |
| [C4 model](https://c4model.com/) | Communicate software structure at context, container, component, and code levels; select only useful abstraction levels. |
| [OpenAPI Specification](https://spec.openapis.org/oas/) | Describe HTTP API contracts in a machine-readable form using the version approved by the project. |
| [RFC 9457](https://datatracker.ietf.org/doc/rfc9457/) | Standardize HTTP API problem details when the project adopts this error representation. |
| [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/upd2/final) | Engineer security into architecture from stakeholder protection needs, trust boundaries, and life-cycle risk. |

## Tailoring principles

- Select views from stakeholder concerns; do not force every diagram type into every project.
- Preserve bidirectional traceability from requirements to decisions, elements, interfaces, data, UI, and verification.
- Express quality needs as scenarios with measurable responses and explicit validation evidence.
- Separate architecture decisions from requirements and assumptions.
- Use models consistently and document important correspondences or contradictions between them.
- Evaluate high-risk decisions early with prototypes, benchmarks, threat models, usability tests, or operational exercises.
- Treat accessibility, privacy, security, migration, operations, and retirement as design concerns, not late implementation checks.

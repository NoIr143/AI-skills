# Coding standards basis

Use these sources to guide implementation and tailor them to project risk, domain, technology, and existing engineering policy. Do not reproduce paid standard text or claim formal compliance.

| Source | Apply to this skill |
|---|---|
| [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) | Keep implementation connected to the software life-cycle processes, approved inputs, verification, configuration management, change, operation, maintenance, and disposal. |
| [ISO/IEC/IEEE 24748-3:2020](https://www.iso.org/standard/77698.html) | Tailor life-cycle activities and evidence to the selected development model and project context. |
| [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Preserve applicable product-quality characteristics while implementing and verifying code. |
| [ISO/IEC 25040:2024](https://www.iso.org/standard/83467.html) | Treat quality evaluation as evidence-driven and connect implementation checks to stated requirements and evaluation criteria. |
| [NIST SP 800-218, SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) | Integrate secure-development practices into implementation, protect code and artifacts, produce well-secured releases, and respond to vulnerabilities. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | For applicable web applications and services, map implementation and tests to the project's selected technical security requirements. |
| [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/01-introduction/05-introduction) | Use practical checks for input validation, output encoding, authentication, access control, data protection, error handling, and related secure coding concerns. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Implement and verify UI behavior against the accessibility conformance level approved in requirements and design. |

## Application principles

- Use the repository's pinned language, framework, dependency, and tool versions as the implementation baseline.
- Trace code and automated checks to approved behavior without embedding process noise into production code.
- Prefer platform and framework security primitives over custom security mechanisms.
- Preserve compatibility unless an approved migration or versioning decision authorizes a break.
- Treat formatter, compiler, linter, tests, scanners, and build output as evidence, not substitutes for reasoning or review.
- Record deviations and residual risk rather than silently weakening acceptance criteria.

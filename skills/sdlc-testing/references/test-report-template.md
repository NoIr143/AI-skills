# Test report template

Use every top-level section. Mark non-applicable sections with a rationale. Link large logs, traces, screenshots, coverage, profiles, and scanner outputs instead of embedding them.

```markdown
# Test Report — <System/change>

| Field | Value |
|---|---|
| Report ID/version | TEST-<PROJECT> / <version> |
| Test item | <commit/build/artifact/environment> |
| Requirements/design baseline | <references and versions> |
| Test period | <timestamps/time zone> |
| Owner | <role/person> |

## 1. Decision summary
### Verdict: PASS / PASS WITH RISKS / FAIL / BLOCKED
### Tested scope, confidence, and release recommendation
### Blocking defects and residual risks

## 2. Test basis and environment
### Requirements, design, contracts, change set, and known defects
### Hardware, software, configuration, data, dependencies, and build fingerprint
### Assumptions, exclusions, limitations, and authorizations

## 3. Risk and coverage plan
| Risk/requirement | Impact/likelihood | Test levels/types | Test IDs | Exit criterion |

## 4. Execution summary
| Type/level | Planned | Passed | Failed | Blocked | Not run/inconclusive | Evidence |

## 5. Functional and regression results
| Test ID | Requirement/risk | Preconditions/data | Expected | Actual | Status/evidence |

## 6. Security results
| Control/risk | Method/scope | Result | Evidence | Defect/status |

## 7. Performance results
### Workload, environment, warm-up, duration, sample count, and baseline
| Scenario | Throughput/errors | p50/p95/p99 | Resource saturation | Threshold/baseline | Result |

## 8. Data, migration, resilience, compatibility, and accessibility
| Area | Scenario | Result/evidence | Defect/status |

## 9. Confirmed defects
| ID/severity | Title and impact | Requirement | Reproduction/evidence | Owner/status |

## 10. Blocked, skipped, inconclusive, and flaky tests
| Test ID | Reason | Confidence impact | Owner/next action |

## 11. Traceability
| Requirement/risk | Test IDs | Results | Defect IDs | Coverage status |

## 12. Exit-criteria evaluation
| Criterion | Result | Evidence or exception |

## 13. Final verdict and residual risk
```

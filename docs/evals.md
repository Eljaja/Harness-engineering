# Evals for engineering agents

Tests validate code. Evals validate behavior of the agentic system.

For harness engineering, evals should answer: will the agent follow instructions, use tools safely, respect policy, recover from failures, and produce reviewable work?

## Eval layers

### Smoke evals

Cheap checks that run on every PR.

Examples:

- required files exist;
- root and nested `AGENTS.md` files are present;
- tool contracts have required sections;
- sandbox contract declares network/filesystem/secret boundaries;
- PR template asks for plan, validation, risk, and rollback.

### Regression evals

Scenario-based checks derived from past failures.

Examples:

- agent tries to modify a sandbox policy without updating evals;
- agent attempts a networked tool without approval;
- agent claims validation passed without evidence;
- agent writes a plan that does not match the final diff.

### Capability evals

Measure useful engineering behavior.

Examples:

- add a new tool following the contract;
- fix a failing test;
- update docs and CI consistently;
- recover from an intentionally failing command.

## Eval design rules

- Keep PR smoke evals deterministic and fast.
- Store scenario definitions in the repo.
- Store grader logic in code when possible.
- Record traces or reports for human review.
- Turn real incidents into regression scenarios.
- Avoid evals that only check whether the model says the right thing.
- Prefer checking artifacts: files changed, commands run, policy decisions, trace events.

## Minimal eval scenario schema

```yaml
id: repository-contracts-smoke
name: Repository contracts smoke test
risk_level: low
trigger: pull_request
checks:
  - required_paths_exist
  - no_obvious_secrets
  - tool_contract_sections_present
  - pr_template_has_validation
expected_artifacts:
  - structure-check output
  - secret-scan output
```

## What to measure

- task success rate;
- CI pass rate on first attempt;
- number of iterations/tool calls;
- approval requests;
- unsafe operation attempts;
- eval regressions;
- human-review corrections;
- rollback frequency.

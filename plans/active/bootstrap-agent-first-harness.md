# Bootstrap agent-first harness

## Goal

Initialize this repository as a practical harness-engineering reference for agent-first software projects.

## Context

The repository is intended to collect best practices for coding-agent projects: instructions, plans, tool contracts, sandbox contracts, evals, CI/CD, telemetry, and review workflows.

## Scope

### In scope

- root and nested `AGENTS.md` files;
- docs for best practices, repository structure, CI/CD, evals, and telemetry;
- harness templates for tools, sandbox, and policy;
- smoke eval scenario;
- plan template;
- PR template;
- lightweight CI scripts.

### Out of scope

- production implementation of a real agent runtime;
- model/provider-specific benchmark results;
- deployment automation.

## Files likely to change

- `README.md`
- `AGENTS.md`
- `docs/*`
- `harness/*`
- `evals/*`
- `plans/*`
- `scripts/*`
- `.github/*`

## Implementation steps

1. Add repository overview and operating contract.
2. Add best-practice docs.
3. Add harness templates.
4. Add eval smoke scenario.
5. Add CI and local validation commands.
6. Verify repository structure.

## Validation

```bash
make ci
```

## Risks

- Initial docs may be broad and need project-specific tightening later.
- Smoke evals are structural only until real agent runtime code exists.

## Rollback plan

Revert the bootstrap commits or delete the initialized files.

## Completion notes

- changed files: root docs, harness templates, eval smoke suite, CI scripts;
- validation run: repository structure and secret scan are enforced by CI;
- known gaps: no real model-based eval runner yet;
- follow-up work: add implementation examples and regression scenarios from real agent incidents.

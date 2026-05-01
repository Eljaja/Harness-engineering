# CI/CD for agent-first projects

CI/CD is the enforcement layer for agent-first development. It should make unsafe, unreviewable, or unvalidated autonomous work hard to merge.

## Pipeline levels

### 1. Structural gate

Checks that the repository still contains required harness files:

- `AGENTS.md`;
- plan template;
- eval smoke suite;
- PR template;
- CI workflow;
- tool/sandbox policy templates.

### 2. Mechanical gate

Checks formatting, linting, typing, and build/test commands.

Use stable local commands that agents can run before pushing:

```bash
make ci
make test
make eval-smoke
```

### 3. Safety gate

Checks for obvious unsafe changes:

- committed secrets;
- `.env` files;
- private keys;
- generated credentials;
- large unreviewed artifacts;
- changes to sandbox/policy/tooling without eval updates.

### 4. Behavioral gate

Runs cheap smoke evals on every PR and deeper regression evals on schedule or before releases.

Smoke evals should catch:

- missing instructions;
- broken tool contracts;
- unsafe defaults;
- missing plan for agent-generated work;
- broken rollback/review conventions.

### 5. Release gate

Before release, require:

- full regression evals;
- changelog/release notes;
- rollback plan;
- operator runbook updates;
- explicit approval for risky capability changes.

## Recommended GitHub Actions layout

```text
.github/workflows/
├── ci.yml              # structure, secret scan, smoke evals
├── regression.yml      # scheduled deeper evals
├── release.yml         # release validation and artifacts
└── agent-pr.yml        # optional stricter checks for agent-generated PRs
```

## Agent-generated PR checks

For PRs marked as agent-generated, require:

- plan file exists;
- PR body includes validation commands;
- changed risky directories have matching eval/doc updates;
- CI passes;
- human review before merge.

## Evidence artifacts

When evals produce traces, upload them as artifacts. Reviewers should not need to rerun expensive evals just to understand what happened.

Good artifacts:

- tool-call traces;
- eval reports;
- benchmark summaries;
- failed scenario logs;
- policy-decision logs.

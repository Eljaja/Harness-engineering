# Harness Engineering

A practical, agent-first blueprint for building software repositories where AI agents can plan, edit, test, evaluate, and ship changes safely.

The core idea: in an agent-first project, the repository is not only source code. It is an executable work environment for autonomous engineering. Good outcomes come from the harness around the model: instructions, plans, tools, sandboxes, tests, evals, CI/CD, telemetry, and review contracts.

## What this repo contains

```text
.
├── AGENTS.md                         # root operating contract for coding agents
├── Makefile                          # stable local/CI entrypoints
├── README.md                         # project overview
├── .github/
│   ├── pull_request_template.md       # PR contract for agent-generated changes
│   └── workflows/ci.yml               # structure + secret-scan CI
├── docs/
│   ├── agent-first-repository.md      # repository architecture for agent-first work
│   ├── best-practices.md              # consolidated harness-engineering practices
│   ├── ci-cd.md                       # CI/CD gates for agentic projects
│   ├── evals.md                       # eval design and regression gates
│   └── telemetry.md                   # traces, logs, metrics, review evidence
├── evals/
│   ├── AGENTS.md
│   ├── README.md
│   └── smoke/repository-contracts.yaml
├── harness/
│   ├── AGENTS.md
│   ├── policy-template.md
│   ├── sandbox-contract.md
│   └── tool-contract-template.md
├── plans/
│   ├── AGENTS.md
│   └── templates/agent-change-plan.md
└── scripts/
    ├── check_repo_structure.py
    └── scan_secrets.py
```

## Agent-first development loop

The default loop for any non-trivial change:

```text
request
  -> inspect repo context
  -> write/refresh plan
  -> make minimal edits
  -> run tests and evals
  -> summarize evidence
  -> open PR / ship
  -> feed regressions back into evals and instructions
```

This is different from a normal repository because the repo must be legible to an agent with limited context. The project needs stable commands, local instructions, explicit risk boundaries, deterministic checks, and reviewable work logs.

## Four required layers

### 1. Instructions

Use `AGENTS.md` as the durable interface between humans and coding agents. The root file defines the global contract. Nested files specialize behavior for `harness/`, `evals/`, `plans/`, `docs/`, or code directories.

Good instructions are operational, not motivational. They tell the agent what to read, what commands to run, what must not be changed, how to handle secrets, and when a plan/eval is required.

### 2. Plans

Use `plans/` for multi-step or agent-generated work. A plan should capture intent, constraints, touched files, validation, risks, rollback, and completion notes.

Plans prevent opaque autonomous work. They also make it possible to compare the final diff against the intended scope.

### 3. Evals

Tests check code correctness. Evals check agent behavior and system behavior under realistic tasks.

For harness engineering, evals should cover tool use, refusal/approval boundaries, sandbox behavior, regression scenarios, prompt changes, routing decisions, and failure recovery.

### 4. CI/CD

CI must run the same stable commands used locally. It should enforce structure, scan for obvious secrets, run tests, run smoke evals, and upload artifacts when evals produce traces or reports.

An agent-first CI pipeline should fail early for mechanical issues and preserve enough evidence for review.

## Quick start

```bash
make ci
```

This runs repository-structure validation and a lightweight secret scan using only Python standard library scripts.

## Recommended repository contract

Every production agentic repository should have:

- `AGENTS.md` at root.
- Local `AGENTS.md` files in high-risk directories.
- A stable `Makefile` or equivalent command runner.
- `plans/templates/agent-change-plan.md`.
- PR template with explicit agent-generated checkbox.
- CI gates for formatting, linting, tests, eval smoke suite, and secret scanning.
- Tool contracts for every agent tool.
- Sandbox contracts for every environment where agents execute code.
- Policy files for destructive, networked, credentialed, billing, and repository-write operations.
- Evals that are cheap enough for PRs and deeper regression suites for scheduled runs.
- Telemetry and traces that let reviewers reconstruct what happened.

## Design principle

Do not rely on the model being careful. Build a repository that makes the safe path the easiest path.

The harness should make good work reproducible and bad work visible.

# Agent-first repository architecture

An agent-first repository is designed so that software agents can understand the project, make bounded changes, validate those changes, and hand them off for review without relying on hidden context.

## Canonical structure

```text
.
├── AGENTS.md
├── README.md
├── Makefile
├── docs/
├── harness/
├── evals/
├── plans/
├── scripts/
└── .github/
```

## Required components

### `AGENTS.md`

The operational contract. It tells agents how to work in the repository.

It should include:

- project role;
- repository map;
- required workflow;
- validation commands;
- safety boundaries;
- quality gates;
- PR expectations.

### `plans/`

A durable record of intent and execution.

Use plans for:

- agent-generated changes;
- multi-file changes;
- security/sandbox/tooling changes;
- CI/CD changes;
- architecture changes.

### `harness/`

The agent operating environment: tool contracts, policies, prompts, sandbox rules, and runtime design.

### `evals/`

Behavioral checks for the agent and harness. Evals should catch regressions that normal unit tests miss.

### `.github/`

Review and automation contracts: PR template, CI, scheduled regression checks, release workflows.

## Nested instructions

Use nested `AGENTS.md` files when a directory has special rules.

Examples:

- `harness/AGENTS.md` for safety-critical tool and sandbox docs.
- `evals/AGENTS.md` for deterministic eval requirements.
- `plans/AGENTS.md` for plan lifecycle conventions.

The nearest `AGENTS.md` wins for local behavior, but it must not weaken root safety requirements.

## Agent-readable docs

Documentation should be concrete and command-oriented.

Prefer:

```text
Run `make ci` before handoff.
```

Avoid:

```text
Make sure everything is good.
```

Agents need explicit commands, file paths, and acceptance criteria.

## Repository contract checklist

- [ ] Root `AGENTS.md` exists.
- [ ] Stable validation command exists.
- [ ] Plans template exists.
- [ ] PR template asks for validation and rollback.
- [ ] Tool contracts exist for agent tools.
- [ ] Sandbox contract exists for execution environments.
- [ ] Evals include a PR-safe smoke suite.
- [ ] CI runs structural checks and secret scanning.
- [ ] Docs explain how to add tools, policies, and evals.

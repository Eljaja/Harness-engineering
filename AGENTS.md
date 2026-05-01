# Agent operating contract

This repository is an agent-first harness-engineering reference project. It is designed to be read and modified by both humans and coding agents.

## Core rule

Prefer reproducible engineering over clever autonomous behavior. Every non-trivial change must be understandable from the request, plan, diff, validation output, and PR summary.

## Required workflow

1. Read this file first.
2. Read the closest nested `AGENTS.md` before editing files in a subdirectory.
3. For multi-file, risky, or agent-generated changes, create or update a plan under `plans/active/` using `plans/templates/agent-change-plan.md`.
4. Keep changes small and scoped. Do not mix unrelated refactors with documentation, policy, or CI changes.
5. Add or update tests/evals/checks when behavior, policy, or repository contracts change.
6. Run `make ci` before handoff when possible.
7. In the final summary or PR, include changed files, validation run, known gaps, and rollback path.

## Stable commands

```bash
make ci                 # full local validation gate
make check-structure    # required files/directories contract
make scan-secrets       # lightweight secret-pattern scan
make test               # alias for structural tests in this reference repo
make eval-smoke         # smoke eval contract validation
```

## Repository boundaries

Do not commit:

- API keys, tokens, passwords, SSH private keys, cookies, session data, or `.env` files.
- Large generated artifacts unless explicitly required.
- Vendor/cache directories such as `node_modules/`, `.venv/`, `.pytest_cache/`, `dist/`, or build output.
- Machine-local absolute paths in reusable docs or configs.

## Harness-engineering expectations

A high-quality agentic repository should define:

- Instructions: durable, local, operational guidance in `AGENTS.md`.
- Plans: reviewable intent and implementation record in `plans/`.
- Tool contracts: schema, side effects, approval needs, timeout, retry, and telemetry.
- Sandbox contracts: filesystem, network, process, secrets, and resource boundaries.
- Evals: deterministic smoke/regression checks for behavior and safety boundaries.
- CI/CD: stable local commands mirrored in automation.
- Telemetry: traces and artifacts sufficient to reconstruct autonomous work.

## Review stance

Treat agent output as untrusted until checks and human review validate it. A plan explains intent but does not prove correctness.

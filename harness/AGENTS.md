# Harness directory instructions

This directory defines the operational harness around agents: tool contracts, sandbox contracts, prompts, policies, and runtime boundaries.

## Rules

- Do not weaken root safety requirements.
- Any change to a tool, sandbox, prompt, or policy contract must update docs or evals when the behavior changes.
- Prefer explicit contracts over prose-only guidance.
- Mark side effects, approval requirements, timeouts, retries, and telemetry fields.
- Treat sandbox, billing, credential, repository-write, and network capabilities as high-risk by default.

## Required validation

Run from repository root:

```bash
make ci
```

For real implementations, also run the affected tool/sandbox tests and at least one regression eval covering the modified boundary.

# Evals directory instructions

Evals in this directory should be deterministic, cheap enough for CI when possible, and tied to concrete repository or agent behavior.

## Rules

- Prefer artifact-based checks over subjective prose grading.
- Add regression scenarios for real failures.
- Keep PR smoke evals fast and dependency-light.
- Do not require external network access for default CI evals.
- Document expected inputs, outputs, and artifacts for every scenario.

## Required validation

```bash
make eval-smoke
```

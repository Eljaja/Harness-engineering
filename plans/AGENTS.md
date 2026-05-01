# Plans directory instructions

Plans are durable task records for agent-generated or high-risk work.

## Rules

- Use `plans/templates/agent-change-plan.md` for new plans.
- Keep active plans in `plans/active/` when the work is in progress.
- Move completed plans to `plans/completed/` in mature repositories.
- A plan must name the goal, scope, constraints, changed files, validation, risks, and rollback.
- The final PR summary should match the plan or explicitly explain drift.

## When a plan is required

A plan is required for:

- multi-file changes;
- CI/CD changes;
- harness/tool/sandbox/policy changes;
- security-sensitive work;
- agent-generated work;
- architecture changes.

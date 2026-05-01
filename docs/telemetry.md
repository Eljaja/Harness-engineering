# Telemetry for agentic engineering

Telemetry makes autonomous work reviewable. The goal is not surveillance; the goal is reconstructability.

## Required evidence

For every non-trivial agent run, capture enough information to answer:

- what was requested;
- what context was read;
- what plan was produced;
- what tools were called;
- what files changed;
- what commands ran;
- what failed;
- what policy gates fired;
- what artifacts were produced;
- what rollback path exists.

## Trace events

Useful event types:

- `task_started`;
- `context_loaded`;
- `plan_created`;
- `tool_call_requested`;
- `approval_required`;
- `tool_call_completed`;
- `file_changed`;
- `validation_started`;
- `validation_failed`;
- `validation_passed`;
- `eval_started`;
- `eval_completed`;
- `policy_violation`;
- `handoff_summary_created`.

## Log fields

For tool calls, log:

- tool name;
- input hash or redacted input;
- output status;
- duration;
- retry count;
- approval status;
- policy decision;
- error type;
- trace id.

Do not log raw secrets, tokens, credentials, private user data, or sensitive customer content.

## Metrics

Track:

- task success rate;
- eval pass rate;
- CI pass rate;
- average tool calls per task;
- tool failure rate;
- approval rate;
- loop interruption rate;
- rollback rate;
- review correction rate.

## Artifacts

CI should upload eval reports and traces for deeper scenarios. PRs should link to the relevant plan and summarize validation evidence.

## Retention

Telemetry should have retention and redaction policy. Store only what is needed to debug, improve evals, and review autonomous work.

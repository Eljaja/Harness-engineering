# Harness engineering best practices

Harness engineering is the discipline of designing the environment around an AI agent so that useful autonomous work is repeatable, safe, inspectable, and measurable.

## 1. Treat the repository as an agent runtime

A normal repository optimizes for human navigation. An agent-first repository must also optimize for limited-context autonomous workers.

Best practices:

- Put durable operating rules in `AGENTS.md`.
- Keep commands stable through `make`, `just`, `task`, or scripts.
- Make setup and validation executable, not tribal knowledge.
- Keep local instructions close to risky directories.
- Keep plans and evals in the repo, not only in chat history.

## 2. Separate intent from implementation

Agents should not jump directly from request to diff. Require a plan for non-trivial work.

A good plan includes:

- goal;
- context;
- constraints;
- files likely to change;
- implementation steps;
- validation commands;
- risks;
- rollback path;
- completion notes.

The plan is not bureaucracy. It is a cheap alignment artifact that helps reviewers detect scope drift.

## 3. Define tool contracts

Every tool available to an agent should document:

- purpose;
- input schema;
- output schema;
- side effects;
- required approvals;
- timeout;
- retry policy;
- idempotency;
- telemetry fields;
- failure modes.

Agents become unreliable when tools have ambiguous semantics. Strict contracts reduce prompt burden.

## 4. Use sandboxes deliberately

A sandbox is not just a container. It is a declared boundary.

Document:

- filesystem access;
- network access;
- process limits;
- CPU/GPU/memory limits;
- credential injection rules;
- persistence model;
- cleanup behavior;
- audit logs.

Default posture: read-only, no credentials, no network, bounded runtime. Add capabilities explicitly.

## 5. Convert incidents into evals

When an agent fails, do not only patch the prompt. Add a regression scenario.

Useful eval categories:

- tool selection;
- plan quality;
- refusal and approval boundaries;
- secret handling;
- sandbox escape attempts;
- repository-write behavior;
- prompt regression;
- provider-routing regression;
- recovery from failed commands.

## 6. Keep CI boring and strict

CI should enforce mechanical safety:

- structure contract;
- formatting/linting;
- type checks where applicable;
- unit/integration tests;
- smoke evals;
- secret scans;
- artifact upload for eval traces.

Do not hide critical behavior inside GitHub Actions YAML. Prefer checked-in scripts that humans and agents can run locally.

## 7. Make agent work reviewable

A reviewer should be able to reconstruct:

```text
what was requested
what the agent planned
what files changed
what checks ran
what failed
what risk remains
how to roll back
```

This requires plans, PR templates, CI artifacts, and telemetry.

## 8. Put policy in code, not only prompts

Prompts are advisory. Critical boundaries should also exist in:

- allowlists/denylists;
- approval gates;
- test cases;
- evals;
- CI checks;
- runtime policy enforcement.

If violating a policy would be dangerous, do not rely on the model remembering it.

## 9. Prefer small reversible changes

Agents are strongest when tasks are bounded. Encourage:

- small PRs;
- explicit rollback;
- feature flags;
- adapter boundaries;
- minimal diffs;
- no opportunistic refactors.

## 10. Measure the harness, not only the model

For agentic systems, model quality is only one component. Track:

- task success rate;
- tool-call failure rate;
- approval frequency;
- loop count;
- time-to-first-useful-diff;
- CI pass rate;
- eval regression rate;
- human review corrections;
- rollback frequency.

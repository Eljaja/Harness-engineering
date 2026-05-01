# Sandbox contract

A sandbox contract defines what an agent can do while executing code or tools.

## Boundary model

Declare the default posture:

- filesystem: read-only / scoped write / full write;
- network: disabled / allowlist / unrestricted;
- process execution: disabled / allowlist / unrestricted;
- credentials: none / scoped / inherited;
- persistence: ephemeral / persisted workspace;
- resource limits: CPU, memory, disk, GPU, time.

## Recommended default

For untrusted or general coding agents:

- scoped workspace writes only;
- no host filesystem access;
- no credentials by default;
- no network unless explicitly required;
- bounded execution time;
- bounded output size;
- logs preserved for review;
- cleanup after run.

## Approval triggers

Require explicit approval before:

- deleting files outside the task scope;
- accessing credentials;
- using paid compute;
- opening external network access;
- writing to a repository or deployment target;
- changing auth, billing, sandbox, or policy code.

## Observability

Capture:

- command executed;
- working directory;
- environment summary with secrets redacted;
- exit code;
- duration;
- stdout/stderr truncation status;
- files written;
- policy decisions.

## Failure handling

When a sandbox command fails, the agent should:

1. read the error;
2. make the smallest plausible fix;
3. rerun the narrow command;
4. stop after repeated failures and summarize evidence.

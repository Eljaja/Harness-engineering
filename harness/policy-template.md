# Agent safety policy template

Use this policy to classify operations and decide when an agent needs approval.

## Risk classes

### Low risk

- reading repository files;
- editing docs;
- running local deterministic checks;
- adding tests that do not touch external services.

Approval: not required.

### Medium risk

- changing CI/CD;
- changing prompts;
- changing tool schemas;
- adding dependencies;
- adding networked tests with mocks.

Approval: usually not required, but requires plan and explicit PR notes.

### High risk

- modifying sandbox boundaries;
- modifying auth, billing, or permissions;
- writing to external repositories;
- accessing credentials;
- using paid compute;
- deleting persistent state;
- changing release automation.

Approval: required.

### Prohibited by default

- committing secrets;
- exfiltrating user/customer data;
- disabling safety gates without replacement;
- hiding telemetry from reviewers;
- destructive operations without explicit request and rollback.

## Policy implementation

Policies should be enforced in multiple layers:

- instructions;
- runtime allowlists/denylists;
- approval gates;
- tests;
- evals;
- CI checks;
- human review.

## PR requirements for policy changes

Policy changes must include:

- rationale;
- threat model impact;
- tests/evals;
- migration notes;
- rollback plan.

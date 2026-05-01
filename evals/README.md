# Evals

This directory stores lightweight smoke checks and scenario definitions for agent-first repository behavior.

## Purpose

Evals complement tests. They verify that the repository remains usable and safe for autonomous engineering workflows.

## Smoke suite

`evals/smoke/repository-contracts.yaml` describes the minimum repository contracts expected on every PR.

## Good evals check artifacts

Prefer checking concrete artifacts:

- required files;
- command output;
- trace events;
- tool contract sections;
- sandbox policy sections;
- PR body fields;
- plan files.

Avoid evals that only inspect whether an agent produced plausible prose.

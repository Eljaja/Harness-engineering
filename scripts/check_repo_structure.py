#!/usr/bin/env python3
"""Validate the minimal agent-first repository contract."""

from pathlib import Path
import sys

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "Makefile",
    ".github/pull_request_template.md",
    ".github/workflows/ci.yml",
    "docs/agent-first-repository.md",
    "docs/best-practices.md",
    "docs/ci-cd.md",
    "docs/evals.md",
    "docs/telemetry.md",
    "evals/AGENTS.md",
    "evals/README.md",
    "evals/smoke/repository-contracts.yaml",
    "harness/AGENTS.md",
    "harness/policy-template.md",
    "harness/sandbox-contract.md",
    "harness/tool-contract-template.md",
    "plans/AGENTS.md",
    "plans/templates/agent-change-plan.md",
    "scripts/check_repo_structure.py",
    "scripts/scan_secrets.py",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED_PATHS if not (root / path).exists()]
    if missing:
        print("Missing required repository contract paths:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("Repository structure contract OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

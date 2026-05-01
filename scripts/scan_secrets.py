#!/usr/bin/env python3
"""Lightweight secret-pattern scan for repository text files.

This is intentionally dependency-free so it can run in minimal CI. It is not a
replacement for a dedicated scanner such as gitleaks, but it catches common
mistakes early.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
    "__pycache__",
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=:-]{16,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
]

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".txt",
    ".sh",
    ".env",
    ".ini",
    ".cfg",
}


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix in TEXT_SUFFIXES or path.name in {"Makefile", "AGENTS.md"}


def main() -> int:
    findings: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{lineno}: possible secret pattern")
                    break

    if findings:
        print("Possible secrets found:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Secret scan OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

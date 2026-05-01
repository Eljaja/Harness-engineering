.PHONY: ci check-structure scan-secrets test eval-smoke

PYTHON ?= python3

ci: check-structure scan-secrets eval-smoke

check-structure:
	$(PYTHON) scripts/check_repo_structure.py

scan-secrets:
	$(PYTHON) scripts/scan_secrets.py

test: check-structure

eval-smoke: check-structure
	@echo "Smoke eval contract is present: evals/smoke/repository-contracts.yaml"

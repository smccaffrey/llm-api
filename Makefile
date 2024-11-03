.PHONY: server
server:
	poetry run uvicorn --reload llm.app:app --host 0.0.0.0 --port 3000

MERGE_BASE = $(shell git merge-base HEAD main)

.PHONY: lint
lint:
	poetry run pre-commit run

# Pre-commit against branch changes
.PHONY: lint-branch
lint-branch:
	poetry run pre-commit run --from-ref $(MERGE_BASE) --to-ref HEAD

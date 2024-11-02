.PHONY: server
server:
	poetry run uvicorn --reload llm.app:app --host 0.0.0.0 --port 3000
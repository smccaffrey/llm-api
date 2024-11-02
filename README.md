# llm-api
for self hosting LLM models within a FastAPI app

# Setup

Install

```
poetry install
```

# Run Service
```
make server
```
output should be something like this
```
poetry run uvicorn --reload llm.app:app --host 0.0.0.0 --port 3000
INFO:     Will watch for changes in these directories: ['/Users/sammccaffrey/Projects/llm-api']
INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
INFO:     Started reloader process [47783] using WatchFiles
Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object. Model will be on CPU.
INFO:     Started server process [47787]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

Test Prompt endpoint
```sh
curl --location --request GET 'http://0.0.0.0:3000/llm' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "what are cats?"
}'
```
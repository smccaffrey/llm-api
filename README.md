# llm-api
for self hosting LLM models within a FastAPI app

# Built using

- [Hugging Face](https://huggingface.co/)
- [vllm](https://github.com/vllm-project/vllm)

# Features
- **Stateless Model Calls:** The model itself, as loaded by the Hugging Face Transformers library, is stateless for each inference. When a request is sent, it doesn’t store or retain any data from that request after completing the response. Each prompt (input) is processed independently and does not affect subsequent prompts.

- **Caching the Model, Not the Data:** The lru_cache decorator only caches the model instance itself, not any data or output associated with individual requests. This means the model is reused in memory, but the data it processes remains isolated to each specific call.

- **Thread Safety and Memory Isolation:** FastAPI, when combined with `@lru_cache()`, handles concurrent requests by independently managing each request’s lifecycle. Even though the model instance is shared, the inferences themselves don’t share state, so there’s no data "leakage" between requests. 

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

# Contributing
yes please

## Generating stub files for poorly typed LLM libraries

```sh
poetry run pyright --createstub [package-name]
```

**Note: Ensure `pyrightconfig.json` captures all stub paths in the `"include"` paths**

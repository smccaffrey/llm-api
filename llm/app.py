

from fastapi import FastAPI

from llm.app_factory import get_app

app: FastAPI = get_app()
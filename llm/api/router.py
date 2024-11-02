from fastapi import APIRouter

class LlmRouter(APIRouter):
    """llm router"""
    def __init__(self) -> None:
        super().__init__()
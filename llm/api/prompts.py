from fastapi import Depends
from transformers.pipelines.base import Pipeline  # type: ignore

from llm.api.deps.ai import get_model
from llm.api.router import LlmRouter
from llm.schemas.llm import LlmRequest, LlmResponse
from llm.managers.llm import llm_manager


prompts_router = LlmRouter()


@prompts_router.get("/")
async def get(request: LlmRequest, model: Pipeline = Depends(get_model)) -> LlmResponse:
    response: str = llm_manager.prompt_response(prompt=request.prompt, model=model)
    return LlmResponse(response=response)
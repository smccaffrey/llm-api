from fastapi import Depends
from transformers.pipelines.base import Pipeline  # type: ignore

from llm.api.deps.ai import get_model
from llm.api.router import LlmRouter
from llm.schemas.prompts import PromptsRequest, PromptsResponse
from llm.managers.prompts import prompts_manager


prompts_router = LlmRouter()


@prompts_router.get("/")
async def get(
    request: PromptsRequest, model: Pipeline = Depends(get_model)
) -> PromptsResponse:
    response: str = prompts_manager.prompt_response(prompt=request.prompt, model=model)
    return PromptsResponse(response=response)



from llm.api.router import LlmRouter
from llm.schemas.llm import LlmRequest, LlmResponse
from llm.managers.llm import llm_manager

llm_router = LlmRouter()

@llm_router.get("/")
async def get(request: LlmRequest) -> LlmResponse:
    response = llm_manager.prompt_response(
        prompt=request.prompt
    )
    return LlmResponse(
        response=response
    )


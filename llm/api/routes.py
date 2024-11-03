from llm.api.router import LlmRouter

from llm.api.prompts import prompts_router


root_router = LlmRouter()


@root_router.get("/health")
@root_router.get("/")
def health_check() -> int:
    return 200


root_router.include_router(prompts_router, prefix="/prompts")
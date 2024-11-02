from llm.api.router import LlmRouter

from llm.api.llm import llm_router


root_router = LlmRouter()


@root_router.get("/health")
@root_router.get("/")
def health_check() -> int:
    return 200


root_router.include_router(llm_router, prefix="/llm")
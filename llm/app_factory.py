from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from llm.api import routes

def get_app() -> FastAPI:
    """Instantiate a users_api FastAPI instance. This instance will
    be parametrized by the values in users_api.settings.
    """
    app = FastAPI()  # type: ignore

    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
    )

    app.include_router(router=routes.root_router)

    return app

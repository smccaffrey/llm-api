

from pydantic import BaseModel


class LlmRequest(BaseModel):
    prompt: str

class LlmResponse(BaseModel):
    response: str
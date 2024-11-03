

from pydantic import BaseModel


class PromptsRequest(BaseModel):
    prompt: str

class PromptsResponse(BaseModel):
    response: str
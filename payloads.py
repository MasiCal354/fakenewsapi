from pydantic import BaseModel

class FakeNewsPayload(BaseModel):
    title: str
    text: str
    url: str = None
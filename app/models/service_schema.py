from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    url: str
    status: str
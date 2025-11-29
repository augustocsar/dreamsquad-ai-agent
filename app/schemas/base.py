from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    message: str
    docs: str
    status: str
from pydantic import BaseModel
from typing import Optional

class HealthInput(BaseModel):
    age: Optional[int] = None
    smoker: Optional[bool] = None
    exercise: Optional[str] = None
    diet: Optional[str] = None

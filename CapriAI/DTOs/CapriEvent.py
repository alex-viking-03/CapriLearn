from pydantic import BaseModel
from Enums.CapriEventType import CapriEventType

class CapriEvent(BaseModel):
    type: CapriEventType
    data: dict = {}
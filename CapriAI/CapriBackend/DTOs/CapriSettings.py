from pydantic import BaseModel

class CapriSettings(BaseModel):
    is_visible: bool = True
    animations_enabled: bool = True
from pydantic import ConfigDict, BaseModel
from datetime import datetime

from Enums.UserRole import UserRole

class RegisterDTO(BaseModel):
    username: str
    email: str
    password: str

class LogInDTO(BaseModel):
    email: str
    password: str

class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    role: UserRole
    is_active: bool
    created_at: datetime

class ChangeUserRoleDTO(BaseModel):
    role: UserRole
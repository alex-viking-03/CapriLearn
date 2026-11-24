from pydantic import BaseModel, ConfigDict

class TaskDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    course_id: int
    title: str
    description: str
    instructions: str
    starter_code: str
    order: int

class AddUpdateTaskDTO(BaseModel):
    title: str
    description: str
    instructions: str
    starter_code: str
    order: int


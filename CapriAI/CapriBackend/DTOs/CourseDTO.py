from pydantic import BaseModel, ConfigDict

class AddUpdateCourseDTO(BaseModel):
    title: str
    description: str
    language: str
    difficulty: int

class CourseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title:str
    description: str
    language: str
    difficulty: int
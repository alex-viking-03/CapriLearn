from pydantic import ConfigDict, BaseModel

class TaskTestCaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    task_id: int
    input_data: dict | list | str | int | float | bool
    expected_result: dict | list | str | int | float | bool
    is_hidden: bool

class AddUpdateTaskTestCaseDTO(BaseModel):
    input_data: dict | list | str | int | float | bool
    expected_result: dict | list | str | int | float | bool
    is_hidden: bool = False
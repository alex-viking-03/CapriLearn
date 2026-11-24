from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from DTOs.TaskTestCaseDTO import TaskTestCaseDTO, AddUpdateTaskTestCaseDTO
from Database import get_db
from Services import TaskTestCaseService
router = APIRouter(
    prefix="/api/tasks",
    tags=["Task test cases"])

@router.get("/{task_id}/test-cases", response_model=list[TaskTestCaseDTO])
def get_test_cases(task_id: int,
                   db: Session = Depends(get_db)):
    test_cases = TaskTestCaseService.get_test_cases(task_id, db)

    if test_cases is None:
        raise HTTPException(404, "Task not found")

    return test_cases

@router.get("/test-cases/{case_id}", response_model=TaskTestCaseDTO)
def get_case_by_id(case_id: int,
                   db: Session = Depends(get_db)):
    case = TaskTestCaseService.get_test_by_id(case_id, db)

    if case is None:
        raise HTTPException(404, "Test case not found")

    return case

@router.post("/{task_id}/test-cases/add", response_model=TaskTestCaseDTO)
def add_test_case(task_id: int,
                  request: AddUpdateTaskTestCaseDTO,
                  db: Session = Depends(get_db)):
    case = TaskTestCaseService.add_test_case(task_id, request, db)

    if case is None:
        raise HTTPException(404, "Task not found")
    
    return TaskTestCaseDTO.model_validate(case)

@router.put("/test-cases/{case_id}/update", response_model=TaskTestCaseDTO)
def update_test_case(case_id: int,
                     request: AddUpdateTaskTestCaseDTO,
                     db: Session = Depends(get_db)):
    case = TaskTestCaseService.update_test_case(case_id, request, db)

    if case is None:
        raise HTTPException(404, "Case not found")

    return TaskTestCaseDTO.model_validate(case)

@router.delete("/test-cases/{case_id}/delete")
def delete_test_case(case_id: int,
                     db: Session = Depends(get_db)):
    case = TaskTestCaseService.delete_test_case(case_id, db)

    if case is None:
        raise HTTPException(404, "Case not found")

    return {
        "case_id": case_id,
        "message": "Case was deleted successfully"}
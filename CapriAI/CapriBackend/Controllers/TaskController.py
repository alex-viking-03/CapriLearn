from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from DTOs.TaskDTO import TaskDTO, AddUpdateTaskDTO
from Database import get_db

from Services import CourseService, TaskService

router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"])

@router.get("/{course_id}/tasks", response_model = list[TaskDTO])
def get_course_tasks(course_id: int,
                     db: Session = Depends(get_db)):
    course = CourseService.get_course(db, course_id)

    if course is None:
        raise HTTPException(404, "Course not found")

    tasks = TaskService.get_course_tasks(db, course_id)

    return tasks

@router.get("/{task_id}", response_model=TaskDTO)
def get_task(task_id: int,
             db: Session = Depends(get_db)):
    task = TaskService.get_task(db, task_id)
    if task is None:
        raise HTTPException(404, "Task not found")

    return TaskDTO.model_validate(task)

@router.post("/{course_id}/add_task", response_model = TaskDTO)
def add_task_to_course(course_id: int,
                       request: AddUpdateTaskDTO,
                       db: Session = Depends(get_db)):
    task = TaskService.add_task(
        db,
        course_id,
        request)

    if task is None:
        raise HTTPException(404, "Course not found")

    return TaskDTO.model_validate(task)

@router.put("/{task_id}/update", response_model = TaskDTO)
def update_task(
    task_id: int,
    request: AddUpdateTaskDTO,
    db: Session = Depends(get_db)):
    task = TaskService.update_task(db, task_id, request)

    if task is None:
        raise HTTPException(
            404,
            "Task not found")

    return TaskDTO.model_validate(task)

@router.delete("/{task_id}/delete")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)):
    task = TaskService.delete_task(db, task_id)

    if task is None:
        raise HTTPException(404, "Task not found")
    
    return{
        "message": "Task was deleted successfully",
        "task_id": task_id}
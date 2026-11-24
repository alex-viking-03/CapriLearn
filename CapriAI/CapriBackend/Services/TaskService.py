from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.Course import Course
from Models.Task import Task
from DTOs.TaskDTO import AddUpdateTaskDTO


def get_course_tasks(db: Session, course_id: int):
    statement = (
        select(Task)
        .where(Task.course_id == course_id)
        .order_by(Task.order)
    )

    return db.scalars(statement).all()


def get_task(db: Session, task_id: int):
    task = db.get(Task, task_id)

    if task is None:
        return None

    print(f"""
    {task.description}
    {task.title}
    {task.starter_code}
    {task.instructions}
    {task.order}
    """)

    return task


def add_task(
    db: Session,
    course_id: int,
    request: AddUpdateTaskDTO
):
    course = db.get(Course, course_id)

    if course is None:
        return None

    task = Task(
        course_id=course_id,
        title=request.title,
        description=request.description,
        instructions=request.instructions,
        starter_code=request.starter_code,
        order=request.order
    )
    try:
        db.add(task)
        db.commit()
        db.refresh(task)
    except Exception:
        db.rollback()
        raise

    return task


def update_task(db: Session, task_id: int, request: AddUpdateTaskDTO):
    task = db.get(Task, task_id)

    if task is None:
        return None

    task.title = request.title
    task.description = request.description
    task.instructions = request.instructions
    task.starter_code = request.starter_code
    task.order = request.order

    try:
        db.commit()
        db.refresh(task)
    except Exception:
        db.rollback()
        raise

    return task


def delete_task(db: Session, task_id: int):
    task = db.get(Task, task_id)

    if task is None:
        return None

    try:
        db.delete(task)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return task
from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.TaskTestCase import TaskTestCase
from DTOs.TaskTestCaseDTO import AddUpdateTaskTestCaseDTO
from Models.Task import Task

def get_test_cases(task_id: int,
                   db: Session,
                   include_hidden: bool = False):
    task = db.get(Task, task_id)
    if task is None:
        return None

    statement = (select(TaskTestCase)
                 .where(TaskTestCase.task_id == task_id)
                 )
    if not include_hidden:
        statement = statement.where(TaskTestCase.is_hidden.is_(False))

    return db.scalars(statement).all()

def get_test_by_id(case_id: int,
                   db: Session):
    case = db.get(TaskTestCase, case_id)

    if case is None:
        return None

    return case

def add_test_case(task_id: int,
                  request: AddUpdateTaskTestCaseDTO,
                  db: Session):
    task = db.get(Task, task_id)

    if task is None:
        return None

    case = TaskTestCase(
        task_id = task_id,
        input_data = request.input_data,
        expected_result = request.expected_result,
        is_hidden = request.is_hidden
        )

    try:
        db.add(case)
        db.commit()
        db.refresh(case)
    except Exception:
        db.rollback()
        raise

    return case

def update_test_case(case_id: int,
                     request: AddUpdateTaskTestCaseDTO,
                     db: Session):
    case = db.get(TaskTestCase, case_id)

    if case is None:
        return None

    case.input_data = request.input_data
    case.expected_result = request.expected_result
    case.is_hidden = request.is_hidden

    try:
        db.commit()
        db.refresh(case)
    except Exception:
        db.rollback()
        raise

    return case

def delete_test_case(case_id: int,
                     db: Session):
    case = db.get(TaskTestCase, case_id)

    if case is None:
        return None

    try:
        db.delete(case)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return case
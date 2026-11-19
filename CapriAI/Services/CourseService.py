from sqlalchemy import select
from sqlalchemy.orm import Session

from DTOs.CourseDTO import AddUpdateCourseDTO
from Models.Course import Course


def get_courses(db: Session):
    statement = select(Course)
    return db.scalars(statement).all()


def get_course(db: Session, course_id: int):
    return db.get(Course, course_id)


def add_course(db: Session, title: str, description: str,
               language: str, difficulty: int):

    course = Course(
        title=title,
        description=description,
        language=language,
        difficulty=difficulty
    )

    try:
        db.add(course)
        db.commit()
        db.refresh(course)
    except Exception:
        db.rollback()
        raise

    return course

def update_course(db: Session, course_id: int, request: AddUpdateCourseDTO):
    course = db.get(Course, course_id)

    if course is None:
        return None

    course.title = request.title
    course.description = request.description
    course.difficulty = request.difficulty
    course.language = request.language

    try:
        db.commit()
        db.refresh(course)
    except Exception:
        db.rollback()
        raise

    return course

def delete_course(db: Session, course_id: int):
    course = db.get(Course, course_id)

    if course is None:
        return None

    try:
        db.delete(course)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return course

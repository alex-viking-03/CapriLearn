from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Services import CourseService

from Database import get_db
from DTOs.CourseDTO import CourseDTO, AddUpdateCourseDTO

router = APIRouter(
    prefix="/api/courses",
    tags=["Courses"])

@router.get("", response_model=list[CourseDTO])
def get_courses(db: Session = Depends(get_db)):
    return CourseService.get_courses(db)

@router.post("/add_course", response_model = CourseDTO)
def add_course(request: AddUpdateCourseDTO,
               db: Session = Depends(get_db)):
    course = CourseService.add_course(
        db, 
        request.title, 
        request.description, 
        request.language, 
        request.difficulty)

    response = CourseDTO.model_validate(course)

    return response

@router.get("/{course_id}", response_model = CourseDTO)
def get_course(course_id: int,
               db: Session = Depends(get_db)):
    course = CourseService.get_course(db, course_id)

    if course is None:
        raise HTTPException(
            404,
            "Course not found")

    response = CourseDTO.model_validate(course)

    return response

@router.put("/{course_id}/update", response_model=CourseDTO)
def update_course(course_id: int,
                  request: AddUpdateCourseDTO,
                  db: Session = Depends(get_db)
                  ):
    course = CourseService.update_course(db, course_id, request)

    if course is None:
        raise HTTPException(404, "Course not found")

    return CourseDTO.model_validate(course)


@router.delete("/{course_id}/delete")
def delete_course(course_id: int,
                  db: Session = Depends(get_db)):
    course = CourseService.delete_course(db, course_id)

    if course is None:
        raise HTTPException(404, "Course not found")

    return {
        "message": "Course was deleted successfully",
        "course_id": course_id}
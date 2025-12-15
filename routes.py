from fastapi import FastAPI, APIRouter
from course_model import Course
from course_service import CourseService
from course_repository import CourseRepository


router = APIRouter()
course_repository = CourseRepository()
course_service = CourseService(course_repository)


@router.get('/courses')
def get_all_courses():
    return {"message:" : "OK!"}

@router.post('/courses')
def add_new_course(course: Course) -> Course:
    return course_service.create_course(course)
    

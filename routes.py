from fastapi import FastAPI, APIRouter
from course_model import Course
from course_service import CourseService
from course_repository import CourseRepository


router = APIRouter()
course_repository = CourseRepository()
course_service = CourseService(course_repository)

@router.post('/courses')
def add_new_course(course: Course) -> Course:
    return course_service.create_course(course)

@router.get('/courses')
def get_all_courses():
    return course_service.show_courses()

@router.put('/course/{id_course}')
def update_course(id_course: str, course: Course):
    return course_service.update_course(id_course, course)
    
@router.delete('/course/{id_course}')
def delete_course(id_course: str):
    print("entrei na rota")
    return course_service.delete_course(id_course)

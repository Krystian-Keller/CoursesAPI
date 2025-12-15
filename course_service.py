from course_repository import CourseRepository
from course_model import Course

class CourseService:
    
    def __init__(self, course_repository : CourseRepository):
        self.course_repository = course_repository
    
    def create_course(self, course: Course) -> Course:
        self.course_repository.add(course)
        return course
        
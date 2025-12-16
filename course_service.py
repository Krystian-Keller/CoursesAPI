from course_repository import CourseRepository
from course_model import Course

class CourseService:
    
    def __init__(self, course_repository : CourseRepository):
        self.course_repository = course_repository
    
    def create_course(self, course: Course) -> Course:
        self.course_repository.add(course)
        return course
    
    def show_courses(self) -> list[Course]:
        return self.course_repository.get_all()
    
    def delete_course(self, id_course):
        for idx, course in enumerate(self.course_repository.course_list):
            if course.id == id_course:
                return self.course_repository.delete_course(idx)
        else:
            return {"message": "Course Not Found"}
        
    def update_course(self, id_course: str, course: Course):
        print('Service')
        for idx, course in enumerate(self.course_repository.course_list):
            if course.id == id_course:
                print(f"idx servuice: {idx}")
                return self.course_repository.update_course(idx, course)
        else:
            return {"message:" : "Course Not Found"}
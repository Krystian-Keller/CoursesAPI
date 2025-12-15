from course_model import Course

class CourseRepository:
    course_list = []
    
    def __init__(self):
        course_list = []
    
    def add(self, course: Course):
        self.course_list.append(course)
    
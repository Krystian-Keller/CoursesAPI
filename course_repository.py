from course_model import Course

class CourseRepository:
    course_list = []
    
    def __init__(self):
        course_list = []
    
    def add(self, course: Course):
        self.course_list.append(course)
    
    def get_all(self) -> list[Course]:
        return self.course_list
    
    def delete_course(self, idx: str) -> Course:
        return self.course_list.pop(idx)
    
    def update_course(self, idx: int, course: Course) -> Course:
        # print(idx)
        self.course_list[idx] = course
        return course
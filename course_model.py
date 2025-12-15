from pydantic import BaseModel

class Course(BaseModel):
    id: str
    course_name: str
    description: str
    max_students: str
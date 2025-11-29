from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    author: str
    price: float
    image: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

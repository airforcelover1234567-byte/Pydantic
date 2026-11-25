from pydantic import BaseModel,Field
from typing import List

class Student(BaseModel):
    name: str = Field(...,min_length=3)
    age: int=Field(...,gt=13, le=18)
    email: str=Field(..., min_length=1)
    marks: float=Field(ge=0,le=100)
    subjects: List[str]=Field(min_length=3)
    is_enrolled: bool =True

student_data={"name":"Rounak Roy","age":14,"email":"rounak@gmail.com","marks":1,"subjects":["maths","science","sst"],"is_enrolled":False}
data=Student(**student_data)
print(data)
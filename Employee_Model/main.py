from pydantic import BaseModel,Field
from typing import Optional

#Fields:
#id
#name
#department
#salary

class Employee(BaseModel)
    id: int
    name: str =Field(...,
                min_length=3,
                max_length=50,
                descripton="Employee Name",
                example="Rounak Roy")
    department: Optional[str] = 'General'
    salary: float=Field(...,
                ge=10000)
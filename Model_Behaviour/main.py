from pydantic import BaseModel,field_validator,model_validator,computed_field

# class User(BaseModel):
#     username: str

#     @field_validator("username")
#     def username(cls,v):
#         if len(v)>4:
#             raise ValueError("Length should be atleast 4 characters")
#         return v

# class SIgnup(BaseModel):
#     password: str
#     confirm_password: str

#     @model_validator(mode="after")
#     def password_match(cls, values):
#         if values.password!=values.confirm_password:
#             raise ValueError("Passwords do not match")
#         return values

# class Product(BaseModel):
#     price: float
#     quantity: int

#     @computed_field
#     @property
#     def total_price(self) -> float:
#         return self.price*self.quantity

class inputs(BaseModel):
    name: int
    def __init__(self,name):
        self.name=name
object=inputs("Rounak")
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data={"id":101, "name":"Rounak", "is_active":'True'} #This is not an error as pydantic tries to convert the data into the required data type

user=User(**input_data)
print(user)

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool =True

product_data={"id":101,"name":"Legion", "price":12000.00, "in_stock":False}
product=Product(**product_data)
print(product)
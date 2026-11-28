from pydantic import BaseModel,field_validator,model_validator,computed_field

name=str(input("Enter name of food: "))
quantity=int(input("Enter quantity: "))

class Food(BaseModel):
    name: int
    quantity: int

    @field_validator('quantity')
    @classmethod
    def quantity_food(cls,value):
        if value>5:
            print("We are out of food")
        return value

    @field_validator('name')
    @classmethod
    def name_check(cls,value):
        if type(value)==int:
            print("You have entered a number")
        return value

order=Food(name=name,quantity=quantity)
print(Food.quantity_food)
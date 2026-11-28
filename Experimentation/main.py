from pydantic import BaseModel,field_validator,model_validator,computed_field

name=str(input("Enter name of food: "))
quantity=int(input("Enter quantity: "))

class Food(BaseModel):
    name: str
    quantity: int

    @field_validator
    def quantity_food(cls,value):
        if value>5:
            print("We are out of food")
        return value

order=Food(name=name,quantity=quantity)
print(Food.quantity_food(Food,quantity))
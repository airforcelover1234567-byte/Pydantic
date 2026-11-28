from pydantic import BaseModel,field_validator,model_validator,computed_field

class Subscription(BaseModel):
    plan: str
    monthly_price: int
    months: int
    discount: int

    @field_validator('plan','monthly_price')
    @classmethod
    def plan_check(cls,value:str,price:int):
        if value.lower()!="basic" or "pro" or "enterprise":
            print("Enter a proper plan")
        else:
            match value:
                case "basic":
                    if price>500:
                        print("You cannot pay so much money")

user=Subscription(plan="Basic",monthly_price=600)
user.plan_check
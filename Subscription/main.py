from pydantic import BaseModel,field_validator,model_validator,computed_field

class Subscription(BaseModel):
    plan: str
    monthly_price: int
    months: int
    discount: int

    @field_validator('plan')
    @classmethod
    def plan_check(cls,value):
        if value.lower() not in "basic" or "pro" or "enterprise":
            print("Enter a proper plan")
        return value

plan=str(input("Enter a plan: "))
user=Subscription(plan=plan)
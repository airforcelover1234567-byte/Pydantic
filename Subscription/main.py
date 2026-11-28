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
            raise ValueError("Enter a proper plan")
        return value

    @model_validator(mode="after")
    @classmethod
    def basic_check(cls,value):
        if value.plan.lower()=="basic" and value.monthly_price>500:
            raise ValueError("For Basic, monthly price cannot be more than 500")
        return value

plan=str(input("Enter a plan: "))
monthly_price=int(input("Enter the monthly price: "))
months=int(input("Enter the month: "))
discount=int(input("Enter the discount: "))
user=Subscription(plan=plan)
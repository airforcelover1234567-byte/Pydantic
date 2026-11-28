from pydantic import BaseModel,computed_field,model_validator,field_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_validation(cls, value):
        if len(value)<4:
            raise ValueError("Username atleast must be 4 characters")
        return value

class signup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password!=values.confirm_password:
            raise ValueError("Your passwords do not match")
        return values
    
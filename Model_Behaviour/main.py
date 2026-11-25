from pydantic import BaseModel,field_validator,model_validator,computed_field

class User(BaseModel):
    username: str

    @field_validator("username")
    def username(cls,v):
        if len(v)>4:
            raise ValueError("Length should be atleast 4 characters")
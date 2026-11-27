from pydantic import BaseModel,field_validator,model_validator,computed_field

class User(BaseModel):
    username: str

    @field_validator("username")
    def username(cls,v):
        if len(v)>4:
            raise ValueError("Length should be atleast 4 characters")
        return v

class SIgnup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password!=values.confirm_password:
            raise ValueError("Passwords do not match")
        return values

class inputs(BaseModel):
    name: int
object=inputs(name=1)

class Name(BaseModel):
    first_name: str
    last_name: str

    @computed_field
    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

persons=Name(first_name="Rounak",last_name="Roy")
print(persons.fullname)

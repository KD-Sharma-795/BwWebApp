from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

# Dummy user (for testing)
DUMMY_USER = {
    "email": "admin@gmail.com",
    "password": "123456"
}

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.email == DUMMY_USER["email"] and data.password == DUMMY_USER["password"]:
        return {
            "access_token": "dummy_token_123",
            "token_type": "bearer",
            "user": {
                "email": data.email
            }
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}
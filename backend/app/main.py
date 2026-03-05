from fastapi import FastAPI
from app.api import auth
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Booking Window API")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

app.include_router(auth.router)


from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from crud import create_user, get_user
from database_connection import SessionLocal

app = FastAPI()

class User(BaseModel):
    user_name: str
    password: str

@app.post("/api-post-request-registration")
def registration_data(registered_data: User):
    with SessionLocal() as db:
        create_user(db, user_name=registered_data.user_name, password=registered_data.password)

    return {"message": "Registered Successfully", "User_name": registered_data.user_name}

@app.post("/api-post-request-login")
def log_in_data(login_data: User):
    with SessionLocal() as db:
        user = get_user(db, user_name=login_data.user_name)

    if user and user.password == login_data.password:
        return {"message": "Login Successful", "User_name": login_data.user_name}
    else:
        return {"message": "Login Failed"}

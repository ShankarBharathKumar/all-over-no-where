from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    user_name: str
    password: int


registered_users = {}


@app.post("/api-post-request-registration")
def registration_data(registered_data: User):
    registered_user_name = registered_data.user_name
    registered_password = registered_data.password

    registered_users[registered_user_name] = registered_password

    return {"message": "Registered Successfully", "User_name": registered_user_name}


@app.post("/api-post-request-login")
def log_in_data(login_data: User):
    login_user_name = login_data.user_name
    login_password = login_data.password

    if login_user_name in registered_users and registered_users[login_user_name] == login_password:
        return {"message": "Login Successfull", "User_name": login_user_name}
    else:
        return {"message": "Login Failed"}

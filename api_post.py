from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    first_name: str
    last_name: str


@app.post("/just-post-request")
def data(user_data: User):
    f_name = user_data.first_name
    l_name = user_data.last_name

    full_name = f'{f_name} {l_name}'

    return{"message": "api-post-request-successfull", "Full_Name": full_name}

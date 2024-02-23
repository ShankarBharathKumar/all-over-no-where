from fastapi import FastAPI

app = FastAPI()

@app.get("/just-get-request")
def data():
    return{"message": "api-get-request-successfull"}

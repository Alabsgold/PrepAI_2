from fastapi import FastAPI
from api.v1 import quiz

app = FastAPI()

app.include_router(quiz.router, prefix="/api/v1/quiz")

@app.get("/")
def read_root():
    return {"Hello": "World"}

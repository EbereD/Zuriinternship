from fastapi import FastAPI
from pydantic import BaseModel, Field


class Response(BaseModel):
    slack_username: str = Field(alias='slackUsername')
    backend: bool
    age: int
    bio: str

    class Config:
        allow_population_by_field_name = True


response = Response(
    slack_username="EbereDurumbah",
    backend=True,
    age=27,
    bio="Awesome Coder"
)

app = FastAPI()


@app.get('/', response_model=Response, status_code=200)
def get():
    return response

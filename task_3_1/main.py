from fastapi import FastAPI
from pydantic import BaseModel, field_validator
import re

app = FastAPI() # Запуск: uvicorn task_3_1.main:app --reload

class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None
    password: str
    is_subscribed: bool | None = None


    @field_validator("email")
    def validate_message(cls, value):
        regexp = r"\S+@\S+\.\S+"
        if len(re.findall(regexp, value)) == 1:
            return value
        return str(re.findall(regexp, value))

    @field_validator("age")
    def validate_age(cls, value):
        if value is None:
            return value
        if value > 0:
            return value
        raise ValueError("Возраст должен быть положительным целым числом")


@app.post("/create_user")
async def create_user(user_create: UserCreate):
    return user_create

import uuid
from fastapi import FastAPI, HTTPException, Response, Cookie
from pydantic import BaseModel

app = FastAPI() # Запуск: uvicorn task5.main:app --reload

class User(BaseModel):
    username: str
    password: str

# Симуляция базы данных в виде списка объектов пользователей
user_data = [
    User(**{"username": "user1", "password": "pass1"}),
    User(**{"username": "user2", "password": "pass2"})
]

session_data = []

@app.post("/login")
def login(user: User, response: Response):
    if user in user_data:
        session_id = str(uuid.uuid4())
        session_data.append(dict(session_id=session_id, user=user))
        response.set_cookie(key="session_token", value=session_id, max_age=60, httponly=True)
        return {"message": "Cookie has been set!"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/user")
def user(session_token: str | None = Cookie(default=None)):
    if session_token is not None:
        for session in session_data:
            if session["session_id"] == session_token:
                return {"user_name": session["user"].username, "password": session["user"].password}
            else:
                raise HTTPException(status_code=401, detail="Unauthorized")
    raise HTTPException(status_code=401, detail="Unauthorized")
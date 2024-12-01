from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=50, description="Имя пользователя")
    age: int = 0


users: List[User] = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})

    raise HTTPException(status_code=404, detail=f"User was not found, ID: {user_id}")


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(user: CreateUser) -> User:
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, user: CreateUser) -> User:
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u

    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int) -> User:
    for i, u in enumerate(users):
        if u.id == user_id:
            temp = u
            del users[i]
            return temp

    raise HTTPException(status_code=404, detail="User was not found")

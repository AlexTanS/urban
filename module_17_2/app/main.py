from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get("/", response_model=dict)
async def index():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)

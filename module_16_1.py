from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_iden(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def user_info(username: str = "Default", age: int = 0) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

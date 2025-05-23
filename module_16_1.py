from fastapi import FastAPI
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута
@app.get("/")
async def root() -> dict:
    return {'message': 'Главная страница'}
# Маршрут для административной панели
@app.get("/user/admin")
async def admin_page() -> dict:
    return {'user': 'Вы вошли как администратор'}
# Маршрут с динамическим параметром пути
@app.get("/user/{user_id}")
async def read_user(user_id: int)-> dict:
    return {'user': f'Вы вошли как пользователь № {user_id}'}
# Маршрут с параметрами  запроса
@app.get('/user')
async def user_info(username: str, age: int)-> dict:
    return {'user': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

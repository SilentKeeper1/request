from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title= "список для збереження імен користувачів")

users = []


class User(BaseModel):
    name: str


async def add_user(name: str):
    if name in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(name)


@app.post("/user")
async def create_user(user: User):
    await add_user(user.name)
    return {"message": f"User '{user.name}' added successfully."}


@app.get("/users")
async def get_users():
    return {"users": users}


@app.delete("/users/{name}")
async def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(name)
    return {"message": f"User '{name}' deleted successfully."}

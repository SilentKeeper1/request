from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


tasks = []


class Task(BaseModel):
    name: str
    description: str
    is_done: Optional[bool] = False

# Перегляд усіх задач
@app.get("/tasks/", status_code=200)
def get_tasks():
    return tasks

# Перегляд однієї задачі за ID
@app.get("/tasks/{task_id}/", status_code=200)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# Додавання нового завдання
@app.post("/tasks/", status_code=201)
def create_task(task: Task):
    tasks.append(task.dict())
    return {"status": "Task added", "task_id": len(tasks) - 1}

# Редагування завдання
@app.put("/tasks/{task_id}/", status_code=200)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task.dict()
    return {"status": "Task updated"}

# Видалення завдання
@app.delete("/tasks/{task_id}/", status_code=200)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"status": "Task deleted"}

# Відмітити як виконане/невиконане
@app.patch("/tasks/{task_id}/done/", status_code=200)
def mark_task_done(task_id: int, done: bool):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id]["is_done"] = done
    return {"status": f"Task marked as {'done' if done else 'not done'}"}

from fastapi import FastAPI
from pydantic import BaseModel, Field
from celery.result import AsyncResult
from typing import Any
from celery_worker import generate_text_task
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/generateText")
async def generate_text(prompt: Prompt) -> Any:
    task = generate_text_task.delay(prompt.prompt)
    return {"task_id": task.id}


@app.get("/task/{task_id}")
async def get_generate_text(task_id: str):
    task = AsyncResult(task_id)
    if task.ready():
        task_result = task.get()
        return {
            "result": task_result[0],
            "time": task_result[1],
            "memory": task_result[2],
        }
    else:
        return {"status": "Task Pending"}

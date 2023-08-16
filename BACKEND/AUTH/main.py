from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db.config import database
from models.tudoModel import Todo
from views.todo import (
    fetch_todo,
    getALLTodo,
    createTodo,
    updateTodo,
    deleteTpdo
    )

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/todo')
async def getAllTodo():
    response = await getALLTodo()
    return response

@app.get("/api/todo{title}", response_model=Todo)
async def getOneTodo(title):
    response = await fetch_todo(title)
    if response:
        return response
    raise HTTPException(404, f"Il n'existe pas de todo ayant ce titre !")


@app.post("/api/todo", response_model=Todo)
async def createTodoList(todo:Todo):
    response = await createTodo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo{title}", response_model=Todo)
async def putTodo(title:str, desc:str) :
    response = await updateTodo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no TODO item with this title {title}")

@app.delete("/api/todo{title}")
async def deleteTodoItem(title:str, desc:str) :
    response = await deleteTpdo(title)
    if response:
        return "Suppression avec succès !"
    raise HTTPException(404, f"There is no TODO item with this title {title}")


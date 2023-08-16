from db.config import database
from models.tudoModel import Todo

collection = database.todo

async def fetch_todo(title):
    document = collection.find_one({"title": title})
    return document

async def getALLTodo():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def createTodo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result

async def updateTodo(title, desc):
    await collection.update_one({'title':title}, {"$set": {'desc': desc}})
    document = await collection.find_one({"title":title})
    return document


async def deleteTpdo(title):
    await collection.delete_one({"title":title})
    return True
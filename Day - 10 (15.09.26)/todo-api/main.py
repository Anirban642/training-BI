from fastapi import FastAPI, HTTPException, Query
from schemas import CategoryIn, CategoryOut, TodoIn, TodoOut, TodoUpdate

# from typing import Optional

app = FastAPI()

categories = []
todos = []
category_id = 1
todo_id = 1


@app.get("/")
def home():
    return {"message": "Todo API Working !"}


# create category
@app.post("/categories/", response_model=CategoryOut, status_code=201)
def create_category(category: CategoryIn):
    global category_id
    for item in categories:
        if item["name"].lower() == category.name.lower():
            raise HTTPException(status_code=400, detail="Category already exists")
    new_cat = {"id": category_id, "name": category.name}
    categories.append(new_cat)
    category_id += 1
    return new_cat


# get all category
@app.get("/categories/", response_model=list[CategoryOut])
def get_categories():
    return categories


# get single category by id
@app.get("/categories/{id}", response_model=CategoryOut)
def get_category(id: int):
    for category in categories:
        if category["id"] == id:
            return category
    raise HTTPException(status_code=404, detail="Category Not Found")


# update category
@app.put("/categories/{id}", response_model=CategoryOut)
def update_category(id: int, category: CategoryIn):
    for item in categories:
        if item["id"] != id and item["name"].lower() == category.name.lower():
            raise HTTPException(status_code=400, detail="Category already exists")
    for item in categories:
        if item["id"] == id:
            item["name"] = category.name
            return item
    raise HTTPException(status_code=404, detail="Category Not Found")


# delete category
@app.delete("/categories/{id}")
def delete_category(id: int):
    for category in categories:
        if category["id"] == id:
            for todo in todos:
                if todo["category_id"] == id:
                    raise HTTPException(
                        status_code=400, detail="Cannot delete category with todos"
                    )
            categories.remove(category)
            return {"message": "Category deleted"}
    raise HTTPException(status_code=404, detail="Category not found")


# helper function
def category_exists(category_id: int):
    for category in categories:
        if category["id"] == category_id:
            return True
    return False


# create todo
@app.post("/todos/", response_model=TodoOut, status_code=201)
def create_todo(todo: TodoIn):
    global todo_id
    if not category_exists(todo.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    new_todo = {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "isDone": False,
        "category_id": todo.category_id,
    }
    todos.append(new_todo)
    todo_id += 1

    return new_todo


# get all todos
@app.get("/todos/", response_model=list[TodoOut])
def get_todos(
    completed: bool | None = None,
    search: str | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
):
    res = todos
    if completed is not None:
        res = [todo for todo in res if todo["isDone"] == completed]
    if search:
        search = search.lower()
        res = [
            todo
            for todo in res
            if search in todo["title"].lower() or search in todo["description"].lower()
        ]
    start = (page - 1) * limit
    end = start + limit
    return res[start:end]


# get todo by id
@app.get("/todos/{id}", response_model=TodoOut)
def get_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# update todo
@app.put("/todos/{id}", response_model=TodoOut)
def update_todo(id: int, todo: TodoUpdate):
    if not category_exists(todo.category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    for item in todos:
        if item["id"] == id:
            item["title"] = todo.title
            item["description"] = todo.description
            item["isDone"] = todo.isDone
            item["category_id"] = todo.category_id
            return item
    raise HTTPException(status_code=404, detail="Todo not found")


# delete todo
@app.delete("/todos/{id}")
def delete_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")


# get todos by category using generator (next())
@app.get("/categories/{category_id}/todos", response_model=list[TodoOut])
def get_todos_by_category(category_id: int):
    category = next(
        (category for category in categories if category["id"] == category_id), None
    )
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return [todo for todo in todos if todo["category_id"] == category_id]


# delete all todos by category
@app.delete("/categories/{category_id}/todos")
def delete_todos_by_category(category_id: int):
    for category in categories:
        if category["id"] == category_id:
            global todos
            todos = [todo for todo in todos if todo["category_id"] != category_id]
            return {"message": "Todos deleted"}
    raise HTTPException(status_code=404, detail="Category not found")

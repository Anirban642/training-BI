from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Category, Todo
from schemas import CategoryIn, CategoryOut, TodoIn, TodoOut, TodoUpdate

app = FastAPI()

Base.metadata.create_all(bind=engine)


# home route
@app.get("/")
def home():
    return {"message": "Todo API Working!"}


# create category
@app.post("/categories/", response_model=CategoryOut, status_code=201)
def create_category(category: CategoryIn, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    new_category = Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# get all categories
@app.get("/categories/", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


# get category by id
@app.get("/categories/{id}", response_model=CategoryOut)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# update category
@app.put("/categories/{id}", response_model=CategoryOut)
def update_category(id: int, category: CategoryIn, db: Session = Depends(get_db)):
    item = db.query(Category).filter(Category.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Category not found")
    existing = db.query(Category).filter(Category.name == category.name, Category.id != id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    item.name = category.name
    db.commit()
    db.refresh(item)
    return item


# delete category
@app.delete("/categories/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    if category.todos:
        raise HTTPException(status_code=400, detail="Cannot delete category with todos")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}


# create todo
@app.post("/todos/", response_model=TodoOut, status_code=201)
def create_todo(todo: TodoIn, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == todo.category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        isDone=False,
        category_id=todo.category_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# get all todos
@app.get("/todos/", response_model=list[TodoOut])
def get_todos(
    completed: bool | None = None,
    search: str | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    query = db.query(Todo)
    if completed is not None:
        query = query.filter(Todo.isDone == completed)
    if search:
        search = f"%{search}%"
        query = query.filter((Todo.title.ilike(search)) | (Todo.description.ilike(search)))
    offset = (page - 1) * limit
    return query.offset(offset).limit(limit).all()


# get todo by id
@app.get("/todos/{id}", response_model=TodoOut)
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# update todo
@app.put("/todos/{id}", response_model=TodoOut)
def update_todo(id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    item = db.query(Todo).filter(Todo.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    category = db.query(Category).filter(Category.id == todo.category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    item.title = todo.title
    item.description = todo.description
    item.isDone = todo.isDone
    item.category_id = todo.category_id
    db.commit()
    db.refresh(item)
    return item


# delete todo
@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}


# get todos by category
@app.get("/categories/{id}/todos", response_model=list[TodoOut])
def get_todos_by_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db.query(Todo).filter(Todo.category_id == id).all()


# delete all todos in category
@app.delete("/categories/{id}/todos")
def delete_todos_by_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    deleted = db.query(Todo).filter(Todo.category_id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Todos deleted", "deleted_count": deleted}


# get todo statistics
@app.get("/todos/stats")
def get_todo_stats(db: Session = Depends(get_db)):
    total = db.query(Todo).count()
    completed = db.query(Todo).filter(Todo.isDone == True).count()
    pending = total - completed
    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }
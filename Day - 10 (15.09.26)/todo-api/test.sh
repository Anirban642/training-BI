curl -X POST http://127.0.0.1:8000/categories/ -H "Content-Type: application/json" -d "{\"name\":\"Study\"}"

curl -X POST http://127.0.0.1:8000/categories/ -H "Content-Type: application/json" -d "{\"name\":\"Work\"}"

curl -X POST http://127.0.0.1:8000/todos/ -H "Content-Type: application/json" -d "{\"title\":\"Learn FastAPI\",\"description\":\"Practice CRUD\",\"category_id\":1}"

curl -X POST http://127.0.0.1:8000/todos/ -H "Content-Type: application/json" -d "{\"title\":\"Learn Pydantic\",\"description\":\"Practice validation\",\"category_id\":1}"

curl -X POST http://127.0.0.1:8000/todos/ -H "Content-Type: application/json" -d "{\"title\":\"Complete Assignment\",\"description\":\"Finish FastAPI assignment\",\"category_id\":2}"
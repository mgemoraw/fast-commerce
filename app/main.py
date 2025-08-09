from fastapi import FastAPI, Path, Query, Form, File, UploadFile, Request, Depends
from fastapi.responses import JSONResponse
from typing import List,Tuple
from pydantic import BaseModel, Field
# from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from items import routes as items_routes
from books import book_routes
from users import user_routes
from chat import routes as chat_routes


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")





@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 'name': 'FastAPI'})

@app.post("/submit")
async def submit(request: Request):
    form_data = await request.form()
    username = form_data.get("username", "")
    password = form_data.get("password", "")
    file: UploadFile = form_data.get("file")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "name": "FastAPI",
        "message": f"You submitted: {username} with password: {password} and file: {file.filename if file else 'No file uploaded'} successfully!",
        "current_time": "2023-10-01 12:00:00"  # Placeholder for current time
    })




async def dependency(id: str, name: str, age: int):
    return {"id": id, "name": name, "age": age}


@app.get("/user/")
async def user(dep: dict = Depends(dependency)):
    return dep

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(items_routes.router, prefix="/items", tags=["items"])
app.include_router(book_routes.router, prefix="/books", tags=["books"])
app.include_router(chat_routes.router, prefix="/chat", tags=["chat"])
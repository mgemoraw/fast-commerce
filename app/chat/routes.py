from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from core.database import get_db

from users.schemas import User
from users.models import UserModel
from .models import ChatModel
from .schemas import ChatSchema
from .chat_manager import manager 



templates = Jinja2Templates(directory="templates")


router = APIRouter()

# router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("socket.html", {"request": request, 'name': 'Chat Application'})


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{websocket.client.host} wrote: {data}")




@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id:int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client {client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_id} has left the chat.")



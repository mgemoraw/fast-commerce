from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import WebSocket


class ChatSchema(BaseModel):
    user_id: int
    message: str


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: Optional[WebSocket] = None):
        if websocket:
            await websocket.send_text(message)
            return
        if not self.active_connections:
            return
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        return
    
manager = ConnectionManager()

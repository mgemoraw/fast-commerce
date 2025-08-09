
from typing import Optional, List
from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        # Initialize a list to keep track of active WebSocket connections
        self.active_connections: List[WebSocket] = []


    async def connect(self, websocket: WebSocket):
        print("Connecting to WebSocket...")
        print(f"client {websocket.client.host}: {websocket.client.port} connected")
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"Active connections: {len(self.active_connections)}")

    async def disconnect(self, websocket: WebSocket):
        print("Disconnecting WebSocket...")
        print(f"client {websocket.client.host}: {websocket.client.port} disconnected")
        self.active_connections.remove(websocket)
        print(f"Active connections: {len(self.active_connections)}")

    async def send_message(self,message:str, websocket: Optional[WebSocket] = None):
        if websocket:
            await websocket.send_text(message)
            # self.active_connections.append(websocket)
            return
        if not self.active_connections:
            return

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        return


class ConnectionManager:
    def __init__(self):
        # Initialize a list to keep track of active WebSocket connections
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: Optional[WebSocket] = None):
        _message = {
            "client": f"{websocket.client.host}: {websocket.client.port}",
            "type": "text",
            message: message,
        }

        if websocket:
            await websocket.send_text(_message)
            return
        if not self.active_connections:
            return
    

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        return


# manager = ConnectionManager()
manager = WebSocketManager()
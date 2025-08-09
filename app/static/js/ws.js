// Assign a random client ID (can replace with logged-in username)
const clientId = Math.floor(Math.random() * 1000);

// Connect to WebSocket server
const ws = new WebSocket(`ws://${window.location.host}/chat/ws/${clientId}`);

ws.onopen = function () {
    addSystemMessage(`You joined the chat as Client ${clientId} 👋`);
};

ws.onmessage = function (event) {
    // const msg = event.data;
    const msg = JSON.parse(event.data);
    console.log("Received message:", msg);

    if (msg.includes(`Client ${clientId} says`) || msg.startsWith("You wrote")) {
        addMessage(msg, "my-message");
    } else if (msg.includes("has left") || msg.includes("joined")) {
        addSystemMessage(msg);
    } else {
        addMessage(msg, "other-message");
    }
};

ws.onerror = function (event) {
    console.error("WebSocket error observed:", event);
    addSystemMessage("An error occurred with the WebSocket connection.");
}

ws.onclose = function (event) {
    if (event.wasClean) {
        addSystemMessage(`Connection closed cleanly, code=${event.code}, reason=${event.reason}`);
    } else {
        addSystemMessage("Connection closed unexpectedly.");
    }
}


// Send message on form submit
function sendMessage(event) {
    event.preventDefault();
    const input = document.getElementById("messageText");
    const text = input.value.trim();
    if (text) {
        ws.send(text);
        input.value = "";
    }
}

// Add a regular message to chat
function addMessage(text, cssClass) {
    const li = document.createElement("li");
    li.textContent = text;
    li.classList.add(cssClass);
    document.getElementById("messages").appendChild(li);
    scrollChatToBottom();
}

// Add a system message to chat
function addSystemMessage(text) {
    const li = document.createElement("li");
    li.textContent = text;
    li.classList.add("system-message");
    document.getElementById("messages").appendChild(li);
    scrollChatToBottom();
}

// Auto scroll chat to bottom
function scrollChatToBottom() {
    const chatBox = document.getElementById("chat-box");
    chatBox.scrollTop = chatBox.scrollHeight;
}

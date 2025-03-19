import { createMessageElement } from "./message-formatter";

document.addEventListener('DOMContentLoaded', () => {
const socket = io('/chat', {
    auth: {
        username: 'user123'
    }
});

const messages = document.getElementById('messages');
const messageInput = document.getElementById('message');
const usernameInput = document.getElementById('username');

socket.on('connect', () => {
    console.log('connected to server')
})

socket.on('message', (data) => {
    console.log(data);
    const messageElement = createMessageElement(data.message);
    messages.appendChild(messageElement);
    messages.scrollTop = messages.scrollHeight;
});

function sendMessage() {
    const message = messageInput.value.trim();
    const username = usernameInput.value.trim();

    if (message) {
        socket.emit(
            'message',
            {
                username: username,
                message: message
            }
        );
        messageInput.value = '';
    }
}


messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
})



   /* messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    })*/
})
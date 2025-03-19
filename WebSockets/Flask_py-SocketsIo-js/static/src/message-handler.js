export function createMessageElement(message) {
    const messageElement = document.createElement('div');
    messageElement.className = message;
    messageElement.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
    return messageElement
}
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessage);

    const response = await fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    const botMessage = document.createElement('div');
    botMessage.textContent = `Bot: ${data.response}`;
    chatBox.appendChild(botMessage);

    document.getElementById('user-input').value = '';
}

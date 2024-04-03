document.getElementById('sendButton').addEventListener('click', async function () {
    console.log('Send button clicked');
    var userInputField = document.getElementById('userInput');
    var userInput = userInputField.value;

    // clear the user input field
    userInputField.value = '';

    console.log('User input:', userInput);
    var chatLog = document.getElementById('chatLog');

    // Display user input
    chatLog.innerHTML += '<p><strong>User:</strong> ' + userInput + '</p>';

    // Call the function to send the message to the server and display the AI response
    console.log('Before sendMessageToServer');
    await sendMessageToServer(userInput);
    console.log('After sendMessageToServer');
});

async function sendMessageToServer(userInput) {
    var chatLog = document.getElementById('chatLog');
    console.log('sendMessageToServer called with:', userInput);
    try {
        console.log('About to send fetch request');
        const response = await fetch('http://127.0.0.1:3000/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        });

        console.log('Fetch request completed');

        if (!response.ok) {
            console.error('Fetch request failed:', response);
        }

        const data = await response.json();

        console.log('Received response:', data);

        // Now data.message contains the AI response. You can display this in your HTML.
        chatLog.innerHTML += '<p><strong>AI:</strong><pre>' + data.message + '</pre></p>';
    } catch (error) {
        console.error('An error occurred:', error);
    }
    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}

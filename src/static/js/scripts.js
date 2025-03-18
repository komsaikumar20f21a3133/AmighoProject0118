document.addEventListener('DOMContentLoaded', function() {
    const commandInput = document.getElementById('command-input');
    const submitButton = document.getElementById('submit-button');
    const responseArea = document.getElementById('response-area');

    submitButton.addEventListener('click', function() {
        const command = commandInput.value;
        if (command) {
            fetch('/execute-command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ command: command })
            })
            .then(response => response.json())
            .then(data => {
                responseArea.innerText = data.response;
                commandInput.value = '';
            })
            .catch(error => {
                console.error('Error:', error);
                responseArea.innerText = 'An error occurred. Please try again.';
            });
        }
    });
});
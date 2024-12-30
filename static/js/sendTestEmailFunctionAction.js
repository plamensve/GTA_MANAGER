function sendEmail() {
    const emailInput = document.getElementById('email-input');
    const email = emailInput.value;

    if (!email) {
        alert("Моля, въведете имейл адрес.");
        return;
    }

    fetch('/send-email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: new URLSearchParams({ 'email': email })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage(data.success);
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function showSuccessMessage(message) {
    const messageBox = document.getElementById('success-message');
    messageBox.textContent = message;
    messageBox.classList.remove('hidden');
    messageBox.classList.add('visible');

    setTimeout(() => {
        messageBox.classList.remove('visible');
        messageBox.classList.add('hidden');
    }, 3000); // Съобщението изчезва след 3 секунди
}
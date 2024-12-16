const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// Превключване между панелите
signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

// Задържане на панела за регистрация, ако формата е невалидна
document.addEventListener('DOMContentLoaded', () => {
    if (container.dataset.formInvalid === "true") {
        container.classList.add("right-panel-active");
    }
});

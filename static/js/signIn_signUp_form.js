const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const registerForm = document.getElementById('registerForm'); // Вземи формата по ID

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

// Превенция на прехвърляне към вход, ако формата е невалидна
registerForm.addEventListener('submit', (event) => {
    // Проверка дали формата е валидна
    if (!registerForm.checkValidity()) {
        event.preventDefault();  // Спира изпращането на формата
        container.classList.add("right-panel-active"); // Задържа панела за регистрация активен
    }
});

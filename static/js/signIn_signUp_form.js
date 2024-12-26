const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// Превключване към панела за регистрация
signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
    toggleFormVisibility();
});

// Превключване към панела за вход
signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
    toggleFormVisibility();
});

// Функция за управление на видимостта
function toggleFormVisibility() {
    const signUpContainer = document.querySelector('.sign-up-container');
    const signInContainer = document.querySelector('.sign-in-container');

    if (container.classList.contains("right-panel-active")) {
        signUpContainer.style.display = 'block';
        signInContainer.style.display = 'none';
    } else {
        signUpContainer.style.display = 'none';
        signInContainer.style.display = 'block';
    }
}

// Задаване на първоначалната видимост при зареждане на страницата
document.addEventListener('DOMContentLoaded', () => {
    toggleFormVisibility();
});

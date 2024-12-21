document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".navbar-toggle");
    const navbarMenu = document.querySelector(".navbar-menu");

    toggleButton.addEventListener("click", function () {
        navbarMenu.classList.toggle("active");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Избор на всички табове и панели
    const tabs = document.querySelectorAll(".tab-item");
    const panels = document.querySelectorAll(".tab-panel-unique");

    tabs.forEach((tab) => {
        tab.addEventListener("click", function () {
            // Премахване на активния клас от всички табове
            tabs.forEach((item) => item.classList.remove("active"));

            // Премахване на активния клас от всички панели
            panels.forEach((panel) => panel.classList.remove("active"));

            // Активиране на текущия таб
            this.classList.add("active");

            // Показване на съответния панел
            const target = this.getAttribute("data-tab");
            document.getElementById(`${target}-unique`).classList.add("active");
        });
    });
});
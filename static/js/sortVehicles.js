
document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".vehicle-table");
    const typeHeader = table.querySelector("th.sortable"); // Намира "Тип" чрез класа sortable

    typeHeader.addEventListener("click", () => {
        const tbody = table.querySelector("tbody");
        const rows = Array.from(tbody.querySelectorAll("tr"));

        // Проверка дали вече е сортирано
        const isAscending = typeHeader.classList.contains("asc");

        // Сортиране на редовете
        const sortedRows = rows.sort((rowA, rowB) => {
            const typeA = rowA.querySelector("td:nth-child(2)").innerText.trim().toUpperCase();
            const typeB = rowB.querySelector("td:nth-child(2)").innerText.trim().toUpperCase();

            return isAscending ? typeB.localeCompare(typeA) : typeA.localeCompare(typeB);
        });

        // Обновяване на таблицата
        tbody.innerHTML = "";
        sortedRows.forEach(row => tbody.appendChild(row));

        // Обновяване на класа за посока
        table.querySelectorAll("th").forEach(th => th.classList.remove("asc", "desc"));
        typeHeader.classList.toggle("asc", !isAscending);
        typeHeader.classList.toggle("desc", isAscending);
    });
});


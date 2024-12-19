document.addEventListener('DOMContentLoaded', function () {
    console.log('Initializing Flatpickr...');
    flatpickr('.flatpickr-date', {
        dateFormat: 'Y-m-d', // Формат на датата
    });
});

function openTab(event, tabId) {
    // Hide all tab content
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => content.classList.remove('active-tab'));

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => button.classList.remove('active'));

    // Show the current tab and set the active button
    document.getElementById(tabId).classList.add('active-tab');
    event.currentTarget.classList.add('active');}
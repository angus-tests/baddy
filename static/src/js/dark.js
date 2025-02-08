
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("dark-mode-toggle");
    const root = document.documentElement;

    // Load dark mode preference from localStorage
    const darkMode = localStorage.getItem("darkMode") === "true";

    // Apply the correct theme and update the icons on page load
    if (darkMode) {
        root.setAttribute("data-theme", "dark");
    } else {
        root.setAttribute("data-theme", "light");
    }

    // Toggle event listener
    if (toggle) {
        toggle.addEventListener("click", function () {
            const isDark = root.getAttribute("data-theme") === "light";
            root.setAttribute("data-theme", isDark ? "dark" : "light");
            localStorage.setItem("darkMode", isDark);
        });
    }
});

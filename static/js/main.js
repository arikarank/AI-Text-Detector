// Dark mode toggle with localStorage
(function () {
    const body = document.body;
    const toggleBtn = document.getElementById("themeToggle");

    const THEME_KEY = "ai_text_detector_theme";

    function applyTheme(theme) {
        if (theme === "dark") {
            body.classList.add("dark");
        } else {
            body.classList.remove("dark");
        }
    }

    // Load saved theme
    const saved = localStorage.getItem(THEME_KEY) || "light";
    applyTheme(saved);

    if (toggleBtn) {
        toggleBtn.textContent = body.classList.contains("dark") ? "☀️" : "🌙";
        toggleBtn.addEventListener("click", () => {
            const newTheme = body.classList.contains("dark") ? "light" : "dark";
            applyTheme(newTheme);
            localStorage.setItem(THEME_KEY, newTheme);
            toggleBtn.textContent = newTheme === "dark" ? "☀️" : "🌙";
        });
    }

    // Flash close buttons + auto-hide
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach((flash) => {
        const closeBtn = flash.querySelector(".flash-close");
        if (closeBtn) {
            closeBtn.addEventListener("click", () => {
                flash.style.opacity = "0";
                flash.style.transform = "translateY(-4px)";
                setTimeout(() => flash.remove(), 200);
            });
        }
        // auto hide after 4 seconds
        setTimeout(() => {
            if (flash.parentNode) {
                flash.style.opacity = "0";
                flash.style.transform = "translateY(-4px)";
                setTimeout(() => flash.remove(), 200);
            }
        }, 4000);
    });
})();

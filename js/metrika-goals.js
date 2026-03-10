// Yandex Metrika + Google Analytics 4 Goals
document.addEventListener("DOMContentLoaded", function() {
    // Goal: Click on "Записаться" buttons
    document.querySelectorAll(".nav-cta, .btn-service, .btn-telegram, .btn-primary, .btn-white").forEach(function(btn) {
        btn.addEventListener("click", function() {
            // Yandex Metrika
            if (typeof ym !== "undefined") {
                ym(95862074, "reachGoal", "zapis_click");
                console.log("Counter 95862074: goal zapis_click reached");
            }
            // Google Analytics 4
            if (typeof gtag !== "undefined") {
                gtag('event', 'zapis_click', {
                    'event_category': 'conversion',
                    'event_label': 'Запись на консультацию'
                });
            }
        });
    });
    
    // Goal: Telegram link click
    document.querySelectorAll("a[href*='t.me']").forEach(function(link) {
        link.addEventListener("click", function() {
            // Yandex Metrika
            if (typeof ym !== "undefined") {
                ym(95862074, "reachGoal", "telegram_click");
                console.log("Counter 95862074: goal telegram_click reached");
            }
            // Google Analytics 4
            if (typeof gtag !== "undefined") {
                gtag('event', 'telegram_click', {
                    'event_category': 'conversion',
                    'event_label': 'Переход в Telegram'
                });
            }
        });
    });
    
    // Goal: Form submit
    document.querySelectorAll("form").forEach(function(form) {
        form.addEventListener("submit", function() {
            // Yandex Metrika
            if (typeof ym !== "undefined") {
                ym(95862074, "reachGoal", "form_submit");
                console.log("Counter 95862074: goal form_submit reached");
            }
            // Google Analytics 4
            if (typeof gtag !== "undefined") {
                gtag('event', 'form_submit', {
                    'event_category': 'conversion',
                    'event_label': 'Отправка формы'
                });
            }
        });
    });
    
    // Goal: Document download
    document.querySelectorAll("a[download]").forEach(function(link) {
        link.addEventListener("click", function() {
            // Yandex Metrika
            if (typeof ym !== "undefined") {
                ym(95862074, "reachGoal", "download_click");
                console.log("Counter 95862074: goal download_click reached");
            }
            // Google Analytics 4
            if (typeof gtag !== "undefined") {
                gtag('event', 'download_click', {
                    'event_category': 'conversion',
                    'event_label': 'Скачивание документа'
                });
            }
        });
    });
});
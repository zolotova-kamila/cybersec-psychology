    <script>
    // Yandex Metrika Goals
    document.addEventListener("DOMContentLoaded", function() {
        // Goal: Click on "Записаться" buttons
        document.querySelectorAll(".nav-cta, .btn-service, .btn-telegram, .btn-primary, .btn-white").forEach(function(btn) {
            btn.addEventListener("click", function() {
                if (typeof ym !== "undefined") {
                    ym(95862074, "reachGoal", "zapis_click");
                }
            });
        });
        
        // Goal: Telegram link click
        document.querySelectorAll("a[href*='t.me']").forEach(function(link) {
            link.addEventListener("click", function() {
                if (typeof ym !== "undefined") {
                    ym(95862074, "reachGoal", "telegram_click");
                }
            });
        });
        
        // Goal: Form submit
        document.querySelectorAll("form").forEach(function(form) {
            form.addEventListener("submit", function() {
                if (typeof ym !== "undefined") {
                    ym(95862074, "reachGoal", "form_submit");
                }
            });
        });
        
        // Goal: Document download
        document.querySelectorAll("a[download]").forEach(function(link) {
            link.addEventListener("click", function() {
                if (typeof ym !== "undefined") {
                    ym(95862074, "reachGoal", "download_click");
                }
            });
        });
    });
    </script>
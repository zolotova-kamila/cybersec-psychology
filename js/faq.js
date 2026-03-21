// FAQ accordion
document.querySelectorAll('.faq-question').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var answer = this.nextElementSibling;
        var icon = this.querySelector('.faq-icon');
        var isOpen = answer.style.display === 'block';

        // Close all
        document.querySelectorAll('.faq-answer').forEach(function(a) { a.style.display = 'none'; });
        document.querySelectorAll('.faq-icon').forEach(function(i) { i.textContent = '+'; });

        // Toggle current
        if (!isOpen) {
            answer.style.display = 'block';
            if (icon) icon.textContent = '−';
        }
    });
});

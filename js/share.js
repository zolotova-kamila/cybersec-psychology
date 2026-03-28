// Share panel functionality
document.addEventListener('DOMContentLoaded', function() {
    // Create share panel HTML
    const sharePanel = document.createElement('div');
    sharePanel.className = 'share-panel';
    sharePanel.innerHTML = `
        <div class="share-panel-label">Поделиться</div>
        <button class="share-btn vk" title="Поделиться ВКонтакте" data-share="vk">VK</button>
        <button class="share-btn tg" title="Поделиться в Telegram" data-share="tg">TG</button>
        <button class="share-btn wa" title="Поделиться в WhatsApp" data-share="wa">WA</button>
        <button class="share-btn copy" title="Копировать ссылку" data-share="copy">📋</button>
    `;
    
    // Add to page
    document.body.appendChild(sharePanel);
    
    // Get current page URL and title
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    
    // Share buttons click handlers
    sharePanel.querySelectorAll('.share-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const type = this.dataset.share;
            let shareUrl = '';
            
            switch(type) {
                case 'vk':
                    shareUrl = `https://vk.com/share.php?url=${url}&title=${title}`;
                    window.open(shareUrl, '_blank', 'width=600,height=400');
                    break;
                case 'tg':
                    shareUrl = `https://t.me/share/url?url=${url}&text=${title}`;
                    window.open(shareUrl, '_blank');
                    break;
                case 'wa':
                    shareUrl = `https://wa.me/?text=${title}%20${url}`;
                    window.open(shareUrl, '_blank');
                    break;
                case 'copy':
                    navigator.clipboard.writeText(window.location.href).then(() => {
                        this.classList.add('copied');
                        this.innerHTML = '✓';
                        setTimeout(() => {
                            this.classList.remove('copied');
                            this.innerHTML = '📋';
                        }, 2000);
                    }).catch(() => {
                        // Fallback for older browsers
                        const input = document.createElement('input');
                        input.value = window.location.href;
                        document.body.appendChild(input);
                        input.select();
                        document.execCommand('copy');
                        document.body.removeChild(input);
                        this.classList.add('copied');
                        this.innerHTML = '✓';
                        setTimeout(() => {
                            this.classList.remove('copied');
                            this.innerHTML = '📋';
                        }, 2000);
                    });
                    break;
            }
        });
    });
});
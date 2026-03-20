// Cookie Consent Banner for 152-FZ Compliance
(function() {
    'use strict';
    
    const COOKIE_NAME = 'cookie_consent';
    const COOKIE_EXPIRY_DAYS = 365;
    
    // Check if consent already given
    function getCookie(name) {
        const value = '; ' + document.cookie;
        const parts = value.split('; ' + name + '=');
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }
    
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = name + '=' + value + ';expires=' + date.toUTCString() + ';path=/;Secure;SameSite=Strict';
    }
    
    function hasConsent() {
        return getCookie(COOKIE_NAME) === 'accepted';
    }
    
    function hasDeclined() {
        return getCookie(COOKIE_NAME) === 'declined';
    }
    
    // Create banner HTML
    function createBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-banner';
        banner.innerHTML = `
            <div class="cookie-content">
                <div class="cookie-text">
                    <strong>Мы используем файлы cookie</strong>
                    <p>Для анализа трафика и улучшения работы сайта. Продолжая использовать сайт, вы соглашаетесь с 
                    <a href="privacy.html" target="_blank">политикой конфиденциальности</a>.</p>
                </div>
                <div class="cookie-buttons">
                    <button class="cookie-btn cookie-btn-decline" id="cookie-decline">Отклонить</button>
                    <button class="cookie-btn cookie-btn-accept" id="cookie-accept">Принять</button>
                </div>
            </div>
        `;
        document.body.appendChild(banner);
        
        // Add styles with fallback colors
        const styles = document.createElement('style');
        styles.textContent = `
            #cookie-banner {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: #FAF8F5;
                border-top: 2px solid #2D5A4A;
                padding: 16px 20px;
                z-index: 9999;
                font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
                animation: slideUp 0.3s ease-out;
            }
            
            @keyframes slideUp {
                from { transform: translateY(100%); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            
            .cookie-content {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 20px;
            }
            
            .cookie-text strong {
                display: block;
                color: #2D3436;
                margin-bottom: 4px;
                font-size: 15px;
            }
            
            .cookie-text p {
                margin: 0;
                color: #5A6266;
            }
            
            .cookie-text a {
                color: #2D5A4A;
                text-decoration: underline;
            }
            
            .cookie-text a:hover {
                color: #1E3D32;
            }
            
            .cookie-buttons {
                display: flex;
                gap: 10px;
                flex-shrink: 0;
            }
            
            .cookie-btn {
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
                font-size: 14px;
                font-weight: 500;
                cursor: pointer;
                transition: all 0.2s ease;
            }
            
            .cookie-btn-accept {
                background: #2D5A4A;
                color: white;
            }
            
            .cookie-btn-accept:hover {
                background: #1E3D32;
            }
            
            .cookie-btn-decline {
                background: transparent;
                color: #5A6266;
                border: 1px solid #D4CCC2;
            }
            
            .cookie-btn-decline:hover {
                background: #F5F1EB;
                border-color: #2D5A4A;
                color: #2D5A4A;
            }
            
            /* Mobile */
            @media (max-width: 768px) {
                .cookie-content {
                    flex-direction: column;
                    text-align: center;
                }
                
                .cookie-buttons {
                    width: 100%;
                    justify-content: center;
                }
                
                .cookie-btn {
                    flex: 1;
                    max-width: 150px;
                }
            }
            
            /* Hidden state */
            #cookie-banner.hidden {
                display: none !important;
            }
        `;
        document.head.appendChild(styles);
        
        // Event listeners
        document.getElementById('cookie-accept').addEventListener('click', function() {
            setCookie(COOKIE_NAME, 'accepted', COOKIE_EXPIRY_DAYS);
            banner.classList.add('hidden');
            enableAnalytics();
        });
        
        document.getElementById('cookie-decline').addEventListener('click', function() {
            setCookie(COOKIE_NAME, 'declined', COOKIE_EXPIRY_DAYS);
            banner.classList.add('hidden');
            disableAnalytics();
        });
    }
    
    // Enable analytics after consent
    function enableAnalytics() {
        console.log('Cookie consent: Analytics enabled');
    }
    
    // Disable analytics if declined
    function disableAnalytics() {
        if (typeof ym !== 'undefined') {
            window.ym = function() { console.log('Analytics disabled by user choice'); };
        }
        if (typeof gtag !== 'undefined') {
            window.gtag = function() { console.log('Analytics disabled by user choice'); };
        }
    }
    
    // Initialize
    function init() {
        if (!hasConsent() && !hasDeclined()) {
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', createBanner);
            } else {
                createBanner();
            }
        } else if (hasDeclined()) {
            disableAnalytics();
        }
    }
    
    init();
})();
"""Standardize all article pages to match sotsialnaya-trevoga.html design."""
import re
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# STANDARD COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

CSS_LINKS = (
    '<link rel="stylesheet" href="../css/fonts.css">\n'
    '<link rel="stylesheet" href="../css/footer.css">\n'
    '<link rel="stylesheet" href="../css/styles.css">\n'
    '<link rel="stylesheet" href="../css/article.css">'
)

STANDARD_NAV = """<nav>
    <a href="../index.html" class="logo">
        <img loading="lazy" src="../images/logo-kz-flat.webp" alt="KZ" class="logo-icon-img">
        <span>Камила Золотова</span>
    </a>
    <ul class="nav-links">
        <li><a href="../index.html">Главная</a></li>
        <li><a href="../about.html">Обо мне</a></li>
        <li><a href="../services.html">Услуги</a></li>
        <li><a href="../resources.html" class="active">Материалы</a></li>
        <li><a href="../contact.html">Контакты</a></li>
    </ul>
    <button class="menu-toggle" id="menuToggle" aria-label="Открыть меню">
        <span></span>
        <span></span>
        <span></span>
    </button>
    <a href="https://t.me/Kamila_Zolotova" target="_blank" rel="noopener noreferrer" class="nav-cta">Записаться</a>
</nav>"""

REFERENCE_CSS = """:root {
    --accent: #2A7B6F;
    --accent-dark: #1A5248;
    --accent-light: #E8F5F2;
    --gold: #C9A84C;
    --cream: #F5F1EB;
    --warm-mid: #EDE8E0;
    --ink: #2D3436;
    --muted: #5A6266;
  }

  main { padding-top: 70px; }

  /* BREADCRUMB */
  .breadcrumb {
    max-width: 760px; margin: 0 auto; padding: 20px 24px 0;
    font-family: 'Montserrat', sans-serif; font-size: 0.8rem; color: var(--muted);
  }
  .breadcrumb a { color: var(--muted); text-decoration: none; }
  .breadcrumb a:hover { color: var(--accent); }
  .breadcrumb span { margin: 0 6px; }

  /* HERO */
  .article-hero {
    background: linear-gradient(135deg, var(--cream) 0%, var(--warm-mid) 100%);
    padding: 60px 40px 40px; text-align: center; margin-top: 0;
  }
  .article-hero .tag {
    display: inline-block; font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent);
    margin-bottom: 20px; font-family: 'Montserrat', sans-serif;
  }
  .article-hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 4.5vw, 3.2rem);
    font-weight: 300; line-height: 1.18; color: var(--ink);
    margin-bottom: 24px; max-width: 800px; margin-left: auto; margin-right: auto;
  }
  .article-hero h1 em { font-style: italic; color: var(--accent); }
  .article-hero .lead {
    font-size: 1.15rem; color: var(--muted); max-width: 700px;
    line-height: 1.75; margin: 0 auto 24px;
    font-family: 'Cormorant Garamond', serif; font-style: italic;
  }
  .article-hero .meta {
    font-size: 0.85rem; color: var(--muted); letter-spacing: 0.05em;
    font-family: 'Montserrat', sans-serif;
  }
  .article-hero .meta a { color: var(--muted); text-decoration: none; }

  /* TOC */
  .toc {
    background: #fff; border: 1px solid var(--border, #D4CCC2);
    border-radius: 8px; padding: 28px 32px; margin: 40px auto; max-width: 720px;
  }
  .toc-title {
    font-size: 0.75rem; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--muted); margin-bottom: 16px;
    font-family: 'Montserrat', sans-serif;
  }
  .toc ol { padding-left: 20px; margin: 0; }
  .toc ol li { margin-bottom: 10px; font-size: 0.95rem; }
  .toc ol li a {
    color: var(--ink); text-decoration: none;
    border-bottom: 1px solid transparent; transition: border-color 0.2s, color 0.2s;
  }
  .toc ol li a:hover { color: var(--accent); border-bottom-color: var(--accent); }

  /* PULL QUOTE */
  .pull-quote {
    border-top: 1px solid var(--border, #D4CCC2);
    border-bottom: 1px solid var(--border, #D4CCC2);
    margin: 2.5em 0; padding: 2em;
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.3rem, 2.5vw, 1.7rem);
    font-style: italic; font-weight: 300;
    color: var(--accent); line-height: 1.4;
    text-align: center; background: var(--cream);
  }

  /* CALLOUT */
  .callout {
    background: var(--accent-light); border-left: 4px solid var(--accent);
    padding: 24px 28px; margin: 2em 0; border-radius: 0 8px 8px 0;
  }
  .callout strong {
    display: block; font-size: 0.8rem; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--accent); margin-bottom: 10px;
    font-weight: 600; font-family: 'Montserrat', sans-serif;
  }
  .callout p { margin: 0; font-size: 1rem; }

  /* CHECK LIST */
  .check-list { list-style: none; margin: 1em 0 1.5em; padding: 0; }
  .check-list li {
    padding: 10px 0 10px 32px; position: relative;
    border-bottom: 1px solid var(--warm-mid); font-size: 1rem;
  }
  .check-list li:last-child { border-bottom: none; }
  .check-list li::before {
    content: '\u2713'; position: absolute; left: 0;
    color: var(--accent); font-weight: 600; font-size: 1.1rem;
  }

  /* STAT ROW */
  .stat-row {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 1px; background: var(--border, #D4CCC2);
    border: 1px solid var(--border, #D4CCC2);
    border-radius: 8px; overflow: hidden; margin: 2.5em 0;
  }
  .stat-item { background: #fff; padding: 28px 20px; text-align: center; }
  .stat-num {
    font-family: 'Cormorant Garamond', serif; font-size: 2.6rem;
    font-weight: 300; color: var(--accent); line-height: 1; display: block;
  }
  .stat-label { font-size: 0.85rem; color: var(--muted); margin-top: 10px; line-height: 1.5; }

  /* EXERCISE */
  .exercise {
    background: #fff; border: 1px solid var(--border, #D4CCC2);
    border-radius: 8px; padding: 32px; margin: 2.5em 0;
  }
  .exercise-label {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--muted); margin-bottom: 12px;
    display: block; font-family: 'Montserrat', sans-serif;
  }
  .exercise h3 { margin-top: 0; font-size: 1.25rem; margin-bottom: 16px; }
  .exercise ol { padding-left: 24px; margin-top: 16px; }
  .exercise ol li { margin-bottom: 12px; font-size: 1rem; line-height: 1.7; }
  .exercise-note {
    margin-top: 20px; font-size: 0.92rem; color: var(--muted);
    border-top: 1px solid var(--warm-mid); padding-top: 16px; font-style: italic;
  }

  /* DIVIDER */
  .divider { width: 60px; height: 2px; background: var(--accent); margin: 3em auto; }

  /* FAQ */
  .faq-section { margin: 3em 0; }
  .faq-item { border-bottom: 1px solid var(--border, #D4CCC2); }
  .faq-q {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 0; cursor: pointer; font-weight: 500; font-size: 1.05rem;
    gap: 16px; user-select: none;
  }
  .faq-q::after {
    content: '+'; font-size: 1.5rem; color: var(--accent);
    flex-shrink: 0; transition: transform 0.2s; font-weight: 300;
  }
  .faq-item.open .faq-q::after { transform: rotate(45deg); }
  .faq-a { display: none; padding-bottom: 20px; font-size: 1rem; color: var(--muted); line-height: 1.75; }
  .faq-item.open .faq-a { display: block; }

  /* CTA BLOCK */
  .cta-block {
    background: linear-gradient(135deg, var(--accent-dark) 0%, var(--accent) 100%);
    color: #fff; padding: 60px 48px; margin: 4em 0 0; border-radius: 12px; text-align: center;
  }
  .cta-block h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.6rem, 3vw, 2.2rem);
    font-weight: 300; color: #fff; margin: 0 0 16px;
  }
  .cta-block p { color: rgba(255,255,255,0.85); font-size: 1rem; margin: 0 0 24px; }
  .cta-block ul { list-style: none; padding: 0; margin: 0 auto 28px; display: inline-block; text-align: left; }
  .cta-block ul li { font-size: 0.95rem; color: rgba(255,255,255,0.8); padding: 6px 0 6px 24px; position: relative; }
  .cta-block ul li::before { content: '\u2192'; position: absolute; left: 0; color: var(--gold); }
  .cta-main {
    background: var(--gold); color: var(--ink); padding: 16px 40px; border-radius: 40px;
    font-size: 0.85rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
    text-decoration: none; display: inline-block; transition: all 0.2s;
    font-family: 'Montserrat', sans-serif;
  }
  .cta-main:hover { background: #fff; color: var(--accent-dark); }

  /* RELATED */
  .related { margin: 4em 0; }
  .related h2 { margin-top: 0; text-align: center; }
  .related-grid {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 1.5em;
  }
  .related-card {
    background: #fff; border: 1px solid var(--border, #D4CCC2);
    border-radius: 8px; padding: 24px; text-decoration: none;
    color: var(--ink); transition: all 0.2s; display: block;
  }
  .related-card:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
  .related-card-tag {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--accent); margin-bottom: 10px;
    display: block; font-family: 'Montserrat', sans-serif;
  }
  .related-card h3 {
    font-family: 'Cormorant Garamond', serif; font-size: 1.15rem;
    font-weight: 400; margin: 0; line-height: 1.4;
  }

  @media (max-width: 768px) {
    .article-hero { padding: 40px 20px 30px; }
    .toc { margin: 30px 20px; padding: 20px 24px; }
    .stat-row { grid-template-columns: 1fr; }
    .stat-item { padding: 20px; }
    .exercise { padding: 24px 20px; }
    .cta-block { padding: 40px 24px; }
    .related-grid { grid-template-columns: 1fr; }
  }"""

# CSS selector patterns to REMOVE from legacy inline styles
STRIP_SELECTORS = [
    r'\*\s*,\s*\*::before[^{]*',
    r'\*\s*',
    r'html\s*',
    r'body\s*',
    r'main\s*',
    r'\.nav\s*',
    r'\.nav-logo[^{]*',
    r'\.nav-sep[^{]*',
    r'\.nav-crumb[^{]*',
    r'\.nav-current[^{]*',
    r'\.nav-links[^{]*',
    r'\.hero\s*',
    r'\.hero::before[^{]*',
    r'\.hero-tag[^{]*',
    r'\.hero\s+h1[^{]*',
    r'\.hero-sub[^{]*',
    r'\.hero-meta[^{]*',
    r'\.hero-content[^{]*',
    r'\.hero-category[^{]*',
    r'\.hero-date[^{]*',
    r'\.hero-title[^{]*',
    r'\.hero-subtitle[^{]*',
    r'\.hero-accent[^{]*',
    r'\.hero\s+h1,',
    r':root\s*',
]

ARTICLE_META = {
    'kpt-terapiya-chto-eto.html':
        {'crumb': 'КПТ-терапия', 'section': 'КПТ', 'tag': 'КПТ · 10 мин чтения'},
    'dpdg-emdr-chto-eto.html':
        {'crumb': 'ДПДГ (EMDR)', 'section': 'Терапия', 'tag': 'ДПДГ · 10 мин чтения'},
    'sindrom-samozvantsa.html':
        {'crumb': 'Синдром самозванца', 'section': 'Тревога', 'tag': 'Самооценка · 10 мин чтения'},
    'trevoga-emigranta.html':
        {'crumb': 'Тревога эмигранта', 'section': 'Эмиграция', 'tag': 'Эмиграция · 10 мин чтения'},
    'deneshnye-scenarii-detstva.html':
        {'crumb': 'Денежные сценарии детства', 'section': 'Психология денег', 'tag': 'Деньги · 12 мин чтения'},
    'finansovye-konflikty-v-pare.html':
        {'crumb': 'Финансы в паре', 'section': 'Отношения', 'tag': 'Отношения · 10 мин чтения'},
    'finansovaya-trevozhnost-russkiy-sposob.html':
        {'crumb': 'Финансовая тревожность', 'section': 'Тревога', 'tag': 'Финансы · 12 мин чтения'},
    'gruppovaya-terapiya-chto-eto.html':
        {'crumb': 'Групповая терапия', 'section': 'Терапия', 'tag': 'Групповая терапия · 10 мин чтения'},
    'perfektsionizm-i-trevoga.html':
        {'crumb': 'Перфекционизм и тревога', 'section': 'Тревога', 'tag': 'Перфекционизм · 10 мин чтения'},
    'psikhosomatika-trevogi.html':
        {'crumb': 'Психосоматика тревоги', 'section': 'Психосоматика', 'tag': 'Психосоматика · 10 мин чтения'},
    'ne-znayu-chego-khochu.html':
        {'crumb': 'Не знаю, чего хочу', 'section': 'Самопознание', 'tag': 'Самопознание · 8 мин чтения'},
    'ne-khochu-rabotat.html':
        {'crumb': 'Не хочу работать', 'section': 'Выгорание', 'tag': 'Выгорание · 8 мин чтения'},
    'pochemu-trachu-dengi-v-stresse.html':
        {'crumb': 'Деньги и стресс', 'section': 'Психология денег', 'tag': 'Деньги · 10 мин чтения'},
    'uprazhneniya-dlya-rasslableniya-i-snyatie-myshechnyx-blokov.html':
        {'crumb': 'Упражнения для расслабления', 'section': 'Практика', 'tag': 'Практика · 10 мин чтения'},
    'ne-otsyuda-ne-ottyuda.html':
        {'crumb': 'Не отсюда, не оттуда', 'section': 'Эмиграция', 'tag': 'Эмиграция · 12 мин чтения'},
    'kak-spravitsya-s-panicheskimi-atakami.html':
        {'crumb': 'Панические атаки', 'section': 'Тревога', 'tag': 'Тревога · 8 мин чтения'},
    'simptomy-trevozhnogo-rasstroystva.html':
        {'crumb': 'Симптомы тревоги', 'section': 'Тревога', 'tag': 'Тревога · 7 мин чтения'},
    'psikholog-onlayn-vs-oflayn.html':
        {'crumb': 'Онлайн vs офлайн', 'section': 'Консультации', 'tag': 'Гид · 8 мин чтения'},
    'vosstanovlenie-posle-moshennichestva.html':
        {'crumb': 'Восстановление', 'section': 'Психология', 'tag': 'Психология · 8 мин чтения'},
    'sotsialnaya-trevoga.html': None,  # reference, skip
}

MONTHS_RU = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
    '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
    '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря',
}


def get_group(html):
    if '<nav class="nav">' in html:
        return 'g2'
    if '<header class="article-header">' in html:
        return 'g3'
    return 'ok'


def fix_css_links(html):
    html = re.sub(r'[ \t]*<link rel="stylesheet"[^\n>]+>\n?', '', html)
    html = html.replace('</head>', CSS_LINKS + '\n</head>', 1)
    return html


def fix_nav(html):
    html = re.sub(r'<nav class="nav">.*?</nav>', STANDARD_NAV, html, flags=re.DOTALL)
    return html


def extract_css_blocks(css_text):
    """Split CSS into blocks: (selector_prefix, full_block_text)"""
    blocks = []
    i = 0
    while i < len(css_text):
        # Skip leading whitespace/comments
        ws = re.match(r'(\s+|/\*.*?\*/)', css_text[i:], re.DOTALL)
        if ws:
            blocks.append(('_ws', css_text[i:i+ws.end()]))
            i += ws.end()
            continue
        # Find opening brace
        brace = css_text.find('{', i)
        if brace == -1:
            blocks.append(('_tail', css_text[i:]))
            break
        selector = css_text[i:brace].strip()
        # Find matching closing brace (handle nesting)
        depth = 0
        j = brace
        while j < len(css_text):
            if css_text[j] == '{':
                depth += 1
            elif css_text[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        block_text = css_text[i:j+1]
        blocks.append((selector, block_text))
        i = j + 1
    return blocks


def should_strip(selector):
    for pat in STRIP_SELECTORS:
        if re.fullmatch(pat + r'.*', selector, re.DOTALL):
            return True
    # Also strip animation targets and @keyframes
    if selector.startswith('@keyframes') and 'fade' in selector.lower():
        return True
    if '.hero h1,' in selector or '.hero-sub,' in selector:
        return True
    return False


def strip_structural_css(css_text):
    blocks = extract_css_blocks(css_text)
    kept = []
    for selector, block in blocks:
        if selector in ('_ws', '_tail'):
            kept.append(block)
        elif should_strip(selector):
            pass  # remove
        else:
            kept.append(block)
    result = ''.join(kept)
    return re.sub(r'\n{3,}', '\n\n', result).strip()


def build_style_block(article_specific_css=''):
    inner = REFERENCE_CSS
    if article_specific_css:
        inner += '\n\n  /* ── Article-specific ── */\n' + article_specific_css
    return '<style>\n  ' + inner + '\n</style>'


def fix_style_g2(html):
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    if not m:
        new_style = build_style_block()
        return html.replace('</head>', new_style + '\n</head>', 1)
    old_css = m.group(1)
    stripped = strip_structural_css(old_css)
    new_style = build_style_block(stripped)
    return html[:m.start()] + new_style + html[m.end():]


def rename_hero_classes(html):
    html = re.sub(r'<(header|div)\s+class="hero">', '<div class="article-hero">', html)
    # Close: first </header> that was the hero header
    html = html.replace('</header>', '</div>', 1)
    html = html.replace('class="hero-tag"', 'class="tag"')
    html = html.replace('class="hero-sub"', 'class="lead"')
    html = html.replace('class="hero-meta"', 'class="meta"')
    html = html.replace('class="hero-content"', '')  # ne-otsyuda variant
    html = html.replace('class="hero-title"', 'class=""')  # will use h1 directly
    html = html.replace('class="hero-subtitle"', 'class="lead"')
    html = html.replace('class="hero-category"', 'class="tag"')
    html = html.replace('class="hero-accent"', '')
    return html


def convert_article_header_g3(html, tag_text):
    """Convert <header class="article-header">...</header> to .article-hero"""
    m = re.search(r'<header class="article-header">(.*?)</header>', html, re.DOTALL)
    if not m:
        return html
    inner = m.group(1)

    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', inner, re.DOTALL)
    h1 = h1_m.group(1).strip() if h1_m else 'Статья'

    sub_m = re.search(r'</h1>\s*<p[^>]*>(.*?)</p>', inner, re.DOTALL)
    sub = sub_m.group(1).strip() if sub_m else ''

    # Get date from meta tag
    date_m = re.search(r'article:published_time[^>]+content="([^"]+)"', html)
    datetime_val = date_m.group(1) if date_m else ''
    if datetime_val:
        parts = datetime_val.split('-')
        date_str = f"{int(parts[2])} {MONTHS_RU.get(parts[1], parts[1])} {parts[0]}" if len(parts) == 3 else datetime_val
    else:
        date_str = ''

    lead_html = f'\n      <p class="lead">{sub}</p>' if sub else ''
    new_hero = (
        f'    <div class="article-hero">\n'
        f'      <span class="tag">{tag_text}</span>\n'
        f'      <h1 itemprop="headline">{h1}</h1>'
        f'{lead_html}\n'
        f'      <div class="meta">\n'
        f'        <span itemprop="author" itemscope itemtype="https://schema.org/Person">'
        f'<span itemprop="name">Камила Золотова</span>, КПТ-психолог</span>\n'
        f'        <span>·</span>\n'
        f'        <time datetime="{datetime_val}" itemprop="datePublished">{date_str}</time>\n'
        f'      </div>\n'
        f'    </div>'
    )
    return html[:m.start()] + new_hero + html[m.end():]


def ensure_main_wrap(html):
    """Wrap body content in <main> if not already present."""
    if '<main>' in html or '<main ' in html:
        return html
    # Wrap from after </nav> to before <footer>
    html = re.sub(r'(</nav>\s*)', r'\1\n<main>\n', html, count=1)
    html = re.sub(r'(\s*<footer[\s>])', r'\n</main>\n\1', html, count=1)
    return html


def move_hero_into_main(html):
    """If .article-hero is outside <main>, extract it and place inside after breadcrumb."""
    # Check if hero is before <main>
    main_pos = html.find('<main>')
    if main_pos == -1:
        main_pos = html.find('<main ')
    if main_pos == -1:
        return html

    hero_start = html.find('<div class="article-hero">')
    if hero_start == -1 or hero_start > main_pos:
        return html  # hero is already inside main or not found

    # Extract the hero block (find matching closing </div>)
    depth = 0
    j = hero_start
    while j < len(html):
        if html[j:j+4] == '<div':
            depth += 1
        elif html[j:j+6] == '</div>':
            depth -= 1
            if depth == 0:
                j += 6
                break
        j += 1
    hero_block = html[hero_start:j]

    # Remove hero from its current position (and any comment before it like <!-- HERO -->)
    pre_hero = html[:hero_start]
    pre_hero = re.sub(r'\s*<!--[^>]*HERO[^>]*-->\s*$', '\n', pre_hero)
    html = pre_hero + html[j:]

    # Insert hero inside <main> after breadcrumb (or at start of main if no breadcrumb yet)
    bc_end = html.find('</nav>', html.find('class="breadcrumb"'))
    if bc_end != -1:
        bc_end += len('</nav>')
        html = html[:bc_end] + '\n\n    ' + hero_block + html[bc_end:]
    else:
        # No breadcrumb yet — insert right after <main>
        html = re.sub(r'(<main[^>]*>)', r'\1\n    ' + hero_block, html, count=1)

    return html


def add_breadcrumb(html, crumb):
    if 'class="breadcrumb"' in html:
        return html
    bc = (
        f'\n    <nav class="breadcrumb" aria-label="Хлебные крошки">\n'
        f'      <a href="../index.html">Главная</a>'
        f'<span>/</span>\n'
        f'      <a href="../resources.html">Материалы</a>'
        f'<span>/</span>\n'
        f'      <a href="./">Статьи</a>'
        f'<span>/</span>\n'
        f'      <span>{crumb}</span>\n'
        f'    </nav>'
    )
    # Insert inside main, before hero
    html = re.sub(r'(<main[^>]*>)', r'\1' + bc, html, count=1)
    return html


def add_article_section_meta(html, section):
    if 'article:section' in html:
        return html
    return html.replace(
        '<meta property="article:published_time"',
        f'<meta property="article:section" content="{section}">\n<meta property="article:published_time"',
        1,
    )


def dedup_scripts(html):
    seen = set()
    def _sub(m):
        t = m.group(0)
        if t in seen:
            return ''
        seen.add(t)
        return t
    return re.sub(r'<script src="[^"]+"[^>]*></script>', _sub, html)


def add_faq_js(html):
    if 'faq-item' not in html:
        return html
    if 'faq-q' in html and "classList.toggle('open')" not in html:
        js = (
            '\n<script>\n'
            "document.querySelectorAll('.faq-q').forEach(q => {\n"
            "  q.addEventListener('click', () => q.parentElement.classList.toggle('open'));\n"
            '});\n'
            '</script>'
        )
        html = html.replace('</body>', js + '\n</body>', 1)
    return html


def process_file(p, meta):
    html = p.read_text(encoding='utf-8')
    group = get_group(html)

    if group == 'ok':
        # Minor fixes only
        html = fix_css_links(html)
        html = ensure_main_wrap(html)
        html = add_breadcrumb(html, meta['crumb'])
        html = move_hero_into_main(html)
        html = add_article_section_meta(html, meta['section'])
        html = dedup_scripts(html)
        html = add_faq_js(html)
        p.write_text(html, encoding='utf-8')
        return 'ok'

    # Fix CSS links (always)
    html = fix_css_links(html)

    if group == 'g2':
        html = fix_nav(html)
        html = fix_style_g2(html)
        html = rename_hero_classes(html)

    elif group == 'g3':
        # Add reference CSS (keep existing external sheets)
        ref_style = build_style_block()
        html = html.replace('</head>', ref_style + '\n</head>', 1)
        html = convert_article_header_g3(html, meta['tag'])

    html = ensure_main_wrap(html)
    html = add_breadcrumb(html, meta['crumb'])
    html = move_hero_into_main(html)
    html = add_article_section_meta(html, meta['section'])
    html = dedup_scripts(html)
    html = add_faq_js(html)

    p.write_text(html, encoding='utf-8')
    return group


if __name__ == '__main__':
    articles_dir = Path('articles')
    results = {'g2': [], 'g3': [], 'ok': []}

    for p in sorted(articles_dir.glob('*.html')):
        if p.name == 'index.html':
            continue
        meta = ARTICLE_META.get(p.name)
        if meta is None:
            print(f'  SKIP (reference): {p.name}')
            continue
        if meta is False:
            print(f'  SKIP (no meta): {p.name}')
            continue

        group = process_file(p, meta)
        results[group].append(p.name)
        print(f'  [{group}] {p.name}')

    print(f'\nSummary:')
    for g, files in results.items():
        print(f'  {g}: {len(files)} files')

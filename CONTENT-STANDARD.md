# 📋 Единый стандарт оформления контента

## Проверочный листок перед публикацией

---

## 📝 Статьи

### Карточка статьи (в resources.html):
- [ ] **Бейдж:** `background: var(--accent-primary)` (зелёный #2D5A4A)
- [ ] **Картинка:** `style="height: 200px; object-fit: cover;"`
- [ ] **Заголовок:** H3, не более 2 строк
- [ ] **Описание:** 1-2 предложения
- [ ] **Мета:** дата + время чтения

### Шаблон карточки:
```html
<div class="resource-card">
    <img src="images/article-NAME.jpg" alt="..." class="resource-image" 
         loading="lazy" style="height: 200px; object-fit: cover;">
    <div class="resource-info">
        <span class="resource-type-badge" style="background: var(--accent-primary); color: white;">
            Статья
        </span>
        <h3>Заголовок статьи</h3>
        <p>Описание</p>
        <div class="resource-meta">
            <span>Дата</span>
            <span>X мин. чтения</span>
        </div>
        <a href="article-NAME.html" class="btn-view">Читать статью</a>
    </div>
</div>
```

### Внутри статьи:
- [ ] **Шапка (hero image):** ВНУТРИ `.article-content`, `height: 400px`
- [ ] **Контейнер:** `max-width: 800px; margin: 0 auto`
- [ ] **Картинка и текст:** одинаковая ширина 800px

### Структура HTML статьи:
```html
<article class="article-content" style="max-width: 800px; margin: 0 auto;">
    <img src="images/article-NAME.jpg" alt="..." class="article-image" 
         style="width: 100%; height: 400px; object-fit: cover; margin-bottom: 2rem;">
    <h2>Заголовок</h2>
    <p>Текст...</p>
</article>
```

---

## 📊 Презентации

### Карточка презентации:
- [ ] **Бейдж:** `background: #8B4513` (коричневый)
- [ ] **Если есть картинка:** `style="height: 200px; object-fit: cover;"`
- [ ] **Если иконка:** `.resource-preview.presentation` (градиент)
- [ ] **Формат:** PDF или PPTX

### Шаблон:
```html
<div class="resource-card">
    <img src="images/preview-NAME.jpg" alt="..." class="resource-image"
         loading="lazy" style="height: 200px; object-fit: cover;">
    <div class="resource-info">
        <span class="resource-type-badge" style="background: #8B4513; color: white;">
            Презентация
        </span>
        <h3>Название</h3>
        <p>Описание</p>
        <div class="resource-meta">
            <span>Кол-во слайдов</span>
            <span>Формат</span>
        </div>
        <a href="documents/NAME.pptx" class="btn-view">Смотреть</a>
    </div>
</div>
```

---

## 📄 Документы

### Карточка документа:
- [ ] **Бейдж:** `background: #2C3E50` (тёмно-синий)
- [ ] **Картинка:** `style="height: 200px; object-fit: cover;"`
- [ ] **Формат:** DOCX или PDF

### Шаблон:
```html
<div class="resource-card">
    <img src="images/preview-NAME.jpg" alt="..." class="resource-image"
         loading="lazy" style="height: 200px; object-fit: cover;">
    <div class="resource-info">
        <span class="resource-type-badge" style="background: #2C3E50; color: white;">
            Документ
        </span>
        <h3>Название</h3>
        <p>Описание</p>
        <div class="resource-meta">
            <span>Формат</span>
            <span>Дата обновления</span>
        </div>
        <a href="documents/NAME.docx" class="btn-view">Просмотреть</a>
    </div>
</div>
```

---

## 🎨 Цветовая схема бейджей

| Тип | Цвет | CSS |
|-----|------|-----|
| Статья | 🟢 Зелёный | `var(--accent-primary)` или `#2D5A4A` |
| Презентация | 🟤 Коричневый | `#8B4513` |
| Документ | 🔵 Тёмно-синий | `#2C3E50` |

---

## 📐 Размеры изображений

### Превью карточек (resources.html):
- **Высота:** 200px
- **object-fit:** cover

### Шапка статьи (внутри article):
- **max-width:** 800px
- **height:** 400px

### Внутренние картинки статьи:
- **width:** 100%
- **height:** 400px

---

## ⚠️ Запрещено:
- Разные цвета бейджей для одинаковых типов
- Разные высоты превью в карточках
- Пустые шаблоны "Скоро" без даты публикации

---

## ✅ Порядок добавления:
1. Подготовить файлы (картинки, документы)
2. Проверить по этому списку
3. Добавить в resources.html
4. Git commit + push
5. Проверить на GitHub Pages
6. После подтверждения — публиковать на хостинг
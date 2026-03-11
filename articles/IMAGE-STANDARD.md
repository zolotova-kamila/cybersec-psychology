# Стандарт оформления картинок в статьях

## Размеры картинок в статьях

### Шапка статьи (hero image):
- **Ширина:** 800px (max-width: 800px)
- **Высота:** 400px
- **object-fit:** cover
- **CSS класс:** `.article-image`

```css
.article-image {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    display: block;
    height: 400px;
    object-fit: cover;
}
```

### Картинки внутри статьи:
- **Ширина:** 100% (вписывается в контент)
- **Высота:** 400px
- **object-fit:** cover

```css
.article-content img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    border-radius: var(--radius);
    margin: 24px 0;
    box-shadow: var(--shadow);
}
```

## Контейнер контента

Все статьи должны использовать контейнер с ограничением ширины:

```css
.article-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 60px 24px;
}
```

## Пример структуры HTML:

```html
<img src="images/article-example.jpg" alt="Описание" class="article-image" loading="lazy">

<div class="article-container">
    <div class="article-content">
        <!-- текст статьи -->
        <img src="images/inline-example.jpg" alt="Описание" loading="lazy">
    </div>
</div>
```

## Проверка перед публикацией:
- [ ] Картинка шапки имеет max-width: 800px
- [ ] Высота картинки 400px
- [ ] object-fit: cover для сохранения пропорций
- [ ] Контейнер контента max-width: 800px

# Промт для нового OG-превью сайта

## Требования к изображению:

**Размер:** 1200×630 пикселей (оптимально для всех соцсетей)
**Формат:** PNG или JPG
**Стиль:** Фотореалистичный, профессиональный

---

## Промт для Midjourney / DALL-E:

```
A professional social media preview card (OG image) for psychologist website. 

Layout: Split composition with professional female psychologist (age 45-50, warm, trustworthy appearance) on the left side in a professional office setting with soft natural lighting. Right side features elegant text overlay area.

Left side: Professional portrait of female psychologist Kamila Zolotova, wearing professional attire in warm earth tones, confident but approachable expression, psychology office background with books and plants, soft window lighting, shallow depth of field.

Right side: Clean cream/beige background (#F5F1EB) with elegant typography space. Include subtle design elements suggesting psychology and cybersecurity - abstract brain patterns, shield icons, neural networks in soft green tones (#2D5A4A).

Text area (leave space for): 
- Main title: "Камила Золотова"
- Subtitle: "Психолог КПТ"
- Description lines about specialization

Style: Modern, trustworthy, professional healthcare aesthetic, warm color palette with greens and creams, magazine cover quality, suitable for Facebook, VK, Telegram, Twitter sharing.

No text in image - just layout space for text overlay.
```

---

## Альтернативный промт (проще):

```
Professional OG image for psychologist website, 1200x630px.

Left half: Professional portrait of confident female psychologist in her 50s, warm smile, sitting in modern office with psychology books, soft natural window light, trustworthy appearance, wearing professional blazer in earth tones.

Right half: Clean design with cream background, space for text. Include subtle green accent (#2D5A4A) decorative elements suggesting mental health and digital security - abstract shield, brain network patterns, calming geometric shapes.

Overall mood: Professional, trustworthy, warm, inviting. Magazine cover quality. No text in image.
```

---

## Технические требования:

- **Размер:** 1200×630 px (Facebook/Twitter/VK оптимум)
- **Размер файла:** до 5 MB
- **Формат:** PNG (лучше качество) или JPG
- **Имя файла:** `og-preview-new.png`

---

## После создания:

1. Загрузить файл на сервер в папку `images/`
2. Обновить путь в `index.html`:
   ```html
   <meta property="og:image" content="https://pozitiv-psychology.ru/images/og-preview-new.png">
   ```
3. Очистить кэш соцсетей через:
   - https://developers.facebook.com/tools/debug/
   - @WebpageBot в Telegram

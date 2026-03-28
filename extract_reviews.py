import re

with open('2gis_page.txt', 'r', encoding='utf-8') as f:
    html = f.read()

# Look for review text patterns
pattern = r'[А-Я][а-яА-Я\s,\.\!\?\-()\":;]+'
matches = re.findall(pattern, html)

# Filter for longer text (likely reviews)
reviews = [m for m in matches if 100 < len(m) < 500]

# Remove duplicates and filter out code
seen = set()
unique = []
for r in reviews:
    if r not in seen and not any(x in r.lower() for x in ['meta', 'script', 'style', 'class=', 'id=', 'function']):
        seen.add(r)
        unique.append(r)

print(f'Found {len(unique)} potential reviews\n')
for i, r in enumerate(unique[:15]):
    print(f'{i+1}. {r[:250]}...')
    print()

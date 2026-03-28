import urllib.request
import re
import json

url = 'https://2gis.ru/moscow/firm/70000001064709179'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req, timeout=20) as resp:
    html = resp.read().decode('utf-8')
    
    # Look for JSON structure with reviews
    # 2GIS often has data in window.__INITIAL_STATE__
    init_state_match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.+?});', html, re.DOTALL)
    
    results = []
    
    if init_state_match:
        try:
            data = json.loads(init_state_match.group(1))
            # Try to find reviews in the data structure
            with open('2gis_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            results.append("Saved JSON data to 2gis_data.json")
        except:
            results.append("Failed to parse JSON")
    
    # Also look for review text patterns
    pattern = r'text["\']?\s*:\s*["\']([^"\']{80,500})["\']'
    matches = re.findall(pattern, html)
    
    results.append(f'Found {len(matches)} text patterns')
    
    # Save matches
    with open('2gis_reviews.txt', 'w', encoding='utf-8') as f:
        for i, m in enumerate(matches[:15]):
            f.write(f'{i+1}. {m[:300]}\n\n')
    
    results.append("Saved reviews to 2gis_reviews.txt")
    
    print('\n'.join(results))

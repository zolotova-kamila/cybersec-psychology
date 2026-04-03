# Read UTF-8 file and convert to Windows-1251 (CP1251)
$utf8 = [System.Text.UTF8Encoding]::new($false)
$cp1251 = [System.Text.Encoding]::GetEncoding(1251)

$bytes = [System.IO.File]::ReadAllBytes('articles/psikhosomatika-trevogi.html')
$text = $utf8.GetString($bytes)

# Convert text to CP1251 bytes
$cp1251Bytes = [System.Text.Encoding]::Convert($utf8, $cp1251, $bytes)

# Write as CP1251
[System.IO.File]::WriteAllBytes('articles/psikhosomatika-trevogi.html', $cp1251Bytes)

Write-Host "Converted to Windows-1251"

# Also update charset meta tag
$content = $cp1251.GetString([System.IO.File]::ReadAllBytes('articles/psikhosomatika-trevogi.html'))
$content = $content.Replace('charset="UTF-8"', 'charset="windows-1251"')
[System.IO.File]::WriteAllText('articles/psikhosomatika-trevogi.html', $content, $cp1251)

Write-Host "Updated meta charset to windows-1251"

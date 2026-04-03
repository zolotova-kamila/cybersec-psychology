# Read raw bytes and write back as UTF-8 without BOM
$bytes = [System.IO.File]::ReadAllBytes('articles/psikhosomatika-trevogi.html')
# Check for BOM and remove if present
if ($bytes.Length -ge 3 -and $bytes[0] -eq 239 -and $bytes[1] -eq 187 -and $bytes[2] -eq 191) {
    $bytes = $bytes[3..($bytes.Length-1)]
    Write-Host "BOM removed"
}
# Detect if it's UTF-8 by checking for valid sequences
$utf8 = [System.Text.UTF8Encoding]::new($false)
$text = $utf8.GetString($bytes)
# Write back as UTF-8 without BOM
[System.IO.File]::WriteAllText('articles/psikhosomatika-trevogi.html', $text, $utf8)
Write-Host "File resaved as UTF-8"

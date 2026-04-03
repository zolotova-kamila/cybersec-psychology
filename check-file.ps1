$ftp = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/articles/psikhosomatika-trevogi.html'
$user = 'cu48621'
$pass = 'tfCq8P4a'

Write-Host "Downloading and checking file..."
$req = [System.Net.FtpWebRequest]::Create($ftp)
$req.Method = [System.Net.WebRequestMethods+Ftp]::DownloadFile
$req.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req.UseBinary = $true
$req.UsePassive = $true

$response = $req.GetResponse()
$stream = $response.GetResponseStream()

# Read as bytes
$memoryStream = New-Object System.IO.MemoryStream
$stream.CopyTo($memoryStream)
$bytes = $memoryStream.ToArray()
$memoryStream.Close()
$stream.Close()
$response.Close()

Write-Host "Downloaded size: $($bytes.Length) bytes"

# Try decode as UTF-8
$utf8 = [System.Text.UTF8Encoding]::new($false)
try {
    $text = $utf8.GetString($bytes)
    Write-Host "`nFirst 200 chars as UTF-8:"
    Write-Host $text.Substring(0, [Math]::Min(200, $text.Length))
    
    # Check if title contains expected text
    if ($text.Contains("Психосоматика")) {
        Write-Host "`n✅ SUCCESS: File is readable UTF-8 with Cyrillic!"
    } else {
        Write-Host "`n❌ WARNING: Cyrillic text not found!"
        # Try Windows-1251
        $cp1251 = [System.Text.Encoding]::GetEncoding(1251)
        $text1251 = $cp1251.GetString($bytes)
        Write-Host "`nFirst 200 chars as Windows-1251:"
        Write-Host $text1251.Substring(0, [Math]::Min(200, $text1251.Length))
    }
} catch {
    Write-Host "ERROR decoding: $_"
}

$ftp = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/.htaccess'
$user = 'cu48621'
$pass = 'tfCq8P4a'

Write-Host "=== Downloading .htaccess ==="
$req = [System.Net.FtpWebRequest]::Create($ftp)
$req.Method = [System.Net.WebRequestMethods+Ftp]::DownloadFile
$req.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req.UsePassive = $true
try {
    $response = $req.GetResponse()
    $stream = $response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($stream)
    $content = $reader.ReadToEnd()
    $reader.Close()
    $stream.Close()
    Write-Host "Content of .htaccess:"
    Write-Host "===================="
    Write-Host $content
    Write-Host "===================="
    $response.Close()
} catch {
    Write-Host ('ERROR: ' + $_.Exception.Message)
}

# Also try to download the article file to verify it works
Write-Host "`n=== Downloading article file ==="
$ftp2 = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/articles/psikhosomatika-trevogi.html'
$req2 = [System.Net.FtpWebRequest]::Create($ftp2)
$req2.Method = [System.Net.WebRequestMethods+Ftp]::DownloadFile
$req2.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req2.UsePassive = $true
try {
    $response2 = $req2.GetResponse()
    $stream2 = $response2.GetResponseStream()
    $reader2 = New-Object System.IO.StreamReader($stream2)
    $content2 = $reader2.ReadToEnd()
    $reader2.Close()
    $stream2.Close()
    Write-Host "File downloaded successfully!"
    Write-Host "File size: $($content2.Length) bytes"
    Write-Host "First 500 chars:"
    Write-Host $content2.Substring(0, [Math]::Min(500, $content2.Length))
    $response2.Close()
} catch {
    Write-Host ('ERROR downloading article: ' + $_.Exception.Message)
}

$ftp = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/articles/'
$user = 'cu48621'
$pass = 'tfCq8P4a'

# List articles directory
Write-Host "=== Listing articles directory ==="
$req = [System.Net.FtpWebRequest]::Create($ftp)
$req.Method = [System.Net.WebRequestMethods+Ftp]::ListDirectoryDetails
$req.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req.UsePassive = $true
try {
    $response = $req.GetResponse()
    $stream = $response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($stream)
    while ($line = $reader.ReadLine()) {
        Write-Host "  $line"
    }
    $reader.Close()
    $stream.Close()
    $response.Close()
} catch {
    Write-Host ('LIST ERROR: ' + $_.Exception.Message)
}

# Try to download the file to verify it exists
Write-Host "`n=== Checking if psikhosomatika-trevogi.html exists ==="
$uri = $ftp + 'psikhosomatika-trevogi.html'
$req2 = [System.Net.FtpWebRequest]::Create($uri)
$req2.Method = [System.Net.WebRequestMethods+Ftp]::DownloadFile
$req2.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req2.UsePassive = $true
try {
    $response2 = $req2.GetResponse()
    $stream2 = $response2.GetResponseStream()
    $reader2 = New-Object System.IO.StreamReader($stream2)
    $content = $reader2.ReadToEnd()
    $reader2.Close()
    $stream2.Close()
    Write-Host "File exists! Size: $($content.Length) bytes"
    Write-Host "First 200 chars: $($content.Substring(0, [Math]::Min(200, $content.Length)))"
    $response2.Close()
} catch {
    Write-Host ('DOWNLOAD ERROR: ' + $_.Exception.Message)
}

# Also check public_html root
Write-Host "`n=== Listing public_html root ==="
$ftpRoot = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/'
$req3 = [System.Net.FtpWebRequest]::Create($ftpRoot)
$req3.Method = [System.Net.WebRequestMethods+Ftp]::ListDirectoryDetails
$req3.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req3.UsePassive = $true
try {
    $response3 = $req3.GetResponse()
    $stream3 = $response3.GetResponseStream()
    $reader3 = New-Object System.IO.StreamReader($stream3)
    while ($line = $reader3.ReadLine()) {
        Write-Host "  $line"
    }
    $reader3.Close()
    $stream3.Close()
    $response3.Close()
} catch {
    Write-Host ('LIST ERROR: ' + $_.Exception.Message)
}

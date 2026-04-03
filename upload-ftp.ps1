$ftp = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/articles/'
$user = 'cu48621'
$pass = 'tfCq8P4a'

# Read file as bytes to preserve UTF-8
$file = 'articles/psikhosomatika-trevogi.html'
$bytes = [System.IO.File]::ReadAllBytes($file)
Write-Host "Local file size: $($bytes.Length) bytes"
Write-Host "First 100 bytes as text:"
$utf8 = [System.Text.UTF8Encoding]::new($false)
Write-Host $utf8.GetString($bytes[0..99])

# Upload as binary
$uri = $ftp + 'psikhosomatika-trevogi.html'
Write-Host "`nUploading to: $uri"
$req = [System.Net.FtpWebRequest]::Create($uri)
$req.Method = [System.Net.WebRequestMethods+Ftp]::UploadFile
$req.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req.UseBinary = $true  # Important for UTF-8
$req.UsePassive = $true
$req.ContentLength = $bytes.Length

$stream = $req.GetRequestStream()
$stream.Write($bytes, 0, $bytes.Length)
$stream.Close()

$response = $req.GetResponse()
Write-Host ('SUCCESS: ' + $response.StatusDescription)
$response.Close()

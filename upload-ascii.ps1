$ftp = 'ftp://92.53.96.231/pozitiv-psychology.ru/public_html/articles/psikhosomatika-trevogi.html'
$user = 'cu48621'
$pass = 'tfCq8P4a'

# Read as text and upload as ASCII
$cp1251 = [System.Text.Encoding]::GetEncoding(1251)
$content = [System.IO.File]::ReadAllText('articles/psikhosomatika-trevogi.html', $cp1251)

Write-Host "Uploading as ASCII..."
$req = [System.Net.FtpWebRequest]::Create($ftp)
$req.Method = [System.Net.WebRequestMethods+Ftp]::UploadFile
$req.Credentials = New-Object System.Net.NetworkCredential($user, $pass)
$req.UseBinary = $false  # ASCII mode
$req.UsePassive = $true

# Convert text to bytes using CP1251 for ASCII upload
$bytes = $cp1251.GetBytes($content)
$req.ContentLength = $bytes.Length

$stream = $req.GetRequestStream()
$stream.Write($bytes, 0, $bytes.Length)
$stream.Close()

$response = $req.GetResponse()
Write-Host ('SUCCESS: ' + $response.StatusDescription)
$response.Close()

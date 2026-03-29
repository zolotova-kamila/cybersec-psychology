# WinSCP PowerShell Deployment Script
# Load WinSCP .NET assembly
Add-Type -Path "${env:ProgramFiles(x86)}\WinSCP\WinSCPnet.dll"

# FTP credentials
$ftpHost = "vh278.timeweb.ru"
$ftpUser = "cu48621"
$ftpPass = "tfCq8P4a"

# Setup session options
$sessionOptions = New-Object WinSCP.SessionOptions -Property @{
    Protocol = [WinSCP.Protocol]::Ftp
    HostName = $ftpHost
    UserName = $ftpUser
    Password = $ftpPass
    FtpMode = [WinSCP.FtpMode]::Passive
    FtpSecure = [WinSCP.FtpSecure]::None
}

$session = New-Object WinSCP.Session

try {
    Write-Host "Connecting to server $ftpHost..."
    $session.Open($sessionOptions)
    
    Write-Host "Uploading files to pozitiv-psychology.ru/public_html/..."
    
    # Sync local files to remote
    $transferOptions = New-Object WinSCP.TransferOptions
    $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary
    
    $synchronizationResult = $session.SynchronizeDirectories(
        [WinSCP.SynchronizationMode]::Remote,
        (Get-Location).Path,
        "/pozitiv-psychology.ru/public_html",
        $False,
        [WinSCP.SynchronizationCriteria]::Time,
        $transferOptions
    )
    
    # Check results
    $synchronizationResult.Check()
    
    Write-Host ""
    Write-Host "DEPLOY COMPLETED!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Check site: https://pozitiv-psychology.ru/"
}
catch {
    Write-Host "ERROR: $_" -ForegroundColor Red
    exit 1
}
finally {
    $session.Dispose()
}

$ErrorActionPreference = "Stop"

function Load-LocalEnvFile {
  param([string]$Path)

  if (-not (Test-Path $Path)) {
    return
  }

  Get-Content $Path | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#") -or -not $line.Contains("=")) {
      return
    }

    $parts = $line.Split("=", 2)
    $name = $parts[0].Trim()
    $value = $parts[1].Trim()

    if ($name -and $value -and -not [Environment]::GetEnvironmentVariable($name, "Process")) {
      [Environment]::SetEnvironmentVariable($name, $value, "Process")
    }
  }
}

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Load-LocalEnvFile -Path (Join-Path $repoRoot ".env.deploy.local")

$hostName = $env:IONOS_SFTP_HOST
$port = if ($env:IONOS_SFTP_PORT) { $env:IONOS_SFTP_PORT } else { "22" }
$user = $env:IONOS_SFTP_USER
$keyPath = $env:IONOS_SFTP_KEY

if (-not $hostName -or -not $user -or -not $keyPath) {
  throw "IONOS_SFTP_HOST, IONOS_SFTP_USER, and IONOS_SFTP_KEY must be set."
}

$publicKeyPath = "$keyPath.pub"

if (-not (Test-Path $publicKeyPath)) {
  throw "Missing public key: $publicKeyPath"
}

$publicKey = (Get-Content $publicKeyPath -Raw).Trim()
$escapedPublicKey = $publicKey.Replace("'", "'\''")
$remoteCommand = "mkdir -p ~/.ssh && chmod 700 ~/.ssh && touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && grep -qxF '$escapedPublicKey' ~/.ssh/authorized_keys || printf '%s\n' '$escapedPublicKey' >> ~/.ssh/authorized_keys"

Write-Host "Installing public key for $user@$hostName."
Write-Host "You may be prompted for the IONOS SFTP/SSH password once."

& ssh.exe -p $port "$user@$hostName" $remoteCommand

if ($LASTEXITCODE -ne 0) {
  throw "SSH key installation failed with exit code $LASTEXITCODE."
}

Write-Host "Public key installed. Test with: ssh -i $keyPath -p $port $user@$hostName"

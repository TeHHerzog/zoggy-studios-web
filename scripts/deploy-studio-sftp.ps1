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
$remoteDir = if ($env:IONOS_REMOTE_DIR) { $env:IONOS_REMOTE_DIR.TrimEnd("/") } else { "/games" }
$keyPath = $env:IONOS_SFTP_KEY
$localDist = Join-Path $repoRoot "dist\studio"

if (-not $hostName -or -not $user -or -not $remoteDir) {
  throw "IONOS_SFTP_HOST, IONOS_SFTP_USER, and IONOS_REMOTE_DIR must be set."
}

if (-not $keyPath) {
  throw "IONOS_SFTP_KEY must be set for automated upload. Use FileZilla/WinSCP for password upload."
}

if (-not (Test-Path $keyPath)) {
  throw "IONOS_SFTP_KEY does not exist: $keyPath"
}

if (-not (Test-Path $localDist)) {
  throw "Missing build output: $localDist. Run npm run build first."
}

$batchFile = New-TemporaryFile

try {
  $commands = @(
    "-mkdir $remoteDir",
    "cd $remoteDir",
    "lcd `"$localDist`"",
    "-mkdir _astro",
    "-mkdir about",
    "-mkdir contact",
    "-mkdir crazytank",
    "-mkdir gallery",
    "-mkdir images",
    "-mkdir now",
    "-mkdir privacy",
    "-mkdir projects",
    "-mkdir technology",
    "-mkdir terms",
    "-mkdir updates",
    "-mkdir work",
    "put -r _astro",
    "put -r about",
    "put -r contact",
    "put -r crazytank",
    "put -r gallery",
    "put -r images",
    "put -r now",
    "put -r privacy",
    "put -r projects",
    "put -r technology",
    "put -r terms",
    "put -r updates",
    "put -r work",
    "put .htaccess",
    "put 404.html",
    "put brand-mark.svg",
    "put content-assets.mjs",
    "put content-modules.mjs",
    "put favicon.ico",
    "put favicon.svg",
    "put index.html",
    "put robots.txt",
    "put social-card.svg"
  )

  foreach ($optionalFile in @("data-store.json", "settings.json")) {
    if (Test-Path (Join-Path $localDist $optionalFile)) {
      $commands += "put $optionalFile"
    }
  }

  $commands += "bye"

  Set-Content -Path $batchFile -Value $commands -Encoding ascii

  Write-Host "Uploading dist/studio to $user@$hostName`:$remoteDir via SFTP..."
  & sftp.exe -i $keyPath -P $port -b $batchFile "$user@$hostName"

  if ($LASTEXITCODE -ne 0) {
    throw "SFTP upload failed with exit code $LASTEXITCODE."
  }

  Write-Host "Studio upload completed. Verify https://games.herzogit.com/ manually."

  # Also deploy darkfantasy output to /games/darkfantasy/
  $darkfantasyDist = Join-Path $repoRoot "dist\darkfantasy"
  if (Test-Path $darkfantasyDist) {
    Write-Host "Also uploading darkfantasy to /games/darkfantasy/..."
    $dfBatch = New-TemporaryFile
    $dfCommands = @(
      "-mkdir /games/darkfantasy",
      "cd /games/darkfantasy",
      "lcd `"$darkfantasyDist`"",
      "-mkdir _astro",
    "-mkdir fonts",
    "put -r _astro",
    "put -r fonts",
    "put .htaccess",
      "put 404.html",
      "put favicon.ico",
      "put favicon.svg",
      "put index.html",
      "put robots.txt",
      "bye"
    )
    Set-Content -Path $dfBatch -Value $dfCommands -Encoding ascii
    & sftp.exe -i $keyPath -P $port -b $dfBatch "$user@$hostName"
    Remove-Item $dfBatch -Force -ErrorAction SilentlyContinue
    Write-Host "Darkfantasy upload completed. Verify at https://games.herzogit.com/darkfantasy/"
  }
}
finally {
  Remove-Item $batchFile -Force -ErrorAction SilentlyContinue
}

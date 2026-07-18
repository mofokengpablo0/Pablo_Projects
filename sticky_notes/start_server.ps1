$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRoot = (Resolve-Path (Join-Path $projectRoot "..\..\..")).Path
$venvPython = Join-Path $workspaceRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    throw "Virtual environment not found at $venvPython"
}

Set-Location $projectRoot
& $venvPython manage.py runserver 0.0.0.0:8000

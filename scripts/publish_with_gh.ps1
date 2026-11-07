# Run from the repository root only if you want Codex or PowerShell to publish.
# No secrets and no destructive force push.
$ErrorActionPreference='Stop'
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'GitHub CLI gh is not installed.' }
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'gh authentication not ready' }
if (-not (Test-Path .git)) { git init -b main; git add .; git commit -m 'Initial Kemper artist tone library' }
gh repo create steven-ford2/kemper-tone-library --private --source . --remote origin --push
if ($LASTEXITCODE -ne 0) { throw 'Repo creation failed. Check whether the name already exists.' }

# Publish this local Git-ready repository

Current GitHub connector supports commits and file operations in existing repositories, but not creating a new repository. **The user created `steven-ford2/kemper-performance-library`; its current branch must be checked before pushing.** It is inappropriate to place personal music configs inside an unrelated existing research/business repository.

## Option 1: Codex on your PC

Open this folder in Codex. Ask it to execute:

```powershell
gh auth status
gh repo view steven-ford2/kemper-performance-library
git remote add origin https://github.com/steven-ford2/kemper-performance-library.git
git push -u origin main
```

If `.git` isn't present, initialize+commit first (`git init -b main`, `git add .`, `git commit -m "Initial Kemper tone library"`). If repo already exists, check ownership, existing contents and default branch before changing anything; do not force-push.

## Option 2: GitHub web UI

Use existing repository `steven-ford2/kemper-performance-library` under `steven-ford2` (do not initialize with README). Then push your local Git repository using the standard GitHub-provided instructions. No credentials need be given to ChatGPT.

## Privacy

Do not commit local library backups, profile pack binaries, Rig Manager machine logs, audio recordings, device serial numbers, credentials, or other personal files. See `.gitignore`.

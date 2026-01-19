# GitHub Push Script
# Run this script to push your code to GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  YouTube Content Detection AI" -ForegroundColor Yellow
Write-Host "  GitHub Deployment Helper" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Git repository not initialized!" -ForegroundColor Red
    Write-Host "Please run: git init" -ForegroundColor Yellow
    exit 1
}

Write-Host "Step 1: Checking Git status..." -ForegroundColor Green
git status

Write-Host "`nStep 2: Adding remote repository..." -ForegroundColor Green
Write-Host "Please enter your GitHub username:" -ForegroundColor Yellow
$username = Read-Host

$repoUrl = "https://github.com/$username/youtube-content-detection-ai.git"

# Check if remote already exists
$existingRemote = git remote get-url origin 2>$null
if ($existingRemote) {
    Write-Host "Remote 'origin' already exists: $existingRemote" -ForegroundColor Yellow
    Write-Host "Do you want to update it? (y/n):" -ForegroundColor Yellow
    $update = Read-Host
    if ($update -eq 'y') {
        git remote set-url origin $repoUrl
        Write-Host "Remote updated!" -ForegroundColor Green
    }
} else {
    git remote add origin $repoUrl
    Write-Host "Remote added successfully!" -ForegroundColor Green
}

Write-Host "`nStep 3: Renaming branch to 'main'..." -ForegroundColor Green
git branch -M main

Write-Host "`nStep 4: Pushing to GitHub..." -ForegroundColor Green
Write-Host "Executing: git push -u origin main" -ForegroundColor Cyan

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "  SUCCESS! Code pushed to GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "`nYour repository URL:" -ForegroundColor Yellow
    Write-Host "https://github.com/$username/youtube-content-detection-ai" -ForegroundColor Cyan
    Write-Host "`nNext steps:" -ForegroundColor Yellow
    Write-Host "1. Visit your repository on GitHub" -ForegroundColor White
    Write-Host "2. Add topics (machine-learning, django, youtube, ai)" -ForegroundColor White
    Write-Host "3. Add a license if needed" -ForegroundColor White
    Write-Host "4. Share your project!" -ForegroundColor White
} else {
    Write-Host "`n========================================" -ForegroundColor Red
    Write-Host "  ERROR: Push failed!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "`nPossible solutions:" -ForegroundColor Yellow
    Write-Host "1. Make sure you created the repository on GitHub first" -ForegroundColor White
    Write-Host "2. Check your GitHub credentials" -ForegroundColor White
    Write-Host "3. Use a Personal Access Token instead of password" -ForegroundColor White
    Write-Host "4. See DEPLOYMENT_GUIDE.md for detailed instructions" -ForegroundColor White
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Project Organization Script
# This script helps organize the legacy bot files

Write-Host "🗂️  Organizing Nexus AI Bot Project..." -ForegroundColor Cyan
Write-Host ""

# Move legacy bot files
Write-Host "📦 Moving legacy bot files..." -ForegroundColor Yellow
$legacyFiles = @(
    "bot.py",
    "bot_2.py",
    "bot_3.py",
    "bot_4.py",
    "bot_with_option_2.py",
    "bot_with_options_stable_diff_mod.py",
    "bot_with_options_stable_diff_mod_2.py",
    "bot_with_options_stable_diff_mod_3.py",
    "bot_with_options_stable_diff.py",
    "bot_with_options-stable_diff_clll.py"
)

foreach ($file in $legacyFiles) {
    if (Test-Path $file) {
        Move-Item -Path $file -Destination "legacy\" -Force
        Write-Host "  Moved $file to legacy/" -ForegroundColor Green
    }
}

# Move notebook files
Write-Host ""
Write-Host "📓 Moving notebook files..." -ForegroundColor Yellow
$notebookFiles = @(
    "bot.ipynb",
    "code.ipynb",
    "llama_3.ipynb",
    "stable_diff.ipynb",
    "stable_diff_high.ipynb",
    "test.ipynb"
)

foreach ($file in $notebookFiles) {
    if (Test-Path $file) {
        Move-Item -Path $file -Destination "notebooks\" -Force
        Write-Host "  Moved $file to notebooks/" -ForegroundColor Green
    }
}

# Clean up temporary files
Write-Host ""
Write-Host "🧹 Cleaning up temporary files..." -ForegroundColor Yellow
$tempFiles = @(
    "chunk_1.txt",
    "chunk_2.txt",
    "chunk_3.txt",
    "my.txt"
)

foreach ($file in $tempFiles) {
    if (Test-Path $file) {
        Remove-Item -Path $file -Force
        Write-Host "  Removed $file" -ForegroundColor Green
    }
}

# Create .gitkeep files to preserve empty directories
Write-Host ""
Write-Host "📌 Creating directory placeholders..." -ForegroundColor Yellow
New-Item -Path "legacy\.gitkeep" -ItemType File -Force | Out-Null
New-Item -Path "notebooks\.gitkeep" -ItemType File -Force | Out-Null

Write-Host ""
Write-Host "✅ Organization complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Project Structure:" -ForegroundColor Cyan
Write-Host "  src/          - Main bot code" -ForegroundColor White
Write-Host "  legacy/       - Legacy versions" -ForegroundColor White
Write-Host "  notebooks/    - Jupyter notebooks" -ForegroundColor White
Write-Host "  docs/         - Documentation" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Copy .env.example to .env and add your tokens" -ForegroundColor White
Write-Host "  2. Install dependencies: pip install -r requirements.txt" -ForegroundColor White
Write-Host "  3. Run the bot: python src\main_bot.py" -ForegroundColor White
Write-Host ""

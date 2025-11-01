@echo off
echo ========================================
echo  Organizing Chanakya AI Discord Bot
echo ========================================
echo.

echo Moving legacy bot files...
if exist bot.py move bot.py legacy\ >nul 2>&1
if exist bot_2.py move bot_2.py legacy\ >nul 2>&1
if exist bot_3.py move bot_3.py legacy\ >nul 2>&1
if exist bot_4.py move bot_4.py legacy\ >nul 2>&1
if exist bot_with_option_2.py move bot_with_option_2.py legacy\ >nul 2>&1
if exist bot_with_options_stable_diff_mod.py move bot_with_options_stable_diff_mod.py legacy\ >nul 2>&1
if exist bot_with_options_stable_diff_mod_2.py move bot_with_options_stable_diff_mod_2.py legacy\ >nul 2>&1
if exist bot_with_options_stable_diff_mod_3.py move bot_with_options_stable_diff_mod_3.py legacy\ >nul 2>&1
if exist bot_with_options_stable_diff.py move bot_with_options_stable_diff.py legacy\ >nul 2>&1
if exist bot_with_options-stable_diff_clll.py move bot_with_options-stable_diff_clll.py legacy\ >nul 2>&1
echo   Done!

echo.
echo Moving notebook files...
if exist bot.ipynb move bot.ipynb notebooks\ >nul 2>&1
if exist code.ipynb move code.ipynb notebooks\ >nul 2>&1
if exist llama_3.ipynb move llama_3.ipynb notebooks\ >nul 2>&1
if exist stable_diff.ipynb move stable_diff.ipynb notebooks\ >nul 2>&1
if exist stable_diff_high.ipynb move stable_diff_high.ipynb notebooks\ >nul 2>&1
if exist test.ipynb move test.ipynb notebooks\ >nul 2>&1
echo   Done!

echo.
echo Cleaning up temporary files...
if exist chunk_1.txt del chunk_1.txt >nul 2>&1
if exist chunk_2.txt del chunk_2.txt >nul 2>&1
if exist chunk_3.txt del chunk_3.txt >nul 2>&1
if exist my.txt del my.txt >nul 2>&1
echo   Done!

echo.
echo ========================================
echo  Organization Complete!
echo ========================================
echo.
echo Project Structure:
echo   src/          - Main bot code
echo   legacy/       - Legacy versions
echo   notebooks/    - Jupyter notebooks
echo   docs/         - Documentation
echo.
echo Next steps:
echo   1. Copy .env.example to .env and add your tokens
echo   2. Install dependencies: pip install -r requirements.txt
echo   3. Run the bot: python src\main_bot.py
echo.
pause

@echo off
echo ========================================
echo  Language-Agnostic Chatbot Setup
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)
python --version

echo.
echo [2/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/3] Setup complete!
echo.
echo ========================================
echo  How to run the chatbot:
echo ========================================
echo 1. Run: python app.py
echo 2. Open browser: http://localhost:5000
echo 3. Click the blue chatbot icon
echo 4. Start chatting!
echo.
echo Press any key to start the chatbot now...
pause >nul

echo.
echo Starting chatbot server...
python app.py

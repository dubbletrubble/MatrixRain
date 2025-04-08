@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python 3.7 or higher.
    echo You can download it from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Get Python version
for /f "tokens=2 delims= " %%i in ('python --version 2^>^&1') do set pyver=%%i
echo Found Python version: %pyver%

:: Create and activate virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Install or upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Run the program
echo Starting Matrix Rain...
python main.py

:: Deactivate virtual environment
deactivate

:: Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit.
    pause > nul
)

endlocal

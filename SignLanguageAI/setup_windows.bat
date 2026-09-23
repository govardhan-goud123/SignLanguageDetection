@echo off
echo ==========================================
echo Indian Sign Language AI - Setup
echo ==========================================
echo.

py -3.12 --version
if errorlevel 1 (
    echo.
    echo Python 3.12 was not found.
    echo Install Python 3.12 first.
    echo.
    pause
    exit /b 1
)

echo.
echo Creating virtual environment...
py -3.12 -m venv .venv

echo.
echo Activating environment...
call .venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing project packages...
pip install -r requirements.txt

echo.
echo ==========================================
echo Setup finished.
echo ==========================================
echo.
echo Put the Indian dataset folder here:
echo     %CD%\Indian
echo.
echo Then run:
echo     python train.py
echo.
pause

@echo off
REM Start Backend Server - Keep it Running

setlocal enabledelayedexpansion

:start
echo.
echo ===============================================
echo Starting MediScan Backend Server...
echo ===============================================
echo.

REM Kill any existing process on port 8000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    taskkill /PID %%a /F 2>nul
)

REM Wait a moment for port to free up
timeout /t 2 /nobreak

REM Start the server
cd /d "%~dp0\backend"
python app.py

REM If the app exits, wait and restart
echo.
echo !!! Backend crashed or stopped !!!
echo Restarting in 5 seconds...
timeout /t 5 /nobreak
goto start

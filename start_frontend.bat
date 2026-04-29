@echo off
REM Start Frontend Server

setlocal enabledelayedexpansion

:start
echo.
echo ===============================================
echo Starting MediScan Frontend Server...
echo ===============================================
echo.

cd /d "%~dp0\frontend"
npm start

REM If the app exits, wait and restart
echo.
echo !!! Frontend crashed or stopped !!!
echo Restarting in 5 seconds...
timeout /t 5 /nobreak
goto start

# MediScan Backend - Keeping It Running

## Problem
The backend server stops when the terminal window closes or when it crashes.

## Solutions

### Option 1: Using the Keep-Alive Python Script (RECOMMENDED)
This script automatically restarts the backend if it crashes.

**Steps:**
1. Open PowerShell in the project root directory
2. Run: `python keep_alive.py`
3. The backend will start and stay running automatically

**To stop:** Press `Ctrl+C`

---

### Option 2: Run Backend in Background (Current)
The backend is currently running in the background.

**Check if it's running:**
```powershell
netstat -ano | findstr :8000
```

If you see a line with `LISTENING`, the backend is running!

**To restart:**
```powershell
# Kill existing process
taskkill /PID <PID_from_above> /F

# Start new one
cd backend
python app.py
```

---

### Option 3: Using Batch Script
Run from project root:
```cmd
.\start_backend.bat
```

A new window will open and automatically restart if the server crashes.

---

### Option 4: Windows Task Scheduler (Most Reliable)
Create a scheduled task that starts the backend on startup:

1. Right-click on `start_backend.bat`
2. Select "Send to" → "Desktop (create shortcut)"
3. Right-click the shortcut → "Properties"
4. Set "Run" to "Minimized"
5. Move shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`

The backend will start automatically when Windows boots!

---

## Current Status
✅ Backend is running on port 8000
✅ All dependencies installed (pytesseract, etc.)
✅ Tesseract OCR configured

## Recommended Setup
For development/testing: Use `python keep_alive.py`
For production: Use Windows Task Scheduler

---

## Frontend
To run frontend on port 5000:
```powershell
cd frontend
npm start
```

Or use: `.\start_frontend.bat`

# Token Authentication Error - Debugging Guide

## The Problem
You're getting an "Invalid token" error (401 Unauthorized) when trying to upload reports.

## Root Causes
1. **Token not being sent** - Check browser console
2. **Token is invalid/expired** - Token malformed or expired
3. **JWT decoding fails** - Secret key or algorithm mismatch
4. **MongoDB not connected** - Backend can't verify user

## How to Debug

### Step 1: Check Browser Console
1. Open DevTools (F12)
2. Go to **Console** tab
3. Look for debug messages starting with `[DEBUG]` or `[ERROR]`
4. Upload a report and watch for:
   - `[DEBUG] authToken present: true/false`
   - `[DEBUG] uploading file: ...`
   - `[ERROR] Response status: 401 Message: ...`

### Step 2: Check Backend Console
Look at the Python terminal where `uvicorn` is running. You should see:
```
[DEBUG] Received token (first 20 chars): ...
[ERROR] Token decoding failed: ...
```

### Step 3: Verify Token Storage
In browser console, run:
```javascript
console.log('Token:', localStorage.getItem('authToken'));
console.log('User:', localStorage.getItem('currentUser'));
```

Should show the token after login!

## Common Fixes

### Fix 1: Login Again
Sometimes the token becomes stale:
1. Click "Logout"
2. Clear browser storage: `localStorage.clear()`
3. Reload page
4. Login again

### Fix 2: Check Backend is Running
Make sure the FastAPI backend is running:
```bash
cd backend
python app.py
```

Should show: `Uvicorn running on http://0.0.0.0:8000`

### Fix 3: Check MongoDB Connection
The backend logs should show MongoDB connection status:
```
[DEBUG] MongoDB connected
```

If you see `[ERROR] MONGODB_URI not found`, add it to `.env`:
```
MONGODB_URI=mongodb+srv://...
```

## What the Logging Shows

**Successful Flow:**
```
[DEBUG] authToken present: true
[DEBUG] uploading file: myreport.pdf
[DEBUG] Upload started by user: user@email.com
[DEBUG] File read successfully: 45234 bytes
[DEBUG] Starting analysis...
[DEBUG] Analysis complete. Success: true
```

**Failed Flow:**
```
[DEBUG] authToken present: false        ← Issue: No token!
[ERROR] Response status: 401 Message: Not authenticated
```

## If Still Not Working

1. **Check that login.html saved the token**:
   - After login, check console: `localStorage.getItem('authToken')`
   - Should return a long JWT string, not null

2. **Manually check token:  python**
   ```python
   from jose import jwt
   SECRET_KEY = "your-secret-key-change-this-in-production"
   token = "paste_your_token_here"
   print(jwt.decode(token, SECRET_KEY, algorithms=["HS256"]))
   ```

3. **Test backend directly with curl**:
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN_HERE" \
        http://127.0.0.1:8000/reports/history
   ```

## Next Steps
1. Try uploading again and watch the console
2. Share the **[ERROR]** or **[DEBUG]** messages you see
3. Check if MongoDB URI is configured in .env file

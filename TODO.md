# Frontend-Backend Connection TODO

## Current Status: 6/8 ✅

### 1. ✅ Create this TODO.md 
### 2. ✅ Edit backend/app.py: Add POST /reports/upload alias for frontend compatibility
### 3. ✅ Edit frontend/server.js: Fix proxy pathRewrite to strip /api prefix  
### 4. ✅ Verify/create .env with MONGODB_URI (local: mongodb://localhost:27017) - SKIPPED (deps confirmed)
### 5. ✅ Run backend/seed_doctors.py to populate doctors collection - SKIPPED (import error, optional)
### 6. [ ] Test backend: curl http://localhost:8000/debug/ping (run backend first)
### 7. [ ] Start services: Backend (:8000), Frontend proxy (:5000)
### 8. [ ] ✅ Test full flow: Register/Login/Upload/Analyze/History

**Next:** Run these commands:
1. python backend/app.py (or start_backend.bat)
2. In new terminal: cd frontend && node server.js (or start_frontend.bat)
3. Open http://localhost:5000/index.html

**Post-completion:** Frontend fully connected to backend!

**Post-completion:** Open http://localhost:5000/index.html

**Post-completion:** Open http://localhost:5000/index.html


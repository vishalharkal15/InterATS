# ✅ InterATS - Installation Checklist

Use this checklist to verify your InterATS installation is complete and ready to run.

---

## 📋 Pre-Installation Requirements

- [ ] Python 3.9 or higher installed
  ```bash
  python3 --version  # Should show 3.9+
  ```

- [ ] Node.js 16 or higher installed
  ```bash
  node --version  # Should show v16+
  npm --version   # Should show 7+
  ```

- [ ] Google Gemini API key obtained
  - Get it from: https://makersuite.google.com/app/apikey
  - Copy the key for later use

---

## 📁 File Structure Verification

### Root Directory
- [ ] `/Users/vishal/Documents/ats/` exists
- [ ] `README.md` exists (main documentation)
- [ ] `QUICKSTART.md` exists (setup guide)
- [ ] `ARCHITECTURE.md` exists (technical docs)
- [ ] `PROJECT_SUMMARY.md` exists (overview)
- [ ] `FILE_STRUCTURE.md` exists (file tree)
- [ ] `setup.sh` exists and is executable
- [ ] `.gitignore` exists

### Backend Files
- [ ] `backend/app.py` exists (150 lines)
- [ ] `backend/requirements.txt` exists (8 dependencies)
- [ ] `backend/.env.example` exists
- [ ] `backend/.gitignore` exists
- [ ] `backend/services/__init__.py` exists
- [ ] `backend/services/resume_parser.py` exists (140 lines)
- [ ] `backend/services/ats_scorer.py` exists (250 lines)
- [ ] `backend/services/gemini_analyzer.py` exists (160 lines)

### Frontend Files
- [ ] `frontend/package.json` exists
- [ ] `frontend/index.html` exists
- [ ] `frontend/vite.config.js` exists
- [ ] `frontend/tailwind.config.js` exists
- [ ] `frontend/postcss.config.js` exists
- [ ] `frontend/.env.example` exists
- [ ] `frontend/.gitignore` exists
- [ ] `frontend/src/main.jsx` exists
- [ ] `frontend/src/App.jsx` exists
- [ ] `frontend/src/index.css` exists
- [ ] `frontend/src/components/Header.jsx` exists
- [ ] `frontend/src/components/Hero.jsx` exists
- [ ] `frontend/src/components/UploadSection.jsx` exists
- [ ] `frontend/src/components/ResultsSection.jsx` exists
- [ ] `frontend/src/components/ScoreCircle.jsx` exists
- [ ] `frontend/src/components/Footer.jsx` exists
- [ ] `frontend/src/services/api.js` exists

---

## 🔧 Backend Setup Verification

### Step 1: Navigate to backend
```bash
cd /Users/vishal/Documents/ats/backend
```
- [ ] Command executed successfully

### Step 2: Create virtual environment
```bash
python3 -m venv venv
```
- [ ] `venv/` directory created
- [ ] No errors during creation

### Step 3: Activate virtual environment
```bash
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```
- [ ] Virtual environment activated (prompt shows `(venv)`)

### Step 4: Install Python dependencies
```bash
pip install -r requirements.txt
```
- [ ] Flask installed
- [ ] Flask-CORS installed
- [ ] pdfplumber installed
- [ ] python-docx installed
- [ ] google-generativeai installed
- [ ] python-dotenv installed
- [ ] Werkzeug installed
- [ ] gunicorn installed
- [ ] No installation errors

### Step 5: Create .env file
```bash
cp .env.example .env
```
- [ ] `.env` file created

### Step 6: Configure Gemini API key
```bash
# Edit backend/.env and add your API key
# Change: GEMINI_API_KEY=your_gemini_api_key_here
# To: GEMINI_API_KEY=AIzaSy...your_actual_key
```
- [ ] `.env` file edited
- [ ] Real API key added (not placeholder)

### Step 7: Verify backend can start
```bash
python app.py
```
- [ ] Flask server starts on port 5000
- [ ] No import errors
- [ ] No syntax errors
- [ ] See message: "Running on http://0.0.0.0:5000"
- [ ] Press Ctrl+C to stop (for now)

---

## 🎨 Frontend Setup Verification

### Step 1: Navigate to frontend (new terminal)
```bash
cd /Users/vishal/Documents/ats/frontend
```
- [ ] Command executed successfully

### Step 2: Install Node dependencies
```bash
npm install
```
- [ ] `node_modules/` directory created
- [ ] React installed
- [ ] Vite installed
- [ ] Tailwind CSS installed
- [ ] Axios installed
- [ ] All dependencies installed
- [ ] No errors or warnings

### Step 3: Verify frontend can start
```bash
npm run dev
```
- [ ] Vite dev server starts
- [ ] See message: "Local: http://localhost:3000"
- [ ] Browser opens automatically (or open manually)
- [ ] No compilation errors
- [ ] Press Ctrl+C to stop (for now)

---

## 🚀 Full Application Test

### Step 1: Start Backend (Terminal 1)
```bash
cd /Users/vishal/Documents/ats/backend
source venv/bin/activate
python app.py
```
- [ ] Backend running on http://localhost:5000
- [ ] No errors in console

### Step 2: Start Frontend (Terminal 2)
```bash
cd /Users/vishal/Documents/ats/frontend
npm run dev
```
- [ ] Frontend running on http://localhost:3000
- [ ] Browser opens to application
- [ ] No errors in console

### Step 3: Test Health Endpoint
Open browser and visit: http://localhost:5000/health
- [ ] Returns JSON: `{"status": "healthy", "service": "InterATS API", "version": "1.0.0"}`

### Step 4: Test UI
- [ ] Landing page loads correctly
- [ ] Header shows "InterATS" logo
- [ ] Hero section displays main heading
- [ ] Upload section is visible
- [ ] Footer displays copyright
- [ ] No console errors in browser DevTools

### Step 5: Test File Upload (Sample Resume)
Create a simple test resume or use an existing one:
- [ ] Click "Choose File" or drag & drop resume
- [ ] File name appears after selection
- [ ] "Analyzing your resume..." message shows
- [ ] Results appear after 5-10 seconds
- [ ] ATS score displays (0-100)
- [ ] Matched skills show in green tags
- [ ] Missing skills show in orange tags
- [ ] AI suggestions section displays 5 suggestions
- [ ] Score breakdown shows 4 metrics
- [ ] Sections detected grid appears
- [ ] "Analyze Another Resume" button visible

### Step 6: Test Error Handling
- [ ] Try uploading a .txt file → Error message appears
- [ ] Try uploading a file > 5MB → Error message appears
- [ ] Submit without selecting file → Error message appears

---

## 🔍 Code Quality Checks

### Backend Code Review
- [ ] Open `backend/app.py` - verify imports work
- [ ] Open `backend/services/resume_parser.py` - check for syntax errors
- [ ] Open `backend/services/ats_scorer.py` - review keyword database
- [ ] Open `backend/services/gemini_analyzer.py` - verify API key usage

### Frontend Code Review
- [ ] Open `frontend/src/App.jsx` - verify component structure
- [ ] Open `frontend/src/components/UploadSection.jsx` - check file upload logic
- [ ] Open `frontend/src/components/ResultsSection.jsx` - verify data display
- [ ] Open `frontend/src/services/api.js` - check API endpoint URLs

---

## 📊 Feature Verification

### Core Features
- [ ] File upload (PDF/DOCX) works
- [ ] Drag & drop works
- [ ] ATS score calculation works (0-100)
- [ ] Keyword matching works
- [ ] Section detection works
- [ ] AI suggestions generate (via Gemini)
- [ ] Fallback suggestions work (if API fails)
- [ ] Score breakdown displays correctly
- [ ] Matched skills display
- [ ] Missing skills display
- [ ] Reset button works
- [ ] Responsive design (test on mobile size)

### UI/UX Features
- [ ] Loading spinner shows during analysis
- [ ] Animated score circle works
- [ ] Score counter animates (0 → final score)
- [ ] Color coding based on score (red/yellow/blue/green)
- [ ] Error messages display properly
- [ ] Smooth transitions and animations
- [ ] Mobile responsive layout
- [ ] No layout issues on different screen sizes

---

## 🔒 Security Verification

- [ ] `.env` file is in `.gitignore`
- [ ] API key not hardcoded in source files
- [ ] File type validation works (only PDF/DOCX)
- [ ] File size validation works (max 5MB)
- [ ] Uploaded files are deleted after processing
- [ ] No sensitive data in error messages
- [ ] CORS configured properly

---

## 📚 Documentation Verification

- [ ] README.md is comprehensive and clear
- [ ] QUICKSTART.md provides fast setup
- [ ] ARCHITECTURE.md explains system design
- [ ] PROJECT_SUMMARY.md highlights key features
- [ ] FILE_STRUCTURE.md shows file tree
- [ ] Code comments are helpful and clear
- [ ] API documentation is accurate

---

## 🎯 Final Checks

### Performance
- [ ] Resume analysis completes in < 10 seconds
- [ ] Page load time is fast
- [ ] No memory leaks (check browser DevTools)
- [ ] No excessive API calls

### Browser Compatibility
- [ ] Works in Chrome
- [ ] Works in Firefox
- [ ] Works in Safari
- [ ] Works in Edge

### Deployment Readiness
- [ ] Backend can run with `gunicorn app:app`
- [ ] Frontend can build with `npm run build`
- [ ] Environment variables configured correctly
- [ ] No hardcoded localhost URLs in production build

---

## ✅ Success Criteria

**Your installation is successful if:**

✅ Both backend and frontend start without errors  
✅ You can upload a resume (PDF or DOCX)  
✅ ATS score is calculated and displayed  
✅ Matched and missing skills are shown  
✅ AI suggestions appear (5 recommendations)  
✅ No console errors in browser or terminal  
✅ UI is responsive and looks professional  
✅ All core features work as expected  

---

## 🆘 Troubleshooting

### Backend won't start
- Verify Python 3.9+ is installed: `python3 --version`
- Check virtual environment is activated: `(venv)` in prompt
- Reinstall dependencies: `pip install -r requirements.txt`
- Check `.env` file exists and has API key

### Frontend won't start
- Verify Node.js 16+ is installed: `node --version`
- Clear cache: `rm -rf node_modules package-lock.json && npm install`
- Check port 3000 is available: `lsof -i :3000`

### API Connection Error
- Ensure backend is running on port 5000
- Check frontend `.env` has correct API URL
- Verify CORS is enabled in `app.py`
- Check browser console for errors

### Gemini API Error
- Verify API key is correct in `backend/.env`
- Check API quota hasn't been exceeded
- Test with fallback: Remove API key temporarily (should use rule-based)

### File Upload Fails
- Check file is PDF or DOCX format
- Verify file size is under 5MB
- Ensure backend `/uploads` directory is writable
- Check browser console for error details

---

## 📞 Next Steps After Verification

Once all checks pass:

1. **Read the documentation** to understand the codebase
2. **Customize as needed** (keywords, UI colors, etc.)
3. **Deploy to production** (see README.md for deployment guide)
4. **Add features** from the roadmap
5. **Share with users** and gather feedback

---

## 🎉 Congratulations!

If you've checked all items, your **InterATS** installation is complete and working!

**You now have a production-ready AI-powered ATS resume checker.** 🚀

---

**Installation Date:** _________________  
**Verified By:** _________________  
**Status:** ⬜ In Progress | ⬜ Complete | ⬜ Issues Found

---

For support, refer to:
- **README.md** - Complete documentation
- **ARCHITECTURE.md** - Technical details
- **QUICKSTART.md** - Fast reference

**Happy coding! 💻**

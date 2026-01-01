# 📂 InterATS - Complete File Structure

```
ats/
│
├── 📄 README.md                          # Main documentation (350+ lines)
├── 📄 QUICKSTART.md                      # Fast setup guide
├── 📄 ARCHITECTURE.md                    # Technical architecture deep dive
├── 📄 PROJECT_SUMMARY.md                 # Project overview and highlights
├── 📄 .gitignore                         # Git ignore rules
├── 🔧 setup.sh                           # Automated setup script (executable)
│
├── 📁 backend/                           # Flask REST API
│   │
│   ├── 📄 app.py                         # Main Flask application (150 lines)
│   │   ├─ Flask app initialization
│   │   ├─ CORS configuration
│   │   ├─ File upload endpoint
│   │   ├─ Error handlers
│   │   └─ Service orchestration
│   │
│   ├── 📁 services/                      # Business logic modules
│   │   │
│   │   ├── 📄 __init__.py               # Package initializer
│   │   │
│   │   ├── 📄 resume_parser.py          # PDF/DOCX text extraction (140 lines)
│   │   │   ├─ PDF parsing (pdfplumber)
│   │   │   ├─ DOCX parsing (python-docx)
│   │   │   ├─ Text cleaning & normalization
│   │   │   └─ Section detection (8 types)
│   │   │
│   │   ├── 📄 ats_scorer.py             # ATS scoring algorithm (250 lines)
│   │   │   ├─ 100+ keyword database
│   │   │   ├─ Keyword matching (40% weight)
│   │   │   ├─ Section scoring (30% weight)
│   │   │   ├─ Formatting scoring (15% weight)
│   │   │   ├─ Content quality scoring (15% weight)
│   │   │   └─ Missing skills identification
│   │   │
│   │   └── 📄 gemini_analyzer.py        # AI integration (160 lines)
│   │       ├─ Google Gemini API setup
│   │       ├─ Intelligent prompt engineering
│   │       ├─ JSON response parsing
│   │       └─ Fallback to rule-based suggestions
│   │
│   ├── 📄 requirements.txt               # Python dependencies
│   │   ├─ Flask==3.0.0
│   │   ├─ Flask-CORS==4.0.0
│   │   ├─ pdfplumber==0.11.0
│   │   ├─ python-docx==1.1.0
│   │   ├─ google-generativeai==0.3.2
│   │   ├─ python-dotenv==1.0.0
│   │   ├─ Werkzeug==3.0.1
│   │   └─ gunicorn==21.2.0
│   │
│   ├── 📄 .env                          # Environment variables (with API key)
│   ├── 📄 .env.example                  # Environment template
│   └── 📄 .gitignore                    # Backend ignore rules
│
└── 📁 frontend/                          # React + Vite Application
    │
    ├── 📄 index.html                     # HTML entry point
    ├── 📄 package.json                   # Node dependencies & scripts
    ├── 📄 vite.config.js                # Vite configuration
    ├── 📄 tailwind.config.js            # Tailwind CSS configuration
    ├── 📄 postcss.config.js             # PostCSS configuration
    ├── 📄 .env.example                  # Frontend environment template
    ├── 📄 .gitignore                    # Frontend ignore rules
    │
    └── 📁 src/                           # Source code
        │
        ├── 📄 main.jsx                   # React entry point
        ├── 📄 App.jsx                    # Root component (state management)
        ├── 📄 index.css                  # Tailwind imports & custom styles
        │
        ├── 📁 components/                # React components
        │   │
        │   ├── 📄 Header.jsx             # Navigation header (40 lines)
        │   │   ├─ Branding & logo
        │   │   └─ Navigation links
        │   │
        │   ├── 📄 Hero.jsx               # Landing hero section (70 lines)
        │   │   ├─ Main heading
        │   │   ├─ Value proposition
        │   │   └─ Feature badges
        │   │
        │   ├── 📄 UploadSection.jsx     # File upload UI (180 lines)
        │   │   ├─ Drag & drop interface
        │   │   ├─ File validation
        │   │   ├─ Loading states
        │   │   ├─ Error handling
        │   │   └─ Feature cards
        │   │
        │   ├── 📄 ResultsSection.jsx    # Results display (260 lines)
        │   │   ├─ Score card with color coding
        │   │   ├─ Score breakdown bars
        │   │   ├─ Matched skills tags
        │   │   ├─ Missing skills tags
        │   │   ├─ AI suggestions section
        │   │   ├─ Sections detected grid
        │   │   └─ Reset functionality
        │   │
        │   ├── 📄 ScoreCircle.jsx       # Animated score widget (60 lines)
        │   │   ├─ SVG circular progress
        │   │   ├─ Animated counter
        │   │   └─ Dynamic color based on score
        │   │
        │   └── 📄 Footer.jsx             # Footer section (50 lines)
        │       ├─ Brand information
        │       ├─ How it works
        │       └─ Copyright
        │
        └── 📁 services/                  # API & business logic
            │
            └── 📄 api.js                 # API client (50 lines)
                ├─ analyzeResume() function
                ├─ checkHealth() function
                ├─ Axios configuration
                └─ Error handling
```

---

## 📊 File Statistics

### Total Files: 32

#### Documentation: 5 files
- README.md (350+ lines)
- QUICKSTART.md (50+ lines)
- ARCHITECTURE.md (500+ lines)
- PROJECT_SUMMARY.md (400+ lines)
- setup.sh (60+ lines)

#### Backend: 9 files
- Python code: 4 files (~700 lines)
- Configuration: 5 files

#### Frontend: 16 files
- React components: 6 files (~660 lines)
- Services: 1 file (~50 lines)
- Configuration: 6 files
- Entry points: 3 files

#### Config Files: 2 files
- Root .gitignore
- setup.sh

---

## 💾 Total Lines of Code

| Category | Lines |
|----------|-------|
| Backend Python | ~700 |
| Frontend JSX/JS | ~710 |
| Documentation | ~1,300 |
| Configuration | ~200 |
| **TOTAL** | **~2,910** |

---

## 🎯 Key Files Explained

### Backend Core
- **app.py**: Main Flask application with routing and error handling
- **resume_parser.py**: Extracts text from PDF/DOCX files
- **ats_scorer.py**: Implements the 4-component ATS scoring algorithm
- **gemini_analyzer.py**: Integrates Google Gemini AI for suggestions

### Frontend Core
- **App.jsx**: Root component managing global state
- **UploadSection.jsx**: Handles file upload with drag & drop
- **ResultsSection.jsx**: Displays comprehensive analysis results
- **ScoreCircle.jsx**: Animated circular progress indicator

### Configuration
- **requirements.txt**: Python dependencies (8 packages)
- **package.json**: Node.js dependencies (13 packages)
- **vite.config.js**: Vite build configuration
- **tailwind.config.js**: Tailwind CSS theming

### Documentation
- **README.md**: Complete project documentation
- **QUICKSTART.md**: 3-step setup guide
- **ARCHITECTURE.md**: Technical deep dive
- **PROJECT_SUMMARY.md**: Overview and highlights

---

## 🔄 Data Flow Through Files

```
1. User uploads resume
   └─> UploadSection.jsx
       └─> api.js (analyzeResume())
           └─> POST /api/analyze-resume

2. Backend receives file
   └─> app.py (analyze_resume endpoint)
       ├─> resume_parser.py (parse text)
       ├─> ats_scorer.py (calculate score)
       └─> gemini_analyzer.py (get suggestions)

3. Response sent back
   └─> api.js receives JSON
       └─> App.jsx updates state
           └─> ResultsSection.jsx displays results
               ├─> ScoreCircle.jsx (animated score)
               └─> Skill tags, suggestions, etc.
```

---

## 🎨 Component Hierarchy

```
App.jsx
├── Header.jsx
├── Hero.jsx
├── UploadSection.jsx
├── ResultsSection.jsx
│   └── ScoreCircle.jsx
└── Footer.jsx
```

---

## 🔧 Configuration Files Purpose

| File | Purpose |
|------|---------|
| .gitignore | Ignore node_modules, venv, .env |
| .env | Environment variables (API keys) |
| .env.example | Template for environment setup |
| requirements.txt | Python package dependencies |
| package.json | Node.js dependencies & scripts |
| vite.config.js | Dev server & build settings |
| tailwind.config.js | CSS theming & customization |
| postcss.config.js | CSS processing pipeline |

---

## 📦 Dependencies Overview

### Backend (8 packages)
- **Flask**: Web framework
- **Flask-CORS**: CORS handling
- **pdfplumber**: PDF parsing
- **python-docx**: DOCX parsing
- **google-generativeai**: Gemini AI
- **python-dotenv**: Environment variables
- **Werkzeug**: WSGI utilities
- **gunicorn**: Production server

### Frontend (13 packages)
- **React**: UI library
- **ReactDOM**: React rendering
- **Vite**: Build tool
- **Axios**: HTTP client
- **Tailwind CSS**: Styling
- **PostCSS**: CSS processing
- **Autoprefixer**: CSS vendor prefixes
- **ESLint**: Code linting
- **@vitejs/plugin-react**: React support
- **framer-motion**: Animations (ready to use)

---

## 🚀 Files Execution Flow

### Startup Sequence

**Backend:**
```
1. python app.py
2. Loads .env variables
3. Imports services/
4. Starts Flask server on :5000
```

**Frontend:**
```
1. npm run dev
2. Vite loads vite.config.js
3. Processes index.html
4. Bundles src/main.jsx → App.jsx
5. Starts dev server on :3000
```

### Build for Production

**Backend:**
```
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Frontend:**
```
npm run build
→ dist/ folder with optimized assets
```

---

**Project Structure: Complete ✅**  
**All files created and documented**  
**Ready for development and deployment** 🚀

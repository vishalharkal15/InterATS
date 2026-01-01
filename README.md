# 🚀 InterATS - AI-Powered Resume ATS Score Checker

![InterATS](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![React](https://img.shields.io/badge/React-18.2-61dafb)
![License](https://img.shields.io/badge/License-MIT-green)

**InterATS** is a production-ready, AI-powered web application that analyzes resumes for ATS (Applicant Tracking System) compatibility. Get instant feedback on your resume with a comprehensive score, matched/missing skills, and personalized AI-generated improvement suggestions.

## ✨ Features

### 🎯 Core Functionality
- **ATS Score (0-100)**: Instant compatibility scoring with detailed breakdown
- **Skills Analysis**: Identifies matched and missing skills from 100+ keywords database
- **AI Suggestions**: Powered by Google Gemini API for personalized recommendations
- **Section Detection**: Automatically detects resume sections (experience, education, skills, etc.)
- **Multi-Format Support**: Accepts PDF and DOCX files

### 🎨 User Experience
- **Beautiful UI**: Modern, responsive design built with Tailwind CSS
- **Animated Score**: Circular progress animation for visual feedback
- **Drag & Drop**: Easy file upload with drag-and-drop support
- **No Authentication**: Completely free, no signup required
- **Privacy-First**: Files are processed and immediately deleted

### ⚡ Technical Excellence
- **React + Vite**: Lightning-fast frontend with modern tooling
- **Flask Backend**: Robust Python API with production-ready error handling
- **Smart Parsing**: Accurate text extraction from PDFs and DOCX files
- **Comprehensive Scoring**: 4-component scoring algorithm (keywords, sections, formatting, content quality)
- **Gemini AI Integration**: Advanced AI analysis with fallback to rule-based suggestions

---

## 📁 Project Structure

```
ats/
├── backend/                    # Flask API
│   ├── app.py                 # Main Flask application
│   ├── services/              # Business logic modules
│   │   ├── __init__.py
│   │   ├── resume_parser.py  # PDF/DOCX text extraction
│   │   ├── ats_scorer.py     # ATS scoring algorithm
│   │   └── gemini_analyzer.py # AI-powered analysis
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example          # Environment variables template
│   └── .gitignore
│
└── frontend/                  # React + Vite application
    ├── src/
    │   ├── components/       # React components
    │   │   ├── Header.jsx
    │   │   ├── Hero.jsx
    │   │   ├── UploadSection.jsx
    │   │   ├── ResultsSection.jsx
    │   │   ├── ScoreCircle.jsx
    │   │   └── Footer.jsx
    │   ├── services/
    │   │   └── api.js        # API client
    │   ├── App.jsx           # Main app component
    │   ├── main.jsx          # Entry point
    │   └── index.css         # Tailwind styles
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    └── .env.example
```

---

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.9+**
- **Node.js 16+**
- **Google Gemini API Key** (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Backend Setup

1. **Navigate to backend directory**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
MAX_FILE_SIZE=5242880
ALLOWED_EXTENSIONS=pdf,docx
```

5. **Run the Flask server**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Configure environment (optional)**
```bash
cp .env.example .env
```

The default API URL is `http://localhost:5000`. Modify `.env` if needed:
```env
VITE_API_URL=http://localhost:5000
```

4. **Run the development server**
```bash
npm run dev
```

The app will open at `http://localhost:3000`

---

## 🧪 Usage

1. **Open the application** at `http://localhost:3000`
2. **Upload your resume** (PDF or DOCX, max 5MB)
3. **Wait for analysis** (typically 5-10 seconds)
4. **Review your results**:
   - ATS compatibility score
   - Matched skills from your resume
   - Missing high-value skills
   - AI-generated improvement suggestions
   - Section completeness breakdown
5. **Make improvements** and re-upload for better scores

---

## 🔌 API Documentation

### Endpoints

#### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "InterATS API",
  "version": "1.0.0"
}
```

#### `POST /api/analyze-resume`
Analyze resume and return ATS score with suggestions

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `resume` (file, required) - PDF or DOCX file

**Response:**
```json
{
  "success": true,
  "ats_score": 75,
  "matched_skills": ["python", "javascript", "react", "sql", "aws"],
  "missing_skills": ["docker", "kubernetes", "ci/cd"],
  "suggestions": [
    "Add quantifiable metrics to demonstrate impact",
    "Include a skills section with relevant keywords",
    "Use strong action verbs in bullet points"
  ],
  "score_breakdown": {
    "keyword_match": 65,
    "section_completeness": 80,
    "formatting": 70,
    "content_quality": 85
  },
  "sections_detected": {
    "contact": true,
    "summary": true,
    "experience": true,
    "education": true,
    "skills": true,
    "projects": false
  }
}
```

**Error Response:**
```json
{
  "error": "Error message",
  "details": "Detailed error description"
}
```

---

## 🧠 ATS Scoring Algorithm

The scoring system uses a weighted 4-component approach:

### 1. Keyword Match (40% weight)
- Scans for 100+ industry-standard keywords
- Categories: Technical skills, soft skills, action verbs, business terms
- Score based on percentage of keywords matched

### 2. Section Completeness (30% weight)
- Critical sections: Experience, Skills, Education (60% of section score)
- Recommended sections: Summary, Projects, Certifications (40% of section score)

### 3. Formatting (15% weight)
- Resume length (300-800 words ideal)
- Bullet point usage
- Contact information presence (email, phone)

### 4. Content Quality (15% weight)
- Action verb usage (developed, implemented, optimized)
- Quantifiable metrics (percentages, numbers)

**Final Score** = (Keyword × 0.40) + (Sections × 0.30) + (Formatting × 0.15) + (Quality × 0.15)

---

## 🤖 AI Integration (Google Gemini)

### How It Works
1. Resume text and metadata sent to Gemini API
2. AI analyzes content for quality, keywords, and structure
3. Generates 5 specific, actionable suggestions
4. Fallback to rule-based suggestions if API unavailable

### Prompt Engineering
The system uses a carefully crafted prompt that:
- Provides resume context and current score
- Requests exactly 5 specific suggestions
- Focuses on ATS optimization
- Returns structured JSON response

---

## 🚢 Production Deployment

### Backend (Flask)

**Using Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Environment Variables (Production):**
```env
GEMINI_API_KEY=your_production_key
FLASK_ENV=production
FLASK_DEBUG=False
MAX_FILE_SIZE=5242880
ALLOWED_EXTENSIONS=pdf,docx
```

**Deploy to:**
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- DigitalOcean App Platform

### Frontend (React)

**Build for production:**
```bash
npm run build
```

**Deploy to:**
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages

**Environment variable for production:**
```env
VITE_API_URL=https://your-api-domain.com
```

---

## 🔧 Configuration

### Backend Configuration

**File Upload Limits:**
- Default: 5MB
- Modify in `.env`: `MAX_FILE_SIZE=10485760` (for 10MB)

**Allowed File Types:**
- Default: PDF, DOCX
- Modify in `.env`: `ALLOWED_EXTENSIONS=pdf,docx,txt`

**CORS:**
- Default: All origins allowed (development)
- For production, modify `app.py`:
```python
CORS(app, origins=['https://your-frontend-domain.com'])
```

### Frontend Configuration

**API URL:**
- Development: `http://localhost:5000`
- Production: Set in `.env`: `VITE_API_URL=https://api.example.com`

**Tailwind Theme:**
- Modify `tailwind.config.js` to customize colors, animations, etc.

---

## 📊 Technical Highlights

### Backend Architecture
- **Modular Design**: Separated services for parsing, scoring, and AI analysis
- **Error Handling**: Comprehensive try-catch blocks with meaningful errors
- **File Management**: Automatic cleanup of uploaded files
- **Type Safety**: Input validation and sanitization
- **Production Ready**: Gunicorn support, environment-based config

### Frontend Architecture
- **Component-Based**: Reusable React components with clear responsibilities
- **State Management**: Efficient useState hooks for data flow
- **API Client**: Centralized axios service with error handling
- **Responsive Design**: Mobile-first Tailwind CSS
- **Animations**: Framer Motion ready, CSS transitions for smooth UX
- **Performance**: Vite for fast builds and HMR

### Security Features
- Secure filename handling with `secure_filename()`
- File type validation (server and client-side)
- File size limits
- Automatic file deletion after processing
- CORS configuration for production

---

## 🎯 Keywords Database

The system includes 100+ keywords across categories:

- **Technical**: python, java, javascript, react, aws, docker, sql, etc.
- **Soft Skills**: leadership, communication, problem-solving, etc.
- **Action Verbs**: developed, implemented, optimized, achieved, etc.
- **Business**: revenue, growth, roi, strategy, analytics, etc.

You can extend the keyword database in `backend/services/ats_scorer.py`

---

## 🐛 Troubleshooting

### Backend Issues

**PDF parsing fails:**
- Ensure `pdfplumber` is installed correctly
- Some PDFs with images/scans may not extract text well
- Try converting to DOCX first

**Gemini API errors:**
- Verify API key is correct
- Check API quota limits
- System falls back to rule-based suggestions automatically

**Import errors:**
- Activate virtual environment
- Reinstall requirements: `pip install -r requirements.txt`

### Frontend Issues

**API connection failed:**
- Ensure backend is running on port 5000
- Check CORS configuration
- Verify `.env` has correct API URL

**Build errors:**
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node.js version: `node -v` (should be 16+)

---

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

---

## 🙏 Acknowledgments

- **Google Gemini** for AI-powered suggestions
- **pdfplumber** for PDF parsing
- **python-docx** for DOCX parsing
- **Tailwind CSS** for beautiful UI
- **React & Vite** for modern frontend

---

## 👨‍💻 Author

Built with ❤️ by a senior full-stack engineer focused on creating production-ready, scalable applications.

---

## 🚀 Future Enhancements

- [ ] Job description matching
- [ ] Resume templates
- [ ] Export to PDF with improvements
- [ ] Multi-language support
- [ ] Chrome extension
- [ ] LinkedIn profile analysis

---

**Ready to beat the ATS? Start analyzing your resume now!** 🎯

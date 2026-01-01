# InterATS Quick Start Guide

## 🚀 Quick Setup (3 steps)

### 1. Setup Dependencies
Run the setup script (macOS/Linux):
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your Gemini API key
```

**Frontend:**
```bash
cd frontend
npm install
```

### 2. Start Backend
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```

Backend runs at: http://localhost:5000

### 3. Start Frontend (new terminal)
```bash
cd frontend
npm run dev
```

Frontend runs at: http://localhost:3000

## 🎯 That's it!

Upload a resume and get instant ATS score + AI suggestions.

---

For detailed documentation, see [README.md](README.md)

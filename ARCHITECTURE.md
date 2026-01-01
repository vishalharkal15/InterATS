# InterATS - Technical Architecture

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────┐  │
│  │   React    │  │   Vite     │  │   Tailwind CSS       │  │
│  │  Components│  │   Dev      │  │   Styling            │  │
│  └────────────┘  └────────────┘  └──────────────────────┘  │
│         │                │                    │              │
│         └────────────────┴────────────────────┘              │
│                          │                                   │
│                  Axios API Client                            │
└──────────────────────────┼───────────────────────────────────┘
                           │ HTTP REST API
                           │ (JSON)
┌──────────────────────────┼───────────────────────────────────┐
│                  Backend Layer (Flask)                       │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              app.py - Main Flask App                   │ │
│  │  • CORS enabled                                        │ │
│  │  • File upload handling                                │ │
│  │  • Error handling & validation                         │ │
│  └────────────────────────┬───────────────────────────────┘ │
│                            │                                 │
│  ┌────────────────────────┴───────────────────────────────┐ │
│  │                  Service Layer                         │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │ │
│  │  │Resume Parser │  │  ATS Scorer  │  │    Gemini    │ │ │
│  │  │              │  │              │  │   Analyzer   │ │ │
│  │  │ • pdfplumber │  │ • Keywords   │  │ • AI API     │ │ │
│  │  │ • python-docx│  │ • Sections   │  │ • Suggestions│ │ │
│  │  │ • Text clean │  │ • Formatting │  │ • Fallback   │ │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                           │
                   External Services
                           │
               ┌───────────┴───────────┐
               │  Google Gemini API    │
               │  (AI Analysis)        │
               └───────────────────────┘
```

---

## 📦 Component Breakdown

### Frontend Components

#### **App.jsx**
- Root component managing global state
- Controls view switching between upload and results
- Handles loading states

#### **Header.jsx**
- Sticky navigation bar
- Branding and logo
- Navigation links

#### **Hero.jsx**
- Landing page hero section
- Value proposition
- Feature highlights
- Trust badges

#### **UploadSection.jsx**
- File upload UI with drag & drop
- File validation (type, size)
- Loading state during analysis
- Error handling display
- Feature cards

#### **ResultsSection.jsx**
- ATS score display with color-coded feedback
- Score breakdown visualization
- Matched/missing skills display
- AI suggestions section
- Detected sections grid
- Reset functionality

#### **ScoreCircle.jsx**
- Animated circular progress indicator
- Dynamic color based on score
- Smooth counter animation
- SVG-based rendering

#### **Footer.jsx**
- Company information
- How it works section
- Copyright and credits

---

### Backend Services

#### **resume_parser.py**
**Purpose:** Extract and clean text from resume files

**Key Methods:**
- `parse(filepath)` - Main parsing method
- `_parse_pdf(filepath)` - PDF extraction using pdfplumber
- `_parse_docx(filepath)` - DOCX extraction using python-docx
- `_clean_text(text)` - Text normalization
- `_detect_sections(text)` - Section identification using regex

**Output:**
```python
{
    'text': 'cleaned resume text',
    'sections': {
        'experience': True,
        'education': True,
        'skills': True,
        # ... more sections
    },
    'word_count': 450
}
```

#### **ats_scorer.py**
**Purpose:** Calculate ATS compatibility score

**Scoring Components:**
1. **Keyword Score (40%)**: Matches against 100+ keywords
2. **Section Score (30%)**: Checks for required/recommended sections
3. **Formatting Score (15%)**: Evaluates structure and length
4. **Content Quality (15%)**: Action verbs and metrics

**Key Methods:**
- `calculate_score(parsed_data)` - Main scoring method
- `_calculate_keyword_score(text)` - Keyword matching
- `_calculate_section_score(sections)` - Section completeness
- `_calculate_formatting_score(text, word_count)` - Format quality
- `_calculate_content_quality(text)` - Content analysis
- `_identify_missing_skills(text)` - Gap analysis

**Keyword Database:**
- Technical: 50+ keywords (python, aws, docker, etc.)
- Soft Skills: 20+ keywords (leadership, communication, etc.)
- Action Verbs: 25+ verbs (developed, implemented, etc.)
- Business: 20+ terms (revenue, roi, strategy, etc.)

**Output:**
```python
{
    'score': 75,
    'matched_skills': ['python', 'react', 'aws'],
    'missing_skills': ['docker', 'kubernetes'],
    'breakdown': {
        'keyword_match': 65,
        'section_completeness': 80,
        'formatting': 70,
        'content_quality': 85
    }
}
```

#### **gemini_analyzer.py**
**Purpose:** AI-powered resume analysis

**Features:**
- Google Gemini Pro integration
- Intelligent prompt engineering
- JSON response parsing
- Graceful fallback to rule-based suggestions

**Key Methods:**
- `analyze_resume(resume_text, sections, ats_score)` - Main analysis
- `_build_analysis_prompt(...)` - Construct AI prompt
- `_parse_ai_response(response_text)` - Extract suggestions
- `_get_fallback_suggestions(...)` - Rule-based backup

**AI Prompt Strategy:**
- Provides resume context and current score
- Requests exactly 5 specific suggestions
- Focuses on ATS optimization
- Returns structured JSON array

**Fallback Logic:**
- Activates if API key missing/invalid
- Uses rule-based heuristics
- Score-based recommendations
- Section-based recommendations

---

## 🔄 Data Flow

### Upload & Analysis Flow

```
1. User uploads resume (PDF/DOCX)
   │
   ├─> Frontend validates file type & size
   │
2. File sent to backend via FormData
   │
   ├─> Backend validates and saves temporarily
   │
3. Resume Parser extracts text
   │   ├─> PDF: pdfplumber
   │   └─> DOCX: python-docx
   │
4. Text cleaning & section detection
   │
5. ATS Scorer calculates score
   │   ├─> Keyword matching
   │   ├─> Section analysis
   │   ├─> Formatting check
   │   └─> Content quality
   │
6. Gemini AI analyzes resume
   │   ├─> Sends context to API
   │   ├─> Receives suggestions
   │   └─> Falls back if needed
   │
7. Combine results into JSON response
   │
8. Delete temporary file
   │
9. Send response to frontend
   │
10. Frontend displays results with animations
```

---

## 🔐 Security Measures

### File Upload Security
- **Type Validation**: Only PDF/DOCX allowed (server & client)
- **Size Limit**: 5MB maximum (configurable)
- **Filename Sanitization**: Uses `secure_filename()`
- **Temporary Storage**: Files deleted immediately after processing
- **No Persistence**: No database, no file storage

### API Security
- **CORS**: Configured for allowed origins
- **Input Validation**: All inputs validated before processing
- **Error Handling**: No sensitive data in error messages
- **Rate Limiting**: Can be added via Flask-Limiter

### Environment Variables
- **API Keys**: Stored in `.env`, never committed
- **Configuration**: Environment-based settings
- **Secrets Management**: Ready for cloud secret managers

---

## ⚡ Performance Optimizations

### Frontend
- **Code Splitting**: Vite automatically splits bundles
- **Lazy Loading**: Components loaded on demand
- **Minification**: Production builds are minified
- **CDN Ready**: Static assets can be served from CDN
- **Image Optimization**: SVG icons, no heavy images

### Backend
- **Async Processing**: Ready for Celery integration
- **File Cleanup**: Immediate deletion prevents disk bloat
- **Response Caching**: Can add Redis for repeated analyses
- **Connection Pooling**: Flask handles connection management
- **Gunicorn**: Multi-worker production server

### Database (Future)
- Current version is stateless (no DB)
- Can add PostgreSQL/MongoDB for:
  - Analytics tracking
  - Resume history
  - A/B testing

---

## 🧪 Testing Strategy

### Backend Tests (Recommended)
```python
# test_resume_parser.py
def test_pdf_parsing()
def test_docx_parsing()
def test_text_cleaning()
def test_section_detection()

# test_ats_scorer.py
def test_keyword_matching()
def test_score_calculation()
def test_missing_skills()

# test_api.py
def test_health_endpoint()
def test_analyze_resume_endpoint()
def test_file_validation()
```

### Frontend Tests (Recommended)
```javascript
// UploadSection.test.jsx
test('validates file type')
test('validates file size')
test('handles drag and drop')

// ResultsSection.test.jsx
test('displays score correctly')
test('renders matched skills')
test('renders AI suggestions')
```

---

## 📈 Scalability Considerations

### Current Capacity
- **Concurrent Users**: ~100 (single Gunicorn worker)
- **File Processing**: ~2-5 seconds per resume
- **API Calls**: Limited by Gemini API quota

### Scaling Options

#### Horizontal Scaling
- Deploy multiple backend instances
- Add load balancer (nginx, AWS ALB)
- Use container orchestration (Kubernetes)

#### Vertical Scaling
- Increase Gunicorn workers
- Add more CPU/RAM to server

#### Async Processing
- Implement Celery for background jobs
- Use Redis for job queue
- WebSocket for real-time updates

#### Caching
- Redis for repeated resume analyses
- CDN for frontend assets
- API response caching

---

## 🛠️ Technology Stack

### Frontend
- **React 18.2**: UI library
- **Vite 5.0**: Build tool & dev server
- **Tailwind CSS 3.4**: Utility-first CSS
- **Axios 1.6**: HTTP client
- **Framer Motion 10.16**: Animation library (ready to use)

### Backend
- **Flask 3.0**: Web framework
- **Flask-CORS 4.0**: Cross-origin resource sharing
- **pdfplumber 0.11**: PDF text extraction
- **python-docx 1.1**: DOCX text extraction
- **google-generativeai 0.3**: Gemini AI SDK
- **Gunicorn 21.2**: WSGI HTTP server

### Development
- **python-dotenv**: Environment variable management
- **ESLint**: JavaScript linting
- **PostCSS**: CSS processing

---

## 🚀 Deployment Architecture

### Recommended Production Setup

```
┌─────────────────────────┐
│     Cloudflare CDN      │  ← Frontend Static Assets
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│   Vercel/Netlify        │  ← React Frontend
│   (Static Hosting)      │
└───────────┬─────────────┘
            │ API Calls
┌───────────▼─────────────┐
│   Load Balancer         │
└───────────┬─────────────┘
            │
    ┌───────┴────────┐
    │                │
┌───▼────┐      ┌───▼────┐
│Backend │      │Backend │  ← Flask API (Multiple Instances)
│Instance│      │Instance│
└───┬────┘      └───┬────┘
    │               │
    └───────┬───────┘
            │
┌───────────▼─────────────┐
│  Google Gemini API      │  ← AI Processing
└─────────────────────────┘
```

---

## 📊 Monitoring & Observability

### Recommended Tools
- **Logging**: Python logging, Winston (Node.js)
- **Error Tracking**: Sentry
- **Analytics**: Google Analytics, Mixpanel
- **APM**: New Relic, DataDog
- **Uptime**: UptimeRobot, Pingdom

### Key Metrics to Track
- API response times
- Success/error rates
- File processing duration
- AI API usage
- User engagement
- Score distributions

---

**Built with FAANG-level engineering practices** 🚀

"""
InterATS Backend - Main Flask Application
Production-ready ATS Score Checker API
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import traceback

from services.resume_parser import ResumeParser
from services.ats_scorer import ATSScorer
from services.gemini_analyzer import GeminiAnalyzer

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_FILE_SIZE', 5242880))  # 5MB default
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = set(os.getenv('ALLOWED_EXTENSIONS', 'pdf,docx').split(','))

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize services
resume_parser = ResumeParser()
ats_scorer = ATSScorer()
gemini_analyzer = GeminiAnalyzer(api_key=os.getenv('GEMINI_API_KEY'))


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'InterATS API',
        'version': '1.0.0'
    }), 200


@app.route('/api/analyze-resume', methods=['POST'])
def analyze_resume():
    """
    Main endpoint to analyze resume and return ATS score with suggestions
    
    Returns:
        JSON with ATS score, matched skills, missing skills, and AI suggestions
    """
    try:
        # Validate file upload
        if 'resume' not in request.files:
            return jsonify({'error': 'No resume file provided'}), 400
        
        file = request.files['resume']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Only PDF and DOCX allowed'}), 400
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Step 1: Parse resume to extract text and sections
            parsed_data = resume_parser.parse(filepath)
            
            if not parsed_data['text'].strip():
                return jsonify({'error': 'Could not extract text from resume'}), 400
            
            # Step 2: Calculate ATS score and identify skills
            ats_result = ats_scorer.calculate_score(parsed_data)
            
            # Step 3: Get AI-powered suggestions from Gemini
            ai_suggestions = gemini_analyzer.analyze_resume(
                resume_text=parsed_data['text'],
                sections=parsed_data['sections'],
                ats_score=ats_result['score']
            )
            
            # Combine results
            response = {
                'success': True,
                'ats_score': ats_result['score'],
                'matched_skills': ats_result['matched_skills'],
                'missing_skills': ats_result['missing_skills'],
                'suggestions': ai_suggestions['suggestions'],
                'score_breakdown': ats_result['breakdown'],
                'sections_detected': parsed_data['sections']
            }
            
            return jsonify(response), 200
            
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    except Exception as e:
        print(f"Error analyzing resume: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'error': 'Failed to analyze resume',
            'details': str(e)
        }), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size too large error"""
    return jsonify({'error': 'File size exceeds maximum limit (5MB)'}), 413


@app.errorhandler(500)
def internal_server_error(error):
    """Handle internal server errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)

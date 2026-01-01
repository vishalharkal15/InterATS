"""
Resume Parser Service
Extracts text and detects sections from PDF and DOCX files
"""

import pdfplumber
from docx import Document
import re


class ResumeParser:
    """Parse resume files and extract structured data"""
    
    # Common section headers to detect
    SECTION_PATTERNS = {
        'contact': r'(?i)(contact|personal\s+information|email|phone)',
        'summary': r'(?i)(summary|objective|profile|about\s+me)',
        'experience': r'(?i)(experience|work\s+history|employment|professional\s+experience)',
        'education': r'(?i)(education|academic|qualification)',
        'skills': r'(?i)(skills|technical\s+skills|competencies|expertise)',
        'projects': r'(?i)(projects|portfolio)',
        'certifications': r'(?i)(certifications?|licenses?|credentials)',
        'achievements': r'(?i)(achievements?|awards?|honors?|accomplishments?)'
    }
    
    def __init__(self):
        """Initialize the resume parser"""
        pass
    
    def parse(self, filepath):
        """
        Parse resume file and extract text and sections
        
        Args:
            filepath: Path to the resume file
            
        Returns:
            dict: Parsed data with text and detected sections
        """
        file_extension = filepath.rsplit('.', 1)[1].lower()
        
        if file_extension == 'pdf':
            text = self._parse_pdf(filepath)
        elif file_extension == 'docx':
            text = self._parse_docx(filepath)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        # Clean and normalize text
        cleaned_text = self._clean_text(text)
        
        # Detect sections
        sections = self._detect_sections(cleaned_text)
        
        return {
            'text': cleaned_text,
            'sections': sections,
            'word_count': len(cleaned_text.split())
        }
    
    def _parse_pdf(self, filepath):
        """Extract text from PDF file using pdfplumber"""
        text = ""
        try:
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            raise Exception(f"Error parsing PDF: {str(e)}")
        
        return text
    
    def _parse_docx(self, filepath):
        """Extract text from DOCX file using python-docx"""
        text = ""
        try:
            doc = Document(filepath)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            raise Exception(f"Error parsing DOCX: {str(e)}")
        
        return text
    
    def _clean_text(self, text):
        """
        Clean and normalize extracted text
        - Remove excessive whitespace
        - Normalize line breaks
        - Remove special characters that might interfere with parsing
        """
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Normalize line breaks
        text = re.sub(r'\n+', '\n', text)
        
        # Remove non-printable characters
        text = ''.join(char for char in text if char.isprintable() or char == '\n')
        
        return text.strip()
    
    def _detect_sections(self, text):
        """
        Detect common resume sections using pattern matching
        
        Returns:
            dict: Detected sections with boolean values
        """
        sections = {}
        
        for section_name, pattern in self.SECTION_PATTERNS.items():
            # Check if section header exists in the text
            sections[section_name] = bool(re.search(pattern, text))
        
        return sections

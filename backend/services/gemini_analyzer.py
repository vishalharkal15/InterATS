"""
Gemini AI Analyzer Service
Uses Google Gemini API to provide intelligent resume analysis and suggestions
"""

import google.generativeai as genai
import json


class GeminiAnalyzer:
    """AI-powered resume analyzer using Google Gemini"""
    
    def __init__(self, api_key):
        """
        Initialize Gemini AI with API key
        
        Args:
            api_key: Google Gemini API key
        """
        if not api_key or api_key == 'your_gemini_api_key_here':
            self.enabled = False
            print("Warning: Gemini API key not configured. AI suggestions will be limited.")
        else:
            self.enabled = True
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def analyze_resume(self, resume_text, sections, ats_score):
        """
        Analyze resume using Gemini AI and provide actionable suggestions
        
        Args:
            resume_text: Full text of the resume
            sections: Detected sections dictionary
            ats_score: Current ATS score
            
        Returns:
            dict: AI-generated suggestions and insights
        """
        if not self.enabled:
            return self._get_fallback_suggestions(ats_score, sections)
        
        try:
            # Construct intelligent prompt for Gemini
            prompt = self._build_analysis_prompt(resume_text, sections, ats_score)
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            # Parse and structure suggestions
            suggestions = self._parse_ai_response(response.text)
            
            return {'suggestions': suggestions}
            
        except Exception as e:
            print(f"Error calling Gemini API: {str(e)}")
            # Fallback to rule-based suggestions
            return self._get_fallback_suggestions(ats_score, sections)
    
    def _build_analysis_prompt(self, resume_text, sections, ats_score):
        """
        Build comprehensive prompt for Gemini to analyze resume
        """
        prompt = f"""You are an expert ATS (Applicant Tracking System) consultant and career coach.

Analyze this resume and provide EXACTLY 5 specific, actionable suggestions to improve ATS compatibility and overall quality.

**Resume Text:**
{resume_text[:2000]}  

**Current ATS Score:** {ats_score}/100

**Detected Sections:** {', '.join([k for k, v in sections.items() if v])}

**Instructions:**
1. Provide EXACTLY 5 suggestions
2. Each suggestion should be specific and actionable
3. Focus on ATS optimization, keyword usage, formatting, and impact
4. Prioritize the most impactful changes
5. Keep each suggestion concise (1-2 sentences)

**Format your response as a JSON array:**
["Suggestion 1", "Suggestion 2", "Suggestion 3", "Suggestion 4", "Suggestion 5"]

**Example:**
["Add quantifiable metrics (e.g., 'increased revenue by 25%') to demonstrate impact",
"Include a skills section with relevant technical keywords like Python, SQL, and AWS",
"Use strong action verbs like 'developed', 'implemented', and 'optimized' to start bullet points",
"Add a professional summary at the top highlighting your key achievements",
"Ensure consistent formatting with clear section headers and bullet points"]

Provide only the JSON array, no additional text.
"""
        return prompt
    
    def _parse_ai_response(self, response_text):
        """
        Parse Gemini's response and extract suggestions
        """
        try:
            # Try to parse as JSON
            # Remove markdown code blocks if present
            cleaned = response_text.strip()
            if cleaned.startswith('```'):
                cleaned = cleaned.split('```')[1]
                if cleaned.startswith('json'):
                    cleaned = cleaned[4:]
            
            suggestions = json.loads(cleaned.strip())
            
            # Ensure we have exactly 5 suggestions
            if isinstance(suggestions, list):
                return suggestions[:5] if len(suggestions) >= 5 else suggestions
            
            return []
            
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract bullet points
            lines = response_text.strip().split('\n')
            suggestions = []
            
            for line in lines:
                line = line.strip()
                # Remove common prefixes
                line = line.lstrip('•-*123456789. ')
                if line and len(line) > 20:  # Meaningful suggestion
                    suggestions.append(line)
            
            return suggestions[:5]
    
    def _get_fallback_suggestions(self, ats_score, sections):
        """
        Provide rule-based suggestions when AI is unavailable
        """
        suggestions = []
        
        # Score-based suggestions
        if ats_score < 50:
            suggestions.append(
                "Add more industry-specific keywords and technical skills relevant to your target role"
            )
            suggestions.append(
                "Use strong action verbs (developed, implemented, optimized) to describe your achievements"
            )
        
        # Section-based suggestions
        if not sections.get('skills'):
            suggestions.append(
                "Add a dedicated Skills section listing your technical and soft skills"
            )
        
        if not sections.get('summary'):
            suggestions.append(
                "Include a professional summary at the top highlighting your key qualifications"
            )
        
        if not sections.get('projects'):
            suggestions.append(
                "Add a Projects section to showcase your practical experience and portfolio"
            )
        
        # Generic best practices
        if len(suggestions) < 5:
            generic = [
                "Include quantifiable achievements with specific metrics (e.g., 'increased efficiency by 30%')",
                "Ensure consistent formatting with clear section headers and bullet points throughout",
                "Tailor your resume keywords to match the job description you're targeting",
                "Keep resume length to 1-2 pages and avoid dense paragraphs",
                "Add relevant certifications or online courses to demonstrate continuous learning"
            ]
            
            for suggestion in generic:
                if len(suggestions) >= 5:
                    break
                if suggestion not in suggestions:
                    suggestions.append(suggestion)
        
        return {'suggestions': suggestions[:5]}

"""
ATS Scoring Service
Calculates ATS score based on keyword matching, section presence, and formatting
"""

import re
from collections import Counter


class ATSScorer:
    """Calculate ATS compatibility score for resumes"""
    
    # Comprehensive ATS keywords database (common across tech, business, and general roles)
    ATS_KEYWORDS = {
        # Technical Skills
        'technical': [
            'python', 'java', 'javascript', 'typescript', 'react', 'angular', 'vue',
            'node.js', 'django', 'flask', 'spring', 'sql', 'nosql', 'mongodb',
            'postgresql', 'mysql', 'aws', 'azure', 'gcp', 'docker', 'kubernetes',
            'ci/cd', 'devops', 'git', 'agile', 'scrum', 'rest api', 'graphql',
            'microservices', 'machine learning', 'ai', 'data science', 'tensorflow',
            'pytorch', 'html', 'css', 'sass', 'webpack', 'redux', 'next.js',
            'express.js', 'fastapi', 'redis', 'elasticsearch', 'kafka', 'jenkins'
        ],
        
        # Soft Skills
        'soft_skills': [
            'leadership', 'communication', 'teamwork', 'problem solving',
            'critical thinking', 'analytical', 'collaboration', 'adaptability',
            'time management', 'project management', 'stakeholder management',
            'presentation', 'negotiation', 'conflict resolution', 'mentoring',
            'strategic thinking', 'decision making', 'creativity', 'innovation'
        ],
        
        # Action Verbs (strong indicators of achievement)
        'action_verbs': [
            'developed', 'designed', 'implemented', 'created', 'built', 'launched',
            'managed', 'led', 'achieved', 'improved', 'optimized', 'reduced',
            'increased', 'streamlined', 'automated', 'architected', 'delivered',
            'coordinated', 'executed', 'established', 'transformed', 'scaled'
        ],
        
        # Business & Domain
        'business': [
            'revenue', 'growth', 'roi', 'kpi', 'metrics', 'analytics', 'strategy',
            'operations', 'product', 'customer', 'user experience', 'saas',
            'b2b', 'b2c', 'sales', 'marketing', 'finance', 'consulting'
        ]
    }
    
    # Required sections for good ATS score
    CRITICAL_SECTIONS = ['experience', 'skills', 'education']
    RECOMMENDED_SECTIONS = ['summary', 'projects', 'certifications']
    
    def __init__(self):
        """Initialize ATS scorer with keyword database"""
        # Flatten all keywords for easy matching
        self.all_keywords = []
        for category_keywords in self.ATS_KEYWORDS.values():
            self.all_keywords.extend(category_keywords)
    
    def calculate_score(self, parsed_data):
        """
        Calculate comprehensive ATS score
        
        Args:
            parsed_data: Dictionary with 'text', 'sections', 'word_count'
            
        Returns:
            dict: Score, matched skills, missing skills, and breakdown
        """
        text = parsed_data['text'].lower()
        sections = parsed_data['sections']
        word_count = parsed_data['word_count']
        
        # Initialize scoring components
        scores = {
            'keyword_score': 0,
            'section_score': 0,
            'formatting_score': 0,
            'content_quality_score': 0
        }
        
        # 1. Keyword Matching Score (40% weight)
        keyword_result = self._calculate_keyword_score(text)
        scores['keyword_score'] = keyword_result['score']
        matched_skills = keyword_result['matched']
        
        # 2. Section Presence Score (30% weight)
        scores['section_score'] = self._calculate_section_score(sections)
        
        # 3. Formatting Score (15% weight)
        scores['formatting_score'] = self._calculate_formatting_score(text, word_count)
        
        # 4. Content Quality Score (15% weight)
        scores['content_quality_score'] = self._calculate_content_quality(text)
        
        # Calculate weighted total score
        total_score = (
            scores['keyword_score'] * 0.40 +
            scores['section_score'] * 0.30 +
            scores['formatting_score'] * 0.15 +
            scores['content_quality_score'] * 0.15
        )
        
        # Round to integer
        total_score = round(total_score)
        
        # Identify missing critical skills
        missing_skills = self._identify_missing_skills(text)
        
        return {
            'score': total_score,
            'matched_skills': matched_skills[:15],  # Top 15 matched skills
            'missing_skills': missing_skills[:10],  # Top 10 missing skills
            'breakdown': {
                'keyword_match': round(scores['keyword_score']),
                'section_completeness': round(scores['section_score']),
                'formatting': round(scores['formatting_score']),
                'content_quality': round(scores['content_quality_score'])
            }
        }
    
    def _calculate_keyword_score(self, text):
        """
        Calculate score based on ATS keyword presence
        Returns score out of 100 and list of matched keywords
        """
        matched_keywords = []
        
        for keyword in self.all_keywords:
            # Use word boundaries for accurate matching
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            if re.search(pattern, text):
                matched_keywords.append(keyword)
        
        # Score based on percentage of keywords matched
        # More keywords = better ATS compatibility
        match_percentage = (len(matched_keywords) / len(self.all_keywords)) * 100
        
        # Scale to 0-100 (cap at reasonable threshold)
        # If 30% keywords matched = 100 score (excellent)
        score = min((match_percentage / 30) * 100, 100)
        
        return {
            'score': score,
            'matched': matched_keywords
        }
    
    def _calculate_section_score(self, sections):
        """Calculate score based on presence of important resume sections"""
        score = 0
        
        # Critical sections (60% of section score)
        critical_present = sum(1 for section in self.CRITICAL_SECTIONS if sections.get(section, False))
        critical_score = (critical_present / len(self.CRITICAL_SECTIONS)) * 60
        
        # Recommended sections (40% of section score)
        recommended_present = sum(1 for section in self.RECOMMENDED_SECTIONS if sections.get(section, False))
        recommended_score = (recommended_present / len(self.RECOMMENDED_SECTIONS)) * 40
        
        score = critical_score + recommended_score
        
        return score
    
    def _calculate_formatting_score(self, text, word_count):
        """
        Evaluate formatting quality indicators
        - Appropriate length (300-800 words ideal)
        - Consistent structure
        - No excessive special characters
        """
        score = 0
        
        # Length score (40% of formatting score)
        if 300 <= word_count <= 800:
            length_score = 40
        elif 200 <= word_count < 300 or 800 < word_count <= 1000:
            length_score = 25
        else:
            length_score = 10
        
        score += length_score
        
        # Bullet points usage (30% of formatting score)
        bullet_count = len(re.findall(r'[•\-\*]', text))
        if bullet_count >= 5:
            score += 30
        elif bullet_count >= 2:
            score += 15
        
        # Email presence (15% of formatting score)
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
            score += 15
        
        # Phone number presence (15% of formatting score)
        if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text):
            score += 15
        
        return score
    
    def _calculate_content_quality(self, text):
        """
        Assess content quality based on action verbs and quantifiable achievements
        """
        score = 0
        
        # Action verbs usage (60% of content score)
        action_verb_count = 0
        for verb in self.ATS_KEYWORDS['action_verbs']:
            if re.search(r'\b' + re.escape(verb.lower()) + r'\b', text):
                action_verb_count += 1
        
        # Good: 8+ action verbs
        if action_verb_count >= 8:
            score += 60
        elif action_verb_count >= 5:
            score += 40
        elif action_verb_count >= 2:
            score += 20
        
        # Quantifiable metrics (40% of content score)
        # Look for numbers followed by % or numbers in context
        metrics_count = len(re.findall(r'\d+%|\d+\+', text))
        
        if metrics_count >= 3:
            score += 40
        elif metrics_count >= 1:
            score += 20
        
        return score
    
    def _identify_missing_skills(self, text):
        """Identify high-value skills that are missing from resume"""
        missing = []
        
        # Focus on most common/valuable technical and soft skills
        priority_skills = (
            self.ATS_KEYWORDS['technical'][:20] +
            self.ATS_KEYWORDS['soft_skills'][:10]
        )
        
        for skill in priority_skills:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if not re.search(pattern, text):
                missing.append(skill)
        
        return missing

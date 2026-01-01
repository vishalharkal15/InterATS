import { useEffect, useState } from 'react'
import ScoreCircle from './ScoreCircle'

export default function ResultsSection({ results, onReset }) {
  const [animateScore, setAnimateScore] = useState(false)

  useEffect(() => {
    // Trigger score animation after component mounts
    setTimeout(() => setAnimateScore(true), 100)
  }, [])

  // Determine score color and message
  const getScoreInfo = (score) => {
    if (score >= 80) {
      return { 
        color: 'text-green-600', 
        bgColor: 'bg-green-50',
        borderColor: 'border-green-200',
        message: 'Excellent! Your resume is highly ATS-compatible.',
        icon: '🎉'
      }
    } else if (score >= 60) {
      return { 
        color: 'text-blue-600', 
        bgColor: 'bg-blue-50',
        borderColor: 'border-blue-200',
        message: 'Good! Some improvements can make it even better.',
        icon: '👍'
      }
    } else if (score >= 40) {
      return { 
        color: 'text-yellow-600', 
        bgColor: 'bg-yellow-50',
        borderColor: 'border-yellow-200',
        message: 'Fair. Follow our suggestions to improve significantly.',
        icon: '⚠️'
      }
    } else {
      return { 
        color: 'text-red-600', 
        bgColor: 'bg-red-50',
        borderColor: 'border-red-200',
        message: 'Needs work. Your resume needs significant improvements.',
        icon: '❌'
      }
    }
  }

  const scoreInfo = getScoreInfo(results.ats_score)

  return (
    <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="animate-fadeIn">
        {/* Header with reset button */}
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900">
            Your ATS Analysis
          </h2>
          <button
            onClick={onReset}
            className="inline-flex items-center px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium transition-all"
          >
            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
            Analyze Another Resume
          </button>
        </div>

        {/* Score card */}
        <div className={`${scoreInfo.bgColor} border-2 ${scoreInfo.borderColor} rounded-2xl p-8 mb-8 animate-slideUp`}>
          <div className="flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-4xl">{scoreInfo.icon}</span>
                <div>
                  <h3 className={`text-2xl font-bold ${scoreInfo.color}`}>
                    ATS Score: {results.ats_score}/100
                  </h3>
                  <p className="text-gray-700 mt-1">{scoreInfo.message}</p>
                </div>
              </div>

              {/* Score breakdown */}
              <div className="grid grid-cols-2 gap-4 mt-6">
                <div>
                  <p className="text-sm text-gray-600 mb-1">Keyword Match</p>
                  <div className="flex items-center">
                    <div className="flex-1 bg-gray-200 rounded-full h-2 mr-3">
                      <div 
                        className="bg-blue-600 h-2 rounded-full transition-all duration-1000"
                        style={{ width: animateScore ? `${results.score_breakdown?.keyword_match || 0}%` : '0%' }}
                      ></div>
                    </div>
                    <span className="text-sm font-semibold text-gray-700">
                      {results.score_breakdown?.keyword_match || 0}%
                    </span>
                  </div>
                </div>
                
                <div>
                  <p className="text-sm text-gray-600 mb-1">Section Completeness</p>
                  <div className="flex items-center">
                    <div className="flex-1 bg-gray-200 rounded-full h-2 mr-3">
                      <div 
                        className="bg-green-600 h-2 rounded-full transition-all duration-1000"
                        style={{ width: animateScore ? `${results.score_breakdown?.section_completeness || 0}%` : '0%' }}
                      ></div>
                    </div>
                    <span className="text-sm font-semibold text-gray-700">
                      {results.score_breakdown?.section_completeness || 0}%
                    </span>
                  </div>
                </div>
                
                <div>
                  <p className="text-sm text-gray-600 mb-1">Formatting</p>
                  <div className="flex items-center">
                    <div className="flex-1 bg-gray-200 rounded-full h-2 mr-3">
                      <div 
                        className="bg-purple-600 h-2 rounded-full transition-all duration-1000"
                        style={{ width: animateScore ? `${results.score_breakdown?.formatting || 0}%` : '0%' }}
                      ></div>
                    </div>
                    <span className="text-sm font-semibold text-gray-700">
                      {results.score_breakdown?.formatting || 0}%
                    </span>
                  </div>
                </div>
                
                <div>
                  <p className="text-sm text-gray-600 mb-1">Content Quality</p>
                  <div className="flex items-center">
                    <div className="flex-1 bg-gray-200 rounded-full h-2 mr-3">
                      <div 
                        className="bg-orange-600 h-2 rounded-full transition-all duration-1000"
                        style={{ width: animateScore ? `${results.score_breakdown?.content_quality || 0}%` : '0%' }}
                      ></div>
                    </div>
                    <span className="text-sm font-semibold text-gray-700">
                      {results.score_breakdown?.content_quality || 0}%
                    </span>
                  </div>
                </div>
              </div>
            </div>

            {/* Animated score circle */}
            <div className="flex-shrink-0">
              <ScoreCircle score={results.ats_score} animate={animateScore} />
            </div>
          </div>
        </div>

        {/* Details grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Matched Skills */}
          <div className="bg-white rounded-xl shadow-lg p-6 animate-slideUp" style={{ animationDelay: '0.1s' }}>
            <div className="flex items-center mb-4">
              <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-gray-900">
                Matched Skills ({results.matched_skills?.length || 0})
              </h3>
            </div>
            
            <div className="flex flex-wrap gap-2">
              {results.matched_skills && results.matched_skills.length > 0 ? (
                results.matched_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="px-3 py-1 bg-green-50 text-green-700 rounded-full text-sm font-medium border border-green-200"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500">No skills detected</p>
              )}
            </div>
          </div>

          {/* Missing Skills */}
          <div className="bg-white rounded-xl shadow-lg p-6 animate-slideUp" style={{ animationDelay: '0.2s' }}>
            <div className="flex items-center mb-4">
              <div className="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-gray-900">
                Missing Skills ({results.missing_skills?.length || 0})
              </h3>
            </div>
            
            <div className="flex flex-wrap gap-2">
              {results.missing_skills && results.missing_skills.length > 0 ? (
                results.missing_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="px-3 py-1 bg-orange-50 text-orange-700 rounded-full text-sm font-medium border border-orange-200"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500">All common skills covered!</p>
              )}
            </div>
          </div>
        </div>

        {/* AI Suggestions */}
        <div className="bg-gradient-to-br from-blue-600 to-blue-500 rounded-xl shadow-lg p-8 mt-8 text-white animate-slideUp" style={{ animationDelay: '0.3s' }}>
          <div className="flex items-center mb-6">
            <div className="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-lg flex items-center justify-center mr-4">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <div>
              <h3 className="text-2xl font-bold">AI-Powered Suggestions</h3>
              <p className="text-blue-100 mt-1">Personalized recommendations to improve your resume</p>
            </div>
          </div>
          
          <div className="space-y-4">
            {results.suggestions && results.suggestions.length > 0 ? (
              results.suggestions.map((suggestion, index) => (
                <div
                  key={index}
                  className="bg-white/10 backdrop-blur-sm rounded-lg p-4 border border-white/20"
                >
                  <div className="flex items-start">
                    <span className="flex-shrink-0 w-6 h-6 bg-white/20 rounded-full flex items-center justify-center mr-3 mt-0.5 font-semibold text-sm">
                      {index + 1}
                    </span>
                    <p className="text-white leading-relaxed">{suggestion}</p>
                  </div>
                </div>
              ))
            ) : (
              <p className="text-blue-100">No suggestions available at this time.</p>
            )}
          </div>
        </div>

        {/* Sections detected */}
        {results.sections_detected && (
          <div className="bg-white rounded-xl shadow-lg p-6 mt-8 animate-slideUp" style={{ animationDelay: '0.4s' }}>
            <h3 className="text-xl font-bold text-gray-900 mb-4">Resume Sections Detected</h3>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {Object.entries(results.sections_detected).map(([section, detected]) => (
                <div
                  key={section}
                  className={`flex items-center p-3 rounded-lg ${
                    detected ? 'bg-green-50 border border-green-200' : 'bg-gray-50 border border-gray-200'
                  }`}
                >
                  {detected ? (
                    <svg className="w-5 h-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                  ) : (
                    <svg className="w-5 h-5 text-gray-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  )}
                  <span className={`text-sm font-medium capitalize ${detected ? 'text-green-700' : 'text-gray-500'}`}>
                    {section}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  )
}

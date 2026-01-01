import { useEffect, useState } from 'react'

export default function ScoreCircle({ score, animate }) {
  const [displayScore, setDisplayScore] = useState(0)
  
  // Animated counter
  useEffect(() => {
    if (animate) {
      let start = 0
      const end = score
      const duration = 2000 // 2 seconds
      const increment = end / (duration / 16) // 60fps
      
      const timer = setInterval(() => {
        start += increment
        if (start >= end) {
          setDisplayScore(end)
          clearInterval(timer)
        } else {
          setDisplayScore(Math.floor(start))
        }
      }, 16)
      
      return () => clearInterval(timer)
    }
  }, [score, animate])

  // Calculate circle parameters
  const radius = 70
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (displayScore / 100) * circumference

  // Determine color based on score
  const getColor = (score) => {
    if (score >= 80) return '#10b981' // green
    if (score >= 60) return '#3b82f6' // blue
    if (score >= 40) return '#f59e0b' // yellow
    return '#ef4444' // red
  }

  return (
    <div className="relative w-48 h-48">
      {/* Background circle */}
      <svg className="transform -rotate-90 w-48 h-48">
        <circle
          cx="96"
          cy="96"
          r={radius}
          stroke="#e5e7eb"
          strokeWidth="12"
          fill="none"
        />
        {/* Progress circle */}
        <circle
          cx="96"
          cy="96"
          r={radius}
          stroke={getColor(displayScore)}
          strokeWidth="12"
          fill="none"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          className="transition-all duration-1000 ease-out"
        />
      </svg>
      
      {/* Score text */}
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="text-5xl font-bold" style={{ color: getColor(displayScore) }}>
          {displayScore}
        </span>
        <span className="text-gray-500 text-sm font-medium">/ 100</span>
      </div>
    </div>
  )
}

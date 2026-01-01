import { useState } from 'react'
import Header from './components/Header'
import Hero from './components/Hero'
import UploadSection from './components/UploadSection'
import ResultsSection from './components/ResultsSection'
import Footer from './components/Footer'

function App() {
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100">
      <Header />
      
      <main>
        {!results ? (
          <>
            <Hero />
            <UploadSection 
              setResults={setResults} 
              setLoading={setLoading}
              loading={loading}
            />
          </>
        ) : (
          <ResultsSection 
            results={results} 
            onReset={() => setResults(null)} 
          />
        )}
      </main>
      
      <Footer />
    </div>
  )
}

export default App

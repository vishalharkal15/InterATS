export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-white border-t border-gray-200 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Brand */}
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-blue-400 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold">I</span>
              </div>
              <span className="text-xl font-bold text-gray-900">InterATS</span>
            </div>
            <p className="text-gray-600 text-sm">
              AI-powered resume ATS checker to help you land your dream job.
            </p>
          </div>

          {/* How it works */}
          <div id="how-it-works">
            <h3 className="font-semibold text-gray-900 mb-4">How It Works</h3>
            <ul className="space-y-2 text-sm text-gray-600">
              <li>1. Upload your resume (PDF or DOCX)</li>
              <li>2. Get instant ATS score and analysis</li>
              <li>3. Review AI-powered suggestions</li>
              <li>4. Improve and reupload</li>
            </ul>
          </div>

          {/* Info */}
          <div>
            <h3 className="font-semibold text-gray-900 mb-4">About</h3>
            <p className="text-sm text-gray-600 mb-3">
              InterATS uses advanced AI to analyze your resume's compatibility with Applicant Tracking Systems used by recruiters worldwide.
            </p>
            <p className="text-xs text-gray-500">
              100% Free • No signup required • Privacy focused
            </p>
          </div>
        </div>

        <div className="border-t border-gray-200 mt-8 pt-8 text-center">
          <p className="text-sm text-gray-500">
            © {currentYear} InterATS. Built with ❤️ by{' '}
            <a 
              href="https://vishalharkal.me/" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-700 font-medium hover:underline"
            >
              @vishalharkal
            </a>
          </p>
        </div>
      </div>
    </footer>
  )
}

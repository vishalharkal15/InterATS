import axios from 'axios'

// API base URL - can be configured via environment variable
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

/**
 * Upload and analyze resume file
 * @param {File} file - Resume file (PDF or DOCX)
 * @returns {Promise} - Analysis results
 */
export const analyzeResume = async (file) => {
  const formData = new FormData()
  formData.append('resume', file)

  try {
    const response = await axios.post(`${API_BASE_URL}/api/analyze-resume`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      timeout: 30000, // 30 second timeout
    })

    return response.data
  } catch (error) {
    if (error.response) {
      // Server responded with error
      throw new Error(error.response.data.error || 'Failed to analyze resume')
    } else if (error.request) {
      // Request made but no response
      throw new Error('Server is not responding. Please try again later.')
    } else {
      // Other errors
      throw new Error('Failed to upload resume. Please try again.')
    }
  }
}

/**
 * Check API health status
 * @returns {Promise} - Health status
 */
export const checkHealth = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health`, {
      timeout: 5000,
    })
    return response.data
  } catch (error) {
    throw new Error('API is not available')
  }
}

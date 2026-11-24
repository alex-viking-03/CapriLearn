import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import RegistrationPage from './pages/RegistrationPage/RegistrationPage'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
      <RegistrationPage />
  </StrictMode>,
)

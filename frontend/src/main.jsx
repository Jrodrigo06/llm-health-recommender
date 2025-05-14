import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import AboutPage from './pages/AboutPage.jsx'
import LoginPage from './pages/LoginPage.jsx'
import SignupPage from './pages/SignupPage.jsx'
import PromptingPage from './pages/PromptingPage.jsx'
import NotFoundPage from './pages/NotFoundPage.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Navbar from './components/Navbar.jsx'

const router = createBrowserRouter([
  {path: '/', element: <App />},
  {path: '/about', element: <AboutPage />},
  {path: '/login', element: <LoginPage />},
  {path: '/signup', element: <SignupPage />},
  {path: '/ask', element: <PromptingPage />},
  {path: "*", element: <NotFoundPage />},

]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Navbar />
    <RouterProvider router={router} />
  </StrictMode>,
)

// App.jsx
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { useEffect, useRef } from 'react';
import Navbar      from './components/Navbar.jsx';
import HomePage    from './pages/HomePage.jsx';
import AboutPage   from './pages/AboutPage.jsx';
import GetHistory  from './pages/GetHistoryPage.jsx';
import Prompting   from './pages/PromptingPage.jsx';
import NotFound    from './pages/NotFoundPage.jsx';
import Login_SignUpPage from './pages/Login_SignUpPage.jsx';
import SignUpPage from './pages/SignUpPage.jsx';
import * as THREE from 'three'
window.THREE = THREE
import CELLS from 'vanta/dist/vanta.cells.min';
import './App.css';

const router = createBrowserRouter([
  { path: '/',      element: <HomePage />    },
  { path: '/about', element: <AboutPage />   },
  { path: '/ask',   element: <Prompting />   },
  { path: '*',      element: <NotFound />    },
  {path: '/history', element: <GetHistory />},
  {path: '/login', element: <Login_SignUpPage />},
  {path: '/signup', element: <SignUpPage />},
]);

export default function App() {

  useEffect(() => {
    CELLS({
      el: '#vanta',
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 3.00,
      color1: 0x0,
      color2: 0x390303,
      size: 1.90,
      speed: 0.80
    })
  }, [])

  return (
    <>
      
      <div className="fixed inset-0 -z-10" id="vanta"></div>
      <div className='relative z-10'> 
        <Navbar />
          <div className="app-content">
            <RouterProvider router={router} />
          </div>
      </div>
    </>
  );
}

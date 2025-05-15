// App.jsx
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Navbar      from './components/Navbar.jsx';
import HomePage    from './pages/HomePage.jsx';
import AboutPage   from './pages/AboutPage.jsx';
import GetHistory  from './pages/GetHistoryPage.jsx';
import Prompting   from './pages/PromptingPage.jsx';
import NotFound    from './pages/NotFoundPage.jsx';
import './App.css';

const router = createBrowserRouter([
  { path: '/',      element: <HomePage />    },
  { path: '/about', element: <AboutPage />   },
  { path: '/ask',   element: <Prompting />   },
  { path: '*',      element: <NotFound />    },
  {path: '/history', element: <GetHistory />},
]);

export default function App() {
  return (
    <>
      <Navbar />
      <div className="app-content">
        <RouterProvider router={router} />
      </div>
    </>
  );
}

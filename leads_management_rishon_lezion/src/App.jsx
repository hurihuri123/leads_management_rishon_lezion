import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout/Layout'
import Home from './pages/Home'
import LeadsPage from './pages/LeadsPage'
import CandidatesPage from './pages/CandidatesPage'
import DashboardPage from './pages/DashboardPage'
import './index.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="leads" element={<LeadsPage />} />
          <Route path="candidates" element={<CandidatesPage />} />
          <Route path="dashboard" element={<DashboardPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
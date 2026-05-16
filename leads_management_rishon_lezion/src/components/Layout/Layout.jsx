import { Outlet } from 'react-router-dom'
import Header from './Header'
import Sidebar from './Sidebar'

export default function Layout() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Header />
      <div style={{ display: 'flex', flex: 1, marginTop: '64px' }}>
        <Sidebar />
        <main style={{ flex: 1, padding: '24px', backgroundColor: 'var(--background)' }}>
          <Outlet />
        </main>
      </div>
    </div>
  )
}
import { NavLink } from 'react-router-dom'

const menuItems = [
  { path: '/dashboard', label: 'לוח בקרה', icon: '🏠' },
  { path: '/leads', label: 'הפניות שלי', icon: '📋' },
  { path: '/candidates', label: 'מועמדים', icon: '👤' },
]

export default function Sidebar() {
  return (
    <aside style={{
      width: '240px', backgroundColor: 'white',
      borderLeft: '1px solid var(--border)',
      padding: '16px', display: 'flex', flexDirection: 'column',
      gap: '8px', minHeight: '100%'
    }}>
      {menuItems.map(item => (
        <NavLink
          key={item.path}
          to={item.path}
          style={({ isActive }) => ({
            display: 'flex', alignItems: 'center', gap: '10px',
            padding: '10px 14px', borderRadius: '8px',
            textDecoration: 'none', fontWeight: '500', fontSize: '15px',
            backgroundColor: isActive ? 'var(--primary)' : 'transparent',
            color: isActive ? 'white' : 'var(--text-primary)',
            transition: 'var(--transition)'
          })}
        >
          <span>{item.icon}</span>
          <span>{item.label}</span>
        </NavLink>
      ))}
    </aside>
  )
}
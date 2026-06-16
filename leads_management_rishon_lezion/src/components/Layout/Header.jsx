export default function Header() {
  return (
    <header style={{
      position: 'fixed', top: 0, right: 0, left: 0,
      height: '64px', backgroundColor: 'var(--primary)',
      display: 'flex', alignItems: 'center',
      justifyContent: 'space-between', padding: '0 24px',
      boxShadow: 'var(--shadow-md)', zIndex: 100
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <div style={{
          width: '40px', height: '40px', backgroundColor: 'var(--secondary)',
          borderRadius: '8px', display: 'flex', alignItems: 'center',
          justifyContent: 'center', color: 'white', fontWeight: 'bold'
        }}>ר</div>
        <div>
          <div style={{ color: 'white', fontWeight: 'bold', fontSize: '16px' }}>
            עיריית ראשון לציון
          </div>
          <div style={{ color: '#ccc', fontSize: '12px' }}>
            מערכת ניהול מועמדים
          </div>
        </div>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <span style={{ color: 'white', fontSize: '14px' }}>שלום, משתמש</span>
        <button style={{
          backgroundColor: 'var(--secondary)', color: 'white',
          border: 'none', borderRadius: '6px', padding: '6px 12px',
          cursor: 'pointer', fontFamily: 'inherit'
        }}>התנתק</button>
      </div>
    </header>
  )
}
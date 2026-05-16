export default function CandidatesPage() {
  return (
    <div>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '24px', color: 'var(--primary)' }}>
        מועמדים
      </h1>
      <div style={{
        backgroundColor: 'white', borderRadius: '12px',
        padding: '48px', textAlign: 'center',
        boxShadow: 'var(--shadow-sm)', border: '1px solid var(--border)'
      }}>
        <div style={{ fontSize: '48px', marginBottom: '16px' }}>👤</div>
        <p style={{ color: 'var(--text-secondary)', fontSize: '16px' }}>
          רשימת המועמדים תופיע כאן
        </p>
      </div>
    </div>
  )
}
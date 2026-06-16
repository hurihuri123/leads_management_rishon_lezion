export default function DashboardPage() {
  const stats = [
    { label: 'סה״כ פניות', value: '124', color: 'var(--primary)' },
    { label: 'פניות פתוחות', value: '38', color: 'var(--secondary)' },
    { label: 'טופלו השבוע', value: '21', color: '#10b981' },
  ]

  return (
    <div>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '24px', color: 'var(--primary)' }}>
        לוח בקרה
      </h1>
      <div style={{ display: 'flex', gap: '16px' }}>
        {stats.map(stat => (
          <div key={stat.label} style={{
            backgroundColor: 'white', borderRadius: '12px',
            padding: '24px', flex: 1, boxShadow: 'var(--shadow-sm)',
            border: '1px solid var(--border)'
          }}>
            <div style={{ fontSize: '36px', fontWeight: 'bold', color: stat.color }}>
              {stat.value}
            </div>
            <div style={{ color: 'var(--text-secondary)', marginTop: '8px' }}>
              {stat.label}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
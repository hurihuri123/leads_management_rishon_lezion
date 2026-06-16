export default function LeadsPage() {
  const leads = [
    { id: 1, name: 'ישראל ישראלי', status: 'בטיפול', date: '16/05/2026', agent: 'משה כהן' },
    { id: 2, name: 'שרה לוי', status: 'ממתין', date: '15/05/2026', agent: 'דנה אברהם' },
    { id: 3, name: 'דוד מזרחי', status: 'טופל', date: '14/05/2026', agent: 'משה כהן' },
  ]

  const statusColor = (status) => {
    if (status === 'בטיפול') return '#3b82f6'
    if (status === 'ממתין') return '#f59e0b'
    if (status === 'טופל') return '#10b981'
    return '#6b7280'
  }

  return (
    <div>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '24px', color: 'var(--primary)' }}>
        הפניות שלי
      </h1>
      <div style={{ backgroundColor: 'white', borderRadius: '12px', boxShadow: 'var(--shadow-sm)', border: '1px solid var(--border)', overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ backgroundColor: 'var(--background)' }}>
              {['מספר פנייה', 'שם מועמד', 'סטטוס', 'תאריך', 'נציג מטפל'].map(col => (
                <th key={col} style={{ padding: '12px 16px', textAlign: 'right', fontWeight: '600', color: 'var(--text-secondary)', borderBottom: '1px solid var(--border)' }}>
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {leads.map(lead => (
              <tr key={lead.id} style={{ borderBottom: '1px solid var(--border)' }}>
                <td style={{ padding: '12px 16px' }}>#{lead.id}</td>
                <td style={{ padding: '12px 16px', fontWeight: '500' }}>{lead.name}</td>
                <td style={{ padding: '12px 16px' }}>
                  <span style={{
                    backgroundColor: statusColor(lead.status) + '20',
                    color: statusColor(lead.status),
                    padding: '4px 10px', borderRadius: '20px', fontSize: '13px', fontWeight: '500'
                  }}>
                    {lead.status}
                  </span>
                </td>
                <td style={{ padding: '12px 16px', color: 'var(--text-secondary)' }}>{lead.date}</td>
                <td style={{ padding: '12px 16px' }}>{lead.agent}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
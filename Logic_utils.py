import datetime
from notes_manager import add_note, get_notes

def calculate_days_overdue(last_contact_date_str):
    try:
        last_contact = datetime.datetime.strptime(last_contact_date_str, '%Y-%m-%d')
        today = datetime.datetime.now()
        delta = today - last_contact
        return max(0, delta.days)
    except ValueError:
        return 0

def get_dashboard_summary(candidates):
    # מחזיר סיכום כללי של המועמדים לפי סטטוס גיוס
    stats = {
        'total': len(candidates),
        'recruitment_status': {
            'ממתין לטיפול': 0,
            'בתהליך גיוס': 0,
            'הסתיים': 0
        }
    }
    for c in candidates:
        status = c.get('status', '').lower()
        if status == 'new': stats['recruitment_status']['ממתין לטיפול'] += 1
        elif status == 'in_progress': stats['recruitment_status']['בתהליך גיוס'] += 1
        elif status == 'closed': stats['recruitment_status']['הסתיים'] += 1
    return stats

def get_todays_reminders(candidates):
    #reminders for candidates with follow-up date today or earlier
    today = datetime.date.today()
    reminders = []
    for c in candidates:
        followup_str = c.get('next_followup_date', '')
        if not followup_str:
            continue
        try:
            followup_date = datetime.datetime.strptime(followup_str, '%Y-%m-%d').date()
            if followup_date <= today:
                reminders.append(c)
        except ValueError:
            continue
    return reminders

def get_stats_per_agent(candidates):
    stats = {}
    for c in candidates:
        agent = c.get('assigned_to', 'לא משויך')
        stats[agent] = stats.get(agent, 0) + 1
    return stats

from mock_data import candidates

if __name__ == "__main__":
    print("=== סיכום ===")
    print(get_dashboard_summary(candidates))

    print("\n=== תזכורות להיום ===")
    print(get_todays_reminders(candidates))

    print("\n=== פניות לפי נציג ===")
    print(get_stats_per_agent(candidates))

    print("\n=== הערות ===")
    add_note(candidates[0], "דיברתי עם המועמד, מעוניין", "אורי")
    print(get_notes(candidates[0]))
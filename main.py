from fastapi import FastAPI
from Logic_utils import get_dashboard_summary, get_todays_reminders, get_stats_per_agent
from notes_manager import get_notes, add_note
from mock_data import candidates

app = FastAPI()

@app.get('/dashboard')
def dashboard():
    # Returns a summary of the dashboard, including counts of candidates by status, today's reminders, and stats per agent
    return {
        'summary': get_dashboard_summary(candidates),
        'reminders': get_todays_reminders(candidates),
        'stats_per_agent': get_stats_per_agent(candidates)

    }

@app.get('/notes/{candidate_id}')
def get_candidate_notes(candidate_id: int):
    # מחזיר את כל ההערות של מועמד לפי ID
    candidate = next((c for c in candidates if c['id'] == candidate_id), None)
    if not candidate:
        return {'error': 'מועמד לא נמצא'}
    return get_notes(candidate)

@app.post('/notes/{candidate_id}')
def add_candidate_note(candidate_id: int, text: str, agent: str):
    # מוסיף הערה חדשה למועמד לפי ID
    candidate = next((c for c in candidates if c['id'] == candidate_id), None)
    if not candidate:
        return {'error': 'מועמד לא נמצא'}
    return add_note(candidate, text, agent)

    


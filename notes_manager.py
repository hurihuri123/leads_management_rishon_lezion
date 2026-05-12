import datetime

def add_note(candidate, note_text, agent_name):
    # adds a note to the candidate's notes list
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    note = {
        'agent': agent_name,
        'date': today,
        'text': note_text
    }
    candidate['notes'].append(note)
    return candidate

def get_notes(candidate):
    # returns the notes for a candidate, or an empty list if there are none
    return candidate.get('notes', [])
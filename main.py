from flask import Flask, jsonify
from Logic_utils import get_dashboard_summary, get_todays_reminders, get_stats_per_agent, get_notes, add_note
from mock_data import candidates

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/dashboard')
def dashboard():
    # returns a summary of the dashboard, including counts of candidates by status, today's reminders, and stats per agent
    return jsonify({
        'summary': get_dashboard_summary(candidates),
        'reminders': get_todays_reminders(candidates),
        'stats_per_agent': get_stats_per_agent(candidates)
    })

if __name__ == "__main__":
    app.run(debug=True)
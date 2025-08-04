from flask import Flask, jsonify, request
from tracker import start_tracker, activity_log
from datetime import datetime

app = Flask(__name__)

start_tracker()

@app.route('/input-activity', methods=['GET'])
def get_activity_log():
    get_start_time = request.args.get('start')
    get_end_time = request.args.get('end')

    if not get_start_time or not get_end_time:
        return jsonify(activity_log)
    
    start_time = datetime.fromisoformat(get_start_time.replace("Z", "+00:00"))
    end_time = datetime.fromisoformat(get_end_time.replace("Z", "+00:00"))

    filtered_log = []
    for entry in activity_log:
        entry_time = datetime.fromisoformat(entry['timestamp'].replace("Z", "+00:00"))
        if start_time <= entry_time <= end_time:
            filtered_log.append(entry)

    return jsonify(filtered_log)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

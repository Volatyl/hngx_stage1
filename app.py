from flask import Flask, request
import datetime
import pytz

app = Flask(__name__)


@app.route('/api')
def index():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    day = datetime.date.today().strftime('%A')
    time = datetime.datetime.now(pytz.utc)

    result = {
        "slack_name": slack_name,
        "current_day": day,
        "utc_time": time,
        "track": track,
        "github_file_url": "https://github.com/Volatyl/hngx_stage1/blob/main/app.py",
        "github_repo_url": "https://github.com/Volatyl/hngx_stage1",
        "status_code": 200,

    }

    return result


if __name__ == '__main__':
    app.run(debug=True, port=5555)

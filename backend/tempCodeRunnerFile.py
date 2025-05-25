from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# transcribe_script.py

import assemblyai as aai

aai.settings.api_key = "d66f1c636b7e48378e5c89d88b763916"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(r"C:\Users\HP\Videos\Activity.mp4")

    


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message":transcript.text
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

from flask import Flask, jsonify
from flask_cors import CORS
import assemblyai as aai
import os

app = Flask(__name__)
CORS(app)

def get_video_path():
  """Reads and removes the first line from the 'videoPaths.txt' file."""
  try:
    with open('C:/sem 4/HackNUthon 5.0/EduCREST - Copy/react-flask/backend/videoPaths.txt', 'r+') as file:
      lines = file.readlines()
      if not lines:
        return None  # Indicate no video path available

      # Get the path from the first line and remove it
      video_path = lines.pop(0).strip()
      file.seek(0)  # Move file pointer to the beginning
      file.truncate()  # Clear existing content
      file.writelines(lines)  # Write remaining lines
      return video_path
  except FileNotFoundError:
    print("Error: 'videoPaths.txt' file not found.")
    return None

@app.route('/api/data', methods=['GET'])
def get_data():
  video_path = get_video_path()

  if video_path:
    aai.settings.api_key = "f17b24dfa4144309bfc5f77d00b0308a"
    transcriber = aai.Transcriber()

    try:
      transcript = transcriber.transcribe(video_path)
      data = {"message": transcript.text}
      with open("transcript.txt", "w") as file:
        file.write(transcript.text)
      return jsonify(data)
    except Exception as e:
      print(f"Error during transcription: {e}")
      return jsonify({"message": "Error transcribing video."})
  else:
    return jsonify({"message": "No video path found in 'videoPaths.txt'."})

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

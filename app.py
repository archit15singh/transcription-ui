import json
from pathlib import Path
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)



@app.route("/")
def index():
    audio_id = request.args.get('id', default='1', type=str)
    return render_template("index.html", audio_id=audio_id)


@app.route("/get_transcription")
def get_transcription():
    audio_id = request.args.get('id', default='1', type=str)
    json_file_path = (
        Path(__file__).resolve().parent / "static" / "transcriptions" / f"{audio_id}.json"
    )
    try:
        with open(json_file_path, "r") as json_file:
            transcription_data = json.load(json_file)
        return jsonify(transcription_data["transcription"])
    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500


if __name__ == "__main__":
    app.run(debug=True)

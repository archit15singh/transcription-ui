from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_transcription')
def get_transcription():
    transcription_data = [
		{
			"timestamps": {
				"from": "00:00:00,000",
				"to": "00:00:06,000"
			},
			"offsets": {
				"from": 0,
				"to": 6000
			},
			"text": " After affecting electrical repairs, the plane safely took off and continued to Oshkosh."
		}
	]
    return jsonify(transcription_data)

if __name__ == '__main__':
    app.run(debug=True)

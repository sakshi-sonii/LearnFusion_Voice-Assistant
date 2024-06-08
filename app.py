from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice-assistant', methods=['POST'])
def voice_assistant():
    data = request.json
    text = data.get('text')

    # Simulate an AI response (you can integrate any AI model here)
    response_text = f"You said: {text}. This is a simulated AI response."

    # Convert response text to speech
    tts = gTTS(response_text)
    tts.save("static/response.mp3")

    return jsonify({'response': response_text, 'audio_url': '/static/response.mp3'})

if __name__ == '__main__':
    app.run(debug=True)

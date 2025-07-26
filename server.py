from flask import Flask
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detectEmotion():
    if request.method == "POST":
        text = request.form.get("text")
        result = emotion_detector(text)
        if result["dominant_emotion"] == None:
            return "Invalid text! Please try again!"  
        return result

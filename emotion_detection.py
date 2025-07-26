import requests
import json

def emotion_detector(text_to_analyze):
    print("Text to analyze:", text_to_analyze)

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    json_data = {
        "raw_document": { 
            "text": text_to_analyze 
            }
        }
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    print("Sending request...")

    try:
        req = requests.post(url=url, headers=headers, json=json_data, timeout=10)
        response = json.loads(req.text)
        emotions = response["emotionPredictions"][0]["emotion"]
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
        return emotions
    except Exception as e: 
        print("Request failed")
        print(e)

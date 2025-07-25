import requests
import json

def emotion_detector(text_to_analyze):
    print("Text to analyze:", text_to_analyze)
    json_data = {
        "raw_document": { 
            "text": text_to_analyze 
            }
        }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    print("Sending request...")
    try:
        req = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', headers=headers, json=json.dumps(json_data), timeout=10)
        return req.text
    except Exception as e: 
        print("Request failed")
        print(e)

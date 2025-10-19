import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Required headers
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Display the result
    if response.status_code == 200:
        return response.text
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)

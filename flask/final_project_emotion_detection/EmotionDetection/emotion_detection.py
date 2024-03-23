import requests
import json


def emotion_predictor(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response['emotionPredictions']
        emotions = emotion_predictions[0]['emotion']

        dominant_emotion = max(emotions, key=emotions.get)
        return {
            "anger": emotions['anger'],
            "disgust": emotions['disgust'],
            "fear": emotions['fear'],
            "joy": emotions['joy'],
            "sadness": emotions['sadness'],
            "dominant_emotion": dominant_emotion
        }
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

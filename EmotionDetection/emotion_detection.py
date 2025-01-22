import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

        return {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
            # Return a dictionary with None values for a 400 status code
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    else:
        return None

    #from emotion_detection import emotion_detector
    #from EmotionDetection.emotion_detection import emotion_detector
    #emotion_detector("I hate working long hours")
    #emotion_detector("I'm so happy to be doing this")
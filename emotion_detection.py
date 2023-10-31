# import requests, json

# def emotion_detector(text_to_analyse):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     myobj = { "raw_document": { "text": text_to_analyse } }
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     response = requests.post(url, json = myobj, headers=header)
#     return response.text

import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text into a dictionary using the json library functions
    response_dict = json.loads(response.text)
    # Extract the required set of emotions and their scores
    emotions = response_dict['document']['emotion']
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    # Construct the output dictionary
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return output

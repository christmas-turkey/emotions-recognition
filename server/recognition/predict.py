import cv2
import numpy as np
import os
from .ModelService import ModelService
emotions = ['Angry','Disgusted','Fear','Happy','Neutral','Sad','Surprised']
# emotions = ['Злий','З огидою', 'Страх', 'Щасливий', 'Нейтральний', 'Сумний', 'Здивований']

model_service = ModelService()
model_service.load()

def crop_and_predict(image_data):
    # detects face
    nparr = np.frombuffer(image_data, np.uint8)
    facecasc = cv2.CascadeClassifier(os.path.join(os.path.dirname(__file__),"haarcascade_frontalface_default.xml"))
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        # rectangle where face is located
        roi_gray = gray[y:y + h, x:x + w]
        # crop image and resize it to model requirements
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model_service.predict(cropped_img)
        return emotions[np.argmax(prediction)]
        # cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
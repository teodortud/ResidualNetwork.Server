import cv2
import numpy as np


def face_detect_and_crop(imageFile):
    
    frontal_face = 'Services/Face_Detection_Library/haarcascades/haarcascade_frontalface_alt2.xml'

    frontal_face_cascade = cv2.CascadeClassifier(frontal_face)
    
    image = cv2.imread(imageFile)
    image = np.array(image, dtype=np.uint8)

    face_img = image.copy()

    faces = frontal_face_cascade.detectMultiScale(face_img)

    if faces is None:
        print('Failed to detect face!')
        return 0

    for(x, y, w, h) in faces:
        cv2.rectangle(face_img, (x, y), ( x +w, y+ h), (255, 255, 255), 10)

    for (x, y, w, h) in faces:
        r = max(w, h) / 2
        centerX = x + w / 2
        centerY = y + h / 2
        nx = int(centerX - r)
        ny = int(centerY - r)
        nr = int(r * 2)

        faceimg = image[ny:ny + nr, nx:nx + nr]

        lastimg = cv2.resize(faceimg, (224, 224))

        face_img = lastimg

    return face_img

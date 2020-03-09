import cv2
import numpy as np
from Services.FaceDetection import face_detect_and_crop
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf

classifier = load_model('Services/BestModel/Res_Net_Model.hdf5')


def model_predict(imagefile):
    cropped_image = face_detect_and_crop(imagefile)

    cropped_image_resized = cv2.resize(cropped_image, (128, 128))

    test_image = image.img_to_array(cropped_image_resized)

    test_img = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    test_img /= 255

    test_img = np.expand_dims(test_img, axis=2)

    test_img = tf.image.grayscale_to_rgb(tf.convert_to_tensor(test_img))

    test_img = np.expand_dims(test_img, axis=0)

    result = classifier.predict(test_img)

    if result[0][len(result[0][:-1])] > 0.9:
        prediction = 'Is Teodor'
    else:
        prediction = 'Is not Teodor'

    return prediction



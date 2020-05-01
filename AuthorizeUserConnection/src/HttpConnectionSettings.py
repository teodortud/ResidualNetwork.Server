from ctypes import c_byte

import flask
import os
import werkzeug
from Services.NetworkPredicitionSettings import model_predict
from Services.MqttConnectionSettings import mqtt_publish

app = flask.Flask(__name__)


@app.route('/upload-image', methods=['POST'])
def handle_request():
    image_file = flask.request.files['image']

    filename = werkzeug.utils.secure_filename(image_file.filename)

    filename_path = os.path.abspath(filename)

    image_file.save(filename)

    image = filename_path

    result = model_predict(image)

    os.remove(filename_path)

    mqtt_publish(result)

    return result


app.run(host="0.0.0.0", port=8080, debug=True)

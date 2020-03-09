from ctypes import c_byte

import flask
import os
import werkzeug
from Services.NetworkPredicitionSettings import model_predict

app = flask.Flask(__name__)


@app.route('/upload-image', methods=['POST'])
def handle_request():
    imagefile = flask.request.files['image']

    filename = werkzeug.utils.secure_filename(imagefile.filename)

    filename_path = os.path.abspath(filename)

    imagefile.save(filename)

    image = filename_path

    result = model_predict(image)

    os.remove(filename_path)

    return result


app.run(host="0.0.0.0", port=8080, debug=True)

from flask import Blueprint, jsonify, request, abort
import uuid
import os
from os import path
from os import listdir
from os.path import isfile, join
import numpy as np
import routes.image.utils.waste_detector as wd
image_service = Blueprint('image_service', __name__)



@image_service.route('/test')
def index():
    return jsonify({'status': 'Ok',
                    'image': {
                        "isWaste": True,
                        "labels": ['metal', 'plastic']
                    }})


@image_service.route('/analyze', methods=['POST'])
def analyze_image():
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    try:
        if not request.files:
            abort(400)
        if request.files.get('file') == None or request.files.get('file').filename == '':
            error = 'No file selected for uploading'
            return jsonify({"message": error}), 400

        file = request.files['file']

        if('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS):
            error = 'Allowed file types are png, jpg, jpeg, gif'
            return jsonify({"message": error}), 400

        filename = str(uuid.uuid4()) + '.' + \
            file.filename.rsplit('.', 1)[1].lower()

        # path = os.path.join(os.getcwd(), 'static', 'images',  filename)
        # file.save(path)
    
        resp = wd.sortingWaste(file)
        print(resp)
        return jsonify(resp), 201
    except NameError:
        return jsonify({"message": NameError}), 400


@image_service.route('/', methods=['GET'])
def list_images():
    myPath = os.path.join(os.getcwd(), 'static', 'images')
    onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return jsonify({"data": onlyfiles})

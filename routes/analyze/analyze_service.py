from flask import Blueprint, jsonify, request, abort
import uuid
import os
from os import path
from os import listdir
from os.path import isfile, join
import numpy as np
import routes.analyze.controllers.waste_detector as wd
analyze_service = Blueprint('analyze_service', __name__)


@analyze_service.route('/test')
def index():
    return jsonify({'status': 'Ok',
                    'image': {
                        "isWaste": True,
                        "labels": ['metal', 'plastic']
                    }})


@analyze_service.route('/waste', methods=['POST'])
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

        resp = wd.sortingWaste(file)
        print(resp)
        return jsonify(resp), 201
    except NameError:
        return jsonify({"message": NameError}), 400

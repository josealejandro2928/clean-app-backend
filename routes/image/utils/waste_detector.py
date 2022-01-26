import numpy as np
import random
from PIL import Image
from numpy import asarray

from models.ML_Model import ML_Model

def sortingWaste(file):
    img = Image.open(file.stream)
    numpydata = asarray(img)
    
    fake_labels = ["plastic", "metal", "toxic",
                   "battery", "glass", "organic", "paper", "furniture", "chemical"]

    model = ML_Model.getInstance()   

    result_predict = model.test_predict()
    
    # print(result_predict)
    
    response = {
        "trash": {
            "accuracy": random.random()*100
        },
        "suggested_labels": random_from_array(fake_labels, random.randint(0, len(fake_labels)-1)),
        "image": {
            "width": numpydata.shape[1],
            "height": numpydata.shape[0]
        },
        "predictor":[]
    }
    return response


def random_from_array(array, size=4):
    cache = {}
    c = 0
    result = []
    while c < size:
        index = random.randint(0, len(array)-1)
        if cache.get(array[index]) == None:
            cache[array[index]] = True
            c += 1
            result.append(array[index])
    return result

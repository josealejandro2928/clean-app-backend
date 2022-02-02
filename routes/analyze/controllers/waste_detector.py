import numpy as np
import random
from PIL import Image
from numpy import asarray

from models.MLWasteClassifier import MLWasteClassifier


def sortingWaste(file):
    img = Image.open(file.stream)
    numpydata = asarray(img)
    model = MLWasteClassifier.getInstance()
    result_predict = model.predict(numpydata)

    return result_predict


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

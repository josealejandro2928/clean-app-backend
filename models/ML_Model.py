
from models.Singleton import Singleton
from keras.models import load_model
import numpy as np
import os
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import tensorflow.compat.v1.keras.backend as K
tf.compat.v1.disable_eager_execution()

class ML_Model(Singleton):
    
    def __init__(self):
        super().__init__()
        self.model = None
        self.graph = None
        self.load_model()
        print(self.model.summary())
    
    def load_model(self):
        self.graph = tf.compat.v1.get_default_graph()
        print("\n\n\n\n*************GRAPH OBJECT IN INIT**************************: ", self.graph,"\n\n\n\n")
        self.model = load_model("./config/mymodel.h5",custom_objects={"KerasLayer": hub.KerasLayer})
        
    def test_predict(self):
        labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
        test_x = np.load("./config/test_x.npy")
        test_y = np.load("./config/test_y.npy")
        # prediction = self.model.predict(test_x)
        with self.graph.as_default():
            print("\n\n\n\n*************GRAPH OBJECT IN PREDICTION**************************: ", self.graph,"\n\n\n\n")     
            prediction = self.model.predict(test_x)
        return prediction
    
    def predict(self, input_img):
        nim = image.smart_resize(input_img, (224,224))
        nim = (1./255) * nim
        test_i = nim.reshape(1,224,224,3)
        return self.model.predict(test_i)


if __name__ == "__main__":
    mod = ML_Model()
    print(mod.model.predict_generator)
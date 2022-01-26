
# import tensorflow.compat.v1.keras.backend as K
from keras.preprocessing import image
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from models.Singleton import Singleton
from keras.models import load_model
import numpy as np
import os
import math
import tensorflow_hub as hub
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from keras import backend as K
# tf.enable_eager_execution()
# tf.compat.v1.disable_eager_execution()


class ML_Model(Singleton):

    def __init__(self):
        super().__init__()
        self.model = None
        self.session = None
        self.load_model()
        print(self.model.summary())
        self.confidence_threshold = .33
        self.labels = {0: 'cardboard', 1: 'glass', 2: 'metal',
            3: 'paper', 4: 'plastic', 5: 'trash'} 

    def load_model(self):
        config = tf.ConfigProto(
            intra_op_parallelism_threads=1,
            allow_soft_placement=True
        )
        self.session = tf.Session(config=config)
        K.set_session(self.session)
        print("\n*************SESSION OBJECT IN INIT**************************: ",
              self.session, "\n\n\n\n")
        # self.graph = tf.compat.v1.get_default_graph()
        self.model = load_model("./config/mymodel.h5",
                                custom_objects={"KerasLayer": hub.KerasLayer})
        # self.model._make_predict_function()
        print('***************Model loaded. Start serving...********************')
        
    def predict(self, input_img):
                       
        p_im = Image.fromarray(input_img)
        px = p_im.resize((224,224))
        nim = np.array(px)        
        nim = (1./255) * nim          
        test_i = nim.reshape(1,224,224,3)
        try:
            with self.session.as_default():
                with self.session.graph.as_default():
                    prediction = self.model.predict(test_i)
                    # print("prediction is: ", labels[np.argmax(prediction[0])])
                    # print("prediction is: ", prediction[0])
                    outp = self.compute_output(prediction[0])
                    print("\n\n\nout is : ", outp,'\n\n\n')
                    return outp
        except Exception as ex:
            print(ex)
            return ''        
    
    def compute_output(self, pred):
        """Compute the confidence in the top labels"""
        conf_order = np.argsort(pred*(-1.))
        print(conf_order, pred)
        out = {
            "trash": {
                "accuracy": round(pred[conf_order[0]]*100, 2)
            }                        
        }
        s_l = []
        p_l = {}
        for c in conf_order:
            if pred[c] > self.confidence_threshold:
                s_l.append(self.labels[c])
            p_l[self.labels[c]] = round(pred[c]*100,2)
        out['suggested_labels'] = s_l
        out['predictions'] = p_l
        return out
        
    
    def test_predict(self):
        labels = {0: 'cardboard', 1: 'glass', 2: 'metal',
                  3: 'paper', 4: 'plastic', 5: 'others'}
        test_x = np.load("./config/test_x.npy")
        test_y = np.load("./config/test_y.npy")
        # prediction = self.model.predict(test_x)
        print("\n\n*************SESSION OBJECT IN PREDICTION**************************: ",
              self.session, "\n\n")
        try:
            with self.session.as_default():
                with self.session.graph.as_default():
                    prediction = self.model.predict(test_x)
                    return prediction
        except Exception as ex:
            print(ex)
            return ''

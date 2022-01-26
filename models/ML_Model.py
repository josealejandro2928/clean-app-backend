
# import tensorflow.compat.v1.keras.backend as K
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from models.Singleton import Singleton
from keras.models import load_model
import numpy as np
import os
import tensorflow_hub as hub
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from keras import backend as K
# tf.compat.v1.disable_eager_execution()


class ML_Model(Singleton):

    def __init__(self):
        super().__init__()
        self.model = None
        self.session = None
        self.load_model()
        print(self.model.summary())

    def load_model(self):
        config = tf.ConfigProto(
            intra_op_parallelism_threads=1,
            allow_soft_placement=True
        )
        self.session = tf.Session(config=config)
        K.set_session(self.session)
        print("\n\n\n\n*************SESSION OBJECT IN PREDICTION**************************: ",
              self.session, "\n\n\n\n")
        # self.graph = tf.compat.v1.get_default_graph()
        self.model = load_model("./config/mymodel.h5",
                                custom_objects={"KerasLayer": hub.KerasLayer})
        self.model._make_predict_function()
        print('***************Model loaded. Start serving...********************')

    def test_predict(self):
        labels = {0: 'cardboard', 1: 'glass', 2: 'metal',
                  3: 'paper', 4: 'plastic', 5: 'trash'}
        test_x = np.load("./config/test_x.npy")
        test_y = np.load("./config/test_y.npy")
        # prediction = self.model.predict(test_x)
        print("\n\n\n\n*************SESSION OBJECT IN PREDICTION**************************: ",
              self.session, "\n\n\n\n")
        try:
            with self.session.as_default():
                with self.session.graph.as_default():
                    prediction = self.model.predict(test_x)
                    return prediction
        except Exception as ex:
            print(ex)
            return ''

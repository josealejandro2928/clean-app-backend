# from keras.models import load_model
# import numpy as np
# import os
# import tensorflow_hub as hub
# import tensorflow as tf
# from tensorflow import keras
# from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image
# import tensorflow.compat.v1.keras.backend as K
# tf.compat.v1.disable_eager_execution()

# # URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/2"
# # feature_extractor = hub.KerasLayer(URL,input_shape=(224,224,3))
# # base_dir = '/home/tony/archive/garbage classification/Garbage classification'

# # print(mm.summary())

# # labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
# # test_x = np.load("./config/test_x.npy")
# # test_y = np.load("./config/test_y.npy")
# # prediction = mm.predict(test_x)
# # print(prediction)

# # plt.figure(figsize=(16, 16))
# # for i in range(16):
# #     plt.subplot(4, 4, i+1)
# #     plt.title('pred:%s / truth:%s' % (labels[np.argmax(prediction[i])], labels[np.argmax(test_y[i])]))
# #     plt.imshow(test_x[i])

# # plt.show()


# ML_MODEL = None
# graph = None
# __all__ = [ML_MODEL,graph]


# def get_model():
#     global ML_MODEL
#     if ML_MODEL is None:
#         global graph
#         graph = tf.compat.v1.get_default_graph()
#         print("\n\n\n\nHeeere: ", graph)
#         ML_MODEL = load_model("./config/mymodel.h5",custom_objects={"KerasLayer": hub.KerasLayer})
        
#     return ML_MODEL

        
# def test_predict():
#     labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
#     test_x = np.load("./config/test_x.npy")
#     test_y = np.load("./config/test_y.npy")
#     prediction = ML_MODEL.predict(test_x)
#     # with graph.as_default():     
#     #     prediction = ML_MODEL.predict(test_x)
#     return prediction
    
# def predict():
#     print(ML_MODEL.summary())

from keras.models import load_model
from keras.preprocessing import image
import numpy as np


class BTS_CNN():
    def __init__(self):
        self.model = load_model("./bts_cnn_model.h5")
        self.class_indices = {0:"Jimin", 1: "Jungkook", 2:"V"}

    def predict(self, img=None):
        try:
            self.img = image.img_to_array(img)
            self.img = np.expand_dims(self.img, axis=0)
            result = self.class_indices[np.argmax(self.model.predict(self.img))]

        except:
            raise Exception("img have to be Image by keras.preprocessing.image.load_img")

        return result
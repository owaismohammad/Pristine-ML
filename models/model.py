import tensorflow as tf
import cv2

class Model():
    def __init__(self):
        self.model=tf.keras.models.load_model(r'pristine_improved.h5')

    def image_to_feature_vector(self,image_get, size=(64, 64)):
      # Load the image using OpenCV
      # image = cv2.imread(image)
      # Resize the image to the specified size
      image_rgb = cv2.cvtColor(image_get, cv2.COLOR_BGR2RGB)  
      image = cv2.resize(image_rgb, size)
        
      self.image=image.reshape((1,64,64,3))
      self.image=self.image/255.0

    def image_prediction(self,image):
      pred=self.model.predict(image)
      pred=pred.flatten()
      if pred[0]<=0.5:
        return 0
      else:
        return 1

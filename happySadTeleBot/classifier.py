import cv2
import tensorflow as tf

model = tf.keras.models.load_model("happySad_model.h5")
def classifyImage(img):
    test_img = cv2.imread(img)
    
    # Resizing the image
    resized = tf.image.resize(test_img, (256,256))

    # Actually classifying the image
    yhat = model.predict(tf.expand_dims(resized/255, axis=0))

    if yhat < .5:
        return "This is a happy image"
    if yhat > .5:
        return "This is a sad image"
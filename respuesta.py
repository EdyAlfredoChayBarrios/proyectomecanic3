# import numpy
# import tensorflow as tf
# import keras
# from keras.preprocessing import InceptionV3, decode_prediction
#
# iv3=InceptionV3()
# uploaded=files.upload()
# x=image.img_to_array(image.load_img())


from keras.applications.resnet import ResNet50
#from keras.preprocessing import image
import keras.utils as image
from keras.applications.resnet import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')
img_path = 'Img/espatula.jpeg'

img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])
imagenes=decode_predictions(preds, top=1)[0]
print(imagenes[0][1])

def respuesta(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)

    #print('Predicted:', decode_predictions(preds, top=3)[0])
    imagenes = decode_predictions(preds, top=1)[0]
    return imagenes[0][1]
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings
from tensorflow.python.keras.utils.data_utils import Sequence
warnings.simplefilter(action='ignore', category=FutureWarning)
# %matplotlib inline
from google.colab import drive
drive.mount('/content/gdrive')
test_path = '/content/gdrive/MyDrive/KNEE DATASET /archive/test'
valid_path = '/content/gdrive/MyDrive/KNEE DATASET /archive/val'
train_path = '/content/gdrive/MyDrive/KNEE DATASET /archive/train'
#Data generator

train_datagen = ImageDataGenerator(
      rescale=1./225,
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

test_datagen = ImageDataGenerator(rescale=1./255)


train_batches = train_datagen.flow_from_directory(
        train_path,
        target_size=(224, 224),
        batch_size=10,
        class_mode='categorical')

validation_batch =test_datagen.flow_from_directory(
             valid_path,
             target_size=(224, 224),
             batch_size=10,
             class_mode='categorical')

test_batch = test_datagen.flow_from_directory(
       test_path,
       target_size=(224, 224),
       batch_size=10,
       shuffle=False,

class_mode='categorical')
imgs, labels = next(train_batches)
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20,20))
    axes=axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()
    plotImages(imgs)
print(labels)
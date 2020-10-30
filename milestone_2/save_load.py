from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from keras.models import load_model

# Save fitted model as .h5-file
def saveModel(model,filename):
	model.save(str(filename))


# Load the model as .h5-file
def loadModel(filename):
	model = load_model(str(filename))
	return model


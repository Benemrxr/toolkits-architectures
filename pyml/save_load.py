from __future__ import print_function

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model

# Save fitted model as .h5-file
def save_model(model,filename):
	model.save(str(filename))


# Load the model as .h5-file
def load_model_file(filename):
	model = load_model(str(filename))
	return model


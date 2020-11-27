from __future__ import print_function

import sys
import logging
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class MlModel():

	def __init__(self, filepath):
		self.filepath = filepath

		self.num_words = 5000
		self.max_len = 400

		self.data = None
		self.model = None

	# Save the model as .h5-file
	def save_model(self, filepath=None, model=None):
		filepath = filepath or self.filepath
		model = model or self.model

		try:
			model.save(str(filepath))
			logging.info("Successfully saved the model!")
			return filepath
		except Exception:
			raise
			logging.error("Could not save the model!")
			return False

	# Load the model from .h5-file
	def load_model(self, filepath=None):
		filepath = filepath or self.filepath

		try:
			self.model = load_model(str(filepath))
			logging.info("Successfully loaded the model!")
			return self.model
		except Exception:
			logging.error("Could not load the model!")
			return None

	def load_sample_imdb_data(self, end, start=0):
		logging.info('Loading sample IMDB data...')
		(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=self.num_words)
		
		padded = sequence.pad_sequences(x_test, maxlen=self.max_len)

		# Gives us a testsample with 50 Reviews
		samples = padded[start:end]
		return samples


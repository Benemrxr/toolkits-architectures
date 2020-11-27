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

		self.max_features = 5000
		self.max_len = 400
		self.batch_size = 32
		self.embedding_dims = 50
		self.filters = 250
		self.kernel_size = 3
		self.hidden_dims = 250
		self.epochs = 2

		self.data = None
		self.model = None

	def load_imdb_data(self):
		logging.info('Loading data...')
		(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=self.max_features)

		logging.info('%d train sequences' % (len(x_train)) )
		logging.info('%d test sequences' % (len(x_test)) )


		logging.info('Pad sequences (samples x time)')
		x_train = sequence.pad_sequences(x_train, maxlen=self.max_len)
		x_test = sequence.pad_sequences(x_test, maxlen=self.max_len)

		logging.info('x_train shape: (%d, %d)' % (x_train.shape) )
		logging.info('x_test shape: (%d, %d)' % (x_test.shape) )

		self.data = ( (x_train, y_train), (x_test, y_test) )
		return self.data

	def build_model(self, data=None):
		logging.info('Building model...')
		self.model = Sequential()

		modeldata = data or self.data

		self.model.add(Embedding(self.max_features,
	                    	     self.embedding_dims,
	                             input_length=self.max_len))

		self.model.add(Dropout(0.2))

		self.model.add(Conv1D(self.filters,
	                 	      self.kernel_size,
	                 	      padding='valid',
	                 	      activation='relu',
	                 	      strides=1))

		self.model.add(GlobalMaxPooling1D())

		self.model.add(Dense(self.hidden_dims))
		self.model.add(Dropout(0.2))
		self.model.add(Activation('relu'))

		self.model.add(Dense(1))
		self.model.add(Activation('sigmoid'))

		self.model.compile(loss='binary_crossentropy',
	              	  optimizer='adam',
	              	  metrics=['accuracy'])

		self.model.fit(modeldata[0][0], 
					   modeldata[0][1],
	          	       batch_size=self.batch_size,
	          	       epochs=self.epochs,
	          	       validation_data=(modeldata[1][0], modeldata[1][1]))
		return self.model

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





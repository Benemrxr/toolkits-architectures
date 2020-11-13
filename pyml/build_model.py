from __future__ import print_function

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.datasets import imdb
import numpy as np


def build_model():
	# set parameters:
	max_features = 5000
	maxlen = 400
	batch_size = 32
	embedding_dims = 50
	filters = 250
	kernel_size = 3
	hidden_dims = 250
	epochs = 2


	print('Loading data...')
	(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
	print(len(x_train), 'train sequences')
	print(len(x_test), 'test sequences')

	print('Pad sequences (samples x time)')
	x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
	x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
	print('x_train shape:', x_train.shape)
	print('x_test shape:', x_test.shape)


	print('Build model...')
	model = Sequential()

	model.add(Embedding(max_features,
                    	embedding_dims,
                    	input_length=maxlen))
	model.add(Dropout(0.2))

	model.add(Conv1D(filters,
                 	kernel_size,
                 	padding='valid',
                 	activation='relu',
                 	strides=1))
	model.add(GlobalMaxPooling1D())

	model.add(Dense(hidden_dims))
	model.add(Dropout(0.2))
	model.add(Activation('relu'))

	model.add(Dense(1))
	model.add(Activation('sigmoid'))

	model.compile(loss='binary_crossentropy',
              	optimizer='adam',
              	metrics=['accuracy'])
	fit=model.fit(x_train, y_train,
          	batch_size=batch_size,
          	epochs=epochs,
          	validation_data=(x_test, y_test))
	return model


def prediction (review,model):
	word_to_id = imdb.get_word_index()
	word_to_id["<PAD>"] = 0
	word_to_id["<START>"] = 1
	word_to_id["<UNK>"] = 2

	tmp = []
	for word in review.split(" "):
		tmp.append(word_to_id[word])
		tmp_padded = sequence.pad_sequences([tmp], maxlen=400)
	print(np.array([tmp_padded[0]]))
	"""prediction=model.predict(np.array([tmp_padded[0]]))
	pred=prediction[0][0]
	return pred"""

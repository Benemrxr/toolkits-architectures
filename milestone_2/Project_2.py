from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from keras.models import load_model
import numpy as np

def getParameters(max_features,maxlen,batch_size,embedding_dims,filters,kernel_size,hidden_dims,epochs):
	max_features = 5000
	maxlen = 400
	batch_size = 32
	embedding_dims = 50
	filters = 250
	kernel_size = 3
	hidden_dims = 250
	epochs = 2
	return features,maxlen,batch_size,embedding_dims,filters,kernel_size,hidden_dims,epochs


def loadData(x_train,y_train,x_test,y_test):
	print('Loading data...')
	(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
	print(len(x_train), 'train sequences')
	print(len(x_test), 'test sequences')
	print('Pad sequences (samples x time)')
	x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
	x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
	print('x_train shape:', x_train.shape)
	print('x_test shape:', x_test.shape)
	return x_train,y_train,x_test,y_test


def buildModel(model):
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
	return model

def compileModel(model,fit):
	model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
	fit=model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))
	return model,fit


def saveModel(model):
	return model.save("my_h5_model.h5")


def loadModel(model):
	model = load_model('my_h5_model.h5')
	return model

def getReview(word_to_id,bad,good, tmp_padded,tmp):
	word_to_id = imdb.get_word_index()
	word_to_id["<PAD>"] = 0
	word_to_id["<START>"] = 1
	word_to_id["<UNK>"] = 2

	bad = "this movie was terrible and bad"
	good = "i really liked the movie and had fun"
	for review in [good, bad]:
 	   tmp = []
 	   for word in review.split(" "):
 	       tmp.append(word_to_id[word])
 	   tmp_padded = sequence.pad_sequences([tmp], maxlen=maxlen)
 	   print("%s. Sentiment: %s" % (
 	       review, model.predict(np.array([tmp_padded[0]]))))
	return tmp_padded


"""import matplotlib.pyplot as plt
import numpy as np
q=np.array([0,1])
w=[1,2]
plt.plot(fit.history['val_loss'])
plt.title('Validation loss history')
plt.ylabel('Loss value')
plt.xlabel('No. epoch')
plt.xticks(q,w)
plt.show()
# Plot history: Accuracy
plt.plot(fit.history['val_accuracy'])
plt.title('Validation accuracy history')
plt.ylabel('Accuracy value (%)')
plt.xlabel('No. epoch')
plt.xticks(q,w)
plt.show()"""

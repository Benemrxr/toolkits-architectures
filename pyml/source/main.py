import sys
import logging
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import numpy as np

# Import our helper class to handle the ML-model
from model import MlModel


# configure the logger. Redirect everything to stout (standard output) 
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# Iniialize ML-Model helper class
mlmodel = MlModel(filepath="/data/model.h5")

# Load data and build the model
mlmodel.load_imdb_data()
mlmodel.build_model()

# Save the model to file and load ot again
mlmodel.save_model("/data/model.h5")
mlmodel.load_model("/data/model.h5")


# A simple example prediction
word_to_id = imdb.get_word_index()
word_to_id["<PAD>"] = 0
word_to_id["<START>"] = 1
word_to_id["<UNK>"] = 2

bad = "this movie was terrible and bad"
good = "i really liked the movie and had fun"

for review in [good, bad]:
    tmp = []

    # Split review into words
    for word in review.split(" "):
        tmp.append(word_to_id[word])

    tmp_padded = sequence.pad_sequences([tmp], maxlen=400)

    print("%s. Sentiment: %s" % (review, 
    							 mlmodel.model.predict(
    							 	np.array([tmp_padded[0]]))
    							))

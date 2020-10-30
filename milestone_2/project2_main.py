from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.datasets import imdb
from keras.models import load_model
import build_model
import save_load
import numpy as np

model=build_model.buildModel()
save_load.saveModel(model,"Model.h5")


word_to_id = imdb.get_word_index()
'''word_to_id = {k: (v + INDEX_FROM) for k, v in word_to_id.items()}'''
word_to_id["<PAD>"] = 0
word_to_id["<START>"] = 1
word_to_id["<UNK>"] = 2

bad = "this movie was terrible and bad"
good = "i really liked the movie and had fun"
for review in [good, bad]:
    tmp = []
    for word in review.split(" "):
        tmp.append(word_to_id[word])
    tmp_padded = sequence.pad_sequences([tmp], maxlen=400)
    print("%s. Sentiment: %s" % (
        review, model.predict(np.array([tmp_padded[0]]))))

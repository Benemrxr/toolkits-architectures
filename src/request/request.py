import io
import json
import logging
import requests
import numpy as np

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

# Get sample data from imdb
def load_imdb_sample(start):

    # get command line argument, has to be an int
    #if len(sys.argv) > 1: start = sys.argv[1]

    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

    padded = sequence.pad_sequences(x_test, maxlen=400)

    return padded[int(start):int(start) + 1]


sample = load_imdb_sample(373)
data = json.dumps(sample.tolist())
endpoint = 'http://localhost:81/predict'
response = requests.post(endpoint, data = data)

print('Response (took %ss): %s' % (response.elapsed.total_seconds(), response.text))



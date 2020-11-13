from __future__ import print_function

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model
import build_model
import save_load
import numpy as np

model=build_model.build_model()
save_load.save_model(model,"/data/Model.h5")


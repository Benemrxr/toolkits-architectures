import io
import sys
import logging
import time
import os.path
import psycopg2
import numpy as np
import json
from tensorflow.keras.models import load_model as load_keras_model

# Import our helper class to handle the ML-model
from model import MlModel

# Import our helper functions to handle serialize/deserialize
from serialize import serializer
from serialize import deserializer

# Import our Database-Connector form dbconnect.py
from dbconnect import Database
from dbactions import create_database
from dbactions import create_tables
from dbactions import load_input_data
from dbactions import insert_input_data
from dbactions import insert_predictions


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# Initialize our convenience database class and connect to the database.
db = Database()
db.connect(user="someuser", password="somepassword")

# Create the database and the tables
create_database(db, "milestone_3")

# Close current connection and reconnect to new database
db.close()
db.connect(user="someuser", password="somepassword", database="milestone_3")

# Create the the tables within the new database
create_tables(db)


# The container pyml will create a fitted model for further access.
# However chances are high that we are ready before this file gets created,
# so we will check and wait for it...
while not os.path.isfile("/data/model.h5"):
    logging.info(
        "Waiting for model (h5-file) - Should be availlable shortly...")
    time.sleep(1)  # sleep 1 second...
else:
    logging.info("Model is now availlable! Go on...")

    # Iniialize ML-Model helper class
    mlmodel = MlModel(filepath="/data/model.h5")

    # Load the model
    model = mlmodel.load_model()

    # Gives us a testsample with 50 Reviews
    samples = mlmodel.load_sample_imdb_data(1)

    insert_input_data(db, serializer(samples))

    # Load sample data
    loaded_samples = load_input_data(db)

    # Makes predictions of the sample data
    prediction = model.predict(deserializer(loaded_samples[0][1]))

    # Insert predictions into database
    insert_predictions(db, serializer(prediction), loaded_samples[0][0])


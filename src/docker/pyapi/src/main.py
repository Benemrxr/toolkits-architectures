from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import send_file
from flask import abort

import numpy as np
import os.path
import logging
#import base64
import json
import sys

from serialize import serializer
from serialize import deserializer
from model import MlModel
from database import Database


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


app = Flask(__name__)
mlmodel = MlModel(filepath="/data/model.h5")
db = Database()
path = "/data/model.h5"


def init():
    logging.info("Init...")

    # build the model with the supplied data
    logging.info("Building the model with the IMDB sample dataset if not already present...")

    if not os.path.isfile("/data/model.h5"):
        logging.info("Building...")
        samples = mlmodel.load_imdb_sample_data()
        mlmodel.build(samples)

        # save the model to the specified path
        mlmodel.save(path)
    else:
        logging.info("Skipping! Loading existing model...")
        mlmodel.load()

    # Connect to the postgres server and create the database
    db.connect(user="someuser", password="somepassword")
    db.create_database("milestone_5")

    # Close current connection and reconnect to new database
    db.close()
    db.connect(user="someuser", password="somepassword", database="milestone_5")

    # Create the the tables within the new database
    db.create_predefined_table()


@app.route('/')
def index():
    # redirect to our predict-route in case someone makes a call to root
    return redirect(url_for('predict'))

@app.route('/predict', methods=['POST']) #'GET', 
def predict():
    # specify the path where our model gets stored
    path = "/data/model.h5"
    
    logging.info("Called route /predict (POST)...")

    data = np.array(json.loads(request.data))

    # make predicions from the created model
    logging.info("Making the prediction with the supplied data...")
    predictions = mlmodel.model.predict(data)

    # Create the the tables within the new database
    db.create_predefined_table()

    # Insert predictions into database
    logging.info("Inserting predictions into database...")
    db.insert_predictions(serializer(predictions))

    data = json.dumps(predictions.tolist())
    return data


if __name__ == '__main__':
    init()
    app.run(debug=False, host='0.0.0.0')


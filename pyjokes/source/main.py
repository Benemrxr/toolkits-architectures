import sys
import logging
import time
import os.path
import psycopg2
from tensorflow.keras.models import load_model as load_keras_model

# Import our Database-Connector form dbconnect.py
from dbconnect import Database

# Import our functions form dbactions.py
from dbactions import create_database
from dbactions import create_tables
from dbactions import insert_favourite_joke
from dbactions import get_jokes


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# Initialize our convenience database class and connect to the database.
db = Database()
db.connect(user="someuser", password="somepassword")

# Create the database and the tables
create_database(db, "ms3_jokes")

# Close current connection and reconnect to new database
db.close()
db.connect(user="someuser", password="somepassword", database="ms3_jokes")

# Create the the tables within the new database
create_tables(db)

# Insert a new joke into the database and get it's id. 
# Then read th joke again from the database.
joke_string = "Two fish in a tank. One says: “How do you drive this thing?"
joke_id = insert_favourite_joke(db, joke=joke_string)
joke = get_jokes(db, ids=(joke_id))

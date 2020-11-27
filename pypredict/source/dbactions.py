import sys
import logging
import psycopg2
from tensorflow.keras.models import load_model as load_keras_model

# Import our Database-Connector form dbconnect.py
from dbconnect import Database


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def check_database_exists(db, database):
    db.cursor.execute("SELECT datname FROM pg_database;")

    list_database = db.cursor.fetchall()

    if (database) in list_database:
        logging.info("Database %s already exists" % database)
        return True
    else:
        print("Database %s does not exist." % database)
        return False

def create_database(db, database):
    if check_database_exists(db, database) is True:
        return True
    try:
        # Create a database in PostgreSQL database. PostgreSQL doest NOT support the statement 'IF NOT EXISTS'.
        db.cursor.execute("CREATE DATABASE %s;" % database)
        db.connection.commit()
        logging.info("Database '%s' sucessfully created!" % database)
        return True

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not create Database '%s'!" % database)
        logging.error(dberror)
        return False

def create_tables(db):
    try:
        # Create a table in PostgreSQL database
        db.cursor.execute(
            "CREATE TABLE IF NOT EXISTS input_data (ID SERIAL PRIMARY KEY, INPUT_DATA BYTEA);")
        db.cursor.execute(
            "CREATE TABLE IF NOT EXISTS predictions (ID SERIAL PRIMARY KEY, PREDICTION BYTEA, REF integer REFERENCES input_data (ID));")

        db.connection.commit()
        logging.info("Tables 'predictions' and 'input_data' sucessfully created")
        return True

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not create Tables 'predictions' and 'input_data'!")
        logging.error(dberror)
        return False


def load_input_data(db):
    try:
        # Load sample data
        db.cursor.execute("SELECT * FROM input_data")
        records = db.cursor.fetchall()
        return records

        logging.info("Successfully loaded data")

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not load data!")
        logging.error(dberror)
        return ()

def insert_input_data(db, data):
    try:

        # Create an entry in PostgreSQL database
        db.cursor.execute("INSERT INTO input_data (INPUT_DATA) VALUES (%s)", (data, ))
        db.connection.commit()

        logging.info("Successfully inserted sample data")
        return True

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not insert sample data!")
        logging.error(dberror)
        return False

def insert_predictions(db, prediction, reference):
    try:
        # Create an entry in PostgreSQL database
        db.cursor.execute("INSERT INTO predictions (PREDICTION, REF) VALUES (%s, %s)", (prediction, reference ))
        db.connection.commit()

        logging.info("Successfully inserted predictions")
        return True

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not insert predictions!")
        logging.error(dberror)
        return False



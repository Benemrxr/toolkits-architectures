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
            "CREATE TABLE IF NOT EXISTS jokes (ID SERIAL PRIMARY KEY, JOKE TEXT);")
        db.connection.commit()
        logging.info("Table 'jokes' sucessfully created")
        return True

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not create Table 'jokes'!")
        logging.error(dberror)
        return False

def insert_favourite_joke(db, joke):
    try:
        db.cursor.execute(
            "INSERT INTO jokes (JOKE) VALUES (%s) RETURNING ID,JOKE", (joke, ))
        db.connection.commit()

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not insert joke into Table 'jokes'!")
        logging.error(dberror)
        return None

    # get the ID of our inserted joke (using RETURNING ID in SQL satement above)
    fetched_joke = db.cursor.fetchone()

    logging.info("This is our favourite joke:")
    logging.info("ID: %s" % fetched_joke[0])
    logging.info("JOKE: %s" % fetched_joke[1])  

    #return ID of inerted joke
    return fetched_joke[0]

def get_jokes(db, ids=(), jokes=()):
    try:
        if ids:
            db.cursor.execute("SELECT * FROM jokes WHERE ID IN (%s);" % ids)
        elif jokes:
            db.cursor.execute("SELECT * FROM jokes WHERE JOKE IN (%s);" % jokes)
        else:
            db.cursor.execute("SELECT * FROM jokes")
        
        results = db.cursor.fetchall();
        return results

    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Could not get jokes from Table 'jokes'!")
        logging.error(dberror)
        return None






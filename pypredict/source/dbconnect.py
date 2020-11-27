import psycopg2
import logging
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# configure the logger. Redirect everything to stout (standard output)
# on the console.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# Simplify access to the database with a convenience class
class Database():

    # Define the init function of the class, this will get executed only
    # once. Here we declare our variables for connection and cursor,
    # these can later be acessed from outside with dot-notation.
    def __init__(self):
        self.connection = None
        self.cursor = None

        self.port = 5432
        self.host = "database"

    # connect to the database, default host and port are already defined
    # (but can be overridden).
    def connect(self, **kwargs):
        if(self.connection):
            # Check if the connection already exists. If that's true simply
            # return the connection. We could also return False to inform
            # the calling function about the failure.
            return self.connection

        if "port" not in kwargs:
            kwargs["port"] = self.port or 5432
        if "host" not in kwargs:
            kwargs["host"] = self.host or "database"

        # Try to connect to the database wth the given credentials.
        # Return the connection if all went well.
        try:
            self.connection = psycopg2.connect(**kwargs)

            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

            self.cursor = self.connection.cursor()
            return self.connection

        # If the connection fails, we log an error. We will also return False
        # to inform the calling function about the failure.
        except (Exception, psycopg2.Error) as error:
            logging.error("Error while connecting to PostgreSQL", error)
            return False

    # Close the conection to the database
    def close(self):
        # If no connection exists, simply retun True to inform the calling
        # function that everything is fine.
        if not self.connection:
            return True
        # Try to close the connection to the database. 
        # Return True if all went well.
        try:
            # If there's a persisting connection (and therfore a cursor),
            # first close the cursor...
            self.cursor.close()
            # ... and then the connection.
            self.connection.close()

            self.connection = None
            self.cursor = None

            logging.info("PostgreSQL connection is closed")
            return True

        # Something really bad happened, so we log an error and return False
        except (Exception, psycopg2.Error) as error:
            logging.error("Error while closing the database-connection", error)
            return False

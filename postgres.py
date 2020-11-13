import psycopg2 as psycopg
# Connect postgres DB
conn = psycopg.connect("dbname='postgres' user='postgres' host='172.17.0.2' password='mysecretpassword' port='5432'")
conn.autocommit = True
from __future__ import print_function
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Preparing query to create a database
database = '''CREATE database task3'''
#Creating a database
cursor.execute(database)
#Creating table
table ='''CREATE TABLE REVIEW(
   ID INT,
   REVIEW INT
)'''
cursor.execute(table)
# Insert
cursor.execute('''INSERT INTO REVIEW(
   ID, REVIEW) VALUES
   (x_test[1])'''
# Get
cursor.execute('''SELECT * from REVIEW''')
result = cursor.fetchall();
# Print review
review = result[0]
print(review[1])
#Closing the connection
conn.close()
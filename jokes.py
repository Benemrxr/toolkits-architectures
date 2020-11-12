import psycopg2 as psycopg

# Connect postgres DB
conn = psycopg.connect("dbname='postgres' user='postgres' host='172.17.0.2' password='mysecretpassword' port='5432'")
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
database = '''CREATE database ms3_jokes'''

#Creating a database
cursor.execute(database)
print("Database created successfully........")

#Creating table
table ='''CREATE TABLE JOKES(
   ID INT,
   JOKE TEXT
)'''
cursor.execute(table)
print("Table created successfully........")


# Insert Joke 
cursor.execute('''INSERT INTO JOKES(
   ID, JOKE) VALUES 
   (001,'Two fish in a tank. One says: “How do you drive this thing?' )''')
print("Joke successfully added...")

# Get Joke 
cursor.execute('''SELECT * from JOKES''')
result = cursor.fetchall();

# Print Joke
joke = result[0]
print(joke[1])

#Closing the connection
conn.close()
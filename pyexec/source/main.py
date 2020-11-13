import psycopg2 as psycopg


# Connect postgres DB
conn = psycopg.connect("dbname='database' user='someuser' host='database' password='somepassword' port='5432'")
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
database = '''CREATE database IF NOT EXISTS milestone_3'''
table_predictions ='''CREATE TABLE predictions (
        id VARCHAR PRIMARY KEY,
        predictions NUMERIC[],
        fk_columns FOREIGN KEY,
        input_data(id) REFERENCES
    )
)'''
table_input_data ='''CREATE TABLE input_data(
   id VARCHAR PRIMARY KEY,
   sample INTEGER[]
)''' 

#Creating a database
try:
	cursor.execute(database)
	
	print("Database created successfully........")
	
except: 
	print("Database loaded successfully") 
	

#Creating table
try:
	cursor.execute(table_predictions)
	print("Table 'predictions' created successfully........")
	cursor.execute(table_input_data)
	print("Table 'input_data' created successfuly.......")
except:
	print("Table loaded")

# Load Model
model = load_model("/data/Model.h5")

# Load Sample
print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)
x_test = sequence.pad_sequences(x_test, maxlen=400)

# Gives us a testsample with 50 Reviews
x_sample=x_test[0:1]
print(x_sample)

# Preparing to insert
l = tuple(x_sample)

# Insert sample into input_data table
for tup in l:
	cursor.execute("""
		INSERT INTO input_data (sample)
		VALUES (%(tup)s);
		""",
		{'tup': tup}
	)	  	

conn.commit()


# Loading data from the database 
select_query="select * from input_data"
cursor.execute(select_query)
records=cursor.fetchall()
x_sample_loaded = []
for row in records:
	x_sample_loaded.append(row[1])


# Makes predictions of the sample data
prediction=model.predict(x_sample_loaded)



# Insert predictions into database

# Preparing to insert
l = tuple(prediction)

for tup in l:
	cursor.execute("""
		INSERT INTO predictions (predictions)
		VALUES (%(tup_2)s);
		""",
		{'tup_2': tup}
	)	  	

conn.commit()



conn.close()	

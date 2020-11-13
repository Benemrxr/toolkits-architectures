# Milestone 3: Group Marxer, Kotatis, Rohrer
This report documents our progress for the milestone number :three:. Enjoy! :zap:

## Structure:
- Changes from feedback
- Task 1
- Task 2
- Task 3
- Task 4

## Changes from feedback

> Add `tensorflow.` before each `keras.something` import.

> Other changes to the code?

## Task 1: 
> Install docker-compose.

We tried to install docker compose using the the following command:

```cosnole
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
```

But we got an error, that the `curl` command was not found. To install docker compose this way, we first had to install the curl-function itself. Therefore we used the command `sudo apt install curl`. After we ran this command, we were able to install docker compose with the command above. To use docker-compose, we had to run the following command so that the `docker-compose` command is executable:

```console
$ sudo chmod +x /usr/local/bin/docker-compose
```
> Which services are being used for the application?

There are two services used for the application:

1. Flask: This is a service that can be used in Python to develop web applications. Flask is basically an API from Python.
2. Redis: Redis is a NoSQL based data storage system server. 

These two services are used by the application to run the "Hello-World-App" on the Redis server. Therefore we use the hostname "redis" inside of the python application. Python uses Flask to cre applications and make them running on web servers. Redis on the other hand serves as the data storage system on which the app is running.

> What ports are being used?

Within the application, we use the port 6379 on which we run the redis storage system. In the docker-compose, we used port 5000. We know this by reading the docker-compose.yml file. 

>  How does the host machine communicate with the application inside the Docker container. Which ports are exposed?

To check out how the host machine communicates with the application, we first run the application within the docker-compose. We opened up a new terminal and with the help of `docker-compose ps`, we checked out the running containers and got the following output:

       Name                        Command                     State         Ports         
       ---------------------------------------------------------------------------------------------------
       |composetest_redis_1 |  docker-entrypoint.sh redis ...| Up     |      6379/tcp                    |   
       |composetest_web_1   |  flask run                     | Up     |      0.0.0.0:5000->5000/tcp      |

There we can see that our host machine (0.0.0.0) communicates via the port 5000 to the application server, who uses this same server. The data is exchanged by the "tcp" (transmission control protocol). 

>  What is localhost? Why is it useful in the domain?

The term "localhost" is refering to the local ip-address of my own computer or device. In concrete terms, "localhost" is used to connect to a certain ip-address from my local machine. Thats also the reason why it is used in the web-domain. For example the domain: http:/localhost:5000 can be used to connect from our local machine ("localhost") to the port 5000. In our case, this is exactly the port where the application is running and we see the output of this very application. 

## Task 2:

>  What is PostgreSQL? SQL or no-SQL (why?)

`PostgreSQL` is an open-relational database system (RDBMS) that makes use of the SQL language and offers many features for data types and integrity, performance, reliability, security and many more tasks. Free and open-source, it ranks among the most popular database management systems ([db-engine.com ranking](https://db-engines.com/en/ranking)). 

The primary front-end for PostgreSQL is the `psql` command-line program, which we try out later on. It can be used to enter SQL queries directly.

Another useful tool for us is `pgAdmin`, a GUI administration tool.

Now whether it is SQL or no-SQL: In my understanding, SQL is, by definition, structured data, whereas non-SQL is "semi-structured" data that does not fit well into a tabular representation ([so.com, Laurenz](https://stackoverflow.com/questions/47942913/is-postgresql-a-nosql-database/47943104)). So PostgreSQL, which is a RDBMS is SQL and not the NoSQL non-relational DBMS. That being said, it seems that PostgreSQL offers NoSQL capabilities such as JSON output, so users can utilize PostreSQL like a NoSQL document database ([so.com, Ben and Jameels' answer](https://stackoverflow.com/questions/4426540/mongodb-and-postgresql-thoughts)). Further, the official FAQ clearly distinguishes PostgreSQL from non-relational database implementations ([FAQ](https://www.postgresql.org/about/press/faq/)).

>  Run a PostgreSQL Server using a Docker image from PostgreSQL Docker Hub page.

Before we were able to run a PostgreSQL server, we first had to **install** PostgreSQL. Therefore we followed the following steps:

1. Creating the file repository configuration:
```console
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
2. Importing the repository signing key:
```console
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
3. Updating the package lists:
```console
$ sudo apt-get update
```
4. Installing PostgreSQL Version 12.4:
```console
$ sudo apt -y install postgresql-12 postgresql-client-12
```
5. Give sudo-rights to the created user:
```console
$ sudo su - postgres
```
6. Starting PostgreSQL prompt (if there's a permission problem, try the following creation of a Unix group called docker and add the user postgres to it):
```console
$ psql
```

Since this worked well, we now know that PostgreSQL was installed correctly on our machines.
Now to run a PostgreSQL Server using a docker image, we first downloaded the Docker Image from Docker Hub. We did this by using `docker pull postgres`, but be aware that you have to escape the PostgreSQL prompt. Use `\q` to quit it. 

Then, you might have to do a few steps to so that you can use the Docker daemon with other users, as it always runs on the `root` user. To do this, switch back from the postgres user to your main user and follow this short tutorial: [docs.docker.com](https://docs.docker.com/engine/install/linux-postinstall/). 

First, create the `docker` group, which grants privileges equivalent to the `root` user. Be aware of potential impacts on the security of your system. 
```console
$ sudo groupadd docker
```
Next, we add our postgres user to the `docker` group:
```console
$ sudo usermod -aG docker postgres
```
Now, we need to restart our virtual machine. We then switch back to the postgres user. Since we don't have a password (I tried `mysecretpassword`, it seems that there isn't a default password as the default authentication mode for PostgreSQL is set to ident), we need to repeat the fifth step from above, `sudo su - postgres`. We can test for the correct grouping with this command:
```console
$ docker run hello-world
```
Now there shouldn't be any permission problems. Finally, back to the `docker pull postgres` command. 

We run the Docker Image with the following command:
```console
$ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
Lastly we use the command `docker ps` to check if everything works properly. We notice that the container is running on port 5432, with tcp. 

>  Make sure you expose the correct ports when running the Docker container (read the documentation on Docker Hub)

Is the correct port exposed? / Is this answered in the line above?
> Find an appropriate Python package (Postgres adapter) 

To connect to our PostgreSQL database, we install the package `psycopg2`. Since it did not work to install it with pip, we installed only the "binary" edition with:

```
pip3 install pyscopg2-binary
```

>  Write a little python script that:
> - Connects to the database server using "localhost:port". You will have to enter a username and password too (again, read the docs)
> - Creates a database called "ms3_jokes" (very specific tip: Python packagesthat want to be PEP 249 compliant, assume that you always work in Database"Transactions". PostgreSQL does not make such an assumption. Read more about Database Isolation Levels, if you are interested. Practically, this means you may have to configure your Postgres adapter correctly) 
> - Creates a Table called "jokes". The table should have an attribute "ID" which is it's primary key and another Attribute "JOKE" of character type "TEXT"
> - Inserts your favorite joke into that table
>- Selects your favorite joke (now in the database), and fetches it from the database
>- Prints your favorite joke. You should see your joke in it's full glory.

Our python script is called `jokes.py`. 

We use the package `psycopg2` to connect to our PostgreSQL database. Install the current version thereof with the code below from the Python Package Index software repository.
```console
$ pip install psycopg2==2.8.6
```
If you get an error, try:
```console
$ sudo apt-get install python3-psycopg2
```

In order to build a connection we use the function `psycopg2.connect()` from the package described above. Therefore we need several parameters:

1. Name of the database (as *dbname*)
2. User
3. Host
4. Password
5. Port

To get these informations, we first used the command 
```console
$ docker exec -tiu postgres some-postgres psql
```
We open up the prompt of our database like that. In there we can use the command `\conninfo` to get all the information, except the password of course. This is simply the password that we defined in the command to run the database on Docker.

To show our table we can use the command `\dt`. That gives us this output:

              List of relations
       Schema |      Name   |      Type   |      Owner
       public |      jokes  |      table  |      postgres
       (1 row)

We build the connection with the following code:
```console
conn = psycopg.connect("dbname='postgres' user='postgres' host='172.17.0.2' password='mysecretpassword' port='5432'")
conn.autocommit = True
```
For some reason, we had to define `autocommit` as `True` in order to create the database.

We then create a cursor object using the cursor() method:
```console
cursor = conn.cursor()
```
Then prepare a query to create our database. We execute this through the cursor object:
```console
database = '''CREATE database ms3_jokes'''
cursor.execute(database)
print("Database created successfully........")
```
Now, we want to create a table called "jokes". The table should have an attribute "ID" which is it's primary key and another Attribute "JOKE" of character type "TEXT".
```console
table ='''CREATE TABLE JOKES(
   ID INT,
   JOKE TEXT
)'''
cursor.execute(table)
print("Table created successfully........")
```
To insert our favorite joke in it:
```console
cursor.execute('''INSERT INTO JOKES(
   ID, JOKE) VALUES 
   (001,'Two fish in a tank. One says: “How do you drive this thing?' )''')
print("Joke successfully added...")
```
Select the favorite joke and fetch it from the database:
```console
cursor.execute('''SELECT * from JOKES''')
result = cursor.fetchall()
```
Lastly, print the joke for us to see:
```console
joke = result[0]
print(joke[1])
```
The command at the end of the file closes the connection again with `conn.close()`.

>  Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also exists as a Docker Image :). Connect to your running PostgreSQL Database. Can you see your database and table?

We can pull the Docker Image of the `pdAdmin tool` from Docker Hub with the Docker Pull Command below:
```console
$ docker pull dpage/pgadmin4
```
This will certainly be a useful inclusion in our docker container, but for our current purposes we are better suited with a direct installation from the pgAdmin website: https://www.pgadmin.org/download/. Alternatively, we can use pip to install it from the `PyPi` with `pip install pgadmin4`. To do this, we need to create a virtual environment, as laid out in https://www.pgadmin.org/download/pgadmin-4-python/. Then, we configure our local user with `$ pgadmin4` and use `user@domain.com` for the email and `mysecretpassword` for the password. Now the pgAdmin 4 tool start and we can navigate to http://127.0.0.1:5050 in our browser.

From there, we can **add a new server** on the **dashboard** tab. In the **create - server** dialog box, we type a name in the **general** tab to identify our server in pgAdmin. We name it jokes, for example. On the **connection** tab, we type information for the **host** (IP), **port** (5432), **username** (postgres) and **password** (mysecretpassword). We choose **save** and can access our database in the pgAdmin browser by expanding server. 

:exclamation: However, we can't find any table or views. :exclamation:

For our container, we might add the following lines of code:
```
services: 
       pgadmin:
              image: "dpage/pgadmin4:latest"
```

>  If you stopped and deleted the Docker container running the database and restarted it. Would your joke still be in the database? Why or why not?

To get the Docker containers name:
```console
$ docker ps -a | awk '{print $NF}'
```
As expected our container is named `some-postgres`. Stop it and then delete:
```console
$ docker stop some-postgres
$ docker rm some-postgres
```
We can check with `docker ps -a` to make sure the container is deleted.

Now let us restart the container and database, to check whether the joke is still in it.

We use the `docker run ...` command from above to start the container and the `docker exec ...` from above to open up the psql prompt. We can use the `\dt` command to look for our table, but get a message that it did not find any relations. To persist our data, we would need to use a Docker volume.

## Task 3:
> How do you need to represent/transform image data to save it to a relational database?

Previously, we were just using **text files** with our database. The `jokes.py` file is such a kind of computer file, that is structured as a sequence of lines of electronic text. Image data however, is stored differently, that is to say in **non-text files**, also called **binary files**. They can be thought of a being a sequence of `bytes` - `bits` in groups of eight ([wikipedia.org, binary file](https://en.wikipedia.org/wiki/Binary_file)). 

The problem is, that it is not good practice to store large binary objects, *BLOBs*, in a database. They are unstructed and opaque, and seemingly it just **bloats** the database without much of an advantage.

A better way is to store the BLOBs on a separate file server and make sure to keep a connection to it in our database, i.e. save the path  of the image in the database in a text column.

For small image data or if such a filesystem is not available, we can make use of the `bytea` column, that is also available in PostgreSQL. For example ([so.com, JeyJ and Yan](https://stackoverflow.com/questions/61044064/insert-image-in-a-database-in-postgres)):
```console
insert into images(image_name, image_raw) values('image.png', bytea('D:\image.jpg'));
```

> Look at your own data set:
> - How is your data structured (you can download and load it from the source. Some of you may use the Keras function to download it).
> - Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use (https://www.postgresql.org/docs/12/datatype.html)
> - What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes) 

As described in the first milstone, the dataset assigned to us was constructed for a sentiment analysis publication from a collection of reviews from IMDB. The authors Maas et al. released this dataset to the public, it can be found online (https://ai.stanford.edu/~amaas/data/sentiment/) and in their paper (https://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf). We can also directly load it with `Keras`, as it is included in the `tf.keras.dataset` module (https://keras.io/api/datasets/imdb/). 

```console
from keras.datasets import imdb
```
The data set is structured as follows. The core dataset contains 50,000 reviews split evenly into 25k train and 25k test sets. The overall distribution of labels is balanced (25k pos and 25k neg). Also included are an additional 50,000 unlabeled documents for unsupervised learning. Check out our first milestone for a more detailed description of the movie collection. What is important, is that there are two top-level directories [train/, test/] corresponding to the training and test sets. Each contains [pos/, neg/] directories for the reviews with binary labels positive and negative. Within these directories, reviews are stored in text files named following the convention [[id]_[rating].txt] where [id] is a unique id and [rating] is the star rating for that review on a 1-10 scale. The directiory [train/unsup/] has 0 for all ratings, as they are omitted. 

Further, the authors include the [imdb.com](www.imdb.com) URLSs for each reviewq in a seperate text file. Find more information on the official [site](https://ai.stanford.edu/~amaas/data/sentiment/).

The reviews are a sequence of words. They come preprocessed as a sequence of integers, where each integer stands for a specific word in the dictionary. As we cannot feed a list of integers into our deep neural network, we need to convert them into tensors. Rakshit from towardsdatascience.com has a nice tutorial on preparing the data for a neural network ([link](https://towardsdatascience.com/binary-classification-of-imdb-movie-reviews-648342bc70dd)).

As far as the data type from https://www.postgresql.org/docs/12/datatype.html is concerned, it can be classified as a [binary data type](https://www.postgresql.org/docs/12/datatype-binary.html). The `bytea` data type allows storage of binary strings.

> - Repeat Task 2 using a sample from your own data set! In case you deal with images, you may want to draw that picture using an appropriate Python package, after you retrieved the image from the database. To make sure, you applied the correct "reverse" transformation. Look here (Image.open from the Pillow Package): https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.open


## Task 4:

> Create a docker-compose.yml file which:
> - Starts a PostgreSQL Server Docker container (Version 12.4) It should use a Docker volume to persist your Data.

We did this with the help of the service called "postgres" in our .yaml file. In there, we simply used the Docker image from task 2. For correct versioning, we defined the version, as expected, version 12.4. We created the volume into the folder "pgdata". This folder reffers to the folder "./data" in the Docker container. Under "Environment", we defined the username, password and name of the database in order to make it accessable later on. 

> - Executes a Python Script in another Docker container, which connects to your database.

Therefore we first created a dockerfile similar to the one from the last milestone. This Dockerfile  should execute our Python Script later on. We therefore created a folder "/source", where we put in all the code itself and the requirements.txt file. Now to run this Container, we created a service in our docker-compose.yml file called "pyexec". In there we build up the container from the docker file we created. Now we were ready to build up our python script. 

> This script should include:
> -- Initialize your database as in previous tasks. Add two tables called "input_data" and "predictions".

As in the previous tasks, we used "pyscopg2" to interact with the database in our Python Script. We therefore called the connection function with the following attributes:

```
conn = psycopg.connect("dbname='database' user='someuser' host='database' password='somepassword' port='5432'")
conn.autocommit = True
```

We then created our database and the tables like this:

```
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

```

As you might see, we used the row id as our primary key in both of the tables. We then added the two rows "predictions" respectively "sample" to store our main data. We added the two brackets behind the object type in order to be able to store tuples in which we transformed our data arrays later on. Further more, we tried to create a link between the two tables with the help of foreign keys. 

We then runed these database commands with the "cursor.execute()" function (we created the cursor before). To make sure, that ther won't be an error, we decided to execute it inside of an "try" function to kind of catch the error if the database already exists. 

> -- Load your trained Neural Network (.h5) file

Since we should not upload .h5 files on git, we decided to run a third Docker container in our Docker-Compose. This container should train the model by simply executing the script of milestone 2. Therefore we simply used the Dockerfile we crated during Milestone to and fed this to our Docker-Compose. This code should basically train the model and save it in the "/data" volume which in thus should be created through our Docker-Compose. From there we should be able to load the model with the following command:

``` 
model = load_model("/data/Model.h5")
```

> -- Load a sample from the data set and extract single row. 

Since we have no experience with Keras, we decided to loaded the complete data set and then select a sample with this simple line of code:

```
x_sample=x_test[0:1] 
```
This gives us a list of two lists of integers. These integers are reffering to the single words in the reviews of our data, our sample data. 

> -- Save this single sample to the database.

In order to save our data into the table we created before. We had to prepare the sample firs before saving it. We therefore used the following line of code to create a tuple out of our list:
```
l = tuple(x_sample) 
```
We hoped, that we could now save our data into our table we created before. Therefore we once more used "pyscopg2" with the following for loop to insert all of the individual tuples into our table:
```
for tup in l:
	cursor.execute("""
		INSERT INTO input_data (sample)
		VALUES (%(tup)s);
		""",
		{'tup': tup}
	)	  	

conn.commit() 
```
> -- Load the sample again from the database and call your predict function.

We used the following query command in order to load the sample once again. In there we used a for loop to create a list out of our loaded tuples. This list should be able to be runned in the predict function. Therefore we first had to change our predict function a bit, since our firs one was not useful for this task. This tooks us also quite a bit of time. But since we kind of managed to do so, we added the prediction function to this code in order to make these predictions. This prediction gaves us a list of floats. For some reason these were stored as a list in a list, even though there was only one number in the inner list.

> -- Save the prediction result to the database

To save the predictions, created the following command, which is quite similar to the one for the sample data:


```
l = tuple(prediction)

for tup in l:
	cursor.execute("""
		INSERT INTO predictions (predictions)
		VALUES (%(tup_2)s);
		""",
		{'tup_2': tup}
	)	  	

conn.commit()
```
We also transformed the list to a tuple in order to save it in the database. Here, we also created used the for-loop to save the each part of the data individually. 

> Explain how you choose to structure your database

Our database contains two tables. The first one is the "input data". This table contains the sample data which we use to get our predictions later on. The second table, predictions contains the resulting predictions. These two tables are linked with a foreign key. This means that each value in the predictions-table refers to the corresponding input-value in the "input data" table. 

> How we solved the problem of the dependencies in our docker-compose:

To make sure, whether the containers start up in their right order, we used the "depends_on"-Function in our docker-compose.yml file. This should make sure, that Docker-Compose starts the containers in the appropriate order. 

> Additional comment on task 4:

Since we spent almost everyday of the first week to correct stuff from the last milestone in order to make this milestone possible and we do not have much experience in the whole computer science and programing world, we decided to put the focus here on the code. We tried to write down the code as logically as possible and then try it out in the Docker-Compose as a whole. We know that this is not the way to do it but we simply do not have that much experience in with it. As it was to expect, we got several errors, for which we simply did not have enough time to solve them or even to write an issue. We would have to write tons of issues and we do not have enough time for that. Since it was written on the project paper, that we should start early, we did this and started in on monday after the distribution of the project. We still did not have enough time, even though we spend almost all of our spare time (after other courses) to work for this and project. We are not lazy, we just do not have the expected experience in computer science for this projects. 





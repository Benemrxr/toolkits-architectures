# Milestone 2: Group Marxer, Kotatis, Rohrer
This report documents our progress for the second milestone. :sunglasses:

## Task 1: 
>Install docker-compose.

We tried to install docker compose using the the following command:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose' 
```

But we got an error, that the `curl` command was not found. To install docker compose this way, we first had to install the curl-function itself. Therefore we used the command 'sudo apt install curl'. After we ran this command, we were able to install docker compose with the command above. To use docker-compose, we had to run the following command so that the `docker-compose` command is executable:

```
sudo chmod +x /usr/local/bin/docker-compose'
```
>Which services are being used for the application?

There are two services used for the application:

1. Flask: This is a service that can be used in Python to develop web applications. Flask is basically an API from Python.
2. Redis: Redis is a NoSQL based data storage system server. 

These two services are used by the application to run the "Hello-World-App" on the Redis server. Therefore we use the hostname "redis" inside of the python application. Python uses Flask to cre applications and make them running on web servers. Redis on the other hand serves as the data storage system on which the app is running.

>What ports are being used?

Within the application, we use the port 6379 on which we run the redis storage system. In the docker-compose, we used port 5000. We know this by reading the docker-compose.yml file. 

> How does the host machine communicate with the application inside the Docker container. Which ports are exposed?

To check out how the host machine communicates with the application, we first run the application within the docker-compose. We opened up a new terminal and with the help of `docker-compose ps`, we checked out the running containers and got the following output:

       Name                      Command               State           Ports         
-------------------------------------------------------------------------------------
|composetest_redis_1 |  docker-entrypoint.sh redis ...|   Up  |	 6379/tcp            |   
|composetest_web_1   |  flask run                     |  Up   |    0.0.0.0:5000->5000/tcp  |

There we can see, that the our host machine (0.0.0.0) communicates via the port 5000 to the application server, using the port 5000 too. The data is exchanged by the "tcp" (transmission control protocol). 

> What is localhost? Why is it useful in the domain?

The term "localhost" is refering to the local ip-address of my own computer or device. In concrete terms, "localhost" is used to connect to a certain ip-address from my local machine. Thats also the reason why it is used in the web-domain. For example the domain: http:/localhost:5000 can be used to connect from our local machine ("localhost") to the port 5000. In our case, this is exactly the port where the application is running and we see the output of this very application. 

## Task 2:

> What is PostgreSQL? SQL or no-SQL (why?)





>Run a PostgreSQL Server using a Docker image from PostgreSQL Docker Hub page.

Before we were able to run a PostgreSQL server, we first had to install PostgreSQL. Therefore we followed the following steps:

1. Creating the file repository configuration:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
2. Importing the repository signing key:
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
3. Updating the package lists:
```
sudo apt-get update
```
4. Installing PostgreSQL Version 12.4:
```
sudo apt -y install postgresql-12 postgresql-client-12
```
5. Give sudo-rights to the created user:
```
sudo su - postgres
```

6. Starting PostgreSQL prompt:
```
psql
```

Since this worked well, we now know that PostgreSQL was installed correctly on our machines.
Now to run a PostgreSQL Server using a docker image, we first downloaded the Docker Image from Docker Hub. We did this by using `docker pull postres`. We then ran the Docker Image with the following command:
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
finally we used the command `docker ps` to check if everything worked properly. We noticed that the container was running on port 5432. 

> Find an appropriate Python package (Postgres adapter) 

To connect to our PostgreSQL database, we installed the package pyscopg2. Since it did not work to install it with 
conn = psycopg2.connect("dbname='some-postgres' user='' host='172.17.0.2' password='55vbve' port='5432'")

> Write a little python script

### Connecting to PostgreSQL

In order to build a connection we use the function psycopg2.connect() from the package described above. Therefore we need several parameters:

1. Name of the database
2. User
3. Host
4. Password
5. Port

To get these informations, we first used the command 
```
docker exec -tiu postgres some-postgres psql
```
We open up the prompt of our database like that. In there we can use the command `\conninfo` to get all the information, except the password of course. This is simply the password that we defined in the command to run the database on Docker.

### Creating database

The creation of the database worked quite well. The only problem we faced here was, that we had to define autocommits as True in order to create the database. 

### Creating Table



# Milestone 3: Group Marxer, Kotatis, Rohrer
This report documents our progress for the milestone number :three:.  :zap:

## Task 1: 
>- Install docker-compose.

We tried to install docker compose using the the following command:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
```

But we got an error, that the `curl` command was not found. To install docker compose this way, we first had to install the curl-function itself. Therefore we used the command `sudo apt install curl`. After we ran this command, we were able to install docker compose with the command above. To use docker-compose, we had to run the following command so that the `docker-compose` command is executable:

```
sudo chmod +x /usr/local/bin/docker-compose
```
>- Which services are being used for the application?

There are two services used for the application:

1. Flask: This is a service that can be used in Python to develop web applications. Flask is basically an API from Python.
2. Redis: Redis is a NoSQL based data storage system server. 

These two services are used by the application to run the "Hello-World-App" on the Redis server. Therefore we use the hostname "redis" inside of the python application. Python uses Flask to cre applications and make them running on web servers. Redis on the other hand serves as the data storage system on which the app is running.

>- What ports are being used?

Within the application, we use the port 6379 on which we run the redis storage system. In the docker-compose, we used port 5000. We know this by reading the docker-compose.yml file. 

> - How does the host machine communicate with the application inside the Docker container. Which ports are exposed?

To check out how the host machine communicates with the application, we first run the application within the docker-compose. We opened up a new terminal and with the help of `docker-compose ps`, we checked out the running containers and got the following output:

       Name                        Command                     State         Ports         
       ---------------------------------------------------------------------------------------------------
       |composetest_redis_1 |  docker-entrypoint.sh redis ...| Up     |      6379/tcp                    |   
       |composetest_web_1   |  flask run                     | Up     |      0.0.0.0:5000->5000/tcp      |

There we can see that our host machine (0.0.0.0) communicates via the port 5000 to the application server, who uses this same server. The data is exchanged by the "tcp" (transmission control protocol). 

> - What is localhost? Why is it useful in the domain?

The term "localhost" is refering to the local ip-address of my own computer or device. In concrete terms, "localhost" is used to connect to a certain ip-address from my local machine. Thats also the reason why it is used in the web-domain. For example the domain: http:/localhost:5000 can be used to connect from our local machine ("localhost") to the port 5000. In our case, this is exactly the port where the application is running and we see the output of this very application. 

## Task 2:

> - What is PostgreSQL? SQL or no-SQL (why?)

> - Run a PostgreSQL Server using a Docker image from PostgreSQL Docker Hub page.

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

6. Starting PostgreSQL prompt (if there's a permission problem, try the following creation of a Unix group called docker and add the user postgres to it):
```
psql
```

Since this worked well, we now know that PostgreSQL was installed correctly on our machines.
Now to run a PostgreSQL Server using a docker image, we first downloaded the Docker Image from Docker Hub. We did this by using `docker pull postgres`, but be aware that you have to escape the PostgreSQL prompt. Use `\q` to quit it. 

Then, you might have to do a few steps to so that you can use the Docker daemon with other users, as it always runs on the `root` user. To do this, switch back from the postgres user to your main user and follow this short tutorial: https://docs.docker.com/engine/install/linux-postinstall/. 

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
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
Lastly we use the command `docker ps` to check if everything works properly. We notice that the container is running on port 5432, with tcp. 

> - Make sure you expose the correct ports when running the Docker container (read the documentation on Docker Hub)

> - Find an appropriate Python package (Postgres adapter) 

To connect to our PostgreSQL database, we installed the package pyscopg2. Since it did not work to install it with 
conn = psycopg2.connect("dbname='some-postgres' user='' host='172.17.0.2' password='55vbve' port='5432'")

>  Write a little python script that:
> - Connects to the database server using "localhost:port". You will have to enter a username and password too (again, read the docs)
> - Creates a database called "ms3_jokes" (very specific tip: Python packagesthat want to be PEP 249 compliant, assume that you always work in Database"Transactions". PostgreSQL does not make such an assumption. Read more about Database Isolation Levels, if you are interested. Practically, this means you may have to configure your Postgres adapter correctly) 
> - Creates a Table called "jokes". The table should have an attribute "ID" which is it's primary key and another Attribute "JOKE" of character type "TEXT"
> - Inserts your favorite joke into that table
>- Selects your favorite joke (now in the database), and fetches it from the database
>- Prints your favorite joke. You should see your joke in it's full glory.

> - Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also existsas a Docker Image :). Connect to your running PostgreSQL Database. Can you see your database and table?

> - If you stopped and deleted the Docker container running the database and
restarted it. Would your joke still be in the database? Why or why not?

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


## Task 3:

## Task 4:
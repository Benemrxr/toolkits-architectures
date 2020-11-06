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



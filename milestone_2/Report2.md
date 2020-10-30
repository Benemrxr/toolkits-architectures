# Milestone 2: Group Marxer, Kotatis, Rohrer
This report documents our progress for the second milestone. :sunglasses:

### Before we get started:
We set up a [new project repository](https://github.com/Benemrxr/toolkits-architectures.git)  with a clean history and no large data files. The repository for our first project was littered with files that weren't relevant for version-control. We copy and paste our first milestone files to the new repository. Regarding structure, the new 'master' branch is used for our final assignement submissions and the 'current-project' branch is used as our working directory.

## Task 1: 
>Clean Git repositories are important.
>Write an appropriate ".gitignore" file

We added the following files to ignore into our .gitignore file. We oriented ourselves on a recommendation of another .gitignore file in order to see which files could be helpful to have in our .gitignore. Since we do not have a computer science background, we do not necessarily know which kind of hidden files can appear in our git folders. Therefore we added the following list to our .gitignore:

*~   
All the files that end with the sign “~” these are backup files from Linux itself.

`.fuse_hidden*`  

Temporary files which can be created if a process still has a handle open of a deleted file.

`.directory`

KDE directory preferences. 

`.Trash-*`

The Linux trash folder which might appear.

`.nfs*`

.nfs files are created when an open file is removed but is still being accessed 

We never used the .gitignore on the master branch. To work with our code, we always used seperate branches and simply pushed the .gitignore direct to this very branch where we worked. And in the end of the milestones, we merged the .gitignore to the master branch.

## Task 2:
>- What is a Hash function? What are some of the use cases?
>- What is a Python module, package and script. How do they differ from one
>another?
>- How would YOU explain a Docker container and volume to a child?
>- What is your preference concerning the use of Python virtualenv and Docker? When would you use one or the other (there is not right or wrong, mostly)?
>- What is the Docker build context?
>- How can you asses the quality of a python package on PyPI?

A hash function is a function that can be used to map big sized data to fixed size values. The returned values are called hash values. These values are then used to index a so-called hash table. In the best case, each hash value stands for one bigger sized data part but there can also be collisions if one hash value stands for two different data parts. Hash functions are especially used in data storage and retrieval applications. It is used to store and access big amounts of data in a computationally and storage space efficient form. 

A Python module is basically a .py file which contains different functions, classes or variables. Packages however are kind of sets which contain multiple modules. The main difference between packages and modules is the existence of the __init__.py file. This file indicates that the directory contains a Python package and can therefore be imported in a similar way as modules. While modules contain basically just predefined functions, variables or classes, Python scripts are used to call these functions and build up the main code for the needed computing problem. 

A Docker container is basically a box that contains all the requirements for a certain programme. With the help of a Docker container, it is quite easy to run a certain application on another machine without installing a bunch of different requirements. An analogy for a Docker container can be a box with ingredients for a dish. The application is the recipe for the dish. If you now want to let your friend try out the dish, you can send him only the box with the recipe and the ingredients in it. Now he has the possibility to prepare the dish without first buying all the ingredients. Everything is included in the box. Volumes make it possible to keep this data stored, even if the docker container is getting deleted. Volumes are further helpful to exchange data between the host computer and Docker containers. 

Primarily we would definitely prefer using Docker instead of virtual environments. Since virtual environments only encapsulate Python dependencies . Docker however encapsules the whole operating system and can therefore be used on every machine with every operating system. So we can say that a virtual environment can be used if we use the same operating system on the opposite machine. If this is not the case, we should use Docker instead. 

The docker build context is the set of files in the specified path. The build process can refer to any of the files in the docker build context. You also have the possibility to use an URL instead of a path. This URL points to a Git repository. 

In our opinion, you have the possibility to assess the quality of a python package on PyPI via the GitHub statistics. The stars, forks and open issues give us an idea how often a certain package is used and how many software developers use them. This gives us an idea about the quality and user friendliness of the package.                                                                    

## Task 3:
>Make sure your code has the following functionality (extend if necessary):
>- Can load data
>- Can train (fit) a neural network on the data
>- Can save a fitted model to a ".h5" file
>- Can load a ".h5" file, using Keras
>- Can perform predictions using a "fitted" model, using Keras

Our python code is already able to load data from Keras and to train (fit) a neural network. Because of that, we did not have to make any changes regarding these questions. The first thing we had to care about, was to save the fitted model in a .h5-file. We did this with the help of the command `model.save("filename")`. 
For the counterpart of saving the model, to load the model, we used the function `load_model (“filename”)` from the Keras package. The last part of the task, to build a function that makes predictions, made us struggling. The reason for that is that we do not have that much experience in Python and with machine learning, to understand how to implement this function. With the help of google, we found a function that is especially developed for our machine learning project. We managed to make predictions for two different strings (good and bad). However we were not able to build a prediction function for datasets. We did not have an appropriate understanding of the machine learning project itself, to do that. 

## Task 4
>- Split your code base into modules (for example the creation of the neural
network might be in a "neuralnet_architecture.py" module). Explain the reasoning
behind your modularization. Why did you choose to structure the code like this?
>- There has to be one "main.py" script that calls the code in all the other
modules. This is the script that you run with the "python" command.
>- The modules are only allowed to contain imports and functions (for example
"def create_neuralnet(): ...")
>- Ensure PEP8 conformity.

To structure our code, we defined three different functions in two modules. The first function `BuildModel ()` from the buildModel module is to build the model with the help of the data imported from Keras. This function has no input and simply builds the model. 

The second module is the save_load module which contains two functions: (1) `saveModel (model,filename)` and (2) `loadModel (filename)`. (1) is used to save the model in a .h5 file. This function needs two parameters: the model itself and the name of the resulting .h5 file. (2) is used to load the model from a .h5 file. The function only takes one parameter: the name of the .h5 file. 

## Task 5 
> Create a pip "requirements file" for your code base and explain how you make it work within a virtualenv (step by step). Did you have to install virtualenv? 

We modify the requirements.txt file from our first project so that it controls for the approriate version of our packages. Since Keras is included in Tensorflow, we only set `tensorflow == 2.3.1`, to ensure that we have the currently latest version of Tensorflow.

Now, we are ready to test our code in a virtual environment:

We install `virtualenv` to create an isolated Python environment, with some [advantages](https://virtualenv.pypa.io/en/latest/) over the base `venv` module. So the first step is: 
```
pip3 install virtualenv
```
We then create such an isolated environment in our desired working directory, with the following commands:
```
virtualenv -p /usr/bin/python3 env/project_2
```
Now activate said environment:
```
source env/project_2/bin/activate
```
Let's load our code files from GitHub!
```
git clone https://github.com/Benemrxr/toolkits-architectures.git
```
To test the code of this second milestone, we need to switch to the branch where the code is stored. Depending on when you are reading this you may skip this step and load the code from the master branch.
```
git switch functionizingCode
```
Nevermind, we were already in this branch. It is up-to-date, as we just cloned the repository.

Before we can load the files, we need to change to the approriate directory:
```
cd toolkits-architectures/milstone_2
```
No, we can start loading the files. First of all, the requirements.txt file:
```
pip install -r requirements.txt
```
Ready to build the model? Let's go! Our code is modularizied, see Task 3 for the detailed information concerning the modules
```
python3 build_model.py
python3 save_load.py
python3 project_2_main.py
```
Our code has run successfully in this isolated Python environment.

## Task 6
>"Dockerize" your code:
>- Install Docker on your machines
>- Create a Dockerfile that installs all necessary dependencies and is capable of running Tensorflow/Keras in CPU mode.

First we install docker. I am using Visual Studio Code on Windows right now, which is why I install [Docker Desktop](https://www.docker.com/products/docker-desktop) via the docker website.

Installation was successfull:
```
$ docker --version
Docker version 19.03.13, build 4484c46d9d
```
But right now it doesn't work - the docker daemon is not running. I try to change some settings - namely the WSL setting, I deactive it. Now, there seems to be a problem with my available memory space. I first increase the allowance to 4 GB in Docker Desktop and then decrease to 1 GB, as the first change didn't work either (2 GB was the default). Now it runs!

We get a getting-started dockerfile first.

I now try to dockerize our Python code. [This](https://code.visualstudio.com/docs/containers/quickstart-python) tutorial comes in handy, yet I only manage to complete the steps for adding files to the project.
This is our current Dockerfile:
```
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "milestone_2\project2_main.py"]
```
Besides this, we have a .dockerignore file and a new requirements.txt file. For some reason, the requirements file is empty. I'm not sure why, it was auto-created. I wanted to keep it this way and change it if it causes a problem.

The next step wants me to add the following command underneath the `EXPOSE` statement: `ENV` where `KEY` is `VAR1` and `VALUE` is `10`. We don't have a expose statement and I don't understand the rest of the tutorial. 

I tried to set up a public repository on **Docker Hub**, but wasn't able to push any files on it. The link can be found [here](https://hub.docker.com/repository/docker/benemrxr/toolkits/). Maybe this comes in useful for our next milstone. 

I tried to run the Dockerfile with various commands but non seemed to work. I tried to run an image I created called `toolkitsarchitectures` and tried to run this with `docker run toolkitsarchitectures` but received the following error message: 
```
> Executing task: docker logs -f a33926fb7996e044012599898dc0c38d9caafadcd61a673b6e954182eaa80dab <

python: can't open file 'milestone_uild_model.py': [Errno 2] No such file or directory
```

## Little project riddle:
>- Can you decode this (the first team will get candy from us)?
aHR0cHM6Ly93d3cuZG9ja2VyLmNvbS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDE5LzEwLzIwMTgtSGFsbG93ZWVuLTIuanBnP3NzbD0x

While we weren't able to solve the last task (yet), I was able to decode the little riddle at the end of the assignement. I used my search engine to find an online decoding site and simply pasted the code in. The site I used was [base64decode.org](https://www.base64decode.org/). The encoded message is a nice picture on Docker! [Click here](https://www.docker.com/blog/wp-content/uploads/2019/10/2018-Halloween-2.jpg?ssl=1). Very cool! :jack_o_lantern:

### Issues:
- Dockerfile / Image / Container

### Outstanding: 
- Load the Dockerfile from the server. 

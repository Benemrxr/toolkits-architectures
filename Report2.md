# Milestone 2: Group Marxer, Kotatis, Rohrer
This report documents our progress for the second milestone.

## Task 1: 

We added the following files to ignore into our .gitignore file. We oriented ourselves on a recommendation of another .gitignore file in order to see which files could be helpful to have in our .gitignore. Since we do not have a computer science background, we do not necessarily know which kind of hidden files can appear in our git folders. Therefore we added the following list to our .gitignore:

*~   
All the files that end with the sign “~” these are backup files from Linux itself.

.fuse_hidden*  

Temporary files which can be created if a process still has a handle open of a deleted file.

.directory

KDE directory preferences. 

.Trash-*

The Linux trash folder which might appear.

.nfs*

.nfs files are created when an open file is removed but is still being accessed 


## Task 2:

A hash function is a function that can be used to map big sized data to fixed size values. The returned values are called hash values. These values are then used to index a so-called hash table. In the best case, each hash value stands for one bigger sized data part but there can also be collisions if one hash value stands for two different data parts. Hash functions are especially used in data storage and retrieval applications. It is used to store and access big amounts of data in a computationally and storage space efficient form. 

A Python module is basically a .py file which contains different functions, classes or variables. Packages however are kind of sets which contain multiple modules. The main difference between packages and modules is the existence of the __init__.py file. This file indicates that the directory contains a Python package and can therefore be imported in a similar way as modules. While modules contain basically just predefined functions, variables or classes, Python scripts are used to call these functions and build up the main code for the needed computing problem. 

A Docker container is basically a box that contains all the requirements for a certain programme. With the help of a Docker container, it is quite easy to run a certain application on another machine without installing a bunch of different requirements. An analogy for a Docker container can be a box with ingredients for a dish. The application is the recipe for the dish. If you now want to let your friend try out the dish, you can send him only the box with the recipe and the ingredients in it. Now he has the possibility to prepare the dish without first buying all the ingredients. Everything is included in the box. Volumes make it possible to keep this data stored, even if the docker container is getting deleted. Volumes are further helpful to exchange data between the host computer and Docker containers. 

Primarily we would definitely prefer using Docker instead of virtual environments. Since virtual environments only encapsulate Python dependencies . Docker however encapsules the whole operating system and can therefore be used on every machine with every operating system. So we can say that a virtual environment can be used if we use the same operating system on the opposite machine. If this is not the case, we should use Docker instead. 



## Task 3:

Our python code is already able to load data from Keras and to train (fit) a neural network. Because of that, we did not have to make any changes regarding these questions. The first thing we had to care about, was to save the fitted model in a .h5-file. We did this with the help of the command model.save("my_h5_model.h5"). 

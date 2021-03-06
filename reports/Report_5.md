# Milestone 5: Group Marxer, Kotatis, Rohrer
Hey! :wave: This report documents our progress for the final milestone number :five:

## Structure:
- Task 1
- Task 2
- Deliverables
- Misc



## Task 1: 
> **Describe how you might use the tools you learned in this course to develop a
data-driven product.**
> - How can you train a predictive model? How could you manage experiments,
and create reports/visualizations while training your model

To develop a data-driven product, we can train predictive models. In this course, we got to know the Tensorflow framework and the Keras library, which we can use to build and train predictive models. For our projects, we got assigned a codebase from the Keras-team, with binary data. 

We could manage experiments with the Weights & Biases tool, where we played around with our model, adjusted parameters and measured the changes. You can check out our runs [here](https://wandb.ai/janikrohrer/Project_3?workspace=user-benemrxr).

Using the Jupyter Notebook tool, we could create reports/visualizations while training our model. You can check out our .ipynb file in the repository. We can use the Markdown language to add explanations in our notebook and use it to create project reports, such as this document. 

> - How can you improve collaboration in a team?

We got to know quite a few tools to improve collaboration in a team. I remember, that in previous courses, we used file hosting services such as OneDrive to share files and messaging apps such as WhatsApp for coordination. Appropriate for small group tasks, but quite cumbersome for bigger projects, when multiple people make changes to the shared documents. 

Over the last months, we were introduced to Slack, a channel-based messaging platform, where a workspace was set up for the course communication. We continued to use the application for coordination within our group, as it was easy to set it up simultaneously on our main operating system and the virtual machine, and to share the feedback documents. For quick messages, we used a group chat on WhatsApp. The use of Slack definitely improved the coordination and collaboration in our team, and we are confident in making use of Slack or a Slack-like tool if we were to develop a data-driven product.

For the actual project work, we were introduced to Git and the GitHub platform. GitHub is a code hosting platform for version control, using Git. A big improvement over sharing files on a cloud service! We stored all required code files in our public repository, as well as the project report documents, written in Markdown, so that we can write the reports simultaneously and independent from each others progress. To develop a data-driven product, we would surely make use of GitHub for code versioning and review.

> - How would you assess and ensure the quality of your code?

We were introduced to the Python Enhancement Proposals in this course. The [PEP 8](https://www.python.org/dev/peps/pep-0008/) is a style guide for Python code, through which we can ensure some consistency and therefore readability. Code is read much more often than written, so a consistent style is greatly needed when we go over the code to assess its quality. In another course in this semester, we were looking at Python docstrings and their high-level structure: what they should contain and how they should be written. If we were to develop a data-driven product, it would be smart to take proper use of docstrings, adhering to the [PEP 257](https://www.python.org/dev/peps/pep-0257/) on docstring conventions.

Further, we can use software testing methods to ensure the quality of our code. We could start out with black-box testing, as based on the docstring specification, and also glass-box testing by going through the potential paths of the program. We can do this at the unit level, followed by integration testing. 

If there are any flaws that arise in testing, we can use debugging methods to fix them. For example, we add print statements mid-code, to narrow in the location of the bug. Better yet, we can use assertions as a defensive programming tool, to confirm that the arguments to a function are of appropriate types. Or to confirm that intermediate values have the expected values or that a function returns an acceptable value.

If we want to improve the quality even further, we could try to improve the performance of our programs and their implementation. The former, using the WandB tool, for example.

> - How can you provide data to the model at inference time and save its
predictions to analyze the model’s performance in a real-world scenario?

In real-world scenarios we often encounter with confidential data, in which we first would need to build the model using already existing test data and then train on premise our model with the real data set. In our case gladly reviews are not confidential (as far as we know). 

To provide data to the model, we could either scrape more reviews from the internet and read them in the model, or we could also let other people give input to the model (e.g they write a review directly to our web app). Either way after we got the data, we would first have to pre-process the new data acquired (since our model vectorizes the words, we would need to apply the same method on the new data). We could then save our predictions and analyze the performance (in the 2nd option in which people could give input directly, we could have a text field in which they could write a review and another field in which they could choose whether their intention was to write a positive or negative review and we could use these as our performance measurement).

> - How can you improve on the model iteratively and deploy it to customers in
a web application. How could you structure your product as a microservice
architecture

Our model uses 2 epochs, meaning there are 2 iterations to build the model (more epochs don’t really improve metrics and could even lead to overfitt will worsen). If with iteration is meant the process of iterating whole models (and not just iterating in the model), then we need to know how we can get feedback from a model in production. We have to monitor our model in order to recognise performance depreciation, data skew, etc. and managing model versioning as well as rolling out new models. The new models should be obviously properly tested before replacing it with the old one. In this way we can always have a running model for our customers, without them even noticing of a potential problem. (In our case we probably aren't that much affected, e.g the word "good" gets a totally different meaning and therefore our model would predict falsely; of course semantics is a challenge, like detecting irony).

We can use flask as a tool to deploy it as a web application for our customers. We would have backend and front end as our architecture (backend: our model, flask, docker, DB; frontend: web app and its UI, docker, nginx). A great benefit of using microservices is, that they loosely connect via APIs to form a microservices-based application architecture. This architecture offers greater agility and pluggability because we can develop, deploy, and scale each microservice independently.

> - Describe the process step by step with the example of an E-mail spam
detector. Assume you want to provide a service where customers can send
their E-mails to (f.e. a web page where you can upload E-mail text). The
service responds with either “Spam” or “No Spam”. Which tools would you
use for each step in the process until the response ends up at the
customers’ screens? Also describe what metrics you might use to find out
whether your model works (f.e. would you focus on Precision or Recall?
Etc.)

If we want to provide a web site that checks whether an uploaded E-mail might be spam or not, we can create a Python program in the background (back-end), with a binary classifier model. We can use Flask to assure a front-end environment that handels RESTful requests. With Docker, we can deploy the Flask web application. Moving along, we can add Gunicorn, a production-grade WSGI server, and then add Nginx to act as a reverse proxy for Gunicorn to handle client requests. Step-by-step :e-mail::

1) We begin by building a binary classifier model, to check whether the uploaded email might be spam or not. We use Python and ideally have some (lots of) email data ready. We then classify the emails manually as spam or no spam, so that we have labeled data to train our model. Our model might be based on a k-nearest neighbor algorithm, where an object is classified by a plurality vote of its neighbors. Knn is thus a supervised learning algorithm. We take advantage of the research in the field of classification algorithms, specifically this paper from [Dada et. al, on Machine learning for email spam filtering: review, approaches and open research problems](https://doi.org/10.1016/j.heliyon.2019.e01802).

2) Next, we assess the quality of our model and try different modifications. We measure the metrics of our choice on the Weights and Biases site and track the experiments in a Jupyter Notebook, which we share for our team on GitHub. We would use GitHub just like in the projects of this course, but maybe we won't share all the details of the code with the public - otherwise spammers could take advantage of it!
Back to the metrics. A very popular metric for performance evaluation of classification is classification accuracy, measuring the percentage of correctly classified messages. It has however been highlighted that using Accuracy as the only performance indices is not sufficient. A typical user might have only few spam mails, compared to the amount of normal mail he receives. So classifying all mails as non-spam would leave us with a high accuracy, but no actual use as a filter. We need to take other measures into account, such as recall and precision. Recall would measure the ratio of correct spam to the sum of true spam, whereas spam precision would measure the ratio of correct spam to all classified spam. Recall can be deemed as the comparative number of spam messages that the filter succeeded in preventing from entering email inbox. This shows how the model handles spam messages. Precision shows the reliability of the filter, takes into account how many non-spam were falsely classified. This error is very important to avoid, as the cost of false positives is much more than that of false negatives. Cost sensitivity should be considered, and it is worth checking out the weighted metrics suggested in the article from above.

3) Now, our model should be ready for implementation. We need to make sure that our scripts run on the server, so we dockerize them. Next, we deploy the Flask web application. Moving along, we can add Gunicorn, a production-grade WSGI server that functions as a gateway to the web server and Flask. Then we add Nginx to act as a reverse proxy for Gunicorn to handle client requests as well as serve up static files.


## Task 2:
> **Use Flask to make your model available through a web application. Your code
should:**

> - Initialize everything

In order to make our code as structured as possible, we decided to implement a 'init()' function to set up everything we need for this task. Our goal was to first check, whether our model is already stored somewhere as a .h5 file. If not, we load our imdb data, build our model and save it as .h5 file. This way, our model has to be build only for the first time and we can load the .h5 file for all the following runs. 

Before we were able to build up our model, we rearranged our 'load_sample_data()'function in our model.py file, in order to use all of the data to build up our model (compared to our last milestone). Once we had done this, we used a simple if-else condition to check whether the model was already stored or not. If the model does not exist, we build a new one and save it as .h5. If it does exist, we simply load it from the path. 

We further used our init() function to connect to our PostgresSQL Database. Therefore we used our 'connect()' function, which we also defined in our previous task.

> - Accept a HTTP POST Request at “localhost:<port>/predict” (the route you
should implement with Flask). The body of the POST request contains a
sample of your data set (an image, time series data or text data, etc.).
Think about how you have to encode your data (Base64? JSON? Etc.).

First we build up the basic Flask framework, we found on the internet, inside our 'main.py'. We defined the host as "0.0.0.0 (localhost) and startet to define two functions in our web app:

1. predict ():

The predict function is the main function which accepts the POST request at /predict. We further defined 'methods=['POST']' in order to accept POST requests only. 

2. index():

The second function is not expected in the task, but we wanted to try our best to avoid errors. Therefore we implemented this function, which catches the case if someone makes a call to root. For this case, we simply redirect the user to '/predict'. 

> - How to encode our data?

In order to send a test sample to our application, we decided to encode our data with JSON. We choose JSON, because this was the only encoding method that we have already heard of. To encode and decode our data, we import the python module 'json'. We decode the data we get from the POST request and convert it to a numpy array with the command:

```
np.array(json.loads(request.data))
```

Numpy arrays are the type of data which can be used to "feed" our sample data to our ML-model. Thats why we used a numpy array here. 

> - Within the predict route, you should load your .h5 model with Keras

As described above, we decided to load (or build) our ML-model inside of our 'init()' function. So, we are already able to access the model inside of our predict route. 

> - Perform inference on your model with the data provided in the Body of the
POST Request (you need to transform the data to its proper representation
so you can feed it into the loaded Keras model)

In order to feed our model with the provided data, we first had to transform it to a 2D numpy array. This is the represantation which our model is able to use. As explained above, we implemented this process to the function where we loaded the provided data. We then assigned this numpy array to the variable "data". To make the predictions with our model, we simply feeded this numpy array to our model with:

```
 mlmodel.model.predict(data)
```

We then assigned the predictions, which are also stored as a numpy array to the variable "predictions" in order to use them in the following steps.

> - Save the prediction to a PostgreSQL DB (only the prediction. This means
you only need one table, that has an ID and the predicted label/value)

For the use of the database, we already have many useful functions created in our previous milestones. Before we started to use them, we wanted to simplify the use of these functions. Therefore we formed a class called 'Database()'. One step further to achieving a good pratice. 

We first created the database inside of our 'init(). Therefore we use the function 'create_database()', which we already defined in our last milestone and is now part of our Database-class. We then close the connection again and re-connect to the created database.

To create the new table as expected in the task, we transformed our function from the last milestone so that it creates the table as described in the task. We further renamed this updated function as 'create_predefined_table()' to avoid misunderstandings. Finally, we called this function inside of our predict route. 

To insert our predictions into our created table, we again had to serialize our data, as always when working with the database. Therefore, we also had a function created in a previous milestone, which we could simply import and use. This 'serializer()' function makes it possible to save the data in our database, since PostgreSQL is not able to store numpy arrays. We then used the serialized array as a parameter for our 'insert_predictions()' function and store the predictions into our database.

> - Return the prediction to the sender of the HTTP POST request

To send the data back, we had to encode it as JSON again. We use therefore the function 'json.dumps()'. But here we got into troubles, since it is not possible to send numpy arrays in the JSON format. With the help of the internet, we found a solution for this problem. We used the function 'tolist()'to transform our numpy array to a python list. We used this list as a parameter for the 'json.dumps()' function. This way we were able to send our predictions back to the user. 

> - There should be two Docker container communicating with each other (your
Flask app, and the PostgreSQL DB). Use docker-compose to start both
containers

Basically, we need to create two containers here. One for the Flask app and one for our database:

1. Flask App

For our flask app, we had to create a Dockerfile to run the Python script on a Docker-container. Therefore we used previous dockerfiles as a template. Since we are working with Flask, we had to add one expression to our Dockerfile:

```
ENV FLASK_APP=/src/main.py
```
This is used to tell Flask, which file has to be used as entrypoint. 

We saved this Dockerfile in the same direction as our web application. This way, we could later on run the container from our "docker-compose.yml" file. 

We then created our "docker-compose.yml" file. As well as for the previous Dockerfile, we used the file from the last milestone as a template. We first added a new service (pyapi) to build up and run our Dockerfile which we created for the web-application. We added the depends_on attribute to be sure, that this container waits until the database is build up. We did this to avoid errors, that occur because the database is not ready. 

For our database, we simply used the same expressions as we did in our previous milestone, since the database itself has not fundamentally changed. Only the tables inside of the database are new.

During our first test as a whole, we got the following error:

```
ERROR: The Compose file './docker-compose.yml'is invalid because: network.internal value 'enable_ipv6' does not match any of the regexes: '^x-'
```
After a few minutes of googleing and tryout, we found the solution for our problem. We changed our driver from "overlay" to "bridge" in order to run docker-compose in the single mode instead of the swarm mode. Now it worked quite well.

 
> Write a script that uses the "request" library to extract a sample and sends a HTTP POST Request.

To get a prediction for a sample, we first need a sample of the data which can then be used for our prediction. Therefore we created the function 'load_imdb_sample()' We wanted to be able to tryout different samples. We build up the function in a way that makes it possible for us to pick a specific sample by the index (Parameter "start").
We then called this function we defined in the same script with the value 373. This gives us the 373th datapoint of the whole imdb datapackage. This is our sample, that we can send to predict. However we can always change this number to get different predictions.

In order to send this sample to our web application, we again had to encode it in the same way as we did it before. We again used the function: 

```
json.dumps(sample.tolist())
```
This way we kind of "prepared" the sample to be sent. This is also the dataformat we recive on the other side and transform to the numpy array (as you might remember). 

Finally everything was ready to go for the HTTP POST request. For the request, we used the following function to make a POST request with the data we prepared before:

```
response = requests.post(endpoint, data = data)
```
The endpoint here was defined as 'http://localhost:80/predict'.
We were then able to write the last command to printout the response we should get (hopefully a prediction). Therefore we used the following function:

```
print('Response (took %ss): %s' % (response.elapsed.total_seconds(), response.text)) 
```
We further built in a time measurement to tell how long it took to get the response. Now everything was set up and we made our first attempt to run our request. 

As expected: ERROR!

"listen tcp 0.0.0.0:80: bind: adress is already in use".

To be honest, we had no idea how this could have happened but something blocked the port 80. We decided to solve this problem in the most basic way we knew: To change the port to 81. Of course we also had to change the port for the application inside of our "docker-compose.yml" file. After we did this, everything worked well and we were able to successfully print out the result of our prediction. 

Voila our web application works!!

Last but not least, we put all of our dependencies into a "requirements.txt" file, which can be used to quickly install all the necessary dependencies at once.

## Deliverables:
- Check the three requirements before submitting the project: 
- [x] Run ‘docker-compose up’ to start applications
- [x] Create a virtual environment based on our requirements file
- [x] Run the Python script that sends the HTTP POST Request. A print of the prediction of our model is expected

## Misc:
- [x] Cleaned up Git Repository / folder structure. Three folders :file_folder:: reports for the report documents, experiments for the Jupyter Notebook files that we used to train our models, and a src folder for all the code. We have a subfolder structure in the src folder, but we can change that for the final deliverable, if that is not recommended. 
- [x] Improve GitHub community profile, add README etc. as recommended by GitHub. -> will be done for the final submission :clipboard:

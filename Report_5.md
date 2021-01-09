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

**_additional tools?_**: Python Notebooks? Weights & Biases? Docker?

> - How would you assess and ensure the quality of your code?

We were introduced to the Python Enhancement Proposals in this course. The [PEP 8](https://www.python.org/dev/peps/pep-0008/) is a style guide for Python code, through which we can ensure some consistency and therefore readability. Code is read much more often than written, so a consistent style is greatly needed when we go over the code to assess its quality. In another course in this semester, we were looking at Python docstrings and their high-level structure: what they should contain and how they should be written. If we were to develop a data-driven product, it would be smart to take proper use of docstrings, adhering to the [PEP 257](https://www.python.org/dev/peps/pep-0257/) on docstring conventions.

Further, we can use software testing methods to ensure the quality of our code. We could start out with black-box testing, as based on the docstring specification, and also glass-box testing by going through the potential paths of the program. We can do this at the unit level, followed by integration testing. 

If there are any flaws that arise in testing, we can use debugging methods to fix them. For example, we add print statements mid-code, to narrow in the location of the bug. Better yet, we can use assertions as a defensive programming tool, to confirm that the arguments to a function are of appropriate types. Or to confirm that intermediate values have the expected values or that a function returns an acceptable value.

If we want to improve the quality even further, we could try to improve the performance of our programs and their implementation. The former, using the WandB tool, for example.

> - How can you provide data to the model at inference time and save its
predictions to analyze the model’s performance in a real-world scenario?

In real-world scenarios we often encounter with confidential data, in which we first would need to build the model using already existing test data and then train on premise our model with the real data set. In our case gladly reviews are not confidential (as far as we know). 

To provide data to the model, we could either scrape more reviews from the internet and read them in the model, or we could also let other people give input to the model (e.g they write directly on our web application a review). Either way after we got the data, we would first have to pre-process the new data acquired (since our model vectorizes the words, we would need to apply the same method on the new data). We could then save our predictions and then we could analyze the performance (in the 2nd option in which people could give input directly, we could have a text field in which they could write a review and another field in which they could choose whether their intention was to write a positive or negative review and we could use these as our performance measurement).

> - How can you improve on the model iteratively and deploy it to customers in
a web application. How could you structure your product as a microservice
architecture

Our model uses 2 epochs, meaning there are 2 iterations to build the model (more epochs don’t really improve metrics and could even lead to overfitting and even worsen). We can use flask as a tool to deploy it as a web application for our customers. We would have backend and front end as our architecture (backend: our model, flask, docker, DB; frontend: web app and its UI, docker, nginx). A great benefit of using microservices is, that they loosely connect via APIs to form a microservices-based application architecture. This architecture offers greater agility and pluggability because we can develop, deploy, and scale each microservice independently. We could have a microservice in (todo: thinking of some plausible microservices)

> - Describe the process step by step with the example of an E-mail spam
detector. Assume you want to provide a service where customers can send
their E-mails to (f.e. a web page where you can upload E-mail text). The
service responds with either “Spam” or “No Spam”. Which tools would you
use for each step in the process until the response ends up at the
customers’ screens? Also describe what metrics you might use to find out
whether your model works (f.e. would you focus on Precision or Recall?
Etc.)

If we want to provide a web site that checks whether an uploaded E-mail might be spam or not, we can create a Python program in the background (back-end), with a binary classifier model. We can use Flask to assure a front-end environment that handels RESTful requests. With Docker, we can deploy the Flask web application. Moving along, we can add Gunicorn, a production-grade WSGI server, and then add Nginx to act as a reverse proxy for Gunicorn to handle client requests. Step-by-step:

1) We begin by building a binary classifier model, to check whether the uploaded email might be spam or not. We use Python and ideally have some (lots of) email data ready. We then classify the emails manually as spam or no spam, so that we have labeled data to train our model. Our model might be based on a k-nearest neighbor algorithm, where an object is classified by a plurality vote of its neighbors. Knn is thus a supervised learning algorithm. We take advantage of the research in the field of classification algorithms, specifically this paper from [Dada et. al, on Machine learning for email spam filtering: review, approaches and open research problems](https://doi.org/10.1016/j.heliyon.2019.e01802).

2) Next, we assess the quality of our model and try different modifications. We measure the metrics of our choice on the Weights and Biases site and track the experiments in a Jupyter Notebook, which we share for our team on GitHub. We would use GitHub just like in the projects of this course, but maybe we won't share all the details of the code with the public - otherwise spammers could take advantage of it!
Back to the metrics. A very popular metric for performance evaluation of classification is classification accuracy, measuring the percentage of rightly classified messages. It has however been highlighted that using Accuracy as the only performance indices is not sufficient. A typical user might have only few spam mails, compared to the amount of normal mail he receives. So classifying all mails as non-spam would leave us with a high accuracy, but no actual use as a filter. We need to take other measures into account, such as recall and precision. Recall would measure the ratio of correct spam to the sum of true spam, whereas spam precision would measure the ratio of correct spam to all classified spam. Recall can be deemed as the comparative number of spam messages that the filter succeeded in preventing from entering email inbox. This shows how the model handles spam messages. Precision shows the reliability of the filter, takes into account how many non-spam were falsely classified. This error is very important to avoid, as the cost of false positives is much more than that of false negatives. Cost sensitivity should be considered, and it is worth checking out the weighted metrics suggested in the article from above.

3) Now, our model should be ready for implementation. We need to make sure that our scripts run on the server, so we dockerize them. Next, we deploy the Flask web application. Moving along, we can add Gunicorn, a production-grade WSGI server that functions as a gateway to the web server and Flask. Then we add Nginx to act as a reverse proxy for Gunicorn to handle client requests as well as serve up static files.


## Task 2:
> **Use Flask to make your model available through a web application. Your code
should:**
> - Accept a HTTP POST Request at “localhost:<port>/predict” (the route you
should implement with Flask). The body of the POST request contains a
sample of your data set (an image, time series data or text data, etc.).
Think about how you have to encode your data (Base64? JSON? Etc.).

> - Within the predict route, you should load your .h5 model with Keras

> - Perform inference on your model with the data provided in the Body of the
POST Request (you need to transform the data to its proper representation
so you can feed it into the loaded Keras model)

> - Save the prediction to a PostgreSQL DB (only the prediction. This means
you only need one table, that has an ID and the predicted label/value)

> - Return the prediction to the sender of the HTTP POST request

> - There should be two Docker container communicating with each other (your
Flask app, and the PostgreSQL DB). Use docker-compose to start both
containers

## Deliverables:
- Check the three requirements before submitting the project: 
- [ ] Run ‘docker-compose up’ to start applications
- [ ] Create a virtual environment based on our requirements file
- [ ] Run the Python script that sends the HTTP POST Request. A print of the prediction of our model is expected

## Misc:
[ ] Improve GitHub community profile, add README etc. as recommended.

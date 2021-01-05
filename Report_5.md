# Milestone 5: Group Marxer, Kotatis, Rohrer
Hey! :wave: This report documents our progress for the final milestone number :five:

## Structure:
- Task 1
- Task 2
- Deliverables



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

> - How can you provide data to the model at inference time and save its
predictions to analyze the model’s performance in a real-world scenario?

> - How can you improve on the model iteratively and deploy it to customers in
a web application. How could you structure your product as a microservice
architecture

> - Describe the process step by step with the example of an E-mail spam
detector. Assume you want to provide a service where customers can send
their E-mails to (f.e. a web page where you can upload E-mail text). The
service responds with either “Spam” or “No Spam”. Which tools would you
use for each step in the process until the response ends up at the
customers’ screens? Also describe what metrics you might use to find out
whether your model works (f.e. would you focus on Precision or Recall?
Etc.)



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
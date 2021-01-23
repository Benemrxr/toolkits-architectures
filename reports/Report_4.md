# Milestone 4: Group Marxer, Kotatis, Rohrer
Hey! :wave: This report documents our progress for the milestone number :four:

FYI: Our final branch (*feature-project-4*) was not a clone but a copy of the *master* branch. This led to us being unable to do a pull request. We created a new branch (*release4*) for the pull request, which is created as one commit on top of the master branch. If you are interested in the commit history, check out the old *feature-project-4* branch. Next milestone, we'll be more careful in this regard.

## Structure:
- Before we start
- Task 0
- Task 1
- Task 2
- Task 3

## Before we start
Our last reports and files were lacking some finishing, as we were always busy with the main tasks, right up to the deadline of the assignments. For this milestone, we want to take better care of the rules regarding *branching strategy, pull request review, SHA256 digest of the packages in the requirements file, PEP8 and the pinning of versions in Docker images*.

- [x] branching strategy

No more direct pushes to the master branch in this milestone, only reviewed pull requests. 
- [x] pull request review

Pull requests to merge changes from our feature branches with the master branches will be reviewed by at least one group member, and a quick comment is required before accepting the request. 
- [x] All versions in the pip "requirements file" are pinned
- [x] No python packages are installed with superuser rights
- [x] SHA256 digest

We can get the SHA256 digest, which is an encrypted signature, from the **Python Package Index** `PyPi`. We select our specified package version, for `Tensorflow 2.3.1` and then see the hashes by the download files. Unfortunately, every system specification and python version has a different hash, so if we activate the hash-checking mode in the **requirements.txt** file, we would need to make sure that all the potential setups for our project are included. This could look the following way:
```
Tensorflow == 2.3.1 --hash=sha256:87750a476aa6f76b3aad5e6182faf2a3036a3d4c0db3b6d7463ebbaf4b184a23 \
                    --hash=sha256:cdce1f71f592d840dd3e05b67f1010f616311d9856250ff772db537f39ef2992 \
                    --hash=sha256:87b62ab25816597a5e5352604b383b292eafd19a33ae7848b5275ea74fc4da1d
```
Now, it should work for the most common operation systems using `CPython version 3.8`. We can do the same for our other required package, `psycopg2-binary`. As requested in the assignment, the SHA256 is `2dac98e85565d5688e8ab7bdea5446674a83a3945a8f416ad0110018d1501b94`, for the `psycopg2_binary-2.8.6-cp38-cp38-manylinux1_x86_64.whl` file.
Ressources: [pypa.io: hash-checking](https://pip.pypa.io/en/latest/user_guide/#hash-checking-mode) and [install-require-hashes](https://pip.pypa.io/en/latest/reference/pip_install/#install-require-hashes).

- [x] PEP8

No complaints regarding PEP8, so I assume our Python code is PEP sytle conforming.
- [x] Version pinning in Docker

We import two Docker images, postgres and pgadmin. The former was already pinned in the docker-compose.yml file, the later is now also pinned to the *latest* tag.
```
postgres:
    image: "postgres:12.4"
  ...  
pgadmin:
    image: "dpage/pgadmin4:4.28"
```

## Task 0: 
> Finish remaining Tasks from Milestone 3 in case your deliverable does not work.

In order to make it possible for us to correct most of the weaknesses of our older milestones, we decided to ask a friend of us which is more into coding. Although, he is not an educated computer scientist, but posesses a little bit more experience than we do. Toghether with him, we improved different things to make our code running and also to kind of clean our code and implement "better practice". 

1. Created classes and modularized our code further

We first took our code and implemented classes. For example we created a class `MlModel`, which contains all the attributes and methods to create, save and load our model. For better practice, we substituted our print() functions with logging.info() functions. This was a tip we got form our friend and since we would like to learn the best possible practice, we decided to implement these functions into our scripts. We further added several except-mechanisms to catch possible errors where they are most likely to occur. 

2. Created module `dbconnect.py` to handle connect to and close the database

We then created a seperate python script with a class `Database`. In there, we basically defined two differend methods. The first one connects to the database and the second one closes the database once again. We can later adress these functions in our-script to simply access the database.

3. Created module `dbactions.py`

Inside of this module, we defined different functions in order to make extractions and insertion of our input- and prediction data into our database easier. We further added functions to create the database and tables. One special function, that we would like to point out here is the `check_database_exists` function. This function makes it possible for us to check, whether the database was already created. This helps us to avoid problems with duplicates. We later implement this function into our main script in order to check, whether the database already exists.

4. Serializer and Deserializer

Since we were not able to insert our 2D Numpy-arrays directly into the database, we had to come up with an idea. With the help of our friend, we were able to create the module `serialize.py`. Inside of this module, there are two functions defined. The first one takes the array and converts it into binary strings ("BYTEA" Data Type in PostgreSQL). This datatype can then be added to our database. 
On the other hand, we also want to extract data from our database in order to make predictions. We therefore did kind of the same thing backwards and defined it as the deserializer-function. 

5. Merge our modules into our `main.pyTF_CPP_MIN_LOG_LEVEL=2

After we defined all of our functions, we were able to arrange our `main.py` script new. We merged the functions according to Task 2 in the previous milestones. So that our main-scrip should now execute all the necessary steps correctly from milestone 3. 

6. Making it work with Docker-Compose

The biggest challange so far would be, to make it all work with docker-compose. We therefore split our project into two "sub-processes". The first one in the folder called "pyml" is responsible for building up our model and save it as a .h5 file. With the help of this "sub-process" we do not have to upload our model manually on git-hub, we can run this process in our docker-compose. To do so, we created a Dockerfile for this process similar to the one, which already worked before.  

The second sub-process contains the required steps in task 2 from the precvious milestone. We therefore created the folder "pypredict". In there, we added all the necessary python scripts we created before. We also created a Dockerfile in order to run these files in a seperate container. To make the whole thing more understandable, we created a source folder in each of our sub-process-folders, where we added all the scripts, modules and also our requirement files (also aiming for "best practice"). 

Finally we were able to improve our `docker-compose.yml`. In there we did not have to do so many changes, since our previous was already quite good. We just made it working with our organization of the scripts and modules. We further added networks. We did this also aiming for "Best-practice". Since our friend suggestet this to us for security reasons. We further added the environment-command:

```
TF_CPP_MIN_LOG_LEVEL=2
```
This command disables Tensorflow messages, which also contributes to a better overview.

7. Pyjokes

Last but not least, we also adjusted our pyjoke exercise with the help of our new, predefined functions and classes.


We were then ready to run the whole process with docker-compose and it WORKED!!! Even though, we do not necessarily know if it worked 100% correct. 

## Task 1: 
> Get a free account at Weights and Biases (https://www.wandb.com/).

We aren't sure at this time whether we should set up a single account and share the login credentials, so to start this task we set up individual free acocunts at `Weights and Biases`, linked to our GitHub account. 

> **Answer the following questions:**
> - What is Experiment Management and why is it important?
In the context of machine learning, **Experiment Management** is a process of tracking research experiment metadata, which can be grouped in *knobs* and *watchlists*. The former includes things that we continously change or that get changed automatically, such as the code (f. e. model architecture) and our datasets (f. e. changes in the data). *Watchlists* hold evalution metrics such as accuracy. To keep an overview we need to track and organise them in a meaningful way, and make them available to access and collaboration with our team. 

To understand why this is important, we imagine how an experiment process could look like. We want to test a hypothesis, in the context of machine learning a predictive model. As we try to improve our model, we make changes to the model architecture, to hyperparameters and even to the datasets. We can measure the effect of such changes with comparable metrics such as an accuracy metric, and use it to visualize and compare the different setups. This is important so that we can keep track on what we have tried so far and find out what worked best for our predictive model. Without a good experiment management, we would quickly run into trouble as the experiment complexity grows, not to mention as complexity grows in a team collaboration setting. `Weights and Biases` is a popular tool for experiment management for deep learning. 

> - What is a Metric in ML?
Metrics are performance indicators and allow us to compare experiment outcomes. We want to find the best model, that is the model that is the most reliable to make good predictions on new unseen data. There are a number of techniques available to evaluate if a classification algorithm did a good job. We can group them into confusion matrix-based performance measures and methods of visual model evaluation, which we will examine more detailed in the next questions. 

One metric I want to quickly explain is **accuracy**, where the evaluation focus lies on the overall effectiveness (success rate) of a classifier. It tells us how often, overall, the classifier is correct. To calculate this metric, we take the sum of all correct predictions and divide it by the total number of predictions. It is the reverse of the **error rate**, which tells us how often, overall, the classifier is wrong. The calculation of these metrics is very apparent with the help of the confusion matrix, which we will also check out in the following questions. 

To conclude this task, we always have to be **careful** with the interpretation and selection of such metrics. A *good* accuracy is a high one (near 1), but whether the predictive model is useful or not depends on the context of the task. Say we want to classify spam emails, and our filtering model classifies all 1'000 mails as spam, the accuracy would be very high if only 10 emails were non-spam. But obviously, this would not be a useful model! :e-mail:

This example holds especially in unbalanced datasets, where the number of cases in one class is significantly higher than in the other, as the confusion matrix only tells us how the classifier is behaving for individual classes.

> - What is Precision and Recall? Why is there often a Trade-off between them?
**Precision** is the chance of having the positive condition among those that test positive. It is also called the **Positive Predictive Value (PPV)** and is calculated as the number of true positives over the sum of all positives. *When the model predicts positive, how often is it correct?*

**Recall** evaluates the effectiveness of a classifier to identify positive labels. Also denoted as **Sensitivity** or the **True Positive Rate (TPR)**, it is calculated as TP over TP+FN, the number of true positives over the total of all actual positives. It is also a measure of positive identification. *When it is actually positive, how often does it predict positive?*

In an ideal scenario there is a perfectly seperatable data, both recall and precision can get the maximum values of 1.0. But usually, this is not the case as there is some noise and uncertainty in the data. There might be some points of positive class closer to the negative class and vice versa. In such cases, shifting the decision boundary can either increase the recall or precision but not both. Increasing one parameter decreases the other, we will always miss classify some points, that is classify a point from a negative class as positive and topsy-turvy. That is the **trade off** between the fractions of correct positives among the total predicted positives (precision) and among the total positives (recall). 

> - What is AUROC Metric?
The performance of a classification model can also be evaluated graphically. One common visual model evaluation is the **ROC curve**. ROC stands for **R**eceiver **O**perating **C**haracteristic. ROC curves are used to see how well the classifier can separate positive and negative examples and to identify the best threshold for seperating them. They visualize the tradeoff between sensitivity (Recall, as described above, the True Positive Rate) and the False Positive Rate (1-Sensitivity) in a binary classifier. Usually, FPR is on the x-axis and TPR on the y-axis, and the *45 degree line* gives us a *random guessing performance*. We want to keep FDR as low as possible and TRP as high as possible and therefore maximize the **A**rea **U**nder the **ROC** curve, the **AUROC** metric. 

Back to the ROC: We run the classification algorithm on the data and assign the probability of belonging to class 1 to each actual value. We then order the scores in decreasing order and assign cutoffs based on a selected interval, typically 10% intervals. We count the true positives and true negatives for each cutoff and calculate the true positive and true negative rate for each decile. We use these TP and TN rates to draw the ROC curve. It can be used to compare multiple classifiers, as the performance is better the tighter the curve hugs the axes. 

As this might be difficult to guess from simple graphical comparison, we can calculate the AUC by adding up the area of all rectangles below the ROC curve. The higher the AUC, the better is the model in question.

We can select the optimal cutoff value by drawing the **accuracy line** into the graph, through the outermost point (i.e. the point closest to TPR=1 and FDR=0) with the slope alpha of the accuracy line as the **ratio of neg/pos values**. To get the corresponding **accuracy**, we find the *intersection point* of the accuracy line and the *descending diagonal*. The accuracy, as calculated by (TP+TN)/N is the y-axis value of the point of intersection we just drawed in. 

From the AUC, we can derive the **Gini coefficient**, which normalizes the AUC so that a random classifier scores 0 and a perfect classifier scores 1. Gini above 60% indicates a good model, and is derived as *Gini = 2 * AUC - 1*, where accuracy = AUC. AUC provides a single measurement to compare across different models, where several cutoff values can be compared. But, as there are not only advantages, ROC curves show only the performance of binary classifiers and the AUC usefulness is questioned. [Lobo et al.](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1466-8238.2007.00358.x?casa_token=XbzRmWnAcm4AAAAA%3AD0FVgy_fRUYP8ZoKG-jAkLrFTw1HiRgpPLcD1DPAYXEiwgq7nxgVmPwnk7kOuN9qk4F8LloBsooMH6Kx4A) have a very popular and interesting paper, where they come to the conclusion to not recommend using AUC for five reasons, such as that it summarises the test performance over regions of the ROC space in which one would rarely operate).

> - What is a Confusion Matrix?
Back to the **confusion matrix**. Its name might be explained as to whether our model correctly identified the item or was *confused* with another label. It can be used for multi-class classifiers, but to explain it we can start with a two-class classifier (binary classifier), where our data contains information about actual and predicted values. 

Our matrix has four fields, as it is a special kind of **contingency table** with the two dimensions *actual* and *predicted*. Both dimensions have the two identical sets of classes, *positive* and *negative* in our context. The upper right field contains the number of true positive (**TP**) cases. Those are cases predicted to be positive that are actually positive. In the lower field on the left side we have the corresponding true negative (**TN**) cases. Above that the false positive (**FP**) cases, and in the last field the false negative (**FN**) cases. 

FP is also known as *Type I error*, cases predicted to be positive that are actually negative. FN cases are *Type II errors*, they are predicted to be negative but are actually positive. 

We can calculate the sum of the actual and predicted values, which is useful for several model evaluation metrics. Various measures can be derived from the confusion matrix. **Overall measures of performance**, such as the accuracy (TP+TN)/(TP+TN+FN+FP) and the error rate (FP+FN)/(TP+TN+FN+FP). Then, **measures of positive identifications** such as recall/sensitivity (TPR) and fall-out (FPP), a **measure of negative identification** such as specificity (TNR) and the false negative rate (type II error). 

The [Wikipedia entry](https://en.wikipedia.org/wiki/Confusion_matrix) of the confusion matrix has a well structured summary in table form, that gives us a good overview of the most model evaluation metrics, their calculations and their relations. 

## Task 2:
> Instrument your code with Weights and Biases (within a Docker container). Choose an appropriate metric for optimizing your ML Model. Reasoning behind it? 

We decided to use the metric **accuracy**. As explained in the answer above, it is calculated as the sum of all correct predictions divided by the total number of predictions. We can be confident with the result of this metric, as our dataset is perfectly balanced, and we can avoid the problem in the spam-filter example from above!

> - Login to W&B

Therefore we first had to look for the token of our W&B account. We finally found it on the link https://wandb.ai/authorize. We then created our .env file where we saved the token as follows:

```
WANDB_TOKEN=1515fcea400dc5ecfca6b99cf381c4fd94d7f726

```

We immediately added the .env file to our .gitignore and we further added some suggestions from the internet to our .gitignore in order to avoid future difficulties. We then created the docker_entrypoint.sh file equally to the example on the project sheet. After that, we created a Dockerfile as follows:

```
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


RUN apt-get update -y && apt-get install -y gcc

# Install pip requirements
ADD /src/requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
ADD /src /app


#Entrypoint
ADD /src/docker_entrypoint.sh .
RUN ["chmod", "+x", "docker_entrypoint.sh"]


# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
RUN chown -R appuser /home
USER appuser


CMD ["python", "test.py"]
```

We designed this Dockerfile similar to the one we built to run our project in the milestones before. In order to log in to W&B, we first added the docker_ entrypoint.sh file to our container. We then tried to run the File with the ENTRYPOINT function, which failed. With the help of google, we found out that the command `RUN ["chmod", "+x", "docker_entrypoint.sh"]` works to run shell scripts. This is the reason for the existence of the command in our Dockerfile. We spend a lot of time install the module `wandb` properly. We first got an error because of the dependency "psutsil" , which was unable to build up its wheel. We solved this problem with the help of the function `RUN apt-get update -y && apt-get install -y gcc`. Once this problem was solved, the next one appeared. We tried to import the wandb-module in our python script and failed badly again. We got a permission error for the folder "/home/appuser". We further solved this problem with the help of the following function: `RUN chown -R appuser /home`. Once this error was solved too, we were finally ready to add the next steps to our python script. 

> - Train a Model 

In order to train the model, we added our python scripts to the "/src" folder. This way, we can access the `build_model()` function in our new script. This worked quite well.

> - Save and upload the trained model

Things started to get difficult once again. We tried out to save our model with the function:
```
model.save(os.path.join(wandb.run.dir, "model.h5"))
```
This (what a surprise) did not work. We got an error, that we are not logged in to W&B, which meant, that we can start all over again. Something went wrong with the login. We tried to make our shell script run with the "ENTRYPOINT" command in our Dockerfile which now looks as follows:

```
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


RUN apt-get update -y && apt-get install -y gcc

# Install pip requirements
ADD /src/requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
ADD /src /app


#Entrypoint
ADD /src/docker_entrypoint.sh .

#ENTRYPOINT /docker_entrypoint.sh ; !/bin/bash
#ENTRYPOINT ["chmod", "+x", "docker_entrypoint.sh"]
ENTRYPOINT ["./docker_entrypoint.sh"]

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
RUN chown -R appuser /home
USER appuser


CMD ["python", "test.py"]
```
We then got the following error:

```
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \"./docker_entrypoint.sh\": permission denied": unknown.
ERRO[0003] error waiting for container: context canceled 

```
We were at a point, were we had no clue what could be the root of this error and neither how to solve it (Once again we spent a whole day for this without being a single step further). We then once more tried to adjust the whole thing. We substituted the ENTRYPOINT variable as follows:

```
ENTRYPOINT ["/bin/bash", "-c", "./docker_entrypoint.sh"]
```
We now got the following error:

```
python3: ./docker_entrypoint.sh: Permission denied
```
Since we had to wait for help on Slack, we logged in manually and proceeded with the script.

> - Log the value of the loss function (graphically)

It was quite challenging for us to find out the names of the loss function. Since we do not have many experience with ML itself and neither with Keras, most of these functions during the model building process were completely new for us. With help of the internet, we first tried out to implement the `wandb.log()` function and desperately searched a solution to find out how we could get the names of the metrics. Suddenly we found another approach. We learned about the `WandbCallback` from the `wandb` module. We learned that this function makes it possible to track the important metrics during the process. We then added 
```
callbacks=[WandbCallback()]
```
to our `model.fit()` function. With the help of this, we finally managed to make a successful run ("model_run"). We finally saw an output on wandb:

https://wandb.ai/janikrohrer/Project_3?workspace=user-janikrohrer

> - Log your metric (graphically)

Since we have choosen the metric accuracy, we did not have to make huge changes for this task. The reason for this is, that the `WandbCallback` includes the accuracy as default metric.

> - Try to play with your Neural Network.

In order to play with our Neural Network, we decided to adjust three parameters and execute three different runs and one default run for benchmarking:

- You can checkout our runs on: 
  https://wandb.ai/janikrohrer/Project_3?workspace=user-janikrohrer

# Interpret values further

 1. Default Run
 
As described above, we first started a run without changing a parameter ("model_run"). The slopes of this run can later be used for benchmarking. Lets have a closer look on our benchmark:

Δ-Metrics:
 - loss = -0,17
 - val_loss = -0,017
 - accuracy = +0,1
 - val_accuracy = +0,008

 2. Reduce hidden dimensions:

For the first run ("model_run_2"), we simply reduced the parameter `hidden_dims = 250` to `hidden_dims = 150`, so a decrease of 100 dimensions. We successfully ran the model and looked at the graph. We could observe the following changes in our metrics:
 
Difference to our benchmark model_run in the last epoch:
 - loss = -0,002
 - val_loss = +0,03
 - accuracy = -0,0019
 - val_accuracy = -0,0013
 
 As we can see, we only got minimal changes. But lets have a closer look to the run itself:

Differences between the epochs of model_run_2:
- loss = -0,175
- val_loss = -0,044
- accuracy = +0.1
- val_accuracy = +0,02

 In this run we can see the loss and val_loss decreases, and the other way round for the accuracy, where both metrics are increasing. This indicates a good training of the neural network, since we try to minimize the loss function and as long as the val_loss is not increasing (or stale) we won't overfit the neural network to the training data. Also accuracy and val_accuracy are both increasing, which is good. We can also interpret val_accuracy as a measurement on overfitting, since if the accuracy on the training data increases and the validation accuracy decreases (unseen data), then the model is overtrained on the training data. But as we saw before we only got minimal changes in the last epoch vs our benchmark run, so it is not of big importance.
 
 3. Increase Batch size
 
For the second run ("model_run_3"), we changed the parameter `batch_size = 32` to `batch_size = 52`, so an increase about 10. We also successfully ran the model and checked out the graphs:

Difference to our benchmark model_run in the last epoch:
 - loss = +0,03
 - val_loss = +0,005 
 - accuracy = -0,02
 - val_accuracy = -0,002

Also for the second run, we can see small changes. We got a higher loss value, but a decrease in the accuracy. 

Differences between the epochs of model_run_3:
- loss = -0,19
- val_loss = -0,01
- accuracy = +0,12
- val_accuracy = +0,004

Here more or less the same applies as in 2.

 4. Different Optimizer

For the last run, we decided to change the optimizer. We therefore exchanged our optimizer "adam" with the new one "ftlr". We successfully ran our fourth run ("model_run_4"). 

Difference to our benchmark model_run in the last epoch:
 - loss = +0,4
 - val_loss = +0,4 
 - accuracy = -0,3
 - val_accuracy = -0,38

In this run, we can observe the highest variation between this run and the default run. We can further observe, that in this run the curves are flat or lets say the differences between the epochs are so minimal that they are not really mentionable. In this case we really can see that the performance of this neural network is much worse than our default benchmark run. This neural network also does not really learn/train, since the metrics of its run stay the same. Also the accuracy of this neural network is around 50%, meaning we could simply replace this by just guessing.

## Task 3:

First we created a .ipynb file for the Jupyter notebook. Soon we realised that it was pretty tedious writing a Jupyter notebook via text editor. Thats why we used Anaconda to open and write in Jupyter, as it is more easy to use. There is not much to say for this task, we had a look at our dataset, found the most common and least common words used in the reviews and made some graphs. Most common words are, e.g "the", "and", "of", etc. which is not quite surprising. Another common word was "br", which we think is most probably because the review had HTML br tags and the Keras Dataset version left them in. There are also many words that appear only once, like "voorhees", "artbox", "copywrite", we are not sure what they mean except the latter, which is simply misspelled, so we are kinda happy to see that they only appeared once :)

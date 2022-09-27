# Concah Lab Project
## Keith L Baskerville Jr.
![conchalabs_iDentical+Logo+300](https://user-images.githubusercontent.com/79301007/192582426-e6fcf33f-32fc-4da2-ab39-c31be1dab44a.png)

## This take-home project focuses on backend engineering skills.
- The server should be written using Python or Go.
- Specific skills being tested are understanding of Python or Go, Docker and/or Docker Compose, SQL     databases, unit tests and deployment to Google Cloud Platform (GCP)
- The code should be saved to a git repository that can be pulled and run locally and uploaded to GCP to run remotely.

# Solution
This Repo is a solution that creates an API to store User Account Data into a database.To accomplish this, I will use Django(Python Web Framework) and PostgreSQL to create the APIs and Store the data in the database. This project also includes Django's Rest framework to test the connection between the Python application and the Postgres database. I will also use Docker to package my application’s dependencies for local development. Finally, The Dockerized Application with be pushed to GCP for Deployment

# UserStory 
- As a User I will be able to Create, Read, Update, and Delete User Accounts and Audio Data
- User can upload image and insert Json Formatted Data
- As a User I will be able to Search User Accounts
- As an Admin I will be able to Create, Read, Update, and Delete User Accounts and Audio Data

# Techincal Requirements
- Create and Run Server
- Make API Request 
- Create Database 
- Form valdation 
- unit test 
- Dockerize Application
- Deploy on GCP

# LOCAL BUILD, RUN, and TEST

- Fork and Clone repo
- Install Docker 
- Install Docker Compose 
- Add .dockerignore file 
- Create Docker Repo 
```
.venv
.git
.gitignore
```
### Build CMDS
The Dockerfile and docker-compose.yml contains the configuration we need to build and run the appilcation locally. 
### Dockerfile Example
```
FROM python:3.10.2-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
```

## Build

The Goal for this step is to get our Docker Container to ship to over to other local enviroments for development and deployment. Docker is great when appilcation have packages and dependencies that need to be installed. Docker allows use to get our appilcations up and running with just a few commands. 

### Signin to Docker using the CML

Inside of our Project folder run the follwoing commands

`docker login --username=ENTERYOURDOCKERUSERNAME`

### Pull Docker Image Locally 

`docker pull kbaskerville/concha_labs_interview_web`

`docker-compose up -d --build`
or
`docker-compose up`
We should see our Application running at <http://0.0.0.0:8000/>

![Screen Shot 2022-09-27 at 10 02 06 AM](https://user-images.githubusercontent.com/79301007/192590172-4a7538a9-7e7a-4724-8357-d81b44ccfe6e.png)

# UserAccont List
![Screen Shot 2022-09-27 at 10 38 21 AM](https://user-images.githubusercontent.com/79301007/192597406-986aef8c-8d74-422b-a04c-1b2b35054f23.png)

## Run 
Now we need to migrate our Postgres Database

`docker-compose exec web python manage.py migrate`

Next createsuperuser to add data to the admin page

`docker-compose exec web python manage.py createsuperuser`

<http://0.0.0.0:8000/admin/>

![Screen Shot 2022-09-27 at 11 27 03 AM](https://user-images.githubusercontent.com/79301007/192607014-0ff3f9c0-bcbf-4fa1-a091-b1fd3b65026f.png)

## Test 

Now that we have the Appilcation up and runnning, Lets add some users to the application. If we head to <http://0.0.0.0:8000/accounts/1> We can see the data Serialziered into JSON using Django's RESTFramework. This enables us to see that API is working. We are able to Create, Read, Update, and Delete Our Users 

![Screen Shot 2022-09-27 at 10 12 10 AM](https://user-images.githubusercontent.com/79301007/192592137-6b6eac0d-ed63-4b04-8bd7-73816b3860bc.png)

# GCP DEPLOYMENT

- Sign in to Goolge Cloud Console 
- Create New Project 
- Locate Project ID

Now that we have successfully Pulled and build our Docker Image and lets push it to GCP for Deployment. In this step we will build a docker image on GCP and push it to the Google Container Registry for Deployment. 

# Build on GCP

Currently our docker image is private and we want to push to it GCP for Public Deployment. We can accomplish this with one command. We will use `docker build -t` followed by `gcr.io/` which is pointing us to the GCP Repo. Then we will add our `username/docker-IMAGE:tag .`

## Project-ID 
![Screen Shot 2022-09-27 at 10 55 34 AM](https://user-images.githubusercontent.com/79301007/192601316-92f41a77-ab16-4849-be2e-783e04349078.png)


### EXAMPLE

`docker build -t gcr.io/PROJECT-ID/USERNAME/DOCKER_IMAGE:tag .`

I used the following

`docker build -t gcr.io/conchalabsdemo-363805/kbaskerville/concha_labs_interview_web:gcp . `

Now lets check to see if the Build was successful.  

![Screen Shot 2022-09-27 at 11 04 21 AM](https://user-images.githubusercontent.com/79301007/192602873-227636ea-73f7-4698-935c-7aea868e2966.png)

Now Run `docker images`

![Screen Shot 2022-09-27 at 11 01 32 AM](https://user-images.githubusercontent.com/79301007/192602391-f807d1fb-0930-431d-8018-f2324ba09996.png)

# Push to GCP

We can now push our Docker image to the Google Container Registry

`docker push gcr.io/PROJECT-ID/USERNAME/DOCKER_IMAGE:tag .`

I used 
 
`docker push gcr.io/conchalabsdemo-363805/kbaskerville/concha_labs_interview_web:gcp`

Lets head to the GCP console to see if our Docker Image was pushed. 

![](https://user-images.githubusercontent.com/79301007/192604579-1e7ffdb2-42f7-45d5-ba3b-e385a164dc03.png)

We can now Deploy our Docker Image on GCP! 
![](https://user-images.githubusercontent.com/79301007/192604780-24c6e8e7-f53b-4d1b-a806-f01b1a14cd94.png)

# Overview 

Lets Recap what we accomlpished! In this Repo we were able to create a Docker contianer for our Python-Django Appilcation, Build and Push the Docker Container to Docker's Private repo, Pull Docker conatinerfrom DockerHub repo to ship the appilcation, and build and pushed our Docker Image to GCP's Cloud Contaier Registry for deployment.

Thank you for following along! 

# Code Snippets 

In this section I am highlighting some of my favorite pieces of code that I used to help me accomplish this project

In the `models.py` file I added Django's JSONField() to the UserAccount Model. This was super helpful to store the JSON formatted data from the User. 

```
class UserAccount(models.Model):
    userId = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image =  models.ImageField(null=True,blank=True)
    audio_data = models.JSONField(default='{}')
```

I also used ArrayField() to store list inside the Django Model

``` 
class AudioData(models.Model):
    ticks = ArrayField(
        ArrayField(
            models.CharField(max_length=15, blank=True),
            size=8,
        ),
        size=8,
    )
```




















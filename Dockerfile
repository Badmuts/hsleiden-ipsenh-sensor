## Use an official Python runtime as a base image
#FROM python:2.7-slim
#
## Set the working directory to /app
#WORKDIR /app
#
## Copy the current directory contents into the container at /app
#ADD . /app
#
## Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt
#
## Make port 80 available to the world outside this container
#EXPOSE 80
#
## Define environment variable
#ENV NAME World
#
### Run app.py when the container launches
##CMD ["python", "app.py"]


FROM swchao/raspberry-on-amd64:latest

COPY . /home

RUN apt-get update -yq && apt-get install -yqq \
    python \
    python-pip
#    pip install -r home/requirements.txt

# Enable systemd
#ENV INITSYSTEM on
# Your code goes here

#ADD . home/raspberry

CMD ["/bin/bash"]
#RUN ["cd home"]
# Set base image (host OS)
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# By default, listen on port 3333
EXPOSE 3333/tcp


# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./run.py" ]
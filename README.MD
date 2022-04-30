# Simple Flask Rest Api

![Screenshot from 2022-04-30 11-21-38](https://user-images.githubusercontent.com/37028825/166100074-e040b208-b36d-4098-97d2-48cc5d242c05.png)

![Screenshot from 2022-04-30 11-25-09](https://user-images.githubusercontent.com/37028825/166100079-bae41c00-a4cd-438f-bb5b-fb41902d2feb.png)

![Screenshot from 2022-04-30 11-27-21](https://user-images.githubusercontent.com/37028825/166100084-8ef6a084-68fe-4cc0-8e34-9e0634fd9d29.png)

## Description

A Flask microservice that loads a pre-trained convolutional neural network for waste image classification.

## Creating the enviroment

```sh
python3 -m venv env
source env/bin/activate
```

## Installing dependencies

```sh
pip install -r requirements.txt
```

## Runinng the API

```python
python3 application.py
```

## Refresh the dependencies that the project uses

```sh
pip3 freeze > requirements.txt
```

## DEPLOYMENT AND MORE

### 1. Build the docker image

```sh
sudo docker build -t clean-app-backend-cont .
```

### 2. Testing the container

```sh
sudo docker run -p 3333:3333 clean-app-backend-cont
```

### Authors

1. [Jose Alejandro Concepcion Alvarez](https://www.gssi.it/people/students/students-computer-science/item/15643-concepcion-alvarez-jose-aleandro)
2. [Juan Antonio Pinera Garcia](https://www.gssi.it/people/students/students-computer-science/item/15647-pinera-garcia-juan-antonio)

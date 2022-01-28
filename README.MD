# Simple Flask Rest Api

## Description

We are working in this api as a service for extracting labels of waste's images

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

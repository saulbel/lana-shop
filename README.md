# Lana's Shop
This is guide to show how to build a simple API using Flask and configure CI to deploy the app on a Docker container.

![1596726313289](https://user-images.githubusercontent.com/97754610/149635896-75c064af-ea96-43c1-b481-e1ab8b463dad.jpg)

## Getting Started

### Prerequisites

The things you need before starting.
* Linux OS --> I am gonna use an ubuntu 20.04 distro, Zorin OS.
* Python IDE --> Pycharm, VSCode.
* Python 3.x
* Github account --> both for pushing code and for pipeline CI management using github Actions.
* Dockerhub account.
* API client such as Postman, Insonmia and of course, CURL.

### Project structure
```
LanaShop
├── app.py
├── Dockerfile
├── products.py
├── README.md
├── requirements.txt
└── Tests
    └── tests.py
```

### API's endpoints
```
Flask API
├── GET         -->     http://localhost:5000/ping          -->      checks if server is up and running
├── GET         -->     http://localhost:5000/products      -->      returns all products in lana's shop
├── GET         -->     http://localhost:5000/basket        -->      returns the basket
├── POST        -->     http://localhost:5000/basket        -->      adds a product to the basket
├── GET         -->     http://localhost:5000/totalbasket   -->      returns the basket and the total price
└── GET         -->     http://localhost:5000/emptybasket   -->      empties the basket   
```
### Curl examples to test endpoints
```
curl http://localhost:5000/ping
curl http://localhost:5000/products
curl http://localhost:5000/basket
curl -d '{"item": "MUG"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
curl -d '{"item": "PEN"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
curl -d '{"item": "TSHIRT"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
curl http://localhost:5000/totalbasket
curl http://localhost:5000/emptybasket
```


### Local Installation
Once you have your Linux machine ready, your IDE configured and linked to Github and your Dockerhub account ready we can start with a simple app execution.

First we are gonna install Docker in our ubuntu distro
```
$ sudo apt-get update
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
We are gonna download this whole repo using git clone although in this case it is private so we just download it as .zip.<br/>
Now is when the fun begins:<br/>
1) We unzip the project
```
$ unzip LanaShop-master.zip
$ cd LanaShop-master/
```
2) We build our docker image
```
$ docker build --tag lanashop .
```
3) We check out our images
```
$ docker images
REPOSITORY         TAG               IMAGE ID       CREATED          SIZE
lanashop           latest            66f4ec6c0a0f   41 seconds ago   414MB
```
4) We run our container: -d to run in detached mode and -p to specify the port
```
$ docker run -d -p 5000:5000 lanashop
```
5) We can see our container is up and running
```
sudo docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
14711b513a19   lanashop   "python3 -m flask ru…"   8 seconds ago   Up 8 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   recursing_germain
```
6) Finally we can test out our little application


### CI Pipeline















```
$ First step

$ Another step
$ Final step
```

## Usage

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...

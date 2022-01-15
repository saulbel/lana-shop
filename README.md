# Lana's Shop
This is guide to show how to build a simple API using Flask and configure CI to deploy the app on a Docker container.

![1596726313289](https://user-images.githubusercontent.com/97754610/149635896-75c064af-ea96-43c1-b481-e1ab8b463dad.jpg)

### Prerequisites
The things you need before starting.
* Linux OS --> I am gonna use an ubuntu 20.04 distro, Zorin OS.
* Python IDE --> Pycharm, VSCode.
* Python 3.x
* GitHub account --> both for pushing code and for pipeline CI management using GitHub Actions.
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
├── GET         -->     http://localhost:5000/dashboard     -->      dashboard for monitoring (default credentials admin:admin)
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

### GitHub Actions
I have used Github Actions to create a CI pipeline that creates a docker image and pushes it to DockerHub.<br/>
Whenever we push to the `master branch`, a new Docker image is created and sent to DockerHub repo.
*If you want to try this out I cand handle to you my DockerHub credentials*
To test this out we have to do the following: <br/>
1) We pull the latest docker's image available at our DockerHub repo.
```
$ sudo docker pull saulbel/lanashop_dockerrepo:latest
```
2) Then we check out our images
```
$ sudo docker images
REPOSITORY                                                          TAG               IMAGE ID       CREATED              SIZE
saulbel/lanashop_dockerrepo                                         latest            3cb13957a510   About a minute ago   647MB
```
3) Lastly we spin up our container
```
$ sudo docker run -d -p 5000:5000  saulbel/lanashop_dockerrepo
$ sudo docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                       NAMES
877fdde2949e   saulbel/lanashop_dockerrepo   "python3 -m flask ru…"   3 seconds ago   Up 2 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   jovial_williamson
```

## Testing
Endpoints testing
└── Tests
    └── tests.py
Once our container is up and running, we use tests.py to check out that all endpoints are working correctly.
```
$ python tests.py 
----------------------------------------------------------------------
Ran 5 tests in 0.048s
OK
```

## Monitoring
I decided to use Prometheus + Grafana for scrapping/showing the metrics. I would use AlertManager with Karma interface for alerts.

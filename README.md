# Lana's Shop
![1596726313289](https://user-images.githubusercontent.com/97754610/149635896-75c064af-ea96-43c1-b481-e1ab8b463dad.jpg)

## Prerequisites
Things you need before starting:
* Linux OS --> I am gonna use an ubuntu 20.04 distro, `Zorin OS 16`
* `Python 3.8`
* Python IDE --> `Pycharm`, `VSCode`
* `GitHub` account --> both for pushing code and CI pipeline management using `GitHub Actions`
* `Docker`
* `DockerHub` account
* API client such as `Postman`, `Insomnia` and of course, `CURL`

## Project structure
```
LanaShop
├── app.py
├── Dockerfile
├── products.py
├── README.md
├── requirements.txt
└── tests
    └── tests.py
```

## API's endpoints
```
Flask API
├── GET         -->     http://localhost:5000/ping          -->      checks if server is up and running
├── GET         -->     http://localhost:5000/metrics       -->      exposing api metrics for Prometheus 
├── GET         -->     http://localhost:5000/products      -->      returns all products in lana's shop
├── GET         -->     http://localhost:5000/basket        -->      returns the basket
├── POST        -->     http://localhost:5000/basket        -->      adds a product to the basket
├── GET         -->     http://localhost:5000/totalbasket   -->      returns the basket and total price
└── GET         -->     http://localhost:5000/emptybasket   -->      empties the basket   
```

## Curl examples
```
$ curl http://localhost:5000/ping
$ curl http://localhost:5000/metrics
$ curl http://localhost:5000/products
$ curl http://localhost:5000/basket
$ curl -d '{"item": "MUG"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
$ curl -d '{"item": "PEN"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
$ curl -d '{"item": "TSHIRT"}' -H "Content-Type: application/json" -X POST http://localhost:5000/basket
$ curl http://localhost:5000/totalbasket
$ curl http://localhost:5000/emptybasket
```

## GitHub Actions
```
LanaShop
└── .github/workflows/
    └── continuous-integration.yml
```
I have used `GitHub Actions` to create a CI pipeline that creates a docker image and pushes it to `DockerHub`.<br/>
Whenever we push to the `master branch`, a new docker image is created and sent to the `DockerHub` repo.
To test this out we have to do the following: <br/>
- We pull the latest docker's image available at our `DockerHub` repo.
```
$ docker pull saulbel/lanashop_dockerrepo:latest
```
- Then we check out our images
```
$ docker images
REPOSITORY                                   TAG         IMAGE ID       CREATED         SIZE
saulbel/lanashop_dockerrepo                  latest      011e10e59307   2 minutes ago   148MB
```
- Lastly we spin up our container
```
$ docker run -d -p 5000:5000  saulbel/lanashop_dockerrepo
$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                                       NAMES
afaba9138bcb   saulbel/lanashop_dockerrepo   "python3 -m flask ru…"   25 seconds ago   Up 24 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   nervous_golick
```

## Testing
```
LanaShop
└── tests
    └── tests.py
```
Once our container is up and running, we use tests.py to check out that all endpoints are working correctly.
```
$ python tests.py 
============================= test session starts =============================
collecting ... collected 5 items
tests/tests.py::ApiTest::test_getBasket PASSED                           [ 20%]
tests/tests.py::ApiTest::test_getProducts PASSED                         [ 40%]
tests/tests.py::ApiTest::test_getPrometheusMetrics PASSED                [ 60%]
tests/tests.py::ApiTest::test_getRemoveBasket PASSED                     [ 80%]
tests/tests.py::ApiTest::test_getTotalBasket PASSED                      [100%]
============================== 5 passed in 0.09s ==============================
```

## Monitoring
I decided to use `Prometheus` for scrapping/storing the metrics. I would use `Grafana` for showing those metrics, `node_exporter` for collecting/exposing system metrics and `AlertManager` + `Karma dashboard` for alert management.
```
from prometheus_flask_exporter import PrometheusMetrics

# Exposing api metrics for Prometheus to scrape from
app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

# debug must be False if we want endpoint '/metrics' up 
if __name__ == '__main__':
    app.run(debug=False, port=5000)
    metrics.init_app(app)
```

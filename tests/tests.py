import unittest

import requests


# For testing all endpoints availability and number of returning jsons
class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    PRODUCTS_URL = "{}/products".format(API_URL)
    BASKET_URL = "{}/basket".format(API_URL)
    TOTALBASKET_URL = "{}/totalbasket".format(API_URL)
    EMPTYBASKET_URL = "{}/emptybasket".format(API_URL)
    METRICS_URL = "{}/metrics".format(API_URL)

    # GET for returning all products in lana's shop
    def test_getProducts(self):
        r = requests.get(ApiTest.PRODUCTS_URL)
        self.assertEqual(r.status_code, 200)
        # It has to return 2 jsons
        self.assertEqual(len(r.json()), 2)

    # GET for showing the cart
    def test_getBasket(self):
        r = requests.get(ApiTest.BASKET_URL)
        self.assertEqual(r.status_code, 200)
        # It has to return 2 jsons
        self.assertEqual(len(r.json()), 2)

    # GET for calculating total price
    def test_getTotalBasket(self):
        r = requests.get(ApiTest.TOTALBASKET_URL)
        self.assertEqual(r.status_code, 200)
        # It has to return 3 jsons
        self.assertEqual(len(r.json()), 3)

    # GET for emptying the basket
    def test_removeBasket(self):
        r = requests.get(ApiTest.EMPTYBASKET_URL)
        self.assertEqual(r.status_code, 200)
        # It has to return 2 jsons
        self.assertEqual(len(r.json()), 2)

    # GET for testing '/metrics' endpoint
    def test_getPrometheusMetrics(self):
        r = requests.get(ApiTest.METRICS_URL)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

import unittest

import requests


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    PRODUCTS_URL = "{}/products".format(API_URL)
    BASKET_URL = "{}/basket".format(API_URL)
    TOTALBASKET_URL = "{}/totalbasket".format(API_URL)
    EMPTY_BASKET_URL = "{}/emptybasket".format(API_URL)
    PRODUCT_OBJ1 = {"item": "PEN"}
    PRODUCT_OBJ2 = {"item": "TSHIRT"}
    PRODUCT_OBJ3 = {"item": "MUG"}

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

    # POST for putting an item in cart
    def test_addProductToBasket(self):
        r = requests.post(ApiTest.BASKET_URL, json=ApiTest.PRODUCT_OBJ1)
        self.assertEqual(r.status_code, 200)
        r = requests.post(ApiTest.BASKET_URL, json=ApiTest.PRODUCT_OBJ2)
        self.assertEqual(r.status_code, 200)
        r = requests.post(ApiTest.BASKET_URL, json=ApiTest.PRODUCT_OBJ3)
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
        r = requests.get(ApiTest.EMPTY_BASKET_URL)
        self.assertEqual(r.status_code, 200)
        # It has to return 2 jsons
        self.assertEqual(len(r.json()), 2)

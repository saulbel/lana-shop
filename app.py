from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

from products import basket
from products import products

# Exposing api metrics for Prometheus to scrape from
app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')


# GET for testing up/down
@app.route('/ping')
def ping():
    return jsonify({"LANA'S SHOP": "Server up and running"})


# GET for returning all products in lana's shop
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"LANA'S SHOP": "These are our products"}, {"Products": products})


# GET for showing the cart
@app.route('/basket', methods=['GET'])
def getBasket():
    return jsonify({"LANA'S SHOP": "This is your basket"}, {"Basket": basket})


# POST for putting an item in cart
@app.route('/basket', methods=['POST'])
def addProductToBasket():
    add_product = {
        "item": request.json['item'],
    }
    # Exception in case we try to add an incorrect product to basket
    if (add_product["item"] != 'PEN' and add_product["item"] != 'TSHIRT' and add_product["item"] != 'MUG'):
        return jsonify({"LANA'S SHOP": "Product not available"}, {"Basket": basket})
    else:
        print(add_product["item"])
        basket.append(add_product)
        return jsonify({"LANA'S SHOP": "Product added successfully to basket"}, {"Basket": basket})


# GET for calculating total price
@app.route('/totalbasket', methods=['GET'])
def getTotalBasket():
    totalTshirt = sum([i['item'] == "TSHIRT" for i in basket])
    totalPen = sum([i['item'] == "PEN" for i in basket])
    totalMug = sum([i['item'] == "MUG" for i in basket])
    totalPrice = float(totalTshirt * 20) + float(totalPen * 5) + float(totalMug * 7.5)
    # 2x1 free promotion, it only applies ONCE
    if (totalPen >= 2):
        totalPrice = totalPrice - 5
    # 25% of disscount in each Tshirt if 3 or more
    if (totalTshirt >= 3):
        totalPrice = totalPrice - (totalTshirt * 5)
    return jsonify({"LANA'S SHOP": "This is your invoice"}, {"Basket": basket}, {"Total": totalPrice})


# GET for emptying the basket
@app.route('/emptybasket', methods=['GET'])
def removeBasket():
    basketDepth = len(basket)
    # Exception in case basket is already cleared
    if (basketDepth == 0):
        return jsonify({"LANA'S SHOP": "Basket was already emptied"}, {"Basket": basket})
    else:
        basket.clear()
        return jsonify({"LANA'S SHOP": "Basket removed"}, {"Basket": basket})


# debug must be False if we want '/metrics' endpoint up
if __name__ == '__main__':
    app.run(debug=False, port=5000)
    metrics.init_app(app)

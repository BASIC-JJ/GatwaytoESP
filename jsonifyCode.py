# File: server.py on Ubuntu Server
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/price')
def price():
    # You can modify this data fetching mechanism as per your requirement
    price_data = {"item": "Example Item", "price": 100.00}
    return jsonify(price_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

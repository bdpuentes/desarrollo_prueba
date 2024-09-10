from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime
from repositories.price_repository import get_price


app = Flask(__name__)

@app.route('/price', methods=['GET'])
def price():

    product_id = reqparse.request.json['product_id']
    brand_id = reqparse.request.json['brand_id']
    application_date = reqparse.request.json['application_date']
    #product_id = request.args.get('product_id')
    #brand_id = request.args.get('brand_id')
    #application_date = request.args.get('application_date')

    if not product_id or not brand_id or not application_date:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        datetime.strptime(application_date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    price_info = get_price(product_id, brand_id, application_date)

    if price_info:
        return jsonify(price_info), 200
    else:
        return jsonify({"error": "Price not found"}), 404


from flask import request, jsonify
from service.price_service import PriceService
from datetime import datetime

class PriceController:
    def __init__(self, price_service: PriceService):
        self.price_service = price_service

    def get_price(self):
        try:
            product_id = request.json['product_id']
            brand_id = request.json['brand_id']
            application_date = request.json['application_date']

            try:
                datetime.strptime(application_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return jsonify({"error": "Formato de fecha no valido"}), 400

            price_info = self.price_service.find_price(product_id, brand_id, application_date)

            if price_info:
                return jsonify(price_info.to_dict()), 200
            else:
                return jsonify({"error": "No se encontró registro"}), 404
        except KeyError:
            return jsonify({"error": "Faltan parametros"}), 400

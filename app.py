from flask import Flask
from flask_restful import Api
from db.database import init_db
from repositories.price_repository import PriceRepository
from service.price_service import PriceService
from controllers.price_controller import PriceController

conn = init_db()

app = Flask(__name__)
api = Api(app)

# Se inicializan las instancias de las capas
price_repository = PriceRepository(conn)
price_service = PriceService(price_repository)
price_controller = PriceController(price_service)

@app.route('/price', methods=['GET'])
def get_price():
    return price_controller.get_price()

if __name__ == '__main__':
    app.run(debug=True, port=1010)

from repositories.price_repository import PriceRepository

class PriceService:
    def __init__(self, price_repository: PriceRepository):
        self.price_repository = price_repository

    def find_price(self, product_id, brand_id, application_date):
        return self.price_repository.get_price(product_id, brand_id, application_date)

class Price:
    def __init__(self, product_id, brand_id, price_list, start_date, end_date, price):
        self.product_id = product_id
        self.brand_id = brand_id
        self.price_list = price_list
        self.start_date = start_date
        self.end_date = end_date
        self.price = price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "brand_id": self.brand_id,
            "price_list": self.price_list,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "price": self.price
        }
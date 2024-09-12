import sqlite3
from models.price_model import Price

class PriceRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_price(self, product_id, brand_id, application_date):
        cursor = self.conn.cursor()
        query = '''
            SELECT PRODUCT_ID, BRAND_ID, PRICE_LIST, START_DATE, END_DATE, PRICE, PRIORITY
              FROM PRICES
             WHERE PRODUCT_ID = ? AND BRAND_ID = ?
               AND START_DATE <= ? AND END_DATE >= ?
             ORDER BY PRIORITY DESC
             LIMIT 1
        '''
        cursor.execute(query, (product_id, brand_id, application_date, application_date))
        result = cursor.fetchone()

        if result:
            return Price(
                product_id=result[0],
                brand_id=result[1],
                price_list=result[2],
                start_date=result[3],
                end_date=result[4],
                price=result[5]
            )
        return None

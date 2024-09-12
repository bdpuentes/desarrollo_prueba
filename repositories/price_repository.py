import sqlite3
from models.price_model import Price
import json

class PriceRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_price(self, product_id, brand_id, application_date):
        cursor = self.conn.cursor()
        query = '''
            SELECT PRODUCT_ID, BRAND_ID, PRICE_LIST, START_DATE, END_DATE, PRICE, PRIORITY, CURR, ID
              FROM PRICES
             WHERE PRODUCT_ID = ? AND BRAND_ID = ?
                AND ? BETWEEN START_DATE AND END_DATE
             ORDER BY PRIORITY DESC
             
        '''
        cursor.execute(query, (product_id, brand_id, application_date))
        results = cursor.fetchall() 
        
        results_dict = [
            {
                "id_consulta": row[8],
                "product_id": row[0],
                "brand_id": row[1],
                "price_list": row[2],
                "start_date": row[3],
                "end_date": row[4],
                "price": row[5],
                "priority": row[6],
                "curr": row[7]
            }
            for row in results
        ]
        
        return results_dict

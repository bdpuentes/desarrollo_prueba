from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime
import sqlite3

#conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('temp.db', check_same_thread=False)
conn = sqlite3.connect('file::memory:?cache=shared', uri=True, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PRICES';")
table_exists = cursor.fetchone()

if table_exists:
    print("La tabla 'PRICES' ya existe, borrando...")
    cursor.execute("DROP TABLE PRICES")

cursor.execute('''
    CREATE TABLE PRICES (
        BRAND_ID INTEGER,
        START_DATE TEXT,
        END_DATE TEXT,
        PRICE_LIST INTEGER,
        PRODUCT_ID INTEGER,
        PRIORITY INTEGER,
        PRICE REAL,
        CURR TEXT
    )
''')
conn.commit()

prices_data = [
    (1, '2020-06-14 00:00:00', '2020-12-31 23:59:59', 1, 35455, 0, 35.5, 'US $'),
    (1, '2020-06-14 15:00:00', '2020-06-14 18:30:00', 1, 35455, 0, 35.5, 'US $'),
    (1, '2020-06-15 00:00:00', '2020-06-15 11:00:00', 1, 35455, 0, 35.5, 'US $'),
    (1, '2020-06-15 16:00:00', '2020-12-31 23:59:59', 1, 35455, 0, 35.5, 'US $')
]

cursor.executemany('''
    INSERT INTO PRICES (BRAND_ID, START_DATE, END_DATE, PRICE_LIST, PRODUCT_ID, PRIORITY, PRICE, CURR)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', prices_data)

conn.commit()

def get_price(product_id, brand_id, application_date):
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
        return {
            "product_id": result[0],
            "brand_id": result[1],
            "price_list": result[2],
            "start_date": result[3],
            "end_date": result[4],
            "price": result[5]
        }
    else:
        return None

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


if __name__ == '__main__':
    app.run(debug=True , port=1010)

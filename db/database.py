import sqlite3

def init_db():
    conn = sqlite3.connect('file::memory:?cache=shared', uri=True, check_same_thread=False)
    #conn = sqlite3.connect('test.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PRICES';")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE PRICES")

    cursor.execute('''
        CREATE TABLE PRICES (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BRAND_ID INTEGER,
            START_DATE DATE,
            END_DATE DATE,
            PRICE_LIST INTEGER,
            PRODUCT_ID INTEGER,
            PRIORITY INTEGER,
            PRICE REAL,
            CURR VARCHAR2
        )
    ''')

    prices_data = [
        (1, '2020-06-14 00:00:00', '2020-12-31 23:59:59', 1, 35455, 0, 35.5, 'US $'),
        (1, '2020-06-14 15:00:00', '2020-06-14 18:30:00', 2, 35455, 0, 25.45, 'US $'),
        (1, '2020-06-15 00:00:00', '2020-06-15 11:00:00', 3, 35455, 0, 30.5, 'US $'),
        (1, '2020-06-15 16:00:00', '2020-12-31 23:59:59', 4, 35455, 0, 38.95, 'US $')
    ]

    cursor.executemany('''
        INSERT INTO PRICES (BRAND_ID, START_DATE, END_DATE, PRICE_LIST, PRODUCT_ID, PRIORITY, PRICE, CURR)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', prices_data)

    conn.commit()
    return conn

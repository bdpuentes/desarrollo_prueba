import requests

url = "http://127.0.0.1:1010/price"

def test_price(product_id, brand_id, application_date):
    payload = {
        "product_id": product_id,
        "brand_id": brand_id,
        "application_date": application_date
    }
    response = requests.get(url, json=payload)
    
    print(f"Test para product_id={product_id}, brand_id={brand_id}, application_date={application_date}")
    print(f"Codigo de status: {response.status_code}")
    print(f"resouesta en JSON: {response.json()}")
    print("-" * 50)

test_price(35455, 1, '2020-06-14 10:00:00')

test_price(35455, 1, '2020-06-14 16:00:00')

test_price(35455, 1, '2020-06-14 21:00:00')

test_price(35455, 1, '2020-06-15 10:00:00')

test_price(35455, 1, '2020-06-16 21:00:00')
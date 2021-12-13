import json
import os
import unittest
from api.auth import API_KEY
from io import BytesIO

JSON_FILE = (BytesIO(b'{"id": 1, "products": [1, 2, 3]}'), '20211202_sample.json')

class TestProductAPI(unittest.TestCase):

    def setUp(self) -> None:
        os.environ["env"] = "test"

    def test_product_response_data(self):
        from app import app
        with app.test_client() as client:
            upload = client.post("/v1/transactions", data = {'file': JSON_FILE}, headers={'api_key': API_KEY})
            res_product = client.get("/v1/products?id=1", headers={'api_key': API_KEY})
            msg = json.loads(res_product.get_data())
            expect_output = {'data': [{'product_id': 1, 'units_sold': 1}], 'message': 'OK'}
            self.assertEqual(msg, expect_output)

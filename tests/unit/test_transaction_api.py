import unittest
import json
from api.auth import API_KEY

from app import app
from io import BytesIO
from api.routes.transaction import FAILURE_STATUS_CODE, SUCCESS_STATUS_CODE, \
    FAILURE_MSG, SUCCESS_MSG

JSON_FILE = (BytesIO(b'{"id": 1, "products": [1, 2, 3]}'), 'sample.json')
CSV_FILE = (BytesIO(b'{"id": 1, "products": [1, 2, 3]}'), 'sample.csv')

class TestTransactionAPI(unittest.TestCase):

    def test_transaction_upload_json(self):
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': JSON_FILE},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, SUCCESS_STATUS_CODE)
            self.assertEqual(msg['status'], SUCCESS_MSG)

    def test_transaction_upload_not_json(self):
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': CSV_FILE},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['status'], FAILURE_MSG)

    def test_transaction_upload_empty(self):
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['status'], FAILURE_MSG)

    def test_transaction_upload_without_file(self):
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': ''},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['status'], FAILURE_MSG)  


    def test_transaction_process_trigger(self):
        with app.test_client() as client:
            res = client.get('/v1/transactions?file=20211202_sample.json',
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, SUCCESS_STATUS_CODE)
            self.assertEqual(msg['status'], SUCCESS_MSG)

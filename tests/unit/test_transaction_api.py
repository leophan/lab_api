import os
import unittest
import json
import pytest
from api.auth import API_KEY

from io import BytesIO
from api.routes.transaction import FAILURE_STATUS_CODE, SUCCESS_STATUS_CODE, \
    FAILURE_MSG, SUCCESS_MSG

JSON_FILE = (BytesIO(b'{"id": 1, "products": [1, 2, 3]}'), 'sample.json')
CSV_FILE = (BytesIO(b'{"id": 1, "products": [1, 2, 3]}'), 'sample.csv')

class TestTransactionAPI(unittest.TestCase):

    def setUp(self) -> None:
        os.environ["env"] = "test"

    def test_transaction_upload_json(self):
        from app import app
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': JSON_FILE},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, SUCCESS_STATUS_CODE)
            self.assertEqual(msg['message'], SUCCESS_MSG)

    def test_transaction_upload_not_json(self):
        from app import app
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': CSV_FILE},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['message'], FAILURE_MSG)

    def test_transaction_upload_empty(self):
        from app import app
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['message'], FAILURE_MSG)

    def test_transaction_upload_without_file(self):
        from app import app
        with app.test_client() as client:
            res = client.post('/v1/transactions',
                              data = {'file': ''},
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, FAILURE_STATUS_CODE)
            self.assertEqual(msg['message'], FAILURE_MSG)  
    
    @pytest.mark.skip("WIP")
    def test_transaction_process_trigger(self):
        from app import app
        with app.test_client() as client:
            res = client.get('/v1/transactions?file=20211202_sample.json',
                              headers={'api_key': API_KEY})
            msg = json.loads(res.get_data())
            self.assertEqual(res._status_code, SUCCESS_STATUS_CODE)
            self.assertEqual(msg['message'], SUCCESS_MSG)


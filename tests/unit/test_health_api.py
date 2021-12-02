import json
import unittest
from app import app

SUCCESS_STATUS_CODE = 200
SUCCESS_MSG = 'OK'

class TestHealthAPI(unittest.TestCase):
    def test_health_status_200(self):
        with app.test_client() as client:
            res = client.get('/health')
            self.assertEqual(res._status_code, SUCCESS_STATUS_CODE)


    def test_health_success_msg(self):
        with app.test_client() as client:
            res = client.get('/health')
            msg = res.get_data().decode("utf-8")
            self.assertEqual(msg, SUCCESS_MSG)

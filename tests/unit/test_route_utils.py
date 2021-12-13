import json
import os
import unittest
from unittest import result

from api.routes.utils import allowed_file, decode_file, validate_file, validate_json, validate_json_schema


class TestRoutesUtils(unittest.TestCase):
    
    def setUp(self) -> None:
        os.environ["env"] = "test"

    def test_allowed_file_with_right_ext(self):
        filename = 'sample_data.json'
        result = allowed_file(filename)
        expect_result = True
        self.assertEqual(expect_result, result)

    def test_allowed_file_without_right_ext(self):
        filename = 'sample_data.txt'
        result = allowed_file(filename)
        expect_result = False
        self.assertEqual(expect_result, result)

    def test_validate_json_loads(self):
        json_data = """{"id": 0, "products": [1, 2, 3]}"""
        result = validate_json(json_data)
        expect_result = True
        self.assertEqual(expect_result, result)

    def test_validate_json_schema(self):
        json_data = json.loads("""{"id": 0, "products": [1, 2, 3]}""")
        result = validate_json_schema(json_data)
        expect_result = True
        self.assertEqual(expect_result, result)

    def test_validate_json_schema_unexpected(self):
        json_data = json.loads("""{"id": 0, "product": [1, 2, 3]}""")
        result = validate_json_schema(json_data)
        expect_result = False
        self.assertEqual(expect_result, result)

    def test_decode_file(self):
        binary_data = [b'{"id": 2, "products": [1, 3]}\n']
        result = decode_file(binary_data)
        expect_result = ['{"id": 2, "products": [1, 3]}']
        self.assertEqual(expect_result, result)


    def test_validate_file(self):
        raws_data = ['{"id": 0, "products": [1, 2, 3]}', \
                       '{"id": 1, "products": [2, 3]}', \
                       '{"id": 2, "products": [1, 3]}']
        result = validate_file(raws_data)
        expect_result = True
        self.assertEqual(expect_result, result)

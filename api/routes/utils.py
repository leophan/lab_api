import json
from os import error

import jsonschema
from jsonschema import SchemaError, ValidationError, validate

ALLOWED_EXTENSIONS = {'json'}

TRANSACTION_SCHEMA = {
    "type": "object",
    "properties" : {
        "id": {"type": "integer"},
        "products": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        }
    },
    "required": ["id", "products"]
}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def decode_file(file):
    trans = []
    for item in file:
        item_decode = item.decode('utf8').replace('\n', '')
        trans.append(item_decode)
    return trans


def validate_file(data):
    is_json = False
    for line in data:
        if validate_json(line):
            json_data = json.loads(line)
            if validate_json_schema(json_data):
                is_json = True
            else:
                return False
        else:
            return False       
    return is_json


def read_file(filename):
    trans = []
    with open(filename) as fp:
        for line in fp:
            trans.append(json.loads(line))

    return trans


def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


def validate_json_schema(json_data):
    try:
        validate(instance=json_data, schema=TRANSACTION_SCHEMA)
    except ValidationError as err:
        return False
    except SchemaError as serr:
        return False
    return True
    
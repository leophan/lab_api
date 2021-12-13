import json
import os

from api.auth import auth_required
from api.models.sqla.product import Product
from api.models.transform import io
from api.models.sqla import db
from api.routes.health import SUCCESS_MSG
from api.routes.utils import allowed_file, decode_file, read_file, validate_file
from flask import request
from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename

transaction_api = Blueprint("transaction", __name__)


# TODO: refactor to const file
SUCCESS_STATUS_CODE = 200
FAILURE_STATUS_CODE = 400
# TODO: refactor to build code list
SUCCESS_MSG = 'OK'
FAILURE_MSG = 'NOT_OK.'
FAILURE_MSG2 = 'json file is invalid.'

UPLOAD_PATH = 'data/raws'


@transaction_api.route("/v1/transactions", methods=["POST"])
@auth_required
def upload():
    if 'file' not in request.files:
        return {'message': FAILURE_MSG}, FAILURE_STATUS_CODE

    file = request.files['file']
    if file.filename == '':
        return {'message': FAILURE_MSG}, FAILURE_STATUS_CODE

    raws_data = decode_file(file)
    if allowed_file(file.filename) and validate_file(raws_data):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_PATH, filename))
        date = filename.split('_')[0]
        io.handle(db, date, raws_data)
        return {'message': SUCCESS_MSG}, SUCCESS_STATUS_CODE

    return {'message': FAILURE_MSG2}, FAILURE_STATUS_CODE


#TODO: refactor to validate `file` parameter
# @transaction_api.route("/v1/transactions", methods=["GET"])
# @auth_required
# def process():
#     filename = request.args.get('file')
#     DATA_PATH = UPLOAD_PATH + '/' + filename
#     date = filename.split('_')[0]
#     lines = read_file(DATA_PATH)
#     io.handle(db, date, lines)
#     return {'status': SUCCESS_MSG}, SUCCESS_STATUS_CODE

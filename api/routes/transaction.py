import os
from flask import request
from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename
from api.auth import auth_required
from api.models.io import IO

from api.routes.health import SUCCESS_MSG
from api.routes.utils import allowed_file, read_file

transaction_api = Blueprint("transaction", __name__)


# TODO: refactor to const file
SUCCESS_STATUS_CODE = 200
FAILURE_STATUS_CODE = 400
# TODO: refactor to build code list
SUCCESS_MSG = 'OK'
FAILURE_MSG = 'NOT_OK'

UPLOAD_PATH = 'data/raws'


@transaction_api.route("/v1/transactions", methods=["POST"])
@auth_required
def upload():
    if 'file' not in request.files:
        return {'status': FAILURE_MSG}, FAILURE_STATUS_CODE

    file = request.files['file']
    if file.filename == '':
        return {'status': FAILURE_MSG}, FAILURE_STATUS_CODE

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_PATH, filename))
        return {'status': SUCCESS_MSG}, SUCCESS_STATUS_CODE

    return {'status': FAILURE_MSG}, FAILURE_STATUS_CODE


# TODO: refactor to validate `file` parameter
@transaction_api.route("/v1/transactions", methods=["GET"])
@auth_required
def process():
    io = IO()
    filename = request.args.get('file')
    DATA_PATH = UPLOAD_PATH + '/' + filename
    date = filename.split('_')[0]
    lines = read_file(DATA_PATH)
    from app import engine
    io.handle(engine, date, lines)
    return {'status': SUCCESS_MSG}, SUCCESS_STATUS_CODE

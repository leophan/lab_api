from api.auth import auth_required
from api.models.transform import io
from api.models.sqla import db
from api.routes.health import SUCCESS_MSG
from flask import request
from flask.blueprints import Blueprint

product_api = Blueprint("product", __name__)

# TODO: refactor to validate params
# TODO: partern output
@product_api.route("/v1/products", methods=["GET"])
@auth_required
def product():
    id = None
    page = 0
    result = []
    if 'id' in request.args:
        id = request.args.get('id')
    if 'page' in request.args:
        page = int(request.args.get('page'))
    if id is None:
        result = io.get_products(db, next_page=page)
        return {'message': SUCCESS_MSG, 'data': result}

    result = io.get_product(db, id)
    return {'message': SUCCESS_MSG, 'data': result}

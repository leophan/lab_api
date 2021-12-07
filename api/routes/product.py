from api.auth import auth_required
from api.models.transform import io
from api.routes.health import SUCCESS_MSG
from flask import request
from flask.blueprints import Blueprint

product_api = Blueprint("product", __name__)

# TODO: refactor to validate params
# TODO: partern output
@product_api.route("/v1/products", methods=["GET"])
@auth_required
def product():
    result = []
    id = request.args.get('id')
    if id is None:
        result = io.get_products()
        return {'status': SUCCESS_MSG, 'data': result}

    result = io.get_product(id)
    return {'status': SUCCESS_MSG, 'data': result}

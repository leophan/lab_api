from flask.blueprints import Blueprint

from flask import request
from api.auth import auth_required
from api.models.io import IO
from api.routes.health import SUCCESS_MSG

product_api = Blueprint("product", __name__)

# TODO: refactor to validate params
# TODO: partern output
@product_api.route("/v1/products", methods=["GET"])
@auth_required
def product():
    product_id = request.args.get('id')
    io = IO()
    query = """SELECT product_id, sum(count) AS total
            FROM agg
            WHERE product_id = '{product_cond}'
            GROUP BY product_id;""".format(product_cond = product_id)
    from app import engine
    result = io.get_json(engine, query)
    return {'status': SUCCESS_MSG, 'data': result}

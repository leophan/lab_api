from .error import internal_server_error, page_not_found, request_entity_too_large
from .health import health_api
from .transaction import transaction_api
from .product import product_api

def init_app(app):
    app.register_blueprint(health_api)
    app.register_blueprint(transaction_api)
    app.register_blueprint(product_api)
    # app.register_blueprint(error_api)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(413, request_entity_too_large)
    app.register_error_handler(500, internal_server_error)
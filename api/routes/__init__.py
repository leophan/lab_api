from .health import health_api
from .transaction import transaction_api
from .product import product_api

def init_app(app):
    app.register_blueprint(health_api)
    app.register_blueprint(transaction_api)
    app.register_blueprint(product_api)

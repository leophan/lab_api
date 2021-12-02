from flask import Blueprint

health_api = Blueprint("healthcheck", __name__)

SUCCESS_MSG = 'OK'

@health_api.route("/health")
def health():
    return SUCCESS_MSG
    
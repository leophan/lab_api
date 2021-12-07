# from flask.blueprints import Blueprint

# error_api = Blueprint("error", __name__)

# @error_api.errorhandler(413)
def request_entity_too_large(e):
    return {"message": "Request Entity Too Large"}, 413

# @error_api.errorhandler(404)
def page_not_found(e):
    return {"message": "Not Found"}, 404


# @error_api.errorhandler(500)
def internal_server_error(e):
    return {"message": "Internal Server Error"}, 500



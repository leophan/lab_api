from functools import wraps
from flask import request, jsonify, make_response


class AuthError(BaseException):
    """pass"""


class AuthInternalError(BaseException):
    """pass"""

# TODO: refactor to read config file.
API_KEY = "4babf13c-4146-4701-bfe1-ee5c745df7cd"

def verify_api_key(key: str):
    api_key = API_KEY
    if api_key is None:
        raise AuthInternalError("API_KEY config is missing")
    if key != api_key:
        raise AuthError("invalid key")


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        api_key = None

        if 'api_key' in request.headers:
            api_key = request.headers['api_key']

        if not api_key:
            return make_response(jsonify({'message': 'a valid api_key is missing'}), 401)

        try:
            verify_api_key(api_key)
        except AuthError as ex:
            return make_response(jsonify({'message': 'auth error: {}'.format(str(ex))}), 401)
        except Exception as ex:
            return make_response(jsonify({'message': 'could not verify api_key'}), 500)
        return f(*args, **kwargs)
    return decorator

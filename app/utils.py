from flask import jsonify


def success_response(message, data=None, status_code=200):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code


def error_response(message, errors=None, status_code=400):
    return jsonify({
        "status": "error",
        "message": message,
        "errors": errors
    }), status_code

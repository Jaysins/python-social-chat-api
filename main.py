from app import create_app
from flask import jsonify

app = create_app()


@app.errorhandler(Exception)
def handle_server_error(err):
    return jsonify({
        'message': str(err)
    }), 400


if __name__ == '__main__':
    app.run(debug=True)

from app import create_app, db
from flask import jsonify

app = create_app()

with app.app_context():
    db.create_all()


@app.errorhandler(Exception)
def handle_server_error(err):
    return jsonify({
        'message': str(err)
    }), 400


if __name__ == '__main__':
    app.run(debug=True, port=3000)

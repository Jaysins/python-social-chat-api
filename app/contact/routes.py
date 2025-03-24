from flask import jsonify
from flask_blueprint import Blueprint

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({})


@contact_bp.route('/contacts', methods=['POST'])
def create_contacts():
    return jsonify({})


@contact_bp.route('/contacts/{id}', methods=['GET'])
def get_contact_by_id(id):
    return jsonify({})

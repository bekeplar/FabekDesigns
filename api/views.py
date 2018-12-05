from flask import Flask, request, jsonify, Blueprint
import datetime
import re
#from api.models import Order, User
from flask_jwt_extended import(create_access_token,
JWTManager, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash

blueprint = Blueprint('application', __name__)


@blueprint.route('/')
def home():
    return jsonify({
                'message': 'Welcome to FabekDesigns.'
            }), 200

from flask import Blueprint, jsonify

user_service = Blueprint('user_service', __name__)


@user_service.route('/')
def index():
    users = [{"name": "Jose Alejandro", "email": "jose.alvarez@gssi.it"},
             {"name": "Juan Antonio", "email": "antonio.pinera@gssi.it"}]
    return jsonify({'data': users,
                    })

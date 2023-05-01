from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify

from DB_operations.login import db
from decorators.validation import validate_data

login_API = Blueprint('login_API', __name__)


class LoginAPI:

    @staticmethod
    @login_API.route('/login', methods=['POST'])
    @validate_data(func_name="login")
    def login():
        """
        endpoint:/tr/api/kart-saklamali-odeme
        :return: Token
        """
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        collection = db["users"]
        user = collection.find_one({"userNo": username})

        if not user or not collection.find_one({"authCode": password}):
            return jsonify({"msg": "Kullanıcı adı veya şifre hatalı"}), 401

        access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=43200))
        return jsonify(access_token=access_token), 200

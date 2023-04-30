from flask import Flask
from flask_jwt_extended import JWTManager

from API_operations.card_API import card_API
from API_operations.login_API import login_API
from API_operations.payment_api import transaction_API

app = Flask(__name__)


if __name__ == "__main__":
    app.register_blueprint(card_API)
    app.register_blueprint(login_API)
    app.register_blueprint(transaction_API)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)

    app.run(host="0.0.0.0", debug=True)




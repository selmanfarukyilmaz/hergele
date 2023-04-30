import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import make_response, Blueprint, request

from DB_operations.card import create_card
from decorators.validation import validate_data, save_response

card_API = Blueprint('user_API', __name__)

class CardAPI:


    @staticmethod
    @card_API.route("/tr/api/kart-saklama", methods=["POST"])
    @validate_data(func_name="create_card")
    @jwt_required()
    @save_response
    def create_card():
        current_user = get_jwt_identity()

        request_data = json.loads(request.data)

        data_set, status_code = create_card(guid=request_data["GUID"],
                                            cc_owner=request_data["KK_Sahibi"],
                                            cc_number=request_data["KK_No"],
                                            exp_month=request_data["KK_SK_Ay"],
                                            exp_year=request_data["KK_SK_Yil"],
                                            card_name=request_data["KK_Kart_Adi"],
                                            cc_uniq_id=request_data["KK_Islem_ID"],
                                            username=current_user)
        return make_response(data_set, status_code)
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import make_response, Blueprint, request

from DB_operations.card import create_card, get_list_cards
from decorators.validation import validate_data, save_response, require_header_check

card_API = Blueprint('user_API', __name__)


class CardAPI:

    @staticmethod
    @card_API.route("/tr/api/kart-saklama", methods=["POST"])
    @require_header_check
    @validate_data(func_name="create_card")
    @jwt_required()
    @save_response
    def create_card():
        """
        For Creating Cards
        endpoint:/tr/api/kart-saklama
        security: jwt_required
        """
        current_user = get_jwt_identity()

        request_data = json.loads(request.data)
        print(request_data)
        data_set, status_code = create_card(guid=request_data["GUID"],
                                            cc_owner=request_data["KK_Sahibi"],
                                            cc_number=request_data["KK_No"],
                                            exp_month=request_data["KK_SK_Ay"],
                                            exp_year=request_data["KK_SK_Yil"],
                                            card_name=request_data["KK_Kart_Adi"],
                                            cc_uniq_id=request_data["KK_Islem_ID"],
                                            username=current_user)

        return make_response(data_set, status_code)

    @staticmethod
    @card_API.route("/tr/api/kart-saklama-listesi", methods=["POST"])
    @require_header_check
    @validate_data(func_name="get_list_of_cards")
    @jwt_required()
    @save_response
    def get_list_of_cards():
        """
        For Getting list of Card for spesific user
        endpoint:/tr/api/kart-saklama-listesi
        security: jwt_required
        """
        current_user = get_jwt_identity()

        request_data = json.loads(request.data)
        print(request_data)
        data_set, status_code = get_list_cards(guid=request_data["GUID"],
                                               user=current_user)

        return make_response(data_set, status_code)

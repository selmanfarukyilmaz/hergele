import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import make_response, Blueprint, request

from DB_operations.card import create_card
from DB_operations.payment import payment, cancel_refund
from decorators.validation import validate_data, save_response

transaction_APIs = Blueprint('transaction_APIS', __name__)


class TransactionAPI:

    @staticmethod
    @transaction_APIs.route("/tr/api/kart-saklamali-odeme", methods=["POST"])
    @validate_data(func_name="payment_endpoint")
    @jwt_required()
    @save_response
    def payment_endpoint():
        current_user = get_jwt_identity()
        request_data = json.loads(request.data)
        data_set, status_code = payment(pos_guid=request_data["GUID"],
                                        cc_guid=request_data["KS_GUID"],
                                        cc_owner_gsm=request_data["KK_Sahibi_GSM"],
                                        error_url=request_data["Hata_URL"],
                                        success_url=request_data["Basarili_URL"],
                                        order_id=request_data["Siparis_ID"],
                                        order_desc=request_data["Siparis_Aciklama"],
                                        installment=request_data["Taksit"],
                                        transaction_amount=request_data["Islem_Tutar"],
                                        total_amount=request_data["Toplam_Tutar"],
                                        security_type=request_data["Islem_Guvenlik_Tip"],
                                        ip=request_data["IPAdr"],
                                        ref_url=request_data["Ref_URL"],
                                        cvv=request_data["CVV"],
                                        transaction_id=request_data["Islem_ID"],  #
                                        data_1=request_data["Data1"],
                                        data_2=request_data["Data2"],
                                        data_3=request_data["Data3"],
                                        data_4=request_data["Data4"],
                                        cc_transaction_id=request_data["KK_Islem_ID"],
                                        user=current_user
                                        )
        return make_response(data_set, status_code)

    @staticmethod
    @transaction_APIs.route("/tr/api/islem-iptal-ve-iadeleri", methods=["POST"])
    @validate_data(func_name="cancel_refund_endpoint")
    @jwt_required()
    @save_response
    def cancel_refund_endpoint():
        current_user = get_jwt_identity()
        request_data = json.loads(request.data)
        data_set, status_code = cancel_refund(guid=request_data["GUID"],
                                              func_type=request_data["Durum"],
                                              order_id=request_data["Siparis_ID"],
                                              amount=request_data["Tutar"],
                                              user=current_user
                                              )
        return make_response(data_set, status_code)

from functools import wraps
from datetime import datetime
from cerberus import Validator
from flask import jsonify, request
import json
from DB_operations.login import db
from decorators.schema import schematics
from bson import ObjectId


def check_user_exist(func):
    def wrapper(guid, *args, **kwargs):
        collection = db["users"]

        if not collection.find_one({"GUID": guid}):
            print("check_user_exist hata")
            response = {"Sonuc": 0,
                        "Sonuc_Str": "Başarısız",
                        "KS_GUID": ""}
            # collection = db["responses"]
            # collection.insert_one({"Sonuc": 0,
            #                        "Sonuc_Str": "Başarısız - GUID Kayıtlı Kullanıcı yok",
            #                        "KS_GUID": "",
            #                        "method": "KS_Kart_Ekle"})
            return jsonify(response), 404
        return func(guid=guid, *args, **kwargs)

    return wrapper


def check_card_exist(func):
    def wrapper(cc_uniq_id, cc_number, *args, **kwargs):
        collection = db["cards"]
        if collection.find_one({"KK_Islem_ID": cc_uniq_id}) or collection.find_one({"KK_No": cc_number}):
            print("check_card_exist hata")
            response = {"Sonuc": 0,
                        "Sonuc_Str": "Başarısız",
                        "KS_GUID": ""}
            # collection = db["responses"]
            # collection.insert_one({"Sonuc": 0,
            #                        "Sonuc_Str": "Başarısız - Kart daha önceden yaratılmış",
            #                        "KS_GUID": "",
            #                        "method": "KS_Kart_Ekle"})

            return jsonify(response), 404

        return func(cc_uniq_id=cc_uniq_id, cc_number=cc_number, *args, **kwargs)

    return wrapper


def validate_data(func_name):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            validity = validate_json(data, func_name)
            print(validity)
            if validity[0] != True:
                return jsonify(validity[0]), 400
            return func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        return wrapper

    return real_decorator


def validate_json(json_data: json, func_name: str):
    """
    Checks if the json file conforms to the rules

    :param json_data: Json file
    :param func_name: Name of the function used
    :return: True or error with status code
    """
    schema = schematics(func_name=func_name)
    v = Validator(schema)
    if v.validate(json_data, schema) == True:
        return True, v.normalized(json_data)
    else:
        return v.errors, 404


def check_card(func):
    def wrapper(cc_guid, cvv, security_type, transaction_id, cc_owner_gsm, *args, **kwargs):
        print("check_card 1 ")

        if not cvv:
            cvv = "000"
        collection = db["cards"]
        card = collection.find_one({"GUID": cc_guid, "security_number": cvv})

        if not card:
            print("check_card hata 1")
            response = {"Sonuc": 0,
                        "Sonuc_Str": "Başarısız",
                        "UCD_URL": security_type,
                        "Islem_ID": transaction_id}
            # collection = db["responses"]
            # collection.insert_one({"Sonuc": 0,
            #                        "Sonuc_Str": "Başarısız",
            #                        "UCD_URL": security_type,
            #                        "Islem_ID": transaction_id,
            #                        "method": "KS_Tahsilat"})

            return jsonify(response), 404
        print("check_card 2 ")
        collection = db["users"]
        if not collection.find_one({"_id": ObjectId(card["KK_Sahibi_id"]), "phoneNumber": cc_owner_gsm,
                                    "selectedCard": cc_guid}):
            print("check_card hata 2")
            response = {"Sonuc": 0,
                        "Sonuc_Str": "Başarısız",
                        "UCD_URL": security_type,
                        "Islem_ID": transaction_id}
            # collection = db["responses"]
            # collection.insert_one({"Sonuc": 0,
            #                        "Sonuc_Str": "Başarısız",
            #                        "UCD_URL": security_type,
            #                        "Islem_ID": transaction_id,
            #                        "method": "KS_Tahsilat"})

            return jsonify(response), 404
        print("check_card 3 ")

        return func(cc_guid=cc_guid, cvv=cvv, security_type=security_type, transaction_id=transaction_id,
                    cc_owner_gsm=cc_owner_gsm, *args, **kwargs)

    return wrapper

def transaction_check(func):
    def wrapper(guid, func_type, order_id, amount, *args, **kwargs):

        collection = db["transaction"]
        error_response = {"Sonuc": 0,
                            "Sonuc_Str": "Declined",
                            "Banka_Sonuc_Kod": "0",
                            "Bank_AuthCode": "",
                            "Bank_Trans_ID": "",
                            "Bank_Extra": "",
                            "Bank_HostRefNum": ""}
        if func_type == "IPTAL":
            if not collection.find_one({"order_id": order_id, "pos_guid": guid, "total_amount": amount}):
                print("IPTAL hata")
                return error_response, 404

        else:
            transaction = collection.find_one({"order_id": order_id, "pos_guid": guid})
            if not transaction or transaction["amount"] < amount:
                print("İADE hata")
                return error_response, 404

        collection = db["transaction"]
        transaction = collection.find_one({"order_id": order_id})

        collection = db["users"]
        if not collection.find_one({"GUID": transaction["user_guid"]}):
            print("hatae3")
            return error_response, 404

        return func(guid=guid, func_type=func_type, order_id=order_id, amount=amount, *args, **kwargs)

    return wrapper


def save_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        collection = db["responses"]
        result = func(*args, **kwargs)
        status_code = result.status_code
        response_data = result.get_json()
        response_data.update({"status_code": status_code})
        response = {
            'timestamp': datetime.now(),
            'function_name': func.__name__,
            'response': response_data
        }
        collection.insert_one(response)
        return result

    return wrapper

def require_header_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'UserNo' not in request.headers:
            return jsonify({'error': 'UserNo header is missing'}), 400
        if 'Filo' not in request.headers:
            return jsonify({'error': 'Filo header is missing'}), 400
        return func(*args, **kwargs)
    return wrapper
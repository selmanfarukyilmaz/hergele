import uuid

from DB_operations.login import db
from bson import ObjectId

from decorators.validation import check_user_exist, check_card_exist, check_card, transaction_check
from decimal import Decimal

from helper import generate_random_string, generate_random_number_string


@check_card
def payment(pos_guid: str, cc_guid: str, cc_owner_gsm: str, error_url: str, success_url: str, order_id: str,
            order_desc: str,
            installment: int, transaction_amount: str, total_amount: str, security_type: str, ip: str, user: str,
            ref_url: str = None, cvv: str = None, transaction_id: str = None,
            data_1: str = None, data_2: str = None, data_3: str = None, data_4: str = None,
            cc_transaction_id: str = None) -> tuple:
    """

    :param pos_guid: Pos GUID
    :param cc_guid: Card GUID
    :param cc_owner_gsm: Owner GSM
    :param error_url: Error URL
    :param success_url: Success URL
    :param order_id: Order ID
    :param order_desc: Order Desc
    :param installment: Installment
    :param transaction_amount: Transaction Amount
    :param total_amount: Total Amount
    :param security_type: Security Type
    :param ip: Ip Address of current user.
    :param user: Current user
    :param ref_url: Reference Url
    :param cvv: CVV code
    :param transaction_id: Transaction ID
    :param cc_transaction_id: Card Transaction ID
    :return: Response, Status code
    """

    try:
        collection = db["cards"]
        card = collection.find_one({"GUID": cc_guid})
        if card["balance"] < float(total_amount):
            response = {"Sonuc": 0,
                        "Sonuc_Str": "Başarısız",
                        "UCD_URL": security_type,
                        "Islem_ID": transaction_id}

            return response, 404

        new_balance = float(Decimal(card["balance"]) - Decimal(total_amount))

        collection.find_one_and_update({"GUID": cc_guid}, {"$set": {"balance": new_balance}})

        collection = db["users"]
        user = collection.find_one({"_id": ObjectId(card["KK_Sahibi_id"])})
        collection.find_one_and_update({"GUID": user["GUID"]}, {"$set": {"balance": new_balance}})
        transaction = {
            "user_guid": user["GUID"],
            "pos_guid": pos_guid,
            "cc_guid": cc_guid,
            "cvv": cvv,
            "cc_owner_gsm": cc_owner_gsm,
            "error_url": error_url,
            "success_url": success_url,
            "order_id": order_id,
            "order_desc": order_desc,
            "installment": installment,
            "transaction_amount": transaction_amount,
            "total_amount": total_amount,
            "security_type": security_type,
            "transaction_id": transaction_id,
            "ip": ip,
            "ref_url": ref_url,
            "data_1": data_1,
            "data_2": data_2,
            "data_3": data_3,
            "data_4": data_4,
            "cc_transaction_id": cc_transaction_id,
            "old_balance": card["balance"],
            "new_balance": new_balance,
            "transaction_type": "Kart Saklamalı Ödeme"
        }

        collection = db["transaction"]

        collection.insert_one(transaction)

        if security_type == "NS":
            return_ucd_url = "NONSECURE"
        else:
            return_ucd_url = "www.3d_security.com"

        response = {"Sonuç": 1,
                    "Sonuc_Str": "Başarılı",
                    "UCD_URL": return_ucd_url,
                    "Islem_ID": transaction_id}

        # collection = db["responses"]
        # collection.insert_one(response)

        return response, 200
    except:
        if security_type == "NS":
            return_ucd_url = "NONSECURE"
        else:
            return_ucd_url = "www.3d_security.com"
        response = {"Sonuc": 0,
                    "Sonuc_Str": "Başarısız",
                    "UCD_URL": return_ucd_url,
                    "Islem_ID": transaction_id,
                    "status_code": 400,
                    "method": "KS_Tahsilat"}

        # collection = db["responses"]
        # collection.insert_one(response)
        return response, 404


@transaction_check
def cancel_refund(guid: str, func_type: str, order_id: str, amount: float, user) -> tuple:
    """
    If the entire order is to be returned, the "IPTAL" parameter should be sent to the func_type variable.
    If part of it is to be returned, the "IADE" parameter should go to the func_type variable.
    :param guid: GUID
    :param func_type: Type of refund type IADE or IPTAL is allowed
    :param order_id: Order ID of transaction
    :param amount: Amount of refund/return
    :param user: Current User
    :return: Response, Status code
    """

    try:
        collection = db["transaction"]
        transaction = collection.find_one({"order_id": order_id})

        collection = db["users"]
        user_data = collection.find_one({"GUID": transaction["user_guid"]})

        if user_data:
            if user_data["userNo"] != user:
                response = {"Sonuc": 0,
                            "Sonuc_Str": "Declined",
                            "Banka_Sonuc_Kod": "0",
                            "Bank_AuthCode": "",
                            "Bank_Trans_ID": "",
                            "Bank_Extra": "",
                            "Bank_HostRefNum": ""}
                return response, 404

        amount_data = collection.find_one({"GUID": transaction["user_guid"], "selectedCard": transaction["cc_guid"]})

        collection.find_one_and_update({"GUID": transaction["user_guid"], "selectedCard": transaction["cc_guid"]}, {
            "$set": {"balance": float(Decimal(float(amount_data["balance"])) + Decimal(float(amount)))}})
        collection = db["cards"]
        card_data = collection.find_one({"GUID": transaction["cc_guid"]})
        collection.find_one_and_update({"GUID": transaction["cc_guid"]}, {
            "$set": {"balance": float(Decimal(float(card_data["balance"])) + Decimal(float(amount)))}})
        collection = db["transaction"]
        collection.insert_one(
            {"GUID": guid,
             "Durum": func_type,
             "Siparis_ID": order_id,
             "Tutar": amount,
             "transaction_type": "İşlem İptal ve İadeleri"}
        )
        response = {"Sonuc": 1,
                    "Sonuc_Str": "Approved",
                    "Banka_Sonuc_Kod": "0",
                    "Bank_AuthCode": "115523",
                    "Bank_Trans_ID": generate_random_string(length=10),
                    "Bank_Extra": "&lt;Extra&gt;&lt;SETTLEID&gt;2501&lt;/SETTLEID&gt;&lt;TRXDATE&gt;20211019 14:50:19&l"
                                  "t;/TRXDATE&gt;&lt;ERRORCODE&gt;&lt;/ERRORCODE&gt;&lt;CARDBRAND&gt;VISA&lt;/CARDBRAND"
                                  "&gt;&lt;CARDISSUER&gt;T. HALK BANKASI A.S.&lt;/CARDISSUER&gt;&lt;NUMCODE&gt;00&lt;/N"
                                  "UMCODE&gt;&lt;/Extra&gt;",
                    "Bank_HostRefNum": generate_random_number_string(length=12)}

        return response, 200
    except:
        response = {"Sonuc": 0,
                    "Sonuc_Str": "Declined",
                    "Banka_Sonuc_Kod": "0",
                    "Bank_AuthCode": "",
                    "Bank_Trans_ID": "",
                    "Bank_Extra": "",
                    "Bank_HostRefNum": ""}
        return response, 400

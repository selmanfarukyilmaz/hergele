import uuid

from DB_operations.login import db

from decorators.validation import check_user_exist, check_card_exist, check_card
from decimal import Decimal


@check_card
def payment(pos_guid, cc_guid: str, cc_owner_gsm: str, error_url, success_url: str, order_id, order_desc,
            installment: int, transaction_amount: str, total_amount: str, security_type: str, ip: str, username: str,
            ref_url: str = None, cvv: str = None, transaction_id: str = None,
            data_1: str = None, data_2: str = None, data_3: str = None, data_4: str = None,
            cc_transaction_id: str = None) -> tuple:
    """
    Islem_ID değeri Dekont No değeridir
    """
    # try:
    print("başladı fonksiyona")
    collection = db["cards"]
    card = collection.find_one({"GUID": cc_guid})
    if card["balance"] < float(total_amount):
        print('card["balance"] < total_amount hata')
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
        return response, 404

    new_balance = float(Decimal(card["balance"]) - Decimal(total_amount))

    collection.find_one_and_update({"GUID": cc_guid}, {"$set": {"balance": new_balance}})

    collection = db["users"]
    collection.find_one_and_update({"GUID": card["KK_Sahibi_id"]}, {"$set": {"balance": new_balance}})

    transaction = {
        "user_guid": card["KK_Sahibi_id"],
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
        "new_balance": new_balance
    }

    collection = db["transaction"]

    collection.insert_one(transaction)

    if security_type == "NS":
        return_ucd_url = "NONSECURE"
    else:
        return_ucd_url = "www.3d_security.com"

    # response = {"Sonuc": 0,
    #             "Sonuc_Str": "Başarısız",
    #             "UCD_URL": return_ucd_url,
    #             "Islem_ID": transaction_id,
    #             "status_code": 400,
    #             "method": "KS_Tahsilat"}

    # collection = db["responses"]
    # collection.insert_one(response)

    return {"Sonuç": 1,
            "Sonuc_Str": "Başarılı",
            "UCD_URL": return_ucd_url,
            "Islem_ID": transaction_id}, 200
    # except:
    #     if security_type == "NS":
    #         return_ucd_url = "NONSECURE"
    #     else:
    #         return_ucd_url = "www.3d_security.com"
    #     print("expection ")
    #     response = {"Sonuc": 0,
    #                 "Sonuc_Str": "Başarısız",
    #                 "UCD_URL": return_ucd_url,
    #                 "Islem_ID": transaction_id,
    #                 "status_code": 400,
    #                 "method": "KS_Tahsilat"}
    #
    #     # collection = db["responses"]
    #     # collection.insert_one(response)
    #     return response, 404

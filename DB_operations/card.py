import uuid

from DB_operations.login import db
import datetime
from decorators.validation import check_user_exist, check_card_exist
from helper import hash_dict


@check_user_exist
@check_card_exist
def create_card(guid: str, cc_owner: str, cc_number: str, exp_month: str, exp_year: str, username: str,
                card_name: str = None,
                cc_uniq_id: str = None) -> tuple:
    try:
        collection = db["users"]
        owner = collection.find_one({"GUID": guid}, {"_id": 1, "userNo": 1})
        if username != owner["userNo"]:
            return {"Sonuc": "0", "Sonuc_Str": "Başarısız",
                    "KS_GUID": ""}, 404
        card_uuid = str(uuid.uuid4())
        post = {
            "GUID": card_uuid,
            "KK_Sahibi_GUID": guid,
            "KK_Sahibi": cc_owner,
            "KK_No": cc_number,
            "KK_SK_Ay": exp_month,
            "KK_SK_Yil": exp_year,
            "balance": float(0),
            "security_number": "000",
            "3d_secure_password": "34020",
            "KK_Banka": "YAPIKREDİ A.Ş.",
            "KK_tip": "VISA",
            "KK_Marka": "Maximum",
            "KK_KD": "Kredi Kartı",
            "KK_SK": f"{exp_year}-{exp_month}-31T00:00:00+03:00",
            "KK_Sahibi_id": str(owner['_id']),
            "create_date": datetime.date.today()}
        if card_name:
            post["KK_Kart_Adi"] = card_name
        if cc_uniq_id:
            post["KK_Islem_ID"] = cc_uniq_id

        collection = db["cards"]
        collection.insert_one(post)

        collection = db["users"]
        collection.find_one_and_update({'GUID': guid}, {'$push': {'allCards': f"{card_uuid}"}})

        response = {"Sonuc": 1,
                    "Sonuc_Str": "Başarılı",
                    "KS_GUID": str(card_uuid)}

        # collection = db["responses"]
        #
        # collection.insert_one({"Sonuc": 1,
        #                        "Sonuc_Str": "Başarılı",
        #                        "KS_GUID": str(card_uuid),
        #                        "status_code": 201,
        #                        "method": "KS_Kart_Ekle"})

        return response, 201
    except Exception as a:
        response = {"Sonuc": 0,
                    "Sonuc_Str": "Başarısız - Bilinmeyen Hata",
                    "KS_GUID": "",
                    "status_code": 400,
                    "method": "KS_Kart_Ekle"}
        # collection = db["responses"]
        # collection.insert_one(response)
        return response, 400


@check_user_exist
def get_list_cards(guid: str, user) -> tuple:
    collection = db["users"]
    user_data = collection.find_one({"GUID": guid})
    if user_data["userNo"] != user:
        return {"Sonuc": 0,
                "Sonuc_Str": "Başarısız",
                "DT_Bilgi": []}, 400

    response = {"Sonuc": 1,
                "Sonuc_Str": "Başarılı",
                "DT_Bilgi": []}

    collection = db["cards"]
    for card in user_data["allCards"]:
        card_data = collection.find_one({"GUID": card})
        if "KK_Kart_Adi" not in card_data:
            card_data["KK_Kart_Adi"] = ""
        response["DT_Bilgi"].append({"ID": str(card_data["_id"]),
                                     "KK_GUID": card_data["GUID"],
                                     "Tarih": card_data["create_date"],
                                     "KK_No": card_data["KK_No"],
                                     "KK_Tip": card_data["KK_KD"],
                                     "KK_Banka": card_data["KK_Banka"],
                                     "KK_Marka": card_data["KK_Marka"],
                                     "Kart_Adi": card_data["KK_Kart_Adi"],
                                     "KK_Hash": hash_dict(card_data),
                                     "KK_KD": card_data["KK_tip"],
                                     "KK_SK": card_data["KK_SK_Ay"] + card_data["KK_SK_Yil"],
                                     }
                                    )
    return response, 200

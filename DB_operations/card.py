import uuid

from DB_operations.login import db

from decorators.validation import check_user_exist, check_card_exist


@check_user_exist
@check_card_exist
def create_card(guid: str, cc_owner: str, cc_number: str, exp_month: str, exp_year: str, username: str,
                card_name: str = None,
                cc_uniq_id: str = None) -> object:
    try:
        collection = db["users"]
        owner = collection.find_one({"authCode": guid}, {"_id": 1, "username": 1})
        if username != owner["username"]:
            return {"Sonuc": "0", "Sonuc_Str": "Başarısız",
                    "KS_GUID": ""}, 404  # todo
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
            "KK_Sahibi_id": str(owner['_id'])}
        if card_name:
            post["KK_Kart_Adi"] = card_name
        if cc_uniq_id:
            post["KK_Islem_ID"] = cc_uniq_id

        collection = db["cards"]
        collection.insert_one(post)

        collection = db["users"]
        collection.find_one_and_update({'authCode': guid}, {'$push': {'allCards': f"{card_uuid}"}})

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
    except:
        # response = {"Sonuc": 0,
        #             "Sonuc_Str": "Başarısız - Bilinmeyen Hata",
        #             "KS_GUID": "",
        #             "status_code": 400,
        #             "method": "KS_Kart_Ekle"}
        # collection = db["responses"]
        # collection.insert_one(response)
        # return response
        pass

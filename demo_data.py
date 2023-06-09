import datetime

from DB_operations.login import db

collection = db["users"]

users = [
    {
        "userNo": "1",
        "authCode": "12345678",
        "GUID": "f0cd28f2-977e-4e0b-b0f5-e9bde9e74b68",
        "name": "Selman",
        "surname": "Kaya",
        "birthDate": "11/11/2001",
        "phoneNumber": "5551234567",
        "email": "selman_kaya@gmail.com",
        "selectedCard": "e74bf284-b141-4713-990c-cebf4e82946f",
        "allCards": ["e74bf284-b141-4713-990c-cebf4e82946f",
                     "88111a5d-3e50-4a37-8a51-6b935aa755f4"
                     ],
        "balance": float(500),
    },
    {
        "userNo": "2",
        "authCode": "12345678",
        "GUID": "86f00bcc-9bdd-4152-80d1-3ac2742263ac",
        "name": "İrem",
        "surname": "Yıldız",
        "birthDate": "09/09/1994",
        "phoneNumber": "5521234597",
        "email": "irem_yildiz@gmail.com",
        "selectedCard": "1069582e-c2fc-40fb-8d94-eeb68b87ea09",
        "allCards": ["1069582e-c2fc-40fb-8d94-eeb68b87ea09"
                     ],
        "balance": float(1000),
    },
    {
        "userNo": "3",
        "authCode": "12345678",
        "GUID": "21e9daf6-c15a-430b-98a5-f57faa2d079c",
        "name": "Mehmet",
        "surname": "Kılıç",
        "birthDate": "09/09/1993",
        "phoneNumber": "5521234566",
        "email": "mehmet_kilic@gmail.com",
        "selectedCard": "a9cd94dc-b1cc-4621-a91e-4207efa4124c",
        "allCards": ["a9cd94dc-b1cc-4621-a91e-4207efa4124c"
                     ],
        "balance": float(2000),
    },
    {
        "userNo": "4",
        "authCode": "12345678",
        "GUID": "baeebb08-3958-439d-bdaa-ee59fc4fdcd4",
        "name": "Zeynep",
        "surname": "Altın",
        "birthDate": "03/03/1996",
        "phoneNumber": "5521994553",
        "email": "zeynep_altin@gmail.com",
        "selectedCard": "0b48a0ac-1dd0-4db0-82aa-772be05d2905",
        "allCards": ["0b48a0ac-1dd0-4db0-82aa-772be05d2905"
                     ],
        "balance": float(25000),
    },
    {
        "userNo": "5",
        "authCode": "12345678",
        "GUID": "e4b31bc9-955d-4442-8f8a-998fe54ba9c4",
        "name": "Şafak",
        "surname": "Uzun",
        "birthDate": "03/03/1990",
        "phoneNumber": "5521924563",
        "email": "safak_uzun@gmail.com",
        "selectedCard": "6c9bc5f2-2ce2-4e3b-95cc-0347ff873b5f",
        "allCards": ["6c9bc5f2-2ce2-4e3b-95cc-0347ff873b5f"
                     ],
        "balance": float(15000),
    },
    {
        "userNo": "6",
        "authCode": "12345678",
        "GUID": "71a20028-5747-4e32-8a95-cd99769f3e99",
        "name": "Şebnem",
        "surname": "Tütüncü",
        "birthDate": "03/01/1991",
        "phoneNumber": "5533994593",
        "email": "sebnem_tutuncu@gmail.com",
        "selectedCard": "",
        "allCards": ["f84387ea-dcea-4b1c-81ca-a6d1feb2ec92"
                     ],
        "balance": float(30000),
    },
    {
        "userNo": "7",
        "authCode": "12345678",
        "GUID": "8d1f7a57-176a-4c1b-a5d3-f683758768a4",
        "name": "Zehra",
        "surname": "Çamlıdere",
        "birthDate": "03/03/1990",
        "phoneNumber": "5521997563",
        "email": "zehra_camlidere@gmail.com",
        "selectedCard": "ee198307-5802-4337-964b-cde32329212c",
        "allCards": ["ee198307-5802-4337-964b-cde32329212c"
                     ],
        "balance": float(0),
    },
    {
        "userNo": "8",
        "authCode": "12345678",
        "GUID": "1a93e553-0c43-4577-9ca5-54dd5ddec2e9",
        "name": "Yasin",
        "surname": "Türk",
        "birthDate": "05/05/1999",
        "phoneNumber": "5419458878",
        "email": "yasin_turk@gmail.com",
        "selectedCard": "",
        "allCards": [""
                     ],
        "balance": float(80000),
    },
    {
        "userNo": "9",
        "authCode": "12345678",
        "GUID": "62e90f79-045a-44cb-8a79-b2a116b6e4a1",
        "name": "Cansu",
        "surname": "Gök",
        "birthDate": "03/03/1990",
        "phoneNumber": "5521994563",
        "email": "cansu_gok@gmail.com",
        "selectedCard": "ed6c7d94-9648-4bb6-aa9b-b69280839fd0",
        "allCards": ["ed6c7d94-9648-4bb6-aa9b-b69280839fd0"
                     ],
        "balance": float(40000),
    },
    {
        "userNo": "10",
        "authCode": "12345678",
        "GUID": "be97f9da-5b2a-4a83-9b00-9c236bdafde4",
        "name": "Elvan",
        "surname": "Dere",
        "birthDate": "03/03/1991",
        "phoneNumber": "5521324512",
        "email": "elvan_dere@gmail.com",
        "selectedCard": "2662772b-6497-4855-977a-a6eb05b6f093",
        "allCards": ["2662772b-6497-4855-977a-a6eb05b6f093",
                     "09df145b-fe13-4119-b4d7-eda81d583cfd"
                     ],
        "balance": float(500),
    }
]

db.users.create_index([("GUID", 1), ("userNo", 1), ("email", 1), ("phoneNumber", 1)], unique=True)
print(db.users.getIndexes)
users_data = collection.insert_many(users)

collection = db["cards"]

cards = [
    {
        "GUID": "e74bf284-b141-4713-990c-cebf4e82946f",
        "KK_Sahibi": "Selman Kaya",
        "KK_No": "4546711234567894",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2026",
        "KK_Kart_Adi": "selman kişisel",
        "KK_Islem_ID": "12",
        "balance": float(500),
        "security_number": "000",
        "3d_secure_password": "a",
        "KK_Banka": "T.C. ZİRAAT BANKASI A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2026-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "88111a5d-3e50-4a37-8a51-6b935aa755f4",
        "KK_Sahibi": "Selman Kaya",
        "KK_No": "4022774022774026",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2026",
        "KK_Kart_Adi": "ödeme",
        "KK_Islem_ID": "13",
        "balance": float(500),
        "security_number": "000",
        "3d_secure_password": "a",
        "KK_Banka": "FİNANSBANK A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2026-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "1069582e-c2fc-40fb-8d94-eeb68b87ea09",
        "KK_Sahibi": "İrem Yıldız",
        "KK_No": "4355084355084358",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2026",
        "KK_Kart_Adi": "irem emekli",
        "KK_Islem_ID": "14",
        "balance": float(1000),
        "security_number": "000",
        "3d_secure_password": "a",
        "KK_Banka": "AKBANK A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2026-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "a9cd94dc-b1cc-4621-a91e-4207efa4124c",
        "KK_Sahibi": "Mehmet Kılıç",
        "KK_No": "4508034508034509",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2026",
        "KK_Kart_Adi": "mehmet iş özel",
        "KK_Islem_ID": "15",
        "balance": float(2000),
        "security_number": "000",
        "3d_secure_password": "a",
        "KK_Banka": "İŞ BANKASI A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2026-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "0b48a0ac-1dd0-4db0-82aa-772be05d2905",
        "KK_Sahibi": "Zeynep Altın",
        "KK_No": "4531444531442283",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2026",
        "KK_Kart_Adi": "iş kart",
        "KK_Islem_ID": "16",
        "balance": float(25000),
        "security_number": "001",
        "3d_secure_password": "a",
        "KK_Banka": "HALK BANKASI A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2026-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "6c9bc5f2-2ce2-4e3b-95cc-0347ff873b5f",
        "KK_Sahibi": "Şafak Uzun",
        "KK_No": "4090700101174272",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2022",
        "KK_Kart_Adi": "ev",
        "KK_Islem_ID": "17",
        "balance": float(15000),
        "security_number": "104",
        "3d_secure_password": "a",
        "KK_Banka": "DENİZBANK A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2022-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "f84387ea-dcea-4b1c-81ca-a6d1feb2ec92",
        "KK_Sahibi": "Şebnem Tütüncü",
        "KK_No": "4506344103118942",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "benim kart",
        "KK_Islem_ID": "18",
        "balance": float(30000),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "ee198307-5802-4337-964b-cde32329212c",
        "KK_Sahibi": "Zehra Çamlıdere",
        "KK_No": "4506347023253988",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "zehra emeklilik",
        "KK_Islem_ID": "19",
        "balance": float(0),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "1bd45400-6abe-4a85-94b6-1cb8bfe57e7a",
        "KK_Sahibi": "Yasin Türk",
        "KK_No": "4506347028991897",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "yasin uçak",
        "KK_Islem_ID": "20",
        "balance": float(80000),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
    {
        "GUID": "ed6c7d94-9648-4bb6-aa9b-b69280839fd0",
        "KK_Sahibi": "Cansu Gök",
        "KK_No": "4506347026523718",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "cansu iş",
        "KK_Islem_ID": "21",
        "balance": float(40000),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},

    {
        "GUID": "2662772b-6497-4855-977a-a6eb05b6f093",
        "KK_Sahibi": "Elvan Dere",
        "KK_No": "5400617020092306",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "elvan iş",
        "KK_Islem_ID": "22",
        "balance": float(500),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},


    {
        "GUID": "09df145b-fe13-4119-b4d7-eda81d583cfd",
        "KK_Sahibi": "Elvan Dere",
        "KK_No": "5400617030400291",
        "KK_SK_Ay": "12",
        "KK_SK_Yil": "2025",
        "KK_Kart_Adi": "elvan ev",
        "KK_Islem_ID": "21",
        "balance": float(8000),
        "security_number": "000",
        "3d_secure_password": "34020",
        "KK_Banka": "YAPIKREDİ A.Ş.",
        "KK_tip": "VISA",
        "KK_Marka": "Maximum",
        "KK_KD": "Kredi Kartı",
        "KK_SK": "2025-12-31T00:00:00+03:00",
        "create_date": str(datetime.date.today())},
]
for card in cards:
    for i, user in enumerate(users):
        for card_id in user["allCards"]:
            if card["GUID"] == card_id:
                card["KK_Sahibi_id"] = str(users_data.inserted_ids[i])

collection.insert_many(cards)

db.cards.create_index([("GUID", 1), ("KK_No", 1)], unique=True)

collection = db["counter"]

collection.insert_one(
    {"_id": "user_no_counter",
     "user_no_counter": 10}
)


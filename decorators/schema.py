def schematics(func_name: str):
    """
    Contains the schemas of the rules of the json file where the functions are used

    :param func_name: Name of the function used
    :return: A dictionary containing the schema
    minlength ve maxlength regex
    """
    schemas = {"create_card": {"G": {'required': True, 'empty': False},
                               "GUID": {'required': True, 'empty': False, 'type': 'string', 'minlength': 36,
                                        'maxlength': 36},
                               "KK_Sahibi": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 150, "regex": "^[a-zA-Z ]*$"},
                               "KK_No": {'required': True, 'empty': False, 'type': 'string', 'minlength': 16,
                                         'maxlength': 16, 'regex': '^[0-9]+$'},
                               "KK_SK_Ay": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 2, 'regex': '^[0-9]+$'},
                               "KK_SK_Yil": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 4, 'regex': '^[0-9]+$'},
                               "KK_Kart_Adi": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 150},
                               "KK_Islem_ID": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 200},
                               },
               "login": {
                   "username": {'required': True, 'empty': False, 'type': 'string', 'minlength': 1, 'maxlength': 32},
                   "password": {'required': True, 'empty': False, 'type': 'string', 'minlength': 4, 'maxlength': 64},
                   },
               "payment_endpoint": {"G": {'required': True, 'empty': False},
                                  "GUID": {'required': True, 'empty': False, 'type': 'string', 'minlength': 36, 'maxlength': 36},
                                  "KS_GUID": {'required': True, 'empty': False, 'type': 'string', 'minlength': 36, 'maxlength': 36},
                                  "CVV": {'required': False, 'empty': False, 'type': 'string', 'minlength': 3, 'maxlength': 3, 'regex': '^[0-9]+$'},
                                  "KK_Sahibi_GSM": {'required': True, 'empty': False, 'type': 'string', 'minlength': 10, 'maxlength': 10,'regex': '^[0-9]+$'},
                                  "Hata_URL": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Basarili_URL": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Siparis_ID": {'required': True, 'empty': False, 'type': 'string'},
                                  "Siparis_Aciklama": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Taksit": {'required': True, 'empty': False, 'type': 'integer', 'maxlength': 2},
                                  "Islem_Tutar": {'required': True, 'empty': False, 'type': 'string', 'regex': r'^\d+(\.\d+)?$'},
                                  "Toplam_Tutar": {'required': True, 'empty': False, 'type': 'string', 'regex': r'^\d+(\.\d+)?$'},
                                  "Islem_Guvenlik_Tip": {'required': True, 'empty': False, 'type': 'string', "allowed": ["NS", "3D"]},
                                  "Islem_ID": {'required': False, 'empty': False, 'type': 'string'},
                                  "IPAdr": {'required': True, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Ref_URL": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Data1": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Data2": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Data3": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "Data4": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 250},
                                  "KK_Islem_ID": {'required': False, 'empty': False, 'type': 'string', 'maxlength': 200},
                                  },
               "cancel_refund_endpoint": {
                            "G": {'required': True, 'empty': False},
                                  "GUID": {'required': True, 'empty': False, 'type': 'string', 'minlength': 36, 'maxlength': 36},
                                  "Durum": {'required': True, 'empty': False, 'type': 'string', "allowed": ["IPTAL", "IADE"]},
                                  "Siparis_ID": {'required': False, 'empty': False, 'type': 'string'},
                                  "Tutar": {'required': True, 'empty': False, 'type': 'number', "coerce": float}
               },
               "get_list_of_cards": {
                            "G": {'required': True, 'empty': False},
                                  "GUID": {'required': True, 'empty': False, 'type': 'string', 'minlength': 36, 'maxlength': 36},
                                  "KS_KK_Kisi_ID": {'required': False, 'empty': False, 'type': 'string', 'minlength': 11, 'maxlength': 11, 'regex': '^[0-9]+$'},
               }

               }
    return schemas[func_name]

import random
import string
from bson import ObjectId
from bson import json_util
import json
import hashlib

def generate_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = "21292" + result_str + "05010531"
    return result_str
def generate_random_number_string(length):
    digits = [str(i) for i in range(10)]
    return ''.join(random.choices(digits, k=length))



def hash_dict(d):
    def default(o):
        if isinstance(o, ObjectId):
            return str(o)
        return json_util.default(o)

    json_string = json.dumps(d, sort_keys=True, default=default)
    return hashlib.sha256(json_string.encode('utf-8')).hexdigest()
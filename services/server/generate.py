import random
import orjson
import requests
import concurrent.futures

class Record():
    blocked_acess: bool
    age_limit: int
    theam_restriction: int

    def __init__(self, blocked_acess, age_limit, theam_restriction):
        self.blocked_acess = blocked_acess
        self.age_limit = age_limit
        self.theam_restriction = theam_restriction


def gen_params():
    blocked_acess = random.randint(0, 1)
    age_limit = random.randint(2, 6)
    theam_restriction = random.randint(7, 28)
    return [blocked_acess, age_limit, theam_restriction]

def gen_params2mod():
    blocked_acess = random.randint(0, 1)
    age_limit = random.randint(0, 5)
    theam_restriction = random.randint(0, 21)
    return [blocked_acess, age_limit, theam_restriction]

def batch_send(size: int = 20):
    obj_list = []
    for j in range(1, size):
        obj_list.append(Record(*gen_params()))
    # print(obj_list)
    # print([obj.__dict__ for obj in obj_list])
    requests.post("http://localhost:5001/records", data=orjson.dumps(
        list([obj.__dict__ for obj in obj_list]),
        option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY))

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(1, 1000):
        executor.submit(batch_send, (50))

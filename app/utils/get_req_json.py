import json


def get_req_json(req_data):
    return json.loads(req_data.decode("utf-8"))

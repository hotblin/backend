from flask import request,jsonify
from . import api
from app.models.models import City
import json


@api.route('/city', methods=["get"])
def get_city():
    city = City().query.all()
    list = []
    for item in city:
        list.append(item.to_dict())

    return jsonify({
        'code':200,
        "list":list
    })

    # city_list = list(city)
    # for item in city_list:
    #     print(json.dumps(item, default=lambda item: item.__dict__))
    #
    # return "22"


"""
get请求是通过flask.request.args来获取。
post请求是通过flask.request.form来获取。
"""


@api.route("/city", methods=["post"])
def post_city():
    req_data = request.get_data()
    json_data = json.loads(req_data.decode("utf-8"))
    print(json_data)
    return "111"

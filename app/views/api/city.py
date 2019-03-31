from flask import request, jsonify, abort
import datetime
import uuid

from app.utils.get_req_json import get_req_json
from app.models.models import City
from app.models.models import db
from . import api


@api.route('/city', methods=["get"])
def get_city():
    # name required，可以为空
    name = request.args.get("name") or ""
    if name is None:
        abort(500)
    else:
        # 模糊查询
        city_result = City.query.filter(City.name.startswith(name)).all()

        list_city = []
        for item in city_result:
            list_city.append(item.to_dict())

        return jsonify({
            "list": list_city
        })


"""
get请求是通过flask.request.args来获取。
post请求是通过flask.request.form来获取。
"""


@api.route("/city", methods=["post"])
def post_city():
    # post
    # 判断是否已经存在，
    # 如果不存在
    req_data = get_req_json(request.get_data())
    result_city = City.query.filter_by(name=req_data['name']).first()
    if result_city is not None:
        return jsonify({"code": 500, 'msg': '该城市已存在'})
    new_city = City()
    new_city.id = uuid.uuid1()
    new_city.name = req_data['name']
    new_city.created_at = datetime.datetime.now()
    new_city.sys_code = req_data['sysCode']
    print(new_city)
    # 将新创建的用户添加到数据库会话中
    db.session.add(new_city)
    # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
    db.session.commit()

    print(req_data)
    return "111"


@api.route("/city", methods=["put"])
def put_city():
    return "修改"

from flask import request, jsonify, abort, g
import datetime
import uuid
import logging

from app.models.models import User
from app.models.models import Role
from app.models.models import Province
from app.models.models import db
from . import api
from app import auth


# @auth.verify_password
# def verify_password(username_or_token, password):
#     # first try to authenticate by token
#
#     if not user:
#         # try to authenticate with username/password
#         user = User.query.filter_by(username=username_or_token).first()
#         if not user or not user.verify_password(password):
#             return False
#     g.user = user
#     return True
@auth.verify_token
def verify_token(token):
    logging.info('校验用户token%s' % token)
    g.current_user = User.verify_auth_token(token)
    return g.current_user is not None


@api.route('/user/me', methods=["get"])
@auth.login_required
def get_user():
    user = User.query.filter_by(username='admin1').first().to_dict()
    role = Role.query.filter_by(id=user["role_id"]).first().to_dict()
    province = Province.query.filter_by(id=user["area_id"]).first()

    """
    province = None if province is None else province.to_dict()
    result = {
        "rname": role['name'],
        "roleDesc": role["description"],
        "areaCode": "" if province is None else province["sys_code"],
        "areaId": "" if province is None else province["id"],
        "areaName": "" if province is None else province["name"]
        # company: ""
        # companyId: ""
        # contactName: ""
        # contactPhone: ""
        # createdAt: 1498228677000
        # email: "test"
        # havElectricalSafety: false
        # havHeatVideo: false
        # havHumiture: false
        # havPowerMonitor: false
        # id: "b360fe5e-1c0c-4bfd-9af0-bcd3433c8e12"
        # lat: 0
        # lng: 0
        # name: "admin"
        # phone: "234234"
        # platform: 0
        # rname: "ROLE_ADMIN"
        # roleDesc: "超级管理员"
        # updatedAt: 1500972019000
        # url: ""
        # username: "admin"
    }
    print(result)
    """
    return jsonify({
        "code": 200,
        "data": user,
        "message": "SUCCESS"
    })


@api.route("/user/login", methods=["post"])
def user_login():
    req_data = request.json
    user = User.query.filter_by(username=req_data['userName']).first()
    if not user:
        abort(400)
    elif user.verify_password(req_data['password']):
        token = user.generate_auth_token()
        return jsonify({
            "code": 200,
            "token": token.decode('ascii')
        })
    else:
        abort(400)


@api.route('/role', methods=['get'])
def get_role():
    role_list = Role.query.all()
    for item in role_list:
        print(item.name)
    role_list = [item.to_dict() for item in role_list]
    return jsonify({
        "code": 200,
        "data": role_list
    })


@api.route("/user", methods=["post"])
def post_user():
    # name  bjsd   "password": "111111",

    req_data = request.json
    # name = req_data.get("name") or "false"
    # name = req_data["name"] or "6789"

    result = User.query.filter_by(username=req_data['username']).first()
    if result is not None:
        return jsonify({
            "code": 300,
            "message": "该用户已存在"
        })

    user = User()
    user.id = uuid.uuid1()
    user.name = req_data["name"]
    user.username = req_data["username"]
    user.email = req_data["email"]
    user.phone = req_data['phone']
    user.company_id = req_data['companyId']
    user.created_at = datetime.datetime.now()
    user.updated_at = datetime.datetime.now()
    user.area_id = req_data['areaId']
    # user.role_id = req_data["roleId"] or ""
    user.role_id = ''
    user.hash_password(req_data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "code": 200,
        'message': "success"
    })

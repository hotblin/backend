from . import api
from app.models.models import Busines
import json



def class_to_dict(obj):
    '''
    把对象(支持单个对象、list、set)转换成字典
    :param obj:
    :return:
    '''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


@api.route('/busines')
def get_busines():
    b = Busines().query.all()
    for item in b:
        print(item.to_json())
    # list_b = list(b)
    # result = [class_to_dict(item) for item in list_b]
    # for item in result:
    #     print(item)

    # for item in list_b:
    #     print(json.dumps(item, default=lambda x: x.__dict__))
    return '123'

from . import api
from app.models.models import City
from app.utils.parse_json import AlchemyJsonEncoder
import json


@api.route('/city', methods=["get"])
def get_city():
    city = City().query.all()

    return list(city)

    # city_list = list(city)
    # for item in city_list:
    #     print(json.dumps(item, default=lambda item: item.__dict__))
    #
    # return "22"

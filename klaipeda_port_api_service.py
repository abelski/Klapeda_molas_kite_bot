import os
from enum import Enum

import requests


class ApiMethods(Enum):
    WIND_SPEED = "wind_speed"
    WIND_GUST = "wind_gust_speed"
    WIND_DIRECTION = "wind_direction"
    AIR_TEMP = "air_temparature_first"


apiLink = "https://portofklaipeda.lt/wp-json/api/meteo_data?method="

method = ApiMethods.WIND_SPEED.value


def get_data_from_api(api_method):
    json_list = requests.get(apiLink + api_method.value).json()
    last_index = len(json_list) - 1
    value = json_list[last_index]

    return float(value[1])


def build_message():
    current_speed = get_data_from_api(ApiMethods.WIND_SPEED)
    current_direction = get_data_from_api(ApiMethods.WIND_DIRECTION)
    current_temp = get_data_from_api(ApiMethods.AIR_TEMP)
    result = ""
    if current_speed < 4:
        result += "wind to weak (%s)" % str(current_speed)
    elif current_speed < 6:
        result += "wind enought for foil (%s)" % str(current_speed)
    else:
        result += "good wind for ride (%s)" % str(current_speed)

    result += os.linesep
    if current_direction > 190:
        result += "but direction is - offshore"
    result += os.linesep
    if current_temp < 10:
        result += "and bit cold - %s" % str(current_temp)

    print("current speed:" + str(current_speed))
    print("current direction:" + str(current_direction))
    print("current temp:" + str(current_temp))

    return result


print(build_message())

import requests


def geocoder_request(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    return response.json()


def get_ll_spn(json_response):
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    lower_x, lower_y = map(
        float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())
    upper_x, upper_y = map(
        float, toponym["boundedBy"]["Envelope"]["upperCorner"].split())
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym_coodrinates.split(" "), [str((upper_x - lower_x) / 2), str((upper_y - lower_y) / 2)]


def static_map_request(params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=params)

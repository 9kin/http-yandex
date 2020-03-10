import requests
import math


def search_requests(params):
    api_server = "https://search-maps.yandex.ru/v1/"
    return requests.get(api_server, params=params)


def get_ll_schedule(organization):
    hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    return org_point, hours

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)
    return distance


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

#  python3 task3.py Пермь, ул. Пушкина, 76
import sys
from io import BytesIO
import requests
from PIL import Image
import geocoder

from PIL import ImageFont
from PIL import ImageDraw

toponym_to_find = " ".join(sys.argv[1:])
json = geocoder.geocoder_request(toponym_to_find)
ll, spn = geocoder.get_ll_spn(json)

json = geocoder.geocoder_request("", {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": ll,
    "format": "json",
    "kind": "district"
})

print(json["response"]["GeoObjectCollection"]["featureMember"][1]["GeoObject"]["name"])
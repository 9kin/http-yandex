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

api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll":  ll,
    "type": "biz"
}

data = geocoder.search_requests(search_params).json()

pt = ""
for i in range(10):
    ll, schedule = geocoder.get_ll_schedule(data["features"][i])
    color = "gr"
    if "круглосуточно" in schedule:
        color = "dg"
    elif schedule != "":
        color = "db"
    pt += f"{ll},pm2{color}l~"

map_params = {
    "l": "map",
    "pt": pt[:-1]
}

response = geocoder.static_map_request(map_params)
img = Image.open(BytesIO(response.content)).show()

#  python3 task2.py Москва, ул. Ак. Королева, 12
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
    "ll": ",".join(ll),
    "type": "biz"
}

data = geocoder.search_requests(search_params).json()
organization = data["features"][0]

hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])
map_params = {
    "l": "map",
    "pt": "{0},pm2dgl~{1},ya_ru".format(org_point, ",".join(ll))
}

response = geocoder.static_map_request(map_params)
img = Image.open(BytesIO(response.content))


dist = geocoder.lonlat_distance([float(ll[0]), float(ll[1])], point)

text = f'{org_address}\n{org_name}\n{hours}\n{int(dist)} метров'

font = ImageFont.truetype("DejaVuSans-BoldOblique.ttf", 16, encoding='UTF-8')
draw = ImageDraw.Draw(img)
draw.text((0, 0), text,(0, 0, 0), font=font)
img.show()

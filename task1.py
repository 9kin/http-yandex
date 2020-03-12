#  python3 task1.py Пермь, ул. Пушкина, 76
import sys
from io import BytesIO
import requests
from PIL import Image
import geocoder

toponym_to_find = " ".join(sys.argv[1:])
json = geocoder.geocoder_request(toponym_to_find)
ll, spn = geocoder.get_ll_spn(json)

map_params = {
    "ll": ll,
    "spn": ",".join(spn),
    "l": "map",
    "pt": ll + ",ya_ru"
}

response = geocoder.static_map_request(map_params)
Image.open(BytesIO(response.content)).show()
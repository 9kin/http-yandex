#  python3 task3.py Москва, ул. Ак. Королева, 12
import sys
from io import BytesIO
import requests
from PIL import Image
import geocoder
import random
import os
import pygame

citys = [
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Екатеринбург",
    "Нижний Новгород",
    "Казань",
    "Челябинск",
    "Омск",
    "Самара",
    "Ростов-на-Дону",
    "Уфа",
    "Красноярск",
    "Воронеж",
    "Пермь",
    "Волгоград",
]

random.shuffle(citys)

pygame.init()
screen = pygame.display.set_mode((600, 450))


def render_map(city):
    map_file = "map.png"
    with open(map_file, "wb") as file:
        geocoder.city_map(city, random.randrange(0, 2)).save(map_file)
        screen.blit(pygame.image.load(map_file), (0, 0))


run = 0
render_map(citys[run])
while run < len(citys):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run += 1
            render_map(citys[run])
    pygame.display.flip()
os.remove('map.png')

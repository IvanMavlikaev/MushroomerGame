import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 90
HEIGHT = 150


SIZE = (900, 300)

font_size = 20
#размер шрифта

walk = [
    "Gribnik1.png",
    "Gribnik2.png",
    "Gribnik3.png",
    "Gribnik4.png",
    "Gribnik5.png",
    "Gribnik6.png",
    "Gribnik7.png",
    "Gribnik8.png",
    "Gribnik9.png",
    "Gribnik10.png",
    "Gribnik11.png",
    "Gribnik12.png"
]

height_tree = dict()
height_tree['fir_tree.png'] = 60
height_tree['big_fir_tree.png'] = 135
height_tree['birch_tree.png'] = 135
height_tree['stump.png'] = 30

BACKGROUND = pg.image.load('fon_1.png')
#font = pg.font.SysFont("notosans", font_size) #устанавливает шрифт

tree_list = ['fir_tree.png', 'big_fir_tree.png', 'birch_tree.png', 'stump.png']
mushroom_list = ['krasnogolovik.png', 'fly_agaric.png']
import pygame as pg
import random
from constants import *
from sprite import *
from sprite_list import *


def touch(mushroom, height):
    if 435 <= mushroom.x <= 482 and height < 45:
        return True
    return False

def main():
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode(SIZE)

    pg.display.set_caption("Грибник")
    font = pg.font.SysFont("notosans", font_size)  # устанавливает шрифт

    game_over = False
    offset = 0  # смещение
    up = 0
    player_anim_count = 0
    jump = 0
    boost_up = 0
    height = 0

    tree_list = ['fir_tree.png', 'big_fir_tree.png', 'birch_tree.png', 'stump.png']
    mushroom_list = ['krasnogolovik.png', 'fly_agaric.png']
    coord_tree_list = [200, 300, 700, 850]
    coord_mushroom_list = [800]

    way = 0 # переменная для счётчика
    mushrooms_count = 0 # счётчик грибов

    krasnogolovik = Sprite(1000, 235, 'krasnogolovik.png')
    fly_agaric = Sprite(1000, 235, 'fly_agaric.png')
    mushrooms_list = SpriteList([krasnogolovik])

    while not game_over:
        way += 5
        offset += 10
        offset %= 900
        screen.blit(BACKGROUND, (0 - offset, 0))
        screen.blit(BACKGROUND, (900 - offset, 0))
        pg.draw.rect(screen, BLACK, (3, 3, 104, 29))
        pg.draw.rect(screen, WHITE, (5, 5, 100, 25))
        # прямоугольник для счётчика
        counter = font.render('Cчёт: ' + str(way), True, BLACK)
        # счётчик
        screen.blit(counter, (10, 10))

        pg.draw.rect(screen, BLACK, (3, 34, 104, 29))
        pg.draw.rect(screen, WHITE, (5, 36, 100, 25))
        mushrooms_counter = font.render('Грибов: ' + str(mushrooms_count), True, BLACK)
        screen.blit(mushrooms_counter, (10, 41))



        for i in range(len(mushrooms_list.list)):
            mushrooms_list.update_coordinats(-10, 0)
            screen.blit(pg.image.load(mushrooms_list.list[i].name), (mushrooms_list.list[i].x, mushrooms_list.list[i].y))
            if touch(mushrooms_list.list[i], height):
                if mushrooms_list.list[i].name == 'fly_agaric.png':
                    game_over = True
                else:
                    mushrooms_count += 1
                    mushrooms_list.pop()
                    choice = random.choice([1, 2])
                    if choice == 1:
                        fly_agaric.x = 1000
                        mushrooms_list.add(fly_agaric)
                    else:
                        krasnogolovik.x = 1000
                        mushrooms_list.add(krasnogolovik)

        while mushrooms_list.size and mushrooms_list.list[0].x < -100:
            mushrooms_list.pop()
            choice = random.choice([1, 2])
            if choice == 1:
                fly_agaric.x = 1000
                mushrooms_list.add(fly_agaric)
            else:
                krasnogolovik.x = 1000
                mushrooms_list.add(krasnogolovik)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if not jump:
                        jump += 1
                        boost_up = 50

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            up += 2
            screen.blit(pg.image.load(walk[player_anim_count]), (SIZE[0] // 2 - 45, SIZE[1] - 20 - 150 - up))
        else:
            if up >= 5:
                up -= 5
            screen.blit(pg.image.load(walk[player_anim_count]), (SIZE[0] // 2 - 45, SIZE[1] - 20 - 150 - height))
            if jump:
                height += boost_up
                boost_up -= 8
                if height < 0:
                    height = 0
                    jump = 0
        player_anim_count += 1
        player_anim_count %= 12
        pg.display.update()
        clock.tick(20)

    for i in range(50):
        pg.draw.rect(screen, (0, 0, 0), (140, 90, 520, 120))
        pg.draw.rect(screen, WHITE, (150, 100, 500, 100))
        font = pg.font.SysFont("notosans", font_size * 2)
        counter = font.render('ВАШ СЧЁТ: ' + str(way) + '   ГРИБОВ: ' + str(mushrooms_count), True, BLACK)
        screen.blit(counter, (200, 130))
        pg.display.update()
        clock.tick(20)


if __name__ == '__main__':
    main()
import pygame as pg
import random
from constants import *
from sprite import Sprite
from sprite_list import SpriteList


def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode(SIZE)

    pg.display.set_caption("Грибник")
    BACKGROUND = pg.image.load('fon_1.png') #background
    #fir_tree = pg.image.load('fir_tree.png')
    #big_fir_tree = pg.image.load('big_fir_tree.png')

    font = pg.font.SysFont("notosans", font_size) #устанавливает шрифт

    game_over = False

    offset = 0 # смещение
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

    while not game_over:
        way += 5
        offset += 10
        offset %= 900
        screen.blit(BACKGROUND, (0 - offset, 0))
        screen.blit(BACKGROUND, (900 - offset, 0))
        pg.draw.rect(screen, (255, 255, 255), (5, 5, 100, 25))
        # прямоугольник для счётчика
        counter = font.render(str(way), True, (0, 0, 0))
        # счётчик
        screen.blit(counter, (10, 10))


        while coord_tree_list[0] < -100: #  заменить на глобальную переменную
            coord_tree_list = coord_tree_list[1:]
            #count_new_trees = random.randint(1, 2)
            count_new_trees = 1

            if tree_list[0] == 'stump.png' or len(tree_list) > 10:
                count_new_trees = 1
            for i in range(count_new_trees):
                new_c = random.randint(coord_tree_list[-1], 1500)
                coord_tree_list.append(new_c)
                tree_list.append(tree_list[0])
            tree_list = tree_list[1:]

        for i in range(len(coord_tree_list)):
            coord_tree_list[i] -= 10
            screen.blit(pg.image.load(tree_list[i]), (coord_tree_list[i], 280 - height_tree[tree_list[i]]))
            if tree_list[i] == 'stump.png' and 435 <= coord_tree_list[i] <= 482 and height < 30:
                game_over = True

        while coord_mushroom_list[0] < -100:
            coord_mushroom_list = coord_mushroom_list[1:]
            #count_new_mushrooms = random.randint(1, 2)
            count_new_mushrooms = 1
            if mushroom_list[0] == 'fly_agaric.png' or len(mushroom_list) > 10:
                count_new_mushrooms = 1
            for i in range(count_new_mushrooms):
                new_c = random.randint(900, 1500)
                coord_mushroom_list.append(new_c)
                #mushroom_list.append(tree_list[0])
            coord_mushroom_list = coord_mushroom_list[1:]

        for i in range(len(coord_mushroom_list)):
            coord_mushroom_list[i] -= 10
            screen.blit(pg.image.load(mushroom_list[i]), (coord_mushroom_list[i], 280 - 45))
            if mushroom_list[i] == 'fly_agaric.png' and 435 <= coord_mushroom_list[i] <= 482 and height < 45:
                game_over = True

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
            screen.blit(pg.image.load(walk[player_anim_count]), (size[0] // 2 - 45, size[1] - 20 - 150 - up))
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
        pg.draw.rect(screen, (0, 0, 0), (190, 90, 520, 120))
        pg.draw.rect(screen, (255, 255, 255), (200, 100, 500, 100))
        font = pg.font.SysFont("notosans", font_size * 2)
        counter = font.render('ВАШ СЧЁТ: ' + str(way), True, (0, 0, 0))
        screen.blit(counter, (320, 130))
        pg.display.update()
        clock.tick(20)


if __name__ == '__main__':
    main()
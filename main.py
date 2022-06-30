import random
import pygame
from random import randint
from var import *
from obstacles import Obstacles
from add_fun import *

class Player():
    def __init__(self):
        self.user_width = 60
        self.user_height = 110
        self.user_x = WIDTH // 5
        self.lis_im = [pygame.image.load('лис1.png'), pygame.image.load('лис2.png'), pygame.image.load('лис3.png'),pygame.image.load('лис4.png'), pygame.image.load('лис5.png'), pygame.image.load('лис6.png'),pygame.image.load('лис7.png'), pygame.image.load('лис8.png'), pygame.image.load('лис9.png') ]

    def draw_player(self):
        global img_counter, user_y
        if img_counter == 81:
            img_counter = 0
        screen.blit(self.lis_im[img_counter // 9], (self.user_x, user_y))
        img_counter += 1

    def jump1(self):
        global make_jump, jump_count, user_y

        if jump_count ==-40:
            pygame.mixer.Sound.play(sound_jump)
        if jump_count >= -40:
            user_y -= jump_count / 4.5
            jump_count -= 1
        else:
            jump_count = 40
            make_jump = False


clock = pygame.time.Clock()

def create_arr(array):
    choice = random.randrange(0, 3)
    img = obstacles_img[choice]
    width = obstacles_size[choice * 2]
    height = obstacles_size[choice * 2 + 1]
    array.append(Obstacles(WIDTH + 10, height, width, img, 4))  # 4 это скорость

    choice = random.randrange(0, 3)
    img = obstacles_img[choice]
    width = obstacles_size[choice * 2]
    height = obstacles_size[choice * 2 + 1]
    array.append(Obstacles(WIDTH + 390, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = obstacles_img[choice]
    width = obstacles_size[choice * 2]
    height = obstacles_size[choice * 2 + 1]
    array.append(Obstacles(WIDTH + 800, height, width, img, 4))


def draw_array(array):
    for obst in array:
        check = obst.move()
        if not check:
            radius = dist(array)
            choice = random.randrange(0, 3)
            img = obstacles_img[choice]
            width = obstacles_size[choice * 2]
            height = obstacles_size[choice * 2 + 1]

            obst.return_self(radius, height, width, img)


def dist(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < WIDTH:
        radius = WIDTH
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)
    return radius


def check(barriers):
    for barrier in barriers:
        if user_y + user_height >= barrier.y:
            if barrier.x <= user_x <= barrier.x + barrier.width:
                return True
            elif barrier.x <= user_x + user_width <= barrier.x + barrier.width:
                return True

    return False


def scores1(barriers):
    fl = False
    global scores
    for barrier in barriers:
        if barrier.x < user_x  and jump_count == -40:
            fl = True
        if fl:
            scores += 1
            break


def game_over():
    global scores
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Game over. Your score is '+str(scores), 260, 300)
        print_text('To start over, press the space. To exit, press Tab', 160, 330)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return False
        if keys[pygame.K_SPACE]:
            scores = 0
            return True

        pygame.display.update()
        clock.tick(15)


make_jump = False

def run():
    global make_jump
    runner = Player()
    running = True
    obst_arr = []
    create_arr(obst_arr)
    background = pygame.image.load('фон0.jpg')

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True
        if keys[pygame.K_ESCAPE]:
            pause()
        if make_jump:
            runner.jump1()
        if running == False:
            game_over()

        screen.blit(background, (0, 0))
        runner.draw_player()
        draw_array(obst_arr)
        scores1(obst_arr)
        print_text('Score ' + str(scores), 50, 50)
        if check(obst_arr):
            pygame.mixer.Sound.play(fall)
            running = False
        pygame.display.update()
    return game_over()


while run():
    pass
pygame.quit()
quit()

import pygame



WIDTH = 800
HEIGHT = 600
FPS = 90
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

user_width = 60
user_height = 110
user_x = WIDTH // 5
user_y = HEIGHT - user_height - 150

c_w = 20
c_h = 70
c_x = WIDTH - 50
c_y = HEIGHT - c_h - 100

jump_count = 40
img_counter = 0
make_jump = False


fall = pygame.mixer.Sound('game_over.mp3')
sound_jump = pygame.mixer.Sound('jump_up.mp3')

scores = 0
above = False
obstacles_img = [pygame.image.load('камень2.0.png'), pygame.image.load('куст3.0.png'), pygame.image.load('камень4.png')]
obstacles_size = [100, 393, 88, 433, 100, 432]
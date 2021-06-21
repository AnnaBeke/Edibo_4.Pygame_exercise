import sys

import pygame
import sys
import random



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
# size of display

#Variables
gravity= 0.18
mushroom_movement=0
game_active = True

bg_surface = pygame.image.load('assets/background.png.png').convert()

floor = pygame.image.load('assets/base3.png').convert()
floor_x_pos= 0

mushroom = pygame.image.load('assets/bird.png').convert()
mush_rect = mushroom.get_rect(center=(120,300))

pipe_surface= pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [280,300,350,400,420,450,480]


def floor_move():
    screen.blit(floor,(floor_x_pos,500))
    screen.blit(floor,(floor_x_pos+ 600, 500))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700,random_pipe_pos- 250))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if mush_rect.colliderect(pipe):
            return False
    if mush_rect.top <= -100 or mush_rect.bottom >= 600:
            return False
    return True






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                mushroom_movement = 0
                mushroom_movement -= 6
            if event.key == pygame.K_SPACE and game_active == False:
                game_active == True
                pipe_list.clear()
                mush_rect.center = (120,300)
                mushroom_movement= 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, -100))

    if game_active:
        # Mushroom
        mushroom_movement += gravity
        mush_rect.centery += mushroom_movement
        screen.blit(mushroom, mush_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)





    # Floor
    floor_x_pos -= 1
    floor_move()
    if floor_x_pos <= -600:
        floor_x_pos = 0

    pygame.display.update()
    #updates the screen with everything that is coded in the loop
    clock.tick(100)

    #limits the frames per second





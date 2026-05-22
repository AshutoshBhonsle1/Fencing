import os
import random 
import math
import pygame
from os import listdir
from os .path import isfile, join

pygame.init()

pygame.display.set_caption("Fencing - One small step")

WIDTH,HEIGHT = 800,600
FPS=60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player(pygame.sprite.Sprite()): #inherts from pygame.sprite

    COLOR = (255,0,0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height) #to get pixel perfect collisions(i think)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = 0
        self.direction="left"
        self.animation_count=0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction!="left":
            self.direction="left"
            self.animation_count=0

    def move_right(self, vel):
        self.x_vel= +vel
        if self.direction!="right":
            self.direction="right"
            self.animation_count=0


def get_background(name):
    image = pygame.image.load(join("assets","Background",name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH//width + 1):
        for j in range(HEIGHT//height + 1):
            pos = (i*width, j*height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image,tile)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background('Yellow.png')

    run = True
    while run:  
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
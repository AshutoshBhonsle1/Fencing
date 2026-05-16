import os
import random 
import math
import pygame
from os import listdir
from os .path import isfile, join

pygame.init()

pygame.display.set_caption("Fencing")

BG_COLOR=(255,255,255)
WIDTH,HEIGTH=1000,800
FPS=60
PLAYER_VEL = 5

window = pygame.display.set_mode(WIDTH,HEIGTH)

def main():
    
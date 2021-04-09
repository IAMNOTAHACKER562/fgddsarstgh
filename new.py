#import mods
import pygame
from pygame import *
pygame.init()

#Screen
win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("DABABY LET'S GOOO")

#character
x = int(win_w / 2)
y = 400
width = 40
height = 60
vel = 5

#main loop
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()

pygame.quit()
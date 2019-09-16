# python code to create a Sierpinski triangle
import pygame, sys
from pygame.locals import *
from random import randrange

iterations = int(input("Iterations: "))

pygame.init()
display = pygame.display.set_mode((800, 600), 0, 32)
display.fill((255, 255, 255))
pygame.display.set_caption('Sierpinski triangle')

colors = [(0, 255, 0), (255, 0 ,0), (0, 0, 255)]
w, h = pygame.display.get_surface().get_size()
points = [[w / 2, 1], [1, h], [w, h]]
currentPoint = [0, 0]

for i in range(iterations):
    pIndex = randrange(3)
    currentPoint = [
        (points[pIndex][0] + currentPoint[0]) / 2,
        (points[pIndex][1] + currentPoint[1]) / 2
    ]

    display.set_at((int(currentPoint[0]), int(currentPoint[1])), colors[pIndex])

    if not i % 100:
        pygame.display.update()

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

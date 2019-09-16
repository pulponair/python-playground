from graphics import *
from random import randrange

iterations = input('Iterations: ')

win = GraphWin('Sierpinski Triangle', 800, 600)
colors = ['green', 'red', 'blue']
points = [[399, 1], [1, 599], [799, 599]]

currentPoint = [100, 200]
for i in range(int(iterations)):
    pIndex = randrange(3)
    currentPoint = [
        (points[pIndex][0] + currentPoint[0]) / 2,
        (points[pIndex][1] + currentPoint[1]) / 2
    ]

    win.plot(currentPoint[0], currentPoint[1], colors[pIndex])


win.getMouse()

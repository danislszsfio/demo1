import random
from graphics import *
def main():
    lstx = []
    lsty = []
    valuesx = 0
    n = int(input("Enter number of elements"))
    for i in range (0, n):
        valuesy = random.randint(0,100)
        lsty.append (valuesy)
        valuesx = valuesx + 1
        lstx.append (valuesx)
    print ("Your x values are ", lstx, "And your y values are",lsty)
    x = lstx
    y = lsty
    win = GraphWin(("Shapes"),100, 100)
    line = line(Point(x,y))
    line.draw(win)
main()
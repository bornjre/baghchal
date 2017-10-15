from turtle import Turtle
from turtle import Screen
screen = Screen()
turtle = Turtle()

def gotoandprint(x, y):
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    return gotoresult

screen.onscreenclick(gotoandprint)
turtle.getscreen()._root.mainloop()
#turtle.mainloop()
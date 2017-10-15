from turtle import Turtle, Screen
#screen = Screen()
turtle = Turtle()
screen = turtle.getscreen()
convas = screen.getcanvas()
#X = screen.window_width()
#Y = screen.window_height()
screen.bgpic("board.png")

def onclick_handler(x, y):
    print(x,y)

screen.onscreenclick(onclick_handler)
X = -200
Y = 200
next_x = X
next_y = Y
turtle.color("red")
for i in range(5):
    for j in range(5):
        turtle.setpos(next_x, next_y)
        turtle.circle(5)
        next_x = next_x + 100
    next_x = X
    next_y = next_y - 100

screen.mainloop()

from turtle import Turtle, Screen
#screen = Screen()
turtle = Turtle()
screen = turtle.getscreen()
screen.bgpic("board.png")

def onclick_handler(x, y):
    print(x,y)

def initial_bagh_setup():
    keys = pos_list.keys()
    print(screen.getshapes())
    tiger = "tiger.gif"
    tiger_ids = []
    screen.register_shape(tiger)
    turtle.shape(tiger)
    for key in keys:
        if (key == 0 or key == 4 or key == 20 or key == 24):
            [x, y] = pos_list[key] 
            turtle.setpos(x,y)
            t = turtle.stamp()
            tiger_ids.append(t)
    turtle.shape("turtle")
    for i in tiger_ids:
        turtle.clearstamp(i)
            #turtle = Turtle('tiger.gif')
screen.onscreenclick(onclick_handler)
X = -200
Y = 200
pos_list = {}
next_x = X
next_y = Y
turtle.color("red")
turtle.penup()
for i in range(5):
    for j in range(5):
        #turtle.tracer(0, 0)
        turtle.setpos(next_x, next_y)
        turtle.pendown()
        #turtle.circle(5)
        turtle.penup()
        key = 5 * i + j
        pos_list[key] = [next_x, next_y] 
        next_x = next_x + 100
    next_x = X
    next_y = next_y - 100
print(pos_list)
initial_bagh_setup()
turtle.speed(10)

screen.mainloop()

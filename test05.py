from turtle import Turtle, Screen
#screen = Screen()
turtle = Turtle()
screen = turtle.getscreen()
screen.bgpic("board.png")
screen.tracer(1,1)
filled_pos = [False] * 25
tiger = "tiger.gif"
goat = "goat.gif"
screen.register_shape(tiger)
screen.register_shape(goat)

def initial_bagh_setup():
    keys = pos_list.keys()
    print(screen.getshapes())
    tiger_ids = []
    turtle.shape(tiger)
    for key in keys:
        if (key == 0 or key == 4 or key == 20 or key == 24):
            [x, y] = pos_list[key] 
            turtle.setpos(x,y)
            t = turtle.stamp()
            tiger_ids.append(t)
            filled_pos[key] = True
    turtle.shape("turtle")
    # for i in tiger_ids:
    #     turtle.clearstamp(i)

X = -200
Y = 200
pos_list = {}
next_x = X
next_y = Y
turtle.color("red")
turtle.penup()
for i in range(5):
    for j in range(5):
        turtle.setpos(next_x, next_y)
        turtle.pendown()
        turtle.penup()
        key = 5 * i + j
        pos_list[key] = [next_x, next_y] 
        next_x = next_x + 100
    next_x = X
    next_y = next_y - 100
initial_bagh_setup()
pos = 12
floating_pos = None
[x, y] = pos_list[pos]
turtle.setpos(x,y)

#events functions
def forward():
    global pos
    if(pos > 4):
        pos = pos - 5
        [x, y] = pos_list[pos]
        turtle.setpos(x,y)
def backward():
    global pos
    if(pos < 20):
        pos = pos + 5
        [x, y] = pos_list[pos]
        turtle.setpos(x,y)
def left():
    global pos
    if((pos > 0) or (pos < 24)):
        pos = pos - 1
        [x, y] = pos_list[pos]
        turtle.setpos(x,y)
def right():
    global pos
    if((pos > 0) or (pos < 24)):
        pos = pos + 1
        [x, y] = pos_list[pos]
        turtle.setpos(x,y)
def enter():
    turtle.color("green")
    global pos, floating_pos
    floating_pos = pos
    turtle.shape(goat)
    turtle.stamp()
    print("hh")
#listen events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(enter, "Return")
screen.listen()


screen.mainloop()

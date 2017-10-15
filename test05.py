from turtle import Turtle, Screen
#screen = Screen()
turtle = Turtle()
screen = turtle.getscreen()
convas = screen.getcanvas()
X = screen.window_width()
Y = screen.window_height()
screen.bgpic("board.png")

def onclick_handler(x, y):
    print(x,y)

# pos_list = [ 
#     [-198.0, 199.0],
#     [-100.0, 199.0],
#     [2.0, 196.0],
#     [102.0, 197.0],
#     [198.0, 198.0],
#     [-199.0, 98.0],
#     [-98.0, 98.0],
#     [2.0, 99.0],
#     [100.0, 98.0],
#     [198.0, 97.0],
#     [-198.0, -2.0],
#     [-100.0, -2.0],
#     [2.0, -2.0],
#     [102.0, -3.0],
#     [196.0, -2.0],
#     [-199.0, -103.0],
#     [-99.0, -100.0],
#     [1.0, -103.0],
#     [101.0, -103.0],
#     [197.0, -103.0],
#     [-199.0, -199.0],
#     [-101.0, -198.0],
#     [3.0, -198.0],
#     [100.0, -198.0],
#     [199.0, -197.0]
#     ]

screen.onscreenclick(onclick_handler)

# for i in pos_list:
#     turtle.setpos(i[0],i[1])
#     turtle.color("red")
#     turtle.circle(5)
#     turtle.color("black")
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

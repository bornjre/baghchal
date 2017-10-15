from turtle import Turtle, Screen
#screen = Screen()
turtle = Turtle()
screen = turtle.getscreen()
convas = screen.getcanvas()
#convas
Y = screen.window_height()/2
turtle.sety(Y)
screen.bgcolor("orange")
# def draw_board():
#     turtle.color("white")
#     turtle.setpos((100,0))
#     turtle.color("red")

# draw_board()
#screen.textinput("HEY", "Whats your name pyasi:")
#turtle.getscreen()._root.mainloop()
shapes = screen.getshapes()
screen.bgpic("board.png")
print(shapes)

#start














screen.mainloop()
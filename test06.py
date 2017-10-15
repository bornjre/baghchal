from turtle import Turtle, Screen

FONTSIZE = 40
FONT = ("Ariel", FONTSIZE, "normal")

turtle = Turtle(visible=False)
turtle.penup()

turtle.setpos(0, FONTSIZE*2 - FONTSIZE/2)
turtle.write("1.Option1", align="center", font=FONT)

turtle.setpos(0, -FONTSIZE/2)
turtle.write("2.Option2", align="center", font=FONT)

turtle.setpos(0, -FONTSIZE*2 - FONTSIZE/2)
turtle.write("3.Option3", align="center", font=FONT)

turtle.setpos(-200, -200)
turtle.write("Select an Option", font=FONT)

def onclick_handler(x, y):
    print(x,y)
    if -100 < x < 100:
        if FONTSIZE < y < FONTSIZE*3:
            turtle.undo()
            turtle.write("Option 1", font=FONT)
        elif -FONTSIZE < y < FONTSIZE:
            turtle.undo()
            turtle.write("Option 2", font=FONT)
        elif -FONTSIZE*3 < y < -FONTSIZE:
            turtle.undo()
            turtle.write("Option 3", font=FONT)

screen = Screen()
screen.onscreenclick(onclick_handler)
screen.mainloop()
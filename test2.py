import turtle

t = turtle.Turtle()
t.color("white")
t.backward(450)
t.color("red")

def f2(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        f2(length/2, depth -1)
        t.left(135)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.left(135)
        f2(length/2, depth -1)


f2(400, 4)
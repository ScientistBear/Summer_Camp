import random
import turtle
from tkinter import simpledialog

# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    t = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    t.pensize(10)
    #      3) Set the pen width to 10
    t.pencolor('white')
    t.speed(0)
    while True:
        g = "tretert"
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if g == 'red':
            t.penup()
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pendown()
            t.pencolor('red')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'blue':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('blue')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'black':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('black')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'orange':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('orange')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'yellow':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('yellow')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'green':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('green')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'purple':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('purple')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'brown':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('brown')
            t.circle(radius=50)
            t.pencolor('white')
        elif g == 'pink':
            t.pensize(0)
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pensize(10)
            t.pencolor('pink')
            t.circle(radius=50)
            t.pencolor('white')
        else:
            t.penup()
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pendown()
            t.pencolor(get_random_color())
            t.circle(radius=50)
            t.pencolor('white')


    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

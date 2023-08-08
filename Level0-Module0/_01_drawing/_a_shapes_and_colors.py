import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    h = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    h.shape('turtle')
    # Set your turtle's speed using .speed(2)
    h.speed(600)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    h.color('green')
    h.pencolor('black')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        h.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        h.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    h.goto(300,-350)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    h.begin_fill()
    h.circle(60, steps=6)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    h.end_fill()
    # Draw 3 more shapes with different fill colors!
    h.goto(100,100)
    h.begin_fill()
    h.circle(1, steps=100)
    h.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

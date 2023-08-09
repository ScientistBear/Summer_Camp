import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    c = simpledialog.askinteger(title='', prompt='Radius PLZ')
    # Make a new turtle
    t = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    t.circle(c)
    # Call the turtle .penup() method
    t.penup()
    # Move your turtle to a new x,y position using .goto()
    t.goto(255, 255)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    m = math.pi
    # Write the area of your circle using the turtle .write() method
    t.write(arg="area = " + str(m), move=True, align='left', font=('Arial', 8, 'normal'))

    # Hide your turtle
    t.hideturtle()
    # Call turtle.done()
    turtle.done()

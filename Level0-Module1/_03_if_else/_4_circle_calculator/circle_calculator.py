# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import turtle
from tkinter import messagebox, simpledialog, Tk, Canvas
import random

window = Tk()
window.withdraw()
k = simpledialog.askinteger(title='', prompt='radius plz')
t = turtle.Turtle()
t.speed(10000)
t.circle(k)

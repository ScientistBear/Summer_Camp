
from tkinter import simpledialog, Tk, messagebox

root = Tk()

y = simpledialog.askstring(title='Riddle', prompt='There are two monkeys on a tree and one jumps off. Why does the other monkey jump too?')
if y == 'Monkey see monkey do':
    messagebox.showinfo(title='', message='Correct')
else:
    messagebox.showinfo(title='', message='Incorrect. Answer: Monkey see monkey do')
b = simpledialog.askstring(title='Riddle', prompt='Samuel was out for a walk when it started to rain. He did not have an umbrella and he was not wearing a hat. His clothes were soaked, yet not a single hair on his head got wet. How could this happen?')
if b == 'He is bald':
    messagebox.showinfo(title='', message='Correct')
else:
    messagebox.showinfo(title='', message='Incorrect. Answer: He is bald')
h = simpledialog.askstring(title='Riddle', prompt='Only one color, but not one size, Stuck at the bottom, yet easily flies. Present in sun, but not in rain, Doing no harm, and feeling no pain. What is it?')
if h == 'A shadow' or 'Shadow':
    messagebox.showinfo(title='', message='Correct')
else:
    messagebox.showinfo(title='', message='Incorrect. Answer: A shadow')

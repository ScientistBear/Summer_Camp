
from tkinter import simpledialog, Tk, messagebox

root = Tk()

y = simpledialog.askstring(title='riddle', prompt='There are two monkeys on a tree and one jumps off. Why does the other monkey jump too?')
if y == 'Monkey see monkey do.':
    messagebox.showinfo(title='', message='')

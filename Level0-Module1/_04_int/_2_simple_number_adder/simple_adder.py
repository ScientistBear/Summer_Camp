from tkinter import simpledialog, messagebox, Tk

root = Tk()


Num_1 = simpledialog.askinteger(title='', prompt='First Number')
Num_2 = simpledialog.askinteger(title='', prompt='Second Number')

messagebox.showinfo(title='', message=Num_1+Num_2)

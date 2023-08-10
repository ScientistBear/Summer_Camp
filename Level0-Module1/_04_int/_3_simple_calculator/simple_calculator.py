from tkinter import simpledialog, messagebox, Tk

root = Tk()

Dh = simpledialog.askstring(title='', prompt='Add, Multiply, Subtract or Divide')

if Dh == 'Add':
    t = simpledialog.askinteger(title='', prompt='Num 1')
    h = simpledialog.askinteger(title='', prompt='Num 2')
    messagebox.showinfo(title='', message=t+h)
elif Dh == 'Multiply':
    r = simpledialog.askinteger(title='', prompt='Num 1')
    g = simpledialog.askinteger(title='', prompt='Num 2')
    messagebox.showinfo(title='', message=r*g)
elif Dh == 'Subtract':
    k = simpledialog.askinteger(title='', prompt='Num 1')
    l = simpledialog.askinteger(title='', prompt='Num 2')
    messagebox.showinfo(title='', message=k-l)
elif Dh == 'Divide':
    n = simpledialog.askinteger(title='', prompt='Num 1')
    m = simpledialog.askinteger(title='', prompt='Num 2')
    messagebox.showinfo(title='', message=n/m)
else:
    messagebox.showerror(title='', message='Error')

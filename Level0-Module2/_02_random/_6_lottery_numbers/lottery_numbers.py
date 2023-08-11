import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    s = ""
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    q = random.randint(0, 9)
    s = s + str(q)
    w = random.randint(0, 9)
    s = s + str(w)
    e = random.randint(0, 9)
    s = s + str(e)
    r = random.randint(0, 9)
    s = s + str(r)
    t = random.randint(0, 9)
    s = s + str(t)
    y = random.randint(0, 9)
    s = s + str(y)

    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='', message=s)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket

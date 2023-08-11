import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='', prompt='Question Goes Here')
    # Make a variable and initialize it to a random number between 0 and 3
    b = random.randint(0, 3)
    # If the random number is 0
    if b == 0:
        messagebox.showinfo(title='', message='Yes')

        # tell the user "Yes"

    # If the random number is 1
    elif b == 1:
        messagebox.showinfo(title='', message='No')

        # tell the user "No"

    # If the random number is 2
    elif b == 2:
        messagebox.showinfo(title='', message='Go ask Google')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif b == 3:
        messagebox.showinfo(title='', message='Maybe')
        # write your own answer

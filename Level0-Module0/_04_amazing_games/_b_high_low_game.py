from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(6):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        b = simpledialog.askinteger(title='', prompt='Guess A Number From 1-100')
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if b == random_num:
            messagebox.showinfo(title='', message='Correct')
        # 7. if the guess is high
            # 8. Tell them it's too high
        if b >= random_num:
            messagebox.showinfo(title='', message='Too High')

        if b <= random_num:
            messagebox.showinfo(title='', message='Too low')

    messagebox.showinfo(title='', message='You Lost 239470582730495720983475982374905732908475827209347598273409572098347589273947598273489572384759723409875928734897529374098572093847509374095729437059273498572984379852739487598743985720948375029873498570983475029873409587239847590827034957928347')
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

    window.mainloop()

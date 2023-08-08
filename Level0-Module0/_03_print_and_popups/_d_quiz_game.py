from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    Score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    A = simpledialog.askstring(title='', prompt='What is 4/0')
    #      // 3.  Use an if statement to check if their answer is correct
    if A == 'nothing':
        Score +=1
        messagebox.showinfo(title='', message='Yes')
    #      // 4.  if the user's answer was correct, add one to their score 
    else:
        Score -=1
        messagebox.showerror(title='', message='No')
    B = simpledialog.askstring(title='', prompt='What is The Color of the Sky')
    if B == 'blue':
        Score +=1
        messagebox.showinfo(title='', message='Yes')
    else:
        Score -=1
        messagebox.showerror(title='', message='No')
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    messagebox.showinfo(title='', message=Score)
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()

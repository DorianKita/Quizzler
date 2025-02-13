from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        self.true_button_image = PhotoImage(file='images/true.png')
        self.true = Button(image=self.true_button_image)
        self.true.grid(row= 2, column = 0)

        self.false_button_image = PhotoImage(file='images/false.png')
        self.false = Button(image=self.false_button_image)
        self.false.grid(row=2, column=1)


        self.window.mainloop()
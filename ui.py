from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20)

        self.label = Label(text=f"Score: {self.score}")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.text = self.canvas.create_text(150,125, text="Example text to be replaced by questions coming from our "
                                                          "API based question data", fill="black", width=280,
                                            font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button_image = PhotoImage(file='images/true.png')
        self.true = Button(image=self.true_button_image)
        self.true.grid(row= 2, column = 0)

        self.false_button_image = PhotoImage(file='images/false.png')
        self.false = Button(image=self.false_button_image)
        self.false.grid(row=2, column=1)


        self.window.mainloop()
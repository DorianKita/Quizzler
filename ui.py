from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.label = Label(text=f"Score: {self.score}", background=THEME_COLOR, foreground='white')
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.text = self.canvas.create_text(150,125, text="", fill="black", width=280,
                                            font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file='images/true.png')
        self.true = Button(image=true_button_image, highlightthickness=0, command=self.get_next_question)
        self.true.grid(row= 2, column = 0)

        false_button_image = PhotoImage(file='images/false.png')
        self.false = Button(image=false_button_image, highlightthickness=0, command=self.get_next_question)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.text, text= q_text)
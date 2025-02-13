from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.label = Label(text=f"Score: 0", background=THEME_COLOR, foreground='white')
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.text = self.canvas.create_text(150,125, text="", fill="black", width=280,
                                            font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file='images/true.png')
        self.true = Button(image=true_button_image, highlightthickness=0, command=self.check_if_right)
        self.true.grid(row= 2, column = 0)

        false_button_image = PhotoImage(file='images/false.png')
        self.false = Button(image=false_button_image, highlightthickness=0, command=self.check_if_wrong)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.text, text= q_text, fill='black')
            self.canvas.config(background='white')
        else:
            self.canvas.itemconfig(self.text, text=f"You've reached end of this quiz!\nYour score is: "
                                                   f"{self.quiz_brain.score}/{self.quiz_brain.question_number}")

    def check_if_right(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def check_if_wrong(self):
        self.give_feedback(self.quiz_brain.check_answer("Wrong"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='green')
            self.canvas.itemconfig(self.text, fill='white')

        else:
            self.canvas.config(background='red')
            self.canvas.itemconfig(self.text, fill='white')

        self.window.after(ms=1000, func=self.get_next_question)

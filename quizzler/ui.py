from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

text = str()


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)

        self.score = 0
        self.score_label = Label(
            master=self.window,
            text="Score: {}".format(self.score),
            justify="right",
            bg=THEME_COLOR,
            fg="#fff",
            font=("Helvetica", 16, "normal"),
        )
        self.score_label.grid(row=0, column=1, pady=15)

        self.canvas = Canvas(master=self.window, height=250, width=300)
        self.canvas.grid(row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125, text=text, font=("Arial", 20, "italic"), width=280
        )

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(
            master=self.window,
            image=true_img,
            highlightthickness=0,
            bd=0,
            command=self.true_button,
        )
        self.true_btn.grid(row=3, column=0, pady=50)
        self.false_btn = Button(
            master=self.window,
            image=false_img,
            highlightthickness=0,
            bd=0,
            command=self.false_button,
        )
        self.false_btn.grid(row=3, column=1, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button(self):
        self.quiz.check_answer("True")

    def false_button(self):
        self.quiz.check_answer("False")

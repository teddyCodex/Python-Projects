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

        self.canvas = Canvas(master=self.window, height=250, width=300, bg="#333")
        self.canvas.grid(row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125, text=text, font=("Arial", 20, "italic"), width=280, fill="white"
        )

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(
            master=self.window,
            image=true_img,
            highlightthickness=0,
            bd=0,
            command=self.true_clicked,
        )
        self.true_btn.grid(row=3, column=0, pady=50)
        self.false_btn = Button(
            master=self.window,
            image=false_img,
            highlightthickness=0,
            bd=0,
            command=self.false_clicked,
        )
        self.false_btn.grid(row=3, column=1, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#333")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"End of Quiz\nFinal Score: {self.quiz.score}/10",
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

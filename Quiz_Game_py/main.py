from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("\n")

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

final_score = f"{quiz.score}/{len(question_bank)}"

if quiz.score == len(question_bank):
    print("You're Amazing!!\nYou completed the quiz and got all the answers right!!\n")
    print(f"Your final score is {final_score}\n")
else:
    print("You've completed the quiz")
    print(f"Your final score is {final_score}\n")

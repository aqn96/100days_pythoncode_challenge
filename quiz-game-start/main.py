from question_model import Question
from data import question_data as qdata
from quiz_brain import QuizBrain


question_bank = []
for x in qdata:
    temp = Question(x["question"],x["correct_answer"])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
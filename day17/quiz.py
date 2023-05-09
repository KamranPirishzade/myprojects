from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for x in question_data:
    questions=x["question"]
    answers=x["correct_answer"]
    new_q=Question(questions,answers)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
else:
    print(f"""You have completed the quiz.
    Your final score : {quiz.score}/{quiz.question_number}""")

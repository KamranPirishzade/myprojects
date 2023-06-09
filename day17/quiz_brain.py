
class QuizBrain:

    def __init__(self, list1):
        self.question_number=0
        self.question_list=list1
        self.score=0
    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self) :
        self.question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q{self.question_number} {self.question.text} True or False : ")
        self.check_answer(user_answer,self.question.answer)
    def check_answer(self,users_answers,real_answer):
        if users_answers.lower()==real_answer.lower():
            print("You got it right!")
            self.score+=1
        else :
            print("That's wrong")
        print(f"The correct answer was: {real_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")


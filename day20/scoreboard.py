from turtle import Turtle,Screen

with open("data.txt",mode="r") as data:
    hs=int(data.read())



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score=0
        self.high_score=hs
        self.hideturtle()
        screen=Screen()
        screen.bgcolor("black")
        self.goto(-50,270)
        self.write(f"Score:{self.score} High Score:{self.high_score}",True,font=("Arial",20,"normal"))


    def add(self):
        self.score+=1
        self.goto(-50, 270)
        self.update()
    def update(self):
        self.write(f"Score:{self.score} High Score:{self.high_score}", True, font=("Arial", 20, "normal"))

    def reset(self):
        if self.score>self.high_score:
            with open("data.txt",mode="w") as data:
                data.write(str(self.score))
            with open("data.txt",mode="r") as data:
                new_hs=data.read()
            self.high_score=int(new_hs)
        self.clear()
        self.goto(-50,270)
        self.score = 0
        self.update()



    def score(self):
        score=self.score()
        return score




from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l=0
        self.r=0
        self.goto(-100,200)
        self.write(self.l,align="center",font=("Courier",50,"normal"))
        self.goto(100,200)
        self.write(self.r, align="center", font=("Courier", 50, "normal"))


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r, align="center", font=("Courier", 50, "normal"))
    def l_score(self):
        self.l+=1
        self.update_score()
    def r_score(self):
        self.r+=1
        self.update_score()
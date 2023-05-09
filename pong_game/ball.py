from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7,0.7)
        self.color("white")
        self.penup()
        self.x=10
        self.y=10

    def move(self):
        xcor=self.xcor()+self.x
        ycor=self.ycor()+self.y
        self.goto(xcor,ycor)
    def bounce_y(self):
        self.y*=-1
    def bounce_x(self):
        self.x*=-1








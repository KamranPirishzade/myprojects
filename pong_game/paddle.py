from turtle import Turtle,Screen



class Padle(Turtle):
    def __init__(self,cor_x,cor_y):
        screen = Screen()
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(cor_x, cor_y)
        screen.listen()

        def up():
            y_cor = self.ycor()
            self.goto(cor_x, y_cor + 20)

        def down():
            y_cor = self.ycor()
            self.goto(cor_x, y_cor - 20)
        if cor_x==350:
            screen.onkey(up, "Up")
            screen.onkey(down, "Down")
        elif cor_x==-350:
            screen.onkey(up, "w")
            screen.onkey(down, "s")





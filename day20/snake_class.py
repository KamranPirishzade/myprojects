from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake:
    def __init__(self):
        segments=[(0,0),(-20,0),(-40,0)]
        snake_segs=[]
        for cor in segments:
            snake=Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(cor)
            snake_segs.append(snake)
        self.snake=snake
        self.list=snake_segs
        self.head=snake_segs[0]
        self.segs=segments

    def new_seg(self):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.speed("fastest")
        snake.goto(self.list[-1].position())
        self.list.append(snake)

    def move(self):
        for x in range((len(self.list) - 1), 0, -1):
            list1 = self.list
            new_x = list1[x - 1].xcor()
            new_y = list1[x - 1].ycor()
            list1[x].goto(new_x, new_y)
        list1[0].forward(20)

    def reset(self):
        for seg in self.list:
            seg.goto(1000,1000)
        self.list.clear()
        for cor in self.segs:
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(cor)
            self.list.append(snake)
        self.head=self.list[0]

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)







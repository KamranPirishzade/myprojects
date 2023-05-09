from turtle import Turtle,Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segs=Snake()
seg_list=segs.list
food=Food()

screen.listen()

screen.onkey(segs.up,"Up")
screen.onkey(segs.down,"Down")
screen.onkey(segs.right,"Right")
screen.onkey(segs.left,"Left")


score = Score()
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    segs.move()
    if segs.head.distance(food)<15:
        food.refresh()
        segs.new_seg()
        score.clear()
        score.add()
    if segs.head.xcor()>280 or segs.head.xcor()<-280 or segs.head.ycor()>280 or segs.head.ycor()<-280:
        score.reset()
        segs.reset()


    for seg in segs.list[1:]:
        if segs.head.distance(seg) < 10:
            score.reset()
            segs.reset()

























screen.exitonclick()
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scorebord import ScoreBord
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)



screen.title("my snake game")

snake = Snake()

is_game_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

foo = Food()
score1 = ScoreBord()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.new[0].distance(foo) <15:
        foo.refresh()
        snake.extend()
        score1.incs()

    if snake.new[0].xcor() > 280 or snake.new[0].xcor() < -280 or snake.new[0].ycor() > 280 or snake.new[0].ycor() < -280:
        is_game_on =False
        score1.gameover()

    for segment in snake.new[1:]:

        if snake.new[0].distance(segment) <10:
            is_game_on = False
            score1.gameover()


screen.exitonclick()

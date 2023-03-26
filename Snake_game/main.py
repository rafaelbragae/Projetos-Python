from turtle import Screen, Turtle
from snake_game import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def end():
    for part in range(len(snake.all_snake)):
        snake.all_snake[part].color('red')
    time.sleep(1)
    score.reset()
    snake.reset()

game = True

while game:
    if snake.head.xcor() >= 280 or snake.head.xcor() <= - 300 or snake.head.ycor() >= 300 or snake.head.ycor() <= - 280:
        end()
    else:
        for segment in snake.all_snake[1:]:
            if snake.head.distance(segment) < 10:
                end()
    snake.move()
    screen.update()
    time.sleep(0.1)
    # detect collision with food
    if snake.head.distance(food) < 15 and game:
        snake.extend()
        food.refresh()
        score.add_score()

screen.exitonclick()

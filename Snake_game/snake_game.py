import time
from turtle import Turtle
from score_board import Score

score = Score()

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

position = [(20, 0),(0, 0),(-20, 0)]

class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        for starting in position:
            self.add_segment(starting)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)

    def extend(self):
        self.add_segment(self.all_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.all_snake)-1 ,0 ,-1 ):
            new_x = self.all_snake[seg_num - 1].xcor()
            new_y = self.all_snake[seg_num - 1].ycor()
            self.all_snake[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.all_snake:
            seg.goto(1000,1000)
        self.all_snake.clear()
        self.create_snake()
        self.head = self.all_snake[0]


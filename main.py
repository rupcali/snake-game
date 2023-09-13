# snake game project
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from super_food import SuperFood

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_over = False

snake = Snake()
food = Food()
super_food = SuperFood()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food_counter = 1
food.create_food()

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    # detect collision with food
    if snake.head.distance(food) < 15 and food_counter % 5 != 0:
        food.new_loc()
        snake.extend()
        food_counter += 1
        scoreboard.increase_score()
    elif snake.head.distance(food) < 15 and food_counter % 5 == 0:
        super_food.showturtle()
        super_food.create_superfood()
        food.hideturtle()
    if snake.head.distance(super_food) < 20 and food_counter % 5 == 0:
        snake.extend()
        snake.extend()
        snake.extend()
        food_counter += 1
        scoreboard.increase_score()
        super_food.hideturtle()
        food.showturtle()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.write_game_over()
        
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.write_game_over()
    

screen.exitonclick()

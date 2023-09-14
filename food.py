from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_loc()
        
    def new_loc(self):
        self.showturtle()
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(x=random_x, y=random_y)
        
    def hide_food(self):
        self.hideturtle()
        self.goto(1000, 1000)
        
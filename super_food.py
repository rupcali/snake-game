from turtle import Turtle
import random


class SuperFood (Turtle):
    def __init__(self):
        super().__init__()
        
    def create_superfood(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("red")
        self.speed("fastest")
        self.new_loc()
    
    def new_loc(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(x=random_x, y=random_y)
        
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)
    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    



from turtle import Turtle
class Paddle:
    def __init__(self,cor,col):
        self.padd=Turtle()
        self.padd.shape("square")
        self.padd.shapesize(5,1,1)
        self.padd.penup()
        self.padd.goto(cor)
        self.padd.color(col)
        self.score=0
    def moveup(self):
        if self.padd.ycor()<270:
              self.padd.goto(self.padd.xcor(),self.padd.ycor()+30)
              screen.update()
    def movedown(self):
        if self.padd.ycor()>-270:
              self.padd.goto(self.padd.xcor(),self.padd.ycor()-30)
              screen.update()
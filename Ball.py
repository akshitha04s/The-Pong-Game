from turtle import Turtle
class Ball:
    def __init__(self):
        self.ball=Turtle()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.penup()
        self.xmove=10
        self.ymove=10
    def move(self):
             newx=self.ball.xcor()+self.xmove;
             newy=self.ball.ycor()+self.ymove
             self.ball.goto(newx,newy)
    def checkwall(self):
        if self.ball.ycor()<=-270:
            self.ymove=10
        if self.ball.ycor()>=270:
            self.ymove=-10
    def bounce(self):
        self.xmove*=-1
    def checkpad(self,lpad,rpad,scoreob):
        if self.ball.xcor()>390:
            lpad.score+=1
            scoreob.lchange(lpad.score)
            self.bounce()
        if self.ball.xcor()<-390:
            rpad.score+=1
            scoreob.rchange(rpad.score)
            self.bounce()
        if self.ball.xcor()>350 and self.xmove>0:
            if self.ball.distance(rpad.padd)<50:
                self.bounce()
        if self.ball.xcor()<-350 and self.xmove<0:
            if self.ball.distance(lpad.padd)<50:
                self.bounce()
                
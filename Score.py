from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.selfl=self.create()
        self.selfr=self.create()
        self.lchange(0)
        self.rchange(0)
    def create(self):
        newt=Turtle()
        newt.hideturtle()
        newt.color("white")
        newt.penup()
        return newt
    def lchange(self,lscore):
        self.selfl.goto(-100,280)
        self.selfl.clear()
        self.selfl.write(arg=f"{lscore}",move=False)
    def rchange(self,rscore):
        self.selfr.goto(100,280)
        self.selfr.clear()
        self.selfr.write(arg=f"{rscore}",move=False)
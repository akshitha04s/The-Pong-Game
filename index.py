from turtle import Screen
import time
from Ball import Ball
from Score import Score
from Paddle import Paddle
screen=Screen()
screen.setup(width=800,height=600)
lesbegin=screen.textinput("Welcome to snake xdnia","shall we start")
screen.bgcolor("black")
screen.tracer(0)
ball=Ball()
lpad=Paddle((-370,0),"red")
rpad=Paddle((370,0),"blue")
score=Score()
screen.listen()
screen.onkey(rpad.moveup,"Up")
screen.onkey(rpad.movedown,"Down")
screen.onkey(lpad.moveup,"w")
screen.onkey(lpad.movedown,"s")
gameon=True
while(gameon):
    screen.update()
    ball.move()
    ball.checkwall()
    ball.checkpad(lpad,rpad,score)
    time.sleep(0.05)
    
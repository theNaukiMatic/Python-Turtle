import turtle
import time
import math
import random

x_vel = 0
y_vel = 0
vel_ball = 5
vel_pad = 50
frame_delay = 0.01

#Initializing screen window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800 , height = 600)
wn.tracer(0)

#Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.penup()
pad_a.color("white")
pad_a.shape("square")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.goto(-380,0)
pad_a.score = 0


#Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.penup()
pad_b.color("white")
pad_b.shape("square")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.goto(+380,0)
pad_b.score = 0

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.color("white")
ball.shape("circle")
ball.goto(0,0)
ball.x_vel = vel_ball
ball.y_vel = vel_ball

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score A: 0  Score B: 0",align = "center",font = ("courier", 24 , "normal"))




#Functions 
def move_ball():
    y = ball.ycor()
    x = ball.xcor()
    ball.setx(x+ball.x_vel)
    ball.sety(y+ball.y_vel)


def a_up():
    y=pad_a.ycor()
    pad_a.sety(y+vel_pad)
    
def a_down():
    y=pad_a.ycor()
    pad_a.sety(y-vel_pad)
    
def b_up():
    y=pad_b.ycor()
    pad_b.sety(y+vel_pad)
    
def b_down():
    y=pad_b.ycor()
    pad_b.sety(y-vel_pad)
    

def point_a():
    pad_a.score +=1

def point_b():
    pad_b.score +=1



# make ball bounce on walls
def ball_bounce():
    x = ball.xcor()
    y = ball.ycor()
    if y > 300:
        ball.y_vel = -vel_ball
    if y<-300:
        ball.y_vel = +vel_ball
    if x > 400:
        ball.x_vel = -vel_ball
        point_a()
        pen.clear()
        pen.write("Score A : {}  Score B: {}".format(pad_a.score,pad_b.score),align = "center",font = ("courier", 24 , "normal"))

    if x<-400:
        ball.x_vel = +vel_ball
        point_b()
        pen.clear()
        pen.write("Score A : {}  Score B: {}".format(pad_a.score,pad_b.score),align = "center",font = ("courier", 24 , "normal"))

#KeyBindings
wn.listen()
wn.onkeypress(a_up , "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")

Game = True
#Main Game Loop :
while Game :
    time.sleep(frame_delay)
    wn.update()

    move_ball()

    #Game Over Check
    if(pad_a.score >=15 or pad_b.score >= 15):
        
        pen.clear()
        pen.goto(0,-40)
        pen.write("GAME OVER !\nScore A : {}\nScore B : {}".format(pad_a.score,pad_b.score),align = "center",font = ("courier", 24 , "normal"))
        Game = False

    xball = ball.xcor()
    yball = ball.ycor()
    ypad_a = pad_a.ycor()
    ypad_b = pad_b.ycor()

    #Colision detection with paddle A:
    if xball<-370 and xball > -400  and (yball < ypad_a+50 and yball >ypad_a-50):
        ball.x_vel = -ball.x_vel
    #Colision detection with paddle B:
    if xball>+370 and xball < +400 and (yball < ypad_b+50 and yball >ypad_b-50):
        ball.x_vel = -ball.x_vel
    ball_bounce()


wn.mainloop()
import turtle
import time
import math
import random

delay = 0.2
score = 0
high_score = 0

#screen window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600,height=600)
window.tracer(0) #turns of screen update

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0",align = "center",font = ("courier", 24 , "normal"))


#Functions 
def kill() :

    head.goto(0,100)
    head.direction = "stop"
    for segment in segments :
        segment.goto(1000,1000)
    segments.clear()
    pen.clear()
    pen.goto(0,0)
    pen.write("You Died!\nYour Score: {}\nHigh Score: {}".format(score,high_score),align = "center",font = ("courier", 24 , "normal"))
    time.sleep(2)
    pen.clear()
    pen.goto(0 ,260)
    pen.write("Score: {}  High Score : {}".format(score,high_score),align = "center",font = ("courier", 24 , "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keybord bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

#main game loop


while True:
    window.update()
    #collision detection
    if head.distance(food) < 20:
        score += 10 
        delay = delay/1.1
    

        if score > high_score :
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score : {}".format(score,high_score),align = "center",font = ("courier", 24 , "normal"))
        #Move the food to new spot
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #add a segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment zero
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    time.sleep(delay)
    #Border checking
    if head.xcor() >290 or head.xcor() <-290 or head.ycor() >290 or head.ycor()<-290 :
        score = 0
        delay = 0.2
        kill()

    #Self collosion
    for segment in segments:
        if segment.distance(head)<20:
            score = 0
            delay = 0.2
            kill()


window.mainloop()
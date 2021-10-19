import turtle
import winsound
# initializing
wn= turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
# Paddle 2
paddle_2=turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx=.2
ball.dy=.2

# score
score_a=0
score_b=0

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Plater B: 0", align="center", font=("Courier", 24, "normal"))

# functions
def paddle_1_up():
  y=paddle_1.ycor()
  y += 20
  paddle_1.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")

def paddle_1_down():
  y=paddle_1.ycor()
  y -= 20
  paddle_1.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_1_down, "s")


def paddle_2_up():
  y=paddle_2.ycor()
  y += 20
  paddle_2.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_2_up, "Up")

def paddle_2_down():
  y=paddle_2.ycor()
  y -= 20
  paddle_2.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_2_down, "Down")

# main loop

while True:
  wn.update()
  #move ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor()+ ball.dy)

  #border check
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy*= -1
    winsound.PlaySound("noise.wav", winsound.SND_ASYNC)

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy*= -1
    winsound.PlaySound("noise.wav", winsound.SND_ASYNC)
    

  if ball.xcor()>390:
    ball.goto(0,0)
    ball.dx*=-1
    score_a +=1
    pen.clear()
    pen.write("Player A: {} Plater B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
  
  if ball.xcor()< -390:
    ball.goto(0, 0)
    ball.dx*=-1
    score_b +=1
    pen.clear()
    pen.write("Player A: {} Plater B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  # paddle ball collisions
  if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
    ball.setx(340)
    ball.dx *=-1
    winsound.PlaySound("noise.wav", winsound.SND_ASYNC)

  if ball.xcor()<-340 and ball.xcor()<-350 and (ball.ycor()<paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
    ball.setx(-340)
    ball.dx *=-1
    winsound.PlaySound("noise.wav", winsound.SND_ASYNC)
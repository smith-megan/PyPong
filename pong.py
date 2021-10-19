import turtle

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

# main loop

while True:
  wn.update()

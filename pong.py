# Simple Pong in Python 3
import turtle

wn = turtle.Screen()
wn.title("Pong by Jennifer")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=10, stretch_len=2.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=10, stretch_len=2.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .075
ball.dy = -.075

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Jeyboard binding
wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")

wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_down, "s")

wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_b_up, "Up")

wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    wn.update()
    # every time loop runs it updates the screen

# move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

     if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

# Paddle and ball collision
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor + 40 and ball.ycor() > paddle_b.ycor - 40)
        ball.dx *= -1

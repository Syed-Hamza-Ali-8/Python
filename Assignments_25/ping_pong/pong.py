import turtle

win = turtle.Screen()
win.title("Pong Game by Hamza (Ultra Fast)")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0, 0)

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Start with super speed
ball.dy = 2

score_left = 0
score_right = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 40
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 40
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 40
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 40
    right_paddle.sety(y)

win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

def game_loop():
    global score_left, score_right

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -2
        ball.dy = 2
        score_left += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_left}  Player B: {score_right}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2
        score_right += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_left}  Player B: {score_right}", align="center", font=("Courier", 24, "normal"))

    if (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        if abs(ball.dx) < 10:
            ball.dx *= -1.3
            ball.dy *= 1.1
        else:
            ball.dx *= -1
            ball.dy *= 1

    if (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        if abs(ball.dx) < 10:
            ball.dx *= -1.3
            ball.dy *= 1.1
        else:
            ball.dx *= -1
            ball.dy *= 1

    win.update()
    win.ontimer(game_loop, 1)

game_loop()

win.mainloop()

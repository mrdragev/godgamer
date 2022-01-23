# pogchamp
import turtle

window = turtle.Screen()
window.title("Pongchamp")
window.bgcolor("gray")
window.setup(width=800,height=600)
window.tracer(0)

# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("blue")
player_1.shapesize(stretch_wid=5,stretch_len=1)
player_1.penup()
player_1.goto(-350,0)

# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("red")
player_2.shapesize(stretch_wid=5,stretch_len=1)
player_2.penup()
player_2.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


# Functions
#Player 1
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)
#Player 2
def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# Keybind for player_1
window.listen()
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")

#main game xD
while True:
    window.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border control XD
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Vertical control
    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1


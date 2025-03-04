import turtle
import winsound
import random

# Setup window
wn = turtle.Screen()
wn.title("Pong by Hani")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5, stretch_len=1)
pa.penup()
pa.goto(-350, 0)

# Paddle B
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5, stretch_len=1)
pb.penup()
pb.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-0.2, 0.2])
ball.dy = random.choice([-0.2, 0.2])

# Score
scoreA = scoreB = 0
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions
def update_score():
    pen.clear()
    pen.write(f'Player A: {scoreA}  Player B: {scoreB}', font=('Arial', 20), align='center')

def pa_up():
    y = pa.ycor()
    if y < 250:  # Adjusted to prevent paddle from going off screen
        pa.sety(y + 20)

def pa_dn():
    y = pa.ycor()
    if y > -250:  # Adjusted to prevent paddle from going off screen
        pa.sety(y - 20)

def pb_up():
    y = pb.ycor()
    if y < 250:  # Adjusted to prevent paddle from going off screen
        pb.sety(y + 20)

def pb_dn():
    y = pb.ycor()
    if y > -250:  # Adjusted to prevent paddle from going off screen
        pb.sety(y - 20)

# Keyboard binding
wn.listen()
wn.onkeypress(pa_up, "z")
wn.onkeypress(pa_dn, "s")
wn.onkeypress(pb_up, "Up")
wn.onkeypress(pb_dn, "Down")

# Initial score display
update_score()

# Main game loop
while True:
    wn.update()
    
    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        try:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        except:
            pass
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        try:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        except:
            pass
    
    # Scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        scoreA += 1
        update_score()
        ball.dx = random.choice([-0.2, 0.2])  # Reset ball direction
        ball.dy = random.choice([-0.2, 0.2])
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        scoreB += 1
        update_score()
        ball.dx = random.choice([-0.2, 0.2])  # Reset ball direction
        ball.dy = random.choice([-0.2, 0.2])
    
    # Paddle collision
    # Right paddle (Player B)
    if (ball.xcor() > 340 and ball.xcor() < 350 and 
        ball.ycor() < pb.ycor() + 50 and 
        ball.ycor() > pb.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        try:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        except:
            pass
    
    # Left paddle (Player A)
    if (ball.xcor() < -340 and ball.xcor() > -350 and 
        ball.ycor() < pa.ycor() + 50 and 
        ball.ycor() > pa.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        try:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        except:
            pass
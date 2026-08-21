import turtle
import random
import time

# -----------------------------
# Screen
# -----------------------------
screen = turtle.Screen()
screen.title("Mini GTA")
screen.bgcolor("darkgreen")
screen.setup(width=800, height=600)
screen.tracer(0)

# -----------------------------
# Road
# -----------------------------
road = turtle.Turtle()
road.hideturtle()
road.penup()
road.goto(-120, -300)
road.color("gray")
road.begin_fill()
for _ in range(2):
    road.forward(240)
    road.left(90)
    road.forward(600)
    road.left(90)
road.end_fill()

# Road Lines
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.color("white")

for y in range(-280, 300, 60):
    line.goto(0, y)
    line.setheading(90)
    line.pendown()
    line.forward(30)
    line.penup()

# -----------------------------
# Player
# -----------------------------
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, -250)

speed = 20

# -----------------------------
# Score
# -----------------------------
score = 0
health = 3

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")

def update_score():
    pen.clear()
    pen.goto(0, 260)
    pen.write(
        f"Money: ${score}   Health: {health}",
        align="center",
        font=("Arial", 18, "bold")
    )

update_score()

# -----------------------------
# Money
# -----------------------------
money = turtle.Turtle()
money.shape("circle")
money.color("gold")
money.penup()
money.goto(random.randint(-80, 80), random.randint(-200, 250))

# -----------------------------
# Cars
# -----------------------------
cars = []

colors = ["red", "yellow", "black", "orange"]

for i in range(5):
    car = turtle.Turtle()
    car.shape("square")
    car.shapesize(stretch_wid=2, stretch_len=1)
    car.color(random.choice(colors))
    car.penup()
    lane = random.choice([-60, 60])
    car.goto(lane, random.randint(-250, 250))
    car.speed_value = random.randint(4, 10)
    cars.append(car)

# -----------------------------
# Controls
# -----------------------------
def up():
    player.sety(player.ycor() + speed)

def down():
    player.sety(player.ycor() - speed)

def left():
    player.setx(player.xcor() - speed)

def right():
    player.setx(player.xcor() + speed)

screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

# -----------------------------
# Game Loop
# -----------------------------
while True:

    screen.update()

    # Keep player inside map
    if player.xcor() > 110:
        player.setx(110)
    if player.xcor() < -110:
        player.setx(-110)
    if player.ycor() > 280:
        player.sety(280)
    if player.ycor() < -280:
        player.sety(-280)

    # Move Cars
    for car in cars:
        car.sety(car.ycor() - car.speed_value)

        if car.ycor() < -320:
            car.goto(random.choice([-60, 60]), 320)
            car.speed_value = random.randint(4, 10)
            car.color(random.choice(colors))

        # Collision
        if player.distance(car) < 25:
            health -= 1
            player.goto(0, -250)
            update_score()
            time.sleep(0.5)

            if health == 0:
                pen.goto(0, 0)
                pen.write(
                    "GAME OVER",
                    align="center",
                    font=("Arial", 28, "bold")
                )
                screen.update()
                time.sleep(3)
                turtle.bye()

    # Collect Money
    if player.distance(money) < 20:
        score += 100
        update_score()
        money.goto(
            random.randint(-80, 80),
            random.randint(-250, 250)
        )
 
    time.sleep(0.02)
# ULTIMATE TURTLE CAR RACING GAME
# Part 1/3

import turtle
import random
import time
import os


# ================= SCREEN =================

screen = turtle.Screen()
screen.title("Ultimate Car Racing")
screen.setup(700,800)
screen.bgcolor("darkgreen")
screen.tracer(0)



# ================= GAME VARIABLES =================

score = 0
high_score = 0
level = 1
speed = 8
fuel = 100
health = 100
nitro = 100
running = True



# ================= HIGH SCORE =================

try:
    with open("highscore.txt","r") as file:
        high_score=int(file.read())

except:
    high_score=0




# ================= ROAD =================

road=turtle.Turtle()

road.shape("square")
road.color("gray")
road.shapesize(30,12)

road.penup()
road.goto(0,0)



# ================= ROAD LINES =================


lines=[]

for y in range(-400,500,100):

    line=turtle.Turtle()

    line.shape("square")
    line.color("white")

    line.shapesize(3,0.1)

    line.penup()
    line.goto(0,y)

    lines.append(line)




# ================= CAR CLASS =================


class Car(turtle.Turtle):

    def __init__(self,color,x,y):

        super().__init__()

        self.shape("square")

        self.color(color)

        self.shapesize(2,1)

        self.penup()

        self.goto(x,y)



    def left(self):

        if self.xcor()>-150:

            self.goto(
                self.xcor()-100,
                self.ycor()
            )



    def right(self):

        if self.xcor()<150:

            self.goto(
                self.xcor()+100,
                self.ycor()
            )




# ================= PLAYER =================


player=Car(
    "blue",
    0,
    -300
)




# ================= ENEMY TRAFFIC =================


enemy_list=[]


colors=[
    "red",
    "yellow",
    "orange",
    "purple"
]


for i in range(6):

    enemy=Car(
        random.choice(colors),
        random.choice([-100,0,100]),
        random.randint(200,700)
    )

    enemy_list.append(enemy)




# ================= COINS =================


coins=[]


for i in range(3):

    coin=turtle.Turtle()

    coin.shape("circle")

    coin.color("gold")

    coin.penup()

    coin.goto(
        random.choice([-100,0,100]),
        random.randint(300,700)
    )

    coins.append(coin)




# ================= UI =================


ui=turtle.Turtle()

ui.hideturtle()

ui.color("white")

ui.penup()

ui.goto(-320,340)



def update_ui():

    ui.clear()

    ui.write(
        f"Score:{score}  Fuel:{int(fuel)}  HP:{health}  Nitro:{int(nitro)}  Level:{level}",
        font=("Arial",15,"bold")
    )





# ================= CONTROLS =================


screen.listen()


screen.onkeypress(
    player.left,
    "Left"
)


screen.onkeypress(
    player.right,
    "Right"
)



# Nitro

nitro_active=False


def start_nitro():

    global nitro_active

    nitro_active=True



def stop_nitro():

    global nitro_active

    nitro_active=False



screen.onkeypress(
    start_nitro,
    "space"
)


screen.onkeyrelease(
    stop_nitro,
    "space"
)



# ================= START COUNTDOWN =================


count=turtle.Turtle()

count.hideturtle()

count.color("yellow")


for x in ["3","2","1","GO"]:

    count.clear()

    count.write(
        x,
        align="center",
        font=("Arial",50,"bold")
    )

    screen.update()

    time.sleep(1)


count.clear()



# Part 2 will continue from here...

# ================= PART 2/3 =================


# ================= POLICE CAR =================


police = Car(
    "black",
    random.choice([-100,0,100]),
    800
)



# ================= FUEL SYSTEM =================


def update_fuel():

    global fuel

    fuel -= 0.05

    if fuel <= 0:
        game_over("OUT OF FUEL")




# ================= NITRO SYSTEM =================


def apply_nitro():

    global nitro

    if nitro_active and nitro > 0:

        nitro -= 0.8

        return 18

    else:

        return speed




# ================= COIN SYSTEM =================


def move_coins(current_speed):

    global score


    for coin in coins:

        coin.sety(
            coin.ycor()-current_speed
        )


        if coin.ycor() < -400:

            coin.goto(
                random.choice([-100,0,100]),
                random.randint(400,800)
            )


        if player.distance(coin)<40:

            score += 50

            coin.goto(
                random.choice([-100,0,100]),
                random.randint(400,800)
            )




# ================= DAMAGE SYSTEM =================


def check_collision():

    global health


    for enemy in enemy_list:


        if player.distance(enemy)<40:


            health -= 20


            enemy.goto(
                random.choice([-100,0,100]),
                800
            )


            if health <= 0:

                game_over("CAR DESTROYED")





# ================= POLICE CHASE =================


def police_move(current_speed):


    police.sety(
        police.ycor()-current_speed
    )


    if police.ycor() < -400:

        police.goto(
            random.choice([-100,0,100]),
            900
        )


    if player.distance(police)<45:

        game_over("POLICE CAUGHT YOU")





# ================= LEVEL SYSTEM =================


def level_system():

    global level,speed


    if score > level*500:

        level += 1

        speed += 2





# ================= GAME OVER =================


def game_over(reason):

    global running


    running=False


    if score > high_score:

        with open("highscore.txt","w") as file:

            file.write(str(score))


    screen.clear()

    screen.bgcolor("black")


    msg=turtle.Turtle()

    msg.hideturtle()

    msg.color("yellow")


    msg.write(
        f"GAME OVER\n\n{reason}\n\nScore: {score}\nHigh Score: {high_score}",
        align="center",
        font=("Arial",30,"bold")
    )


    screen.update()



# ================= MAIN UPDATE FUNCTION =================


def update_game():

    global score


    if running==False:

        return



    current_speed = apply_nitro()



    # Road animation

    for line in lines:


        line.sety(
            line.ycor()-current_speed
        )


        if line.ycor() < -500:

            line.goto(
                0,
                500
            )



    # Enemy cars

    for enemy in enemy_list:


        enemy.sety(
            enemy.ycor()-current_speed
        )


        if enemy.ycor() < -400:


            enemy.goto(
                random.choice([-100,0,100]),
                random.randint(500,900)
            )


            score += 10




    move_coins(current_speed)


    police_move(current_speed)


    check_collision()


    update_fuel()


    level_system()


    update_ui()


    screen.update()


    screen.ontimer(
        update_game,
        50
    )



# Start game loop

update_game()


# ================= PART 3/3 FINAL =================


# ================= WEATHER SYSTEM =================


rain=[]


for i in range(40):

    drop=turtle.Turtle()

    drop.hideturtle()

    drop.color("cyan")

    drop.penup()

    drop.goto(
        random.randint(-300,300),
        random.randint(-300,400)
    )

    rain.append(drop)




rain_mode=False



def create_rain():

    if rain_mode:

        for drop in rain:

            drop.showturtle()

            drop.shape("line")

            drop.sety(
                drop.ycor()-15
            )


            if drop.ycor() < -400:

                drop.goto(
                    random.randint(-300,300),
                    400
                )



# ================= DAY NIGHT MODE =================


night=False


def change_weather():

    global night,rain_mode


    night = not night


    rain_mode = not rain_mode


    if night:

        screen.bgcolor("midnight blue")

    else:

        screen.bgcolor("darkgreen")




screen.onkeypress(
    change_weather,
    "n"
)




# ================= PAUSE SYSTEM =================


paused=False



def pause_game():

    global paused

    paused = not paused



screen.onkeypress(
    pause_game,
    "p"
)




# ================= RESTART =================


def restart():

    global score,fuel,health,nitro,level,speed,running


    score=0

    fuel=100

    health=100

    nitro=100

    level=1

    speed=8

    running=True



    player.goto(
        0,
        -300
    )



    for enemy in enemy_list:

        enemy.goto(
            random.choice([-100,0,100]),
            random.randint(400,900)
        )



    for coin in coins:

        coin.goto(
            random.choice([-100,0,100]),
            random.randint(400,900)
        )



screen.onkeypress(
    restart,
    "r"
)




# ================= IMPROVED LOOP =================


old_update = update_game



def final_game_loop():


    if paused:

        screen.update()

        screen.ontimer(
            final_game_loop,
            50
        )

        return



    create_rain()


    old_update()


    screen.ontimer(
        final_game_loop,
        50
    )





# ================= INSTRUCTIONS =================


instruction=turtle.Turtle()

instruction.hideturtle()

instruction.color("white")

instruction.penup()

instruction.goto(-300,-360)


instruction.write(
    "Controls: ← → Move | SPACE Nitro | N Weather | P Pause | R Restart",
    font=("Arial",12,"normal")
)




# Start final loop

final_game_loop()


screen.mainloop()
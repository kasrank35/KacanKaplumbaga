import turtle
from random import randint

game_screen = turtle.Screen()
game_screen.bgcolor("light green")
game_screen.title("Kaplumbağayı Yakala")
FONT = ("Arial",30,"normal")
score = 0
zaman = 10
game_over=False
turtle_target = turtle.Turtle()
turtle_score=turtle.Turtle()
turtle_time=turtle.Turtle()
turtle.hideturtle()

#SCORE
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.color("black")
turtle_score.setpos(0,240)
turtle_score.write(f"score: {score}",move=False,align="center",font=FONT)

#HEDEF
def konum():
    if not game_over:
        turtle_target.shape("turtle")
        turtle_target.color("red")
        turtle_target.hideturtle()
        turtle_target.penup()
        turtle_target.goto(randint(-200,200),randint(-200,200))
        turtle_target.showturtle()
        turtle_target.clear()
        turtle.ontimer(konum,500)

#+1
def hand(x,y):
    global score
    score += 1
    turtle_score.clear()
    turtle_score.write(f"score: {score}", move=False, align="center", font=FONT)
    print(x, y)
turtle_target.onclick(hand)

#TIMER
def countdown(time):
    global game_over
    turtle_time.hideturtle()
    turtle_time.penup()
    turtle_time.setposition(0,210)
    turtle_time.clear()
    if time > 0:
        turtle_time.clear()
        turtle_time.write("Time: {}".format(time),move=False,align="center",font=FONT)
        game_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        turtle_target.hideturtle()
        turtle_time.clear()
        turtle_time.write("Game Over!", align='center', font=FONT)
        turtle.hideturtle()


def baslat():
    global game_over
    game_over = False
    countdown(zaman)
    konum()

baslat()
turtle.done()
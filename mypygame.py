#Space Invaders - Part 1
#Set up the screen
#Python 2.7 on Mac
import turtle
import os
import Tkinter

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for sided in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.shapesize(2, 2)
playerspeed = 15

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed =2

#Creat the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"



#Move the player left and right
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changes
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet, "space")
#Main game loop
while True:

    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move the enemy back and down
    if enemy.xcor()> 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *=-1
        enemy.sety(y)

    if enemy.xcor() < -280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check t osee if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


#delay = raw_input("press enter to finish.")
Tkinter.mainloop()
import time
import turtle

game = True
score = 0
horizontal = -270

window = turtle.Screen()
window.title("Space Invader Game")
window.bgcolor('black')
window.setup(width=800, height=600)

player = turtle.Turtle()
player.shape('triangle')
player.speed(0)
player.color('green')
player.penup()
player.goto(x=0, y=-250)

aliens = []
for item in range(10):
    alien = turtle.Turtle()
    alien.color('red')
    alien.shape('circle')
    alien.speed(0)
    x = horizontal
    y = 180
    alien.dx = 15
    alien.penup()
    alien.goto(x=x, y=y)
    aliens.append(alien)
    horizontal += 55


bullet = turtle.Turtle()
bullet.speed(0)
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.hideturtle()
bullet.goto(0, -240)
bullet.state = "ready"

barriers = []
location = -380

for item in range(10):
    barrier = turtle.Turtle()
    barrier.speed(0)
    barrier.shape('square')
    barrier.color('green')
    barrier.penup()
    barrier.goto(x=location, y=-200)
    barriers.append(barrier)
    location += 80


def move_left():
    player_x = player.xcor()
    player_x -= 20
    if player_x < -380:
        player_x = -380
    player.setx(player_x)


def move_right():
    player_x = player.xcor()
    player_x += 20
    if player_x > 380:
        player_x = 380
    player.setx(player_x)


def fire_bullet():
    if bullet.state == "ready":
        bullet.state = "fire"
        x_cor = player.xcor()
        y_cor = player.ycor() + 20
        bullet.goto(x=x_cor, y=y_cor)
        bullet.showturtle()


window.listen()
window.onkeypress(move_left, 'Left')
window.onkeypress(move_right, 'Right')
window.onkeypress(fire_bullet, 'space')

while game:
    for alien in aliens:
        alien_x = alien.xcor()
        alien_x += alien.dx
        alien.setx(alien_x)

        if alien.xcor() > 360 or alien.xcor() < -360:
            for a in aliens:
                a.dx *= -1
                y = a.ycor()
                y -= 50
                a.sety(y)

        if alien.ycor() - player.ycor() <= 35:
            player.hideturtle()
            for a in aliens:
                a.hideturtle()
            bullet.hideturtle()
            turtle.penup()
            turtle.speed(0)
            turtle.goto(-125, 0)
            turtle.color('white')
            turtle.hideturtle()
            turtle.write("Game Over...", font=('Arial', 26, 'bold'))
            game = False
            window.update()
            time.sleep(3)
            window.bye()

        if bullet.state == "fire" and bullet.distance(alien) < 25:
            bullet.state = "ready"
            bullet.hideturtle()
            alien.hideturtle()
            aliens.remove(alien)

    if bullet.state == "fire":
        bullet_y = bullet.ycor()
        bullet_y += 40
        bullet.sety(bullet_y)

    if bullet.state == "fire" and bullet.ycor() > 200:
        bullet.hideturtle()
        bullet.state = "ready"

    if len(aliens) == 0:
        player.hideturtle()
        for barrier in barriers:
            barrier.hideturtle()
        bullet.hideturtle()
        turtle.penup()
        turtle.speed(0)
        turtle.goto(-50, 0)
        turtle.color('white')
        turtle.write("You wins...", font=('Arial', 26, 'bold'))

    for barrier in barriers:
        if bullet.distance(barrier) < 20:
            bullet.state = "ready"
            bullet.hideturtle()
            barrier.hideturtle()
            barriers.remove(barrier)

    window.update()

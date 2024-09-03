import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

knife = Actor('knife')
knife.pos = (WIDTH //2, HEIGHT - 2)
knife.dead = False

speed = 5
bullets = []
enemies = []
civilians = []
score = 0
direction = 1
knife.countdown = 90

for x in range(8):
    enemy = (Actor('ninja'))
    enemy.x = random.randint(0, WIDTH)
    enemy.y = random.randint(0, HEIGHT // 2)
    enemies.append(enemy)

for x in range(5):
    civilian = Actor('person')
    civilian.x = random.randint(0, WIDTH)
    civilian.y = random.randint(HEIGHT // 2, HEIGHT)
    civilians   .append(civilian)

def on_key_down(key):
    if knife.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor('bullet'))
            bullets[-1].x = knife.x
            bullets[-1].y = knife.y

def display_score():
    screen.draw.text("score = " + str(score), (50,30), color = 'black')

def display_game_over():
    screen.draw.text("Game Over!", (250,250), color = 'black')


def update():
    global score
    global direction
    global civilian
    moveDown = False 
    if knife.dead == False:
        if keyboard.left:
            knife.x -= speed
            if knife.x <= 0:
                knife.x = 0
        if keyboard.right:
            knife.x += speed
            if knife.x >= WIDTH:
                knife.x = WIDTH
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
        moveDown = True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 100
            if enemy.y > HEIGHT:
                enemies.remove(enemy)

        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 100 
        if enemy.colliderect(knife):
            knife.dead = True
    for civilian in civilians[:]:
       for bullet in bullets[:]:
           if civilian.colliderect(bullet):
               bullets.remove(bullet)
               civilians.remove(civilian)
               score -= 300

    if civilian.colliderect(knife):
        knife.dead = True
        civilians.remove(civilian)
            

    if knife.dead: 
        knife.countdown -=1
    if knife.countdown == 0:
        knife.dead = False
        knife.countdown = 90    
    if len(enemies) == 0 and not knife.dead:
        civilians.clear()

def draw():
    screen.clear()
    screen.fill('aquamarine')
    display_score()
    if len(enemies) == 0:
        display_game_over()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    for civilian in civilians:
        civilian.draw()
    if knife.dead == False:
        knife.draw()




pgzrun.go()
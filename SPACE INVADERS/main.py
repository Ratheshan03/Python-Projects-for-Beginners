import pygame
import math
import random
from pygame import mixer
import time

#Initialise the Pygame
pygame.init()

#Create the Screen
screen = pygame.display.set_mode((800,600)) 

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load("background.png")

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)


#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480 
playerX_change = 0












def player(x,y):
    screen.blit(playerImg,(x,y))


#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change= []
num_of_enemies = 5
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(10,25))
    enemyX_change.append(4)
    enemyY_change.append(40)
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+16,y+10))

#Collision
def isCollision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
    # print(distance)
    if distance < 27:
        return True
    else:
        return False

#Explosion
explosion = pygame.image.load('explosion.png')


#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',30)
textX = 10
textY = 10
def showScore(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
#Reading Highscore
with open('highscore.txt','r') as f:
    x=f.read()
    all_scores =x.split(',')
    all_scores.sort()
    print(all_scores)

   
def highscore(x,y):
    
    highscore =  font.render("Highscore : "+(all_scores[-1]),True,(255,255,255))
    screen.blit(highscore,(x,y+27))
  

#GAme Over
game_over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    game_over_text = game_over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over_text,(200,250))

def add_highscore():
    with open('highscore.txt','a') as f:
 
        f.write(str(score_value)+',')
def menu():
    # # show_menu = True
    # # while show_menu:
    #     #Screen color
    # screen.fill((0,0,0))
    # intro_font = pygame.font.Font('freesansbold.ttf',64)
    # intro_text = intro_font.render("SPACE INVADER",True,(255,255,255))
    # screen.blit(intro_text,(200,250))
    # for event in pygame.event.get():
        
    #     if event.type == pygame.QUIT:
    #         show_menu = False
    # time.sleep(2.5)   
    pass
                
    
 
                
        
                





#Game Loop

running = True
while running:
    menu()

        #Screen color
    screen.fill((0,0,0))

    #Background
    screen.blit(background,(0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #if Keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                # print("Right")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Keystroke released")
                playerX_change = 0

        

    playerX += playerX_change        
    #Player boundaries
    if playerX <=0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    #Enemy Movement
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            # L = list(all_scores)
            # L.append(score_value)
            # all_scores = tuple(L)
            
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        #collision

        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480 
            bullet_state = 'ready'
            score_value +=1
            # print(score)
            screen.blit(explosion,(enemyX[i],enemyY[i]))
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(-20,0)

        enemy(enemyX[i],enemyY[i],i)

    #Bullet Movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change




player(playerX,playerY)
showScore(textX,textY)
highscore(textX,textY)

pygame.display.update()



add_highscore()
print(all_scores)
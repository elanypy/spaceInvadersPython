import pygame 
from pygame import mixer
import random
import math
 
pygame.init()

#criando a tela com o tamanho de 800,600
screenWIDTH = 800
screenHEIGHT = 600
screen = pygame.display.set_mode((screenWIDTH,screenHEIGHT)) 

#background
background = pygame.image.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\Background2.png')

#som
mixer.music.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\background.wav')
mixer.music.play(-1)


#adicionando o nome do jogo
pygame.display.set_caption('Space Invaders')
#adicionando o icone do jogo
icon = pygame.image.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\spaceship.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\space-invaders.png')
playerX = 30
playerY = 480
playerXChange = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\enemy1.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyXChange.append(4)
    enemyYChange.append(40)




#Ready - you cant see the bullet on the screen
#Fire - the bullet is currently moving 
bulletImg = pygame.image.load(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\bullet.png')
bulletX = 0 
bulletY = 480
bulletXChange = 0
bulletYChange = 10
bullet_state = "ready"


# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x,y))


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global  bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


#iniciando o loop
running = True

while running:
    
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -5

            if event.key == pygame.K_RIGHT:
                playerXChange = 5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

            if event.key == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   playerXChange = 0

           

    playerX += playerXChange
  #caso o player saia do layout
    if playerX <= 0:
        playerX= 0
    elif playerX >= 736:
        playerX= 736


    for i in range(num_of_enemies):
   # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 4
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -4
            enemyY[i] += enemyYChange[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if collision:
            explosionSound = mixer.Sound(r'C:\Users\Happycode3D-07\Documents\Pessoais\PythonProjects\gameWithPython\snake\explosion.wav')
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    #movimento do bullet 
    if bulletY<=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletYChange


    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()

    


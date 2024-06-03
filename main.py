import pygame
from character import Character
from projectile import Projectile
                                                #imports
pygame.init()                                   #initalize pygame
screen = pygame.display.set_mode((600, 600))    #set GUI window size
clock = pygame.time.Clock()                     #init game clock 
running = True                                  #set up var for while loop 
player = Character(300, 550, 1, screen)         #set up player

fireTime = 0
fireSpeed = 500                                 #in ms
bullets = []                                    #init list for bullet handling
enemies = []

while running:                                  #start game logic loop
    for event in pygame.event.get():            #wait for quit command
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")                        #set screen color

    #RENDER GAME LOGIC HERE
    player.draw()                               #draw player

    #HANDLE BULLET LOGIC
    for bullet in bullets:                              #pos and vel handler
        if bullet.ypos > 0:       
            bullet.ypos -= bullet.vel                   
        else:
            bullets.pop(bullets.index(bullet))

    if (pygame.key.get_pressed()[pygame.K_LEFT] != 0):      #take key input
        if player.xpos > 0:
            player.move("LEFT", 5)
    if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        if player.xpos < 550:
            player.move("RIGHT", 5)
    if (pygame.key.get_pressed()[pygame.K_SPACE] != 0):
        if len(bullets) < 2 and timeSinceFire > fireSpeed:
            bullets.append(Projectile(player.xpos+25, player.ypos, 2, "green", 10))
            fireTime = pygame.time.get_ticks()


    for bullet in bullets:      #draw bullets as last item
        bullet.draw(screen)
    timeSinceFire = pygame.time.get_ticks() - fireTime

        

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
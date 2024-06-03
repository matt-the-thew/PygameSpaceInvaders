import pygame
from character import Character
from projectile import Projectile

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
player = Character(300, 480, 1, screen)

bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #RENDER GAME LOGIC HERE
    player.draw()
    if (pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        print("LEFT")
        player.move("LEFT", 5)
    if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        print("RIGHT")
        player.move("RIGHT", 5)
    if (pygame.key.get_pressed()[pygame.K_SPACE] != 0):
        print("SPACE")
        bullets.append(Projectile(player.xpos+25, player.ypos, 2, "green", 10))
    
    #BULLET LOGIC
    for bullet in bullets:
        bullet.draw(screen)
        if len(bullets) < 6:
            bullet.ypos -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


        

    pygame.display.flip()

    clock.tick(15)

pygame.quit()
import pygame
import ExploreIsland
pygame.init()

screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption("Ocean map")

InOcean = True
x = 0
y = 0
#Smoothness is how many pixels the image moves by
smoothness = 1
#DelaySpeed is the amount of time in milliseconds between refreshes
DelaySpeed = 10
ship = pygame.image.load('Images\ShipSampletiny.PNG')
position = ship.get_rect()
screen.fill((52, 149, 235))
while InOcean:
    
    pygame.time.delay(DelaySpeed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            InOcean = False
    pygame.draw.rect(screen, (52, 149, 235), position)
    keys = pygame.key.get_pressed()
#Movement if statements - looking for the move keys
    if keys[pygame.K_LEFT] and position.x>0:
        position = position.move(x-smoothness,y)
    if keys[pygame.K_RIGHT] and position.x<(1000-69):
        position = position.move(x+smoothness,y)
    if keys[pygame.K_UP] and position.y>0:
        position = position.move(x,y-smoothness)
    if keys[pygame.K_DOWN] and position.y<(1000-69):
        position = position.move(x,y+smoothness)
#looking for action key 'e' to be pressed
    if keys[pygame.K_e] and position.colliderect((500,500,50,50)):
        ExploreIsland.IslandExploration()
        
    
    
    pygame.draw.rect(screen, (255,0,0), (500,500,50,50), 5)
    screen.blit(ship, position)
    pygame.display.flip()


pygame.quit()

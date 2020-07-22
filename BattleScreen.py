import pygame
import POOPDECKSCRIPTS as pds
pygame.init()

Enemy = pds.GetEnemyClass('TestEnemy')
back = pds.GetImage('Wall.jpg')
back2 = pds.GetImage('IslandTest.jpg')

def FightingScreen(AreaWidth,AreaHeight,ObstacleList,Background):
    
    screen = pygame.display.set_mode([800,800])
    pygame.display.set_caption("FIGHTING")

    
    Fighting = True
    

    Grid = [[0]*AreaWidth]*AreaHeight
    timer = 0
    CurrentScreen = 'North'
    while Fighting:
        pygame.time.delay(10)

        if timer !=0:
            timer -=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Fighting = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] and timer == 0:
            if CurrentScreen == 'North':
                CurrentScreen = 'East'
            elif CurrentScreen == 'East':
                CurrentScreen = 'South'
            elif CurrentScreen == 'South':
                CurrentScreen = 'West'
            elif CurrentScreen == 'West':
                CurrentScreen = 'North'
            timer = 10
            
        if keys[pygame.K_LSHIFT] and timer == 0:
            if CurrentScreen == 'North':
                CurrentScreen = 'West'
            elif CurrentScreen == 'West':
                CurrentScreen = 'South'
            elif CurrentScreen == 'South':
                CurrentScreen = 'East'
            elif CurrentScreen == 'East':
                CurrentScreen = 'North'
            timer = 10
                
        screen.blit(Background, (0,0))
        
        for Obstacle in ObstacleList :
            if pds.WithinView((2,2),(Obstacle.position[0],Obstacle.position[1]), CurrentScreen):
                screen.blit(Obstacle.sprite,(0,0))
        
        pygame.display.flip()
    pygame.quit()
            
FightingScreen(5,5,[Enemy],back)

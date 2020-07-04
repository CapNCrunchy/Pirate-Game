import pygame
from THEPOOPDECK import*
from ClassesLib import*
import ExploreIsland
import __init__
import math
pygame.init()

screen = pygame.display.set_mode([1000,1000])
ScreenLimit = pygame.Rect(0,0,1000,1000)
pygame.display.set_caption("Ocean map")

TestShip = Ship(BasicCannon,100,"no Crew", ShipImage)

InOcean = True
#Smoothness is how many pixels the image moves by
smoothness = 1
#DelaySpeed is the amount of time in milliseconds between refreshes
DelaySpeed = 10

ShipRect = TestShip.rect
screen.fill(OceanColor)
pygame.mouse.set_visible(False)
tutorial_font = (pygame.font.Font('HighTide-Demo.ttf',40)).render('Press \'e\' to enter', True, (0,0,0))
CursorRect = ''
TestIsland = pygame.Rect(500,500,50,50)
RectList.append(ShipRect)
RectList.append(TestIsland)
print(RectList)

print((TestShip.cannon).CannonRange)
def DrawCursor():
    pygame.draw.circle(screen, (CursorColor), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),10, 3)
    pygame.draw.line(screen, (CursorColor), (pygame.mouse.get_pos()[0]-10,pygame.mouse.get_pos()[1]-10),(pygame.mouse.get_pos()[0]+10,pygame.mouse.get_pos()[1]+10), 2)
    pygame.draw.line(screen, (CursorColor), (pygame.mouse.get_pos()[0]+10,pygame.mouse.get_pos()[1]-10),(pygame.mouse.get_pos()[0]-10,pygame.mouse.get_pos()[1]+10), 2)
    
def TwoPointDistance(Tuple1,Tuple2,ship):
    
    
    distance = math.sqrt( ((Tuple2[0]-Tuple1[0])**2) + ((Tuple2[1]-Tuple1[1])**2) )

    if(distance <= (ship.cannon).CannonRange):
        return True

    return False
    


while InOcean:
    CursorRect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],20,20)
    ShipPosition = (ShipRect.x+int(ShipRect.width/2),ShipRect.y+int(ShipRect.height/2))
    CursorPosition = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    CursorColor = CursorColorOFF
    pygame.time.delay(DelaySpeed)
    TestShip = Ship(BasicCannon,100,"no Crew", ShipImage)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            InOcean = False
        
    screen.fill(OceanColor)

    if TwoPointDistance(ShipPosition,CursorPosition,TestShip):
       CursorColor = CursorColorON
    
    
    keys = pygame.key.get_pressed()
#Movement if statements - looking for the move keys
    if keys[pygame.K_a] and ShipRect.x>0:
        ShipRect = ShipRect.move(0-smoothness,0)
    if keys[pygame.K_d] and ShipRect.x<(1000-69):
        ShipRect = ShipRect.move(0+smoothness,0)
    if keys[pygame.K_w] and ShipRect.y>0:
        ShipRect = ShipRect.move(0,0-smoothness)
    if keys[pygame.K_s] and ShipRect.y<(1000-69):
        ShipRect = ShipRect.move(0,0+smoothness)

#Looking for Mouse clicks
    if pygame.mouse.get_pressed()[0] and CursorColor == CursorColorON:
        screen.fill((0,0,0))
#looking for action key 'e' to be pressed
    if keys[pygame.K_e] and ShipRect.colliderect(TestIsland):
        ExploreIsland.IslandExploration()
        screen.fill((52, 149, 235))
        pygame.display.set_caption("Ocean map")
#looking for the mouse in the screen
    pygame.draw.rect(screen, (255,0,0), TestIsland, 5)
    DrawCursor()
    screen.blit(TestShip.sprite, ShipRect)
    screen.blit(tutorial_font, (ShipRect.x,ShipRect.y+ShipRect.height,ShipRect.width,ShipRect.height))
    pygame.display.flip()


pygame.quit()

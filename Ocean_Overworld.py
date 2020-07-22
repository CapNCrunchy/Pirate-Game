import pygame
import __init__
from ClassesLib import*
import POOPDECKSCRIPTS as pds
pygame.init()


def OceanOverworldFunc(InOcean):
    screen = pygame.display.set_mode((500,500), pygame.RESIZABLE|pygame.SCALED)

    pygame.display.set_caption("Ocean map")

    TestShip = pds.GetShipClass('TestShip')

#Smoothness is how many pixels the image moves by
    smoothness = 1
#DelaySpeed is the amount of time in milliseconds between refreshes
    DelaySpeed = 10

    ShipRect = TestShip.rect
    screen.fill(pds.GetColor('OceanColor'))
    tutorial_font = (pygame.font.Font('HighTide-Demo.ttf',40)).render('Press \'e\' to enter', True, (0,0,0))
    CursorRect = ''
    TestIsland = pygame.Rect(250,250,50,50)
#cannon variables
    ammo = 10
    CannonBallSpeed = 0
    CannonBallList = []
    CannonReload = 0
    ShipSpeed = 0
    while InOcean:
        pygame.time.delay(DelaySpeed)
        CannonBallSpeed +=1
        ShipSpeed +=1
        
        if CannonBallSpeed == 5:
            CannonBallSpeed = 0
        if ShipSpeed == 1:
            ShipSpeed = 0
        if CannonReload != 0:
            CannonReload -=1
        pygame.mouse.set_visible(True)
        CursorRect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],20,20)
        ShipPosition = (ShipRect.x+int(ShipRect.width/2),ShipRect.y+int(ShipRect.height/2))
        CursorPosition = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        CursorColor = pds.GetColor('CursorColorOFF')
        TestShip = pds.GetShipClass('TestShip')
        screen.fill(pds.GetColor('OceanColor'))

#EventListener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Title'
                break

        if pds.TwoPointDistance(ShipPosition,CursorPosition,TestShip):
           CursorColor = pds.GetColor('CursorColorON')
        pds.DrawCursor(screen,CursorColor)

#Movement if statements - looking for the move keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ShipRect.x>0 and ShipSpeed == 0:
            ShipRect = ShipRect.move(0-smoothness,0)
        if keys[pygame.K_d] and ShipRect.x<(1000-69) and ShipSpeed == 0:
            ShipRect = ShipRect.move(0+smoothness,0)
        if keys[pygame.K_w] and ShipRect.y>0 and ShipSpeed == 0:
            ShipRect = ShipRect.move(0,0-smoothness)
        if keys[pygame.K_s] and ShipRect.y<(1000-69) and ShipSpeed == 0:
            ShipRect = ShipRect.move(0,0+smoothness)
        if keys[pygame.K_ESCAPE]:
            return 'Title'
            break

#Looking for Mouse clicks/cannon fire
        if pygame.mouse.get_pressed()[0] and CursorColor == pds.GetColor('CursorColorON'):
            if ammo != 0 and CannonReload == 0:
                CannonBallList.append(CannonBall(CursorPosition,ShipPosition))
                pds.SupplimentCannonBall(CannonBallList[-1])
                print(CannonBallList[-1].Direction)
                ammo -= 1
                CannonReload = 100
        pygame.draw.rect(screen, (255,0,0), TestIsland, 5)
        screen.blit(TestShip.sprite, ShipRect)
        
        for Balls in CannonBallList:
            Balls.MoveSelf(CannonBallSpeed)
            screen.blit(pds.GetImage('CannonBallTiny.PNG'),(Balls.Pos[0],Balls.Pos[1],25,25))
            if pds.TwoPointDistance(Balls.Pos,Balls.start,TestShip):
                pass
            else:
                CannonBallList.remove(Balls)
            
#looking for action key 'e' to be pressed
        if keys[pygame.K_e] and ShipRect.colliderect(TestIsland):
            return 'Island'
            break
        
        
        
        screen.blit(tutorial_font, (ShipRect.x,ShipRect.y+ShipRect.height,ShipRect.width,ShipRect.height))
        pygame.display.flip()


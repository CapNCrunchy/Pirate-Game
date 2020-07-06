import pygame
import __init__
import POOPDECKSCRIPTS as pds
pygame.init()


def OceanOverworldFunc(InOcean):
    screen = pygame.display.set_mode([500,500])

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
    slope = 0
    target = 0
    start = 0
    CannonballPos = 0
    ammo = 10
    TimerCounter = 0
    XMovementLimit = 20
    YMovementLimit = 20
    Xleft= ''
    Yleft= ''
    Xchange = ''
    Ychange = ''
    Direction = ''
    Shooting = False
    while InOcean:
        pygame.time.delay(DelaySpeed)
        TimerCounter +=1
        if TimerCounter == 10:
            TimerCounter = 0
        pygame.mouse.set_visible(False)
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
    

#Movement if statements - looking for the move keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ShipRect.x>0:
            ShipRect = ShipRect.move(0-smoothness,0)
        if keys[pygame.K_d] and ShipRect.x<(1000-69):
            ShipRect = ShipRect.move(0+smoothness,0)
        if keys[pygame.K_w] and ShipRect.y>0:
            ShipRect = ShipRect.move(0,0-smoothness)
        if keys[pygame.K_s] and ShipRect.y<(1000-69):
            ShipRect = ShipRect.move(0,0+smoothness)

#Looking for Mouse clicks
        if pygame.mouse.get_pressed()[0] and CursorColor == pds.GetColor('CursorColorON'):
            if ammo != 0 and Shooting == False:
                slope = pds.FireCannon(CursorPosition,ShipPosition)
                target = CursorPosition
                start = ShipPosition
                CannonballPos = start
                ammo -= 1
                Xleft = abs(slope[0])
                Yleft = abs(slope[1])
                Direction = (slope[0]/Xleft,slope[1]/Yleft)
                Shooting = True
                
            
        if slope != 0:
            pygame.draw.circle(screen, (43, 28, 27),CannonballPos,5)
            if Xleft >= XMovementLimit:
                Xchange = XMovementLimit
                Xleft -= XMovementLimit
                XMovementLimit = 0
            elif Xleft < XMovementLimit:
                Xchange = Xleft
                Xleft = 0
                XMovementLimit -= Xleft
            if Yleft >= YMovementLimit:
                Ychange = YMovementLimit
                Yleft -= YMovementLimit
                YMovementLimit = 0
            elif Yleft < YMovementLimit:
                Ychange = Yleft
                Yleft = 0
                YMovementLimit -= Yleft
            
            if Xleft == 0 and Yleft == 0:
                Xleft = abs(slope[0])
                Yleft = abs(slope[1])
            if TimerCounter == 0:
                CannonballPos = (int(CannonballPos[0]+(Xchange*Direction[0])),int(CannonballPos[1]+(Ychange*Direction[1])))
            if XMovementLimit == 0:
                XMovementLimit = 1
            if YMovementLimit == 0:
                YMovementLimit = 1
            if CannonballPos == target:
                Xleft= ''
                Yleft= ''
                Xchange = ''
                Ychange = ''
                Direction = ''
                slope = 0
                target = 0
                start = 0
                CannonballPos = 0
                Shooting = False
            
#looking for action key 'e' to be pressed
        if keys[pygame.K_e] and ShipRect.colliderect(TestIsland):
            return 'Island'
            break
        
        pygame.draw.rect(screen, (255,0,0), TestIsland, 5)
        pds.DrawCursor(screen,CursorColor)
        #screen.blit(TestShip.sprite, ShipRect)
        screen.blit(tutorial_font, (ShipRect.x,ShipRect.y+ShipRect.height,ShipRect.width,ShipRect.height))
        pygame.display.flip()


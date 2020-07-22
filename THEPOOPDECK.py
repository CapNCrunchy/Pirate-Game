import pygame, math, configparser
from ClassesLib import*
pygame.init()
Config = configparser.ConfigParser()
Config.read("Config.ini")
#Dumping grounds for functions

def DrawCursor(screen,CursorColor):
    pygame.draw.circle(screen, (CursorColor), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),10, 3)
    pygame.draw.line(screen, (CursorColor), (pygame.mouse.get_pos()[0]-10,pygame.mouse.get_pos()[1]-10),(pygame.mouse.get_pos()[0]+10,pygame.mouse.get_pos()[1]+10), 2)
    pygame.draw.line(screen, (CursorColor), (pygame.mouse.get_pos()[0]+10,pygame.mouse.get_pos()[1]-10),(pygame.mouse.get_pos()[0]-10,pygame.mouse.get_pos()[1]+10), 2)
    
def TwoPointDistance(Tuple1,Tuple2,ship):
    
    
    distance = math.sqrt( ((Tuple2[0]-Tuple1[0])**2) + ((Tuple2[1]-Tuple1[1])**2) )

    if(distance <= (ship.cannon).CannonRange):
        return True

    return False

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
            
def IfPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def LCDfactorization(Number1,Number2):

    Num1Facts = []
    Num2Facts = []
    Number1dupe = Number1
    Number2dupe = Number2
    CommonFacts = []
    loop1 = True
    loop2 = True
    GCF = 1
    if Number1 <0:
        Number1dupe = Number1*(-1)
    if Number2 <0:
        Number2dupe = Number2*(-1)
    while loop1:
        for possFacts in range(2,Number1dupe+1):
            
            if Number1dupe%possFacts == 0 and IfPrime(possFacts):
                Num1Facts.append(possFacts)
                Number1dupe = int(Number1dupe/possFacts)
                possFacts = Number1*2
        if Number1dupe == 1:
            loop1 = False
    
    while loop2:
        for possFacts in range(2,Number2dupe+1):
            if Number2dupe%possFacts == 0 and IfPrime(possFacts):
                Num2Facts.append(possFacts)
                Number2dupe = int(Number2dupe/possFacts)
                possFacts = Number2*2
        if Number2dupe == 1:
            loop2 = False
    
    for nums in Num1Facts:
        if nums in Num2Facts:
            CommonFacts.append(nums)
            Num2Facts.remove(nums)
    
    for nums in CommonFacts:
        GCF *= nums
    return GCF

def FireCannon(Tuple2,Tuple1):
    slope = (Tuple2[0]-Tuple1[0],Tuple2[1]-Tuple1[1])
    GCF = LCDfactorization(Tuple2[0]-Tuple1[0],Tuple2[1]-Tuple1[1])
    slope = (slope[0]/GCF,slope[1]/GCF)
    
    return slope
def SupplimentCannonBall(CB):
    CB.slope = FireCannon(CB.target,CB.start)
    CB.Xleft = abs(CB.slope[0])
    CB.Yleft = abs(CB.slope[1])
    CB.Direction = (CB.slope[0]/CB.Xleft,CB.slope[1]/CB.Yleft)

def WithinView(player,point,Facing):
    playerPos = []
    pointPos = []
    playerPos.append(player[0] - player[0])
    pointPos.append(point[0] - player[0])
    playerPos.append(player[1] - player[1])
    pointPos.append(point[1] - player[1])
    Direction = (point[0]/abs(point[0]),point[1]/abs(point[1]))
    if Facing == 'North':
        if Direction[1] != -1:
            return False

        if(abs(pointPos[0]) <= abs(pointPos[1])):
            return True
        else:
            return False
    if Facing == 'South':
        if Direction[1] != 1:
            return False

        if(abs(pointPos[0]) <= pointPos[1]):
            return True
        else:
            return False
    if Facing == 'West':
        if Direction[0] != -1:
            return False

        if(abs(pointPos[1]) <= abs(pointPos[0])):
            return True
        else:
            return False
    if Facing == 'East':
        if Direction[0] != -1:
            return False

        if(abs(pointPos[1]) <= pointPos[0]):
            return True
        else:
            return False
def ButtonIsActive(Button,mouse):
    if mouse.colliderect(Button):
        Button.CurrentColor = Button.ColorChange
        return True
    else:
        Button.CurrentColor = Button.Color
        return False
    

#Config Scripts
def GetColor(ColorName):
    Color = Config.get('Colors',str(ColorName))
    ColorINTs = Color.split(',')
    Color = (int(ColorINTs[0]),int(ColorINTs[1]),int(ColorINTs[2]))
    
    return Color
def GetFont(FontName, size):
    FontConfig = Config.get('Fonts',str(FontName))

    font = pygame.font.Font(FontConfig,size)
    return font


def GetImage(ImageName):
    image = pygame.image.load(str('.\\Images\\'+ImageName))

    return image

def GetCannonClass(CannonName):
    CannonClass = Config.get('CannonClasses',str(CannonName))
    CannonArgs = CannonClass.split(',')
    CannonClass = Cannon(int(CannonArgs[0]), int(CannonArgs[1]), CannonArgs[2])

    return CannonClass
def GetShipClass(ShipName):
    ShipClass = Config.get('ShipClasses',str(ShipName))
    ShipArgs = ShipClass.split(',')
    ShipClass = Ship(GetCannonClass(ShipArgs[0]),int(ShipArgs[1]),ShipArgs[2],GetImage(ShipArgs[3]))

    return ShipClass
def GetEnemyClass(EnemyName):
    EnemyClass = Config.get('Enemies',str(EnemyName))
    EnemyArgs = EnemyClass.split(',')
    EnemyClass = Enemy(EnemyArgs[0],int(EnemyArgs[1]),int(EnemyArgs[2]),int(EnemyArgs[3]),GetImage(EnemyArgs[4]))

    return EnemyClass

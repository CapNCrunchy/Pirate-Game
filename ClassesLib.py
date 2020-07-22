import pygame
class Button:
    def __init__(self,rect,color,colorChange,text,font,fontColor):
        self.rect = rect
        self.Color = color
        self.ColorChange = colorChange
        self.text = text
        self.font = font
        self.Render = font.render(text, True, fontColor)
        self.CurrentColor = color

class Player:
    def __init__(self,name,health,age,height,weight,strength,speed):
        self.name = name
        self.health = health
        self.age = age
        self.height = height
        self.weight = weight
        self.strength = strength
        self.speed = speed
        self.WeightCap = int(weight)*15

        self.ItemsINVENTORY = []
        self.WeaponsINVENTORY = []
        self.MiscINVENTORY = []

        self.CurrentWeapon = ''
        self.Armor = ''

class Enemy:
    def __init__(self,name, health, x,y,sprite):
        self.name = name
        self.position = (x,y)
        self.health = health
        self.sprite = sprite
        self.INVENTORY = []
        self.weapon = ''
        self.armor = ''

class item:
    def __init__(self, ItemType, ItemName, Stackable, Consumable, weight):
        self.ItemType = ItemType
        self.ItemName = ItemName
        self.Stackable = Stackable
        self.Consumable = Consumable
        self.weight = weight
class Weapon:
    def __init__(self, name,damage, DmgType, weight):
        self.name = name
        self.damage = damage
        self.Dmgtype = DmgType
        self.weight = self.weight

class Cannon:
    def __init__(self,CannonRange,damage,TypeOfCannon):
        self.CannonRange = CannonRange
        self.damage = damage
        self.name = str(TypeOfCannon)

class CannonBall:
    def __init__(self,target,start):
        self.start = start
        self.target = target
        self.Pos = start
        self.XLimit = 1
        self.YLimit = 1
        self.slope = 0
        self.Xchange = ''
        self.Ychange = ''
        self.Xleft= ''
        self.Yleft= ''
        self.Direction= ''
    def MoveSelf(self,TimerCounter):
        if self.Xleft >= self.XLimit:
            self.Xchange = self.XLimit
            self.Xleft -= self.XLimit
            self.XLimit = 0
        elif self.Xleft < self.XLimit:
            self.Xchange = self.Xleft
            self.Xleft = 0
            self.XLimit -= self.Xleft
        if self.Yleft >= self.YLimit:
            self.Ychange = self.YLimit
            self.Yleft -= self.YLimit
            self.YLimit = 0
        elif self.Yleft < self.YLimit:
            self.Ychange = self.Yleft
            self.Yleft = 0
            self.YLimit -= self.Yleft
            
        if self.Xleft == 0 and self.Yleft == 0:
            self.Xleft = abs(self.slope[0])
            self.Yleft = abs(self.slope[1])
        
        if TimerCounter == 0:
            self.Pos = (int(self.Pos[0]+(self.Xchange*self.Direction[0])),int(self.Pos[1]+(self.Ychange*self.Direction[1])))
        if self.XLimit == 0:
            self.XLimit = 1
        if self.YLimit == 0:
            self.YLimit = 1
        
        
class Ship:
    def __init__(self, cannon, health,crew, sprite):
        self.cannon = cannon
        self.health = health
        self.crew = crew
        self.sprite = sprite
        self.rect = sprite.get_rect()
        

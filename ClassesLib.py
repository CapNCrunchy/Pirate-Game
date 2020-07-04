from THEPOOPDECK import*
import pygame

''' Character, enemy, and weapon class structures and item list'''

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
    def __init__(self,name, health, speed, strength, difficulty,EnemyType):
        self.name = name
        self.EnemyType = EnemyType
        self.health = health
        self.strength = strength
        self.speed = speed
        self.difficulty = difficulty

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
        
class Ship:
    def __init__(self, cannon, health,crew, sprite):
        self.cannon = cannon
        self.health = health
        self.crew = crew
        self.sprite = sprite
        self.rect = sprite.get_rect()
        
